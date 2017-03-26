# -*- coding:utf-8 -*-
from __future__ import print_function, absolute_import, division
import maya.cmds as cmds
import maya.api.OpenMaya as om
from metan.exception import *
# from metan.logger import log


def to_dependencynode(name):
    sellist = om.MSelectionList()
    sellist.add(name)
    try:
        return om.MFnDependencyNode(sellist.getDependNode(0))
    except TypeError:
        return


class MetanObject(object):
    u"""
    """

    metan_class = None

    def __new__(cls, *args, **kws):
        import metan.dag as dag

        _api_objects = dict([(k, None) for k in ["_ApiCls", "_MFn", "_MDagPath", "_MObject",
                                                 "_MObjectHandle", "_mDependNode"]])
        _newobj = super(cls.__class__, cls).__new__(cls)

        if len(args) == 0:
            raise MetanArgumentError("{0}() takes one or more arguments (0 given)".format(cls.__name__))


        arg0 = args[0]

        # Case : Node or Attribute
        #   cls(u"pCube1")
        #   cls(u"pCube1.aaa")
        #   cls(u"pCube1.aaa.bbb")
        #   cls(u"pCube1.aaa[0]")
        #   cls(u"pCube1.aaa[0].bbb")
        if isinstance(arg0, basestring):

            # Case : Attribute
            #   cls(u"pCube1.aaa")
            #   cls(u"pCube1.aaa.bbb")
            #   cls(u"pCube1.aaa[0]")
            #   cls(u"pCube1.aaa[0].bbb")
            if u"." in arg0:
                if cls.__name__ == MetanObject.__name__:
                    return Attribute(arg0)

                attrnames = arg0.split(u".")
                arg0 = attrnames[0]
                _attrname = attrnames[1]
                _dependnode = to_dependencynode(arg0)

                #   cls(u"pCube1.aaa[0]")
                if u"[" in _attrname:

                    _attrname = _attrname.split(u"[")
                    _plug = _dependnode.findPlug(_dependnode.attribute(_attrname[0]), False)
                    _plug = _plug.elementByLogicalIndex(int(_attrname[-1][-2]))

                #   cls(u"pCube1.aaa")
                else:
                    _plug = _dependnode.findPlug(_dependnode.attribute(_attrname), False)

                for _attrname in attrnames[2:]:

                    #   cls(u"pCube1.aaa[0].bbb")
                    if u"[" in _attrname:
                        _attrname = _attrname.split(u"[")
                        _plug = _plug.child(_dependnode.attribute(_attrname[0]))
                        _plug = _plug.elementByLogicalIndex(int(_attrname[-1][-2]))

                    #   cls(u"pCube1.aaa.bbb")
                    else:
                        _plug = _plug.child(_dependnode.attribute(_attrname))

                _attribute = _plug.attribute()
                _api_objects["_mDependNode"] = _dependnode
                _api_objects["_MPlug"] = _plug
                _api_objects["_MObject"] = _attribute
                for k, v in _api_objects.items():
                    _newobj.__setattr__(k, v)
                return _newobj

            # Case : Node
            #   cls(u"pCube1")
            else:
                name = arg0
                sellist = om.MSelectionList()
                sellist.add(name)
                try:
                    _api_objects["_MDagPath"] = sellist.getDagPath(0)
                    _api_objects["_MObject"] = _api_objects["_MDagPath"].node()
                    if _api_objects["_MObject"].apiType() == om.MFn.kTransform and cls.__name__ == MetanObject.__name__:
                        return dag.Transform(name)
                    elif _api_objects["_MObject"].apiType() == om.MFn.kJoint and cls.__name__ == MetanObject.__name__:
                        return dag.Joint(name)
                    _api_objects["_MObjectHandle"] = om.MObjectHandle(_api_objects["_MObject"])
                except TypeError:
                    pass
                try:
                    _api_objects["_MObject"] = sellist.getDependNode(0)
                    _api_objects["_MObjectHandle"] = om.MObjectHandle(_api_objects["_MObject"])
                    _api_objects["_mDependNode"] = om.MFnDependencyNode(_api_objects["_MObject"])
                    _api_objects["_MFn"] = om.MFnDependencyNode(_api_objects["_MObject"])
                except TypeError:
                    pass

                for k, v in _api_objects.items():
                    _newobj.__setattr__(k, v)

                return _newobj

        # Case : Attribute
        #   cls(MPlug)
        #   cls(MPlug, u"aaa")
        elif isinstance(arg0, om.MPlug):
            _plug = arg0
            _dependnode = om.MFnDependencyNode(_plug.node())

            #   cls(MPlug, u"aaa")
            if len(args) == 2:
                if _plug.isElement:
                    _plug = _plug.child(_dependnode.attribute(args[1]))
                elif _plug.isArray:
                    _plug = _plug.elementByLogicalIndex(0)
                    _plug = _plug.child(_dependnode.attribute(args[1]))
                else:
                    _plug = _dependnode.findPlug(_dependnode.attribute(args[1]), False)

            _attribute = _plug.attribute()
            _api_objects["_mDependNode"] = _dependnode
            _api_objects["_MPlug"] = _plug
            _api_objects["_MObject"] = _attribute
            for k, v in _api_objects.items():
                _newobj.__setattr__(k, v)
            return _newobj

        # Case : Attribute
        #   cls(Attribute, u"aaa")
        #   cls(Attribute, u"aaa.bbb")
        #   cls(Attribute, u"aaa[0]")
        #   cls(Attribute, u"aaa[0].bbb")
        elif isinstance(arg0, Attribute):
            _mattr = arg0
            _attrname = args[1]
            _pplug = _mattr._MPlug
            _dependnode = _mattr._mDependNode

            if _pplug.isElement:
                if u"[" in _attrname:
                    _attrname = _attrname.split(u"[")
                    _plug = _pplug.child(_dependnode.attribute(_attrname[0]))
                    _plug = _plug.elementByLogicalIndex(int(_attrname[-1][-2]))
                else:
                    _plug = _pplug.child(_dependnode.attribute(_attrname))

            elif _pplug.isArray:
                _plug = _pplug.elementByLogicalIndex(0)
                if u"[" in _attrname:
                    _attrname = _attrname.split(u"[")
                    _plug = _plug.child(_dependnode.attribute(_attrname[0]))
                    _plug = _plug.elementByLogicalIndex(int(_attrname[-1][-2]))
                else:
                    _plug = _plug.child(_dependnode.attribute(_attrname))

            else:
                _plug = _dependnode.findPlug(_dependnode.attribute(_attrname), False)
                # print(_plug.name())
                """
                todo: Arrayのインデックスが[-1]になる問題

                m = mtn.M(u"pCubeShape1")
                # 全部文字列で取得するなら大丈夫
                mtn.M(u"pCubeShape1.vertexColor[0].vertexFaceColor[0].vertexFaceColorRGB.vertexFaceColorB").name()

                # 以下のケースはエラー発生
                m.vertexColor[0].vertexFaceColor[0].vertexFaceColorRGB.vertexFaceColorB.name()
                m.attr("vertexColor[0]").attr("vertexFaceColor")[0].attr("vertexFaceColorRGB").attr("vertexFaceColorB").name()

                """


            _attribute = _plug.attribute()
            _api_objects["_mDependNode"] = _dependnode
            _api_objects["_MPlug"] = _plug
            _api_objects["_MObject"] = _attribute
            for k, v in _api_objects.items():
                _newobj.__setattr__(k, v)
            return _newobj

        # Case : Attribute
        #   cls(u"pCube1","aaa")
        #   cls(u"pCube1","aaa[0]")
        #   cls(MFnDependencyNode,"aaa")
        #   cls(MFnDependencyNode,"aaa[0]")
        if len(args) == 2:
            _attrname = args[1]
            if cls.__name__ == MetanObject.__name__:
                return Attribute(arg0, _attrname)

            if isinstance(arg0, basestring):
                _dependnode = to_dependencynode(arg0)
            elif isinstance(arg0, om.MFnDependencyNode):
                _dependnode = arg0

            if u"[" in _attrname:
                _attrname = _attrname.split(u"[")
                _plug = _dependnode.findPlug(_dependnode.attribute(_attrname[0]), False)
                _plug = _plug.elementByLogicalIndex(int(_attrname[-1][-2]))
            else:
                _plug = _dependnode.findPlug(_dependnode.attribute(_attrname), False)


            _attribute = _plug.attribute()
            _api_objects["_mDependNode"] = _dependnode
            _api_objects["_MPlug"] = _plug
            _api_objects["_MObject"] = _attribute
            for k, v in _api_objects.items():
                _newobj.__setattr__(k, v)
            return _newobj



    def attr(self, attr):
        self.validCheck()
        attrname = self.name()+u"."+attr
        if cmds.objExists(attrname):
            return Attribute(self._mDependNode, attr)
        else:
            raise AttributeError("%r has no attribute or method named '%s'" % (self, attr))

    def __getattr__(self, attr):
        return self.attr(attr)


    # def __repr__(self):
    #     if self.metan_class:
    #         return '<Meta> {0}("{1}", type="{2}")'.format(self.__class__.__name__, self.__name(), self.nodeType())
    #     else:
    #         return '<Standard> {0}("{1}", type="{2}")'.format(self.__class__.__name__, self.__name(), self.nodeType())

    def __str__(self):
        return self.__repr__()

    def nodeType(self):
        if self._mDependNode:
            return self._mDependNode.typeName

    def __name(self):
        if self._MDagPath:
            return self._MDagPath.partialPathName()
        elif self._mDependNode:
            return self._MDependNode.name()

    def name(self):
        self.validCheck()
        return self.__name()


    def isValid(self):
        return self._MObjectHandle.isValid()

    def validCheck(self):
        if not self.isValid():
            raise MetanObjectNotFoundError(self.__name())


class Attribute(MetanObject):

    def attr(self, attr):
        try:
            return Attribute(self, attr)
        except RuntimeError:
            try:
                _attr = self._MPlug.partialName()+attr
                return Attribute(self, _attr)
            except RuntimeError:
                raise AttributeError("%r has no attribute or method named '%s'" % (self, attr))

    def __getattr__(self, attr):
        return self.attr(attr)

    def __repr__(self):
        return u'{0}("{1}")'.format(self.__class__.__name__, self.__name())

    def __str__(self):
        return self.__repr__()

    def __iter__(self):
        size = self.size()
        if size is None:
            raise TypeError("iter() returned non - iterator of type '{0}'".format(self.__class__.__name__))
        for i in range(size):
            yield self.__getitem__(i)

    def __getitem__(self, index):
        return Attribute(self._MPlug.elementByLogicalIndex(index))

    def __len__(self):
        size = self.size()
        if size is not None:
            return size
        else:
            raise TypeError("object of type '{0}' has no len()".format(self.__class__.__name__))

    def size(self):
        _mplug = self._MPlug
        if self._MPlug.isArray:
            return _mplug.numElements()

    def __name(self):
        return self.name().split(".")[-1]

    def name(self):
        return self._MPlug.name()

    def longName(self):
        return self.attrName(longName=True)

    def sortName(self):
        return self.attrName(longName=False)

    def nodeName(self):
        return self.name().split(".")[0]

    def attrName(self, longName=False):
        if longName:
            return self.__name()
        return self._MPlug.partialName()

    def getChildren(self):
        if self._MPlug.isCompound:
            return [Attribute(self._MPlug.child(i)) for i in range(self._MPlug.numChildren())]
        else:
            raise TypeError("Data type is not valid here")

    def _getPlugValue(self, plug):
        _obj = plug.attribute()
        _apitype = _obj.apiType()

        if _apitype in [om.MFn.kAttribute3Double, om.MFn.kAttribute3Float, om.MFn.kAttribute4Double,
                        om.MFn.kAttribute2Double, om.MFn.kAttribute2Float]:
            res = []
            _plug = None
            if plug.isArray:
                _count = plug.numElements()
                if _count == 0:
                    _plug = plug.elementByLogicalIndex(0)
                    return [self._getPlugValue(_plug)]

                for i in range(_count):
                    _plug = plug.elementByPhysicalIndex(i)
                    res.append(self._getPlugValue(_plug))
            else:
                _count = plug.numChildren()
                for i in range(_count):
                    _plug = plug.child(i)
                    res.append(self._getPlugValue(_plug))

            _child_apitype = _plug.attribute().apiType()

            if _count == 3:
                if _child_apitype in [om.MFn.kDoubleLinearAttribute, om.MFn.kFloatLinearAttribute]:
                    return om.MVector(res)
                elif _child_apitype in [om.MFn.kDoubleAngleAttribute, om.MFn.kFloatAngleAttribute]:
                    return om.MVector(res)

            return res

        elif _apitype in [om.MFn.kDoubleAngleAttribute, om.MFn.kFloatAngleAttribute]:
            angle_unit = om.MAngle.uiUnit()
            if angle_unit == om.MAngle.kDegrees:
                return plug.asMAngle().asDegrees()
            else:
                return plug.asDouble()

        elif _apitype in [om.MFn.kDoubleLinearAttribute, om.MFn.kFloatLinearAttribute]:
            return plug.asDouble()

        elif _apitype == om.MFn.kNumericAttribute:
            _mfnattr = om.MFnNumericAttribute(_obj)
            _type = _mfnattr.numericType()
            if _type == om.MFnNumericData.kBoolean:
                return plug.asBool()
            elif _type in [om.MFnNumericData.kShort, om.MFnNumericData.kInt, om.MFnNumericData.kLong, om.MFnNumericData.kByte]:
                return plug.asInt()
            elif _type in [om.MFnNumericData.kFloat, om.MFnNumericData.kDouble, om.MFnNumericData.kAddr]:
                return plug.asDouble()

        elif _apitype == om.MFn.kEnumAttribute:
            return plug.asInt()

        elif _apitype == om.MFn.kTypedAttribute:
            _mfnattr = om.MFnTypedAttribute(_obj)
            _type = _mfnattr.attrType()
            if _type == om.MFnData.kString:
                return plug.asString()
            elif _type == om.MFnData.kMatrix:
                if plug.isArray:
                    return om.MFnMatrixData(plug.elementByLogicalIndex(0).asMObject()).matrix()
                return om.MFnMatrixData(plug.asMObject()).matrix()

        elif _apitype == om.MFn.kCompoundAttribute:
            res = []
            _plug = None
            _count_children = plug.numChildren()
            for i in range(_count_children):
                _plug = plug.child(i)
                res.append(self._getPlugValue(_plug))
            return res

    def get(self):
        return self._getPlugValue(self._MPlug)

    def set(self, value):
        self.__setUseCmd(value)

    def _set(self, value):
        self.__setUseApi(value)

    def __setUseCmd(self, value):
        # todo: 型に応じて適切な値をset cmds.setAttr()を利用する
        cmds.setAttr(self._MPlug.name(), value)

    def __setUseApi(self, value):
        # todo: 型に応じて適切な値をset apiでsetする undo非サポート
        self._MPlug.setDouble(value)

