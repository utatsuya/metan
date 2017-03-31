# -*- coding:utf-8 -*-
from __future__ import print_function, absolute_import, division
import math
import maya.cmds as cmds
import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as oma
from maya.OpenMaya import MGlobal as _api1_MGlobal

from metan.exception import *
from metan.datatype.euler import EulerRotation
from metan.datatype.matrix import Matrix
from metan.datatype.quaternion import Quaternion
from metan.datatype.vector import Vector


class TESTMObjectHandle(object):
    u"""これは仮のMObjectHandleです
    """
    def __init__(self, *args, **kws):
        pass
    def isValid(self):
        return True

# todo: バージョンで分けるような処理はここじゃなくてファイルを別にする
current_version = _api1_MGlobal.apiVersion()
_MFn_MFnSkinCluster = om.MFnDependencyNode
_MFn_MFnAnimCurve = om.MFnDependencyNode
_MFn_MObjectHandle = TESTMObjectHandle

if current_version >= 201600:
    _MFn_MFnSkinCluster = oma.MFnSkinCluster
    _MFn_MFnAnimCurve = oma.MFnAnimCurve
    _MFn_MObjectHandle = om.MObjectHandle



def to_dependencynode(name):
    sellist = om.MSelectionList()
    sellist.add(name)
    try:
        _mobj = sellist.getDependNode(0)
        return om.MFnDependencyNode(_mobj), _mobj
    except TypeError:
        return

def set_api_objects(cls, api_objs):
    _newobj = super(cls.__class__, cls).__new__(cls)
    for k, _obj in api_objs.items():
            _newobj.__setattr__(k, _obj)

    return _newobj


class MetanObject(object):
    u"""
    """

    metan_class = None

    def __new__(cls, *args, **kws):
        import metan.dag as dag
        import metan.dependency as dep

        mobj = None
        mobjh = None
        mdag = None
        mfn = None
        mplg = None

        if len(args) == 0:
            raise MetanArgumentError("{0}() takes 1 or 2 arguments (0 given)".format(cls.__name__))
        elif len(args) > 2:
            raise MetanArgumentError("{0}() takes at most 2 arguments ({1} given)".format(cls.__name__, len(args)))


        arg0 = args[0]

        # Case : Attribute
        #   cls(u"pCube1","aaa")
        #   cls(u"pCube1","aaa[0]")
        #   cls(MFnDependencyNode,"aaa")
        #   cls(MFnDependencyNode,"aaa[0]")
        if len(args) == 2:
            if isinstance(arg0, om.MFnDependencyNode):
                arg0 = arg0.name() + u"." + unicode(args[1])
            elif isinstance(arg0, basestring):
                arg0 = arg0 + u"." + unicode(args[1])

            if cls.__name__ == MetanObject.__name__:
                return Attribute(arg0)

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
                mfn, _mobj= to_dependencynode(arg0)
                mobjh = _MFn_MObjectHandle(_mobj)

                #   cls(u"pCube1.aaa[0]")
                if u"[" in _attrname:

                    _attrname = _attrname.split(u"[")
                    mplg = mfn.findPlug(mfn.attribute(_attrname[0]), False)
                    mplg = mplg.elementByLogicalIndex(int(_attrname[-1][-2]))

                #   cls(u"pCube1.aaa")
                else:
                    mplg = mfn.findPlug(mfn.attribute(_attrname), False)

                for _attrname in attrnames[2:]:

                    #   cls(u"pCube1.aaa[0].bbb")
                    if u"[" in _attrname:
                        _attrname = _attrname.split(u"[")
                        mplg = mplg.child(mfn.attribute(_attrname[0]))
                        mplg = mplg.elementByLogicalIndex(int(_attrname[-1][-2]))

                    #   cls(u"pCube1.aaa.bbb")
                    else:
                        if mplg.isCompound and mplg.isArray:
                            mplg = mplg.elementByLogicalIndex(0)
                            mplg = mplg.child(mfn.attribute(_attrname))
                        else:
                            mplg = mplg.child(mfn.attribute(_attrname))

                # _kws = {"_MPlug":mplg, "_MFn":mfn, "_MObject":mplg.attribute()}
                _kws = {"_MPlug":mplg, "_MFn":mfn, "_MObject":mplg.attribute(), "_MObjectHandle":mobjh}
                return set_api_objects(cls, _kws)

            # Case : Node
            #   cls(u"pCube1")
            else:
                name = arg0
                sellist = om.MSelectionList()
                sellist.add(name)
                try:
                    mobj = sellist.getDependNode(0)
                    if cls.__name__ == MetanObject.__name__:
                        if mobj.apiType() == om.MFn.kTransform:
                            return dag.Transform(name)
                        elif mobj.apiType() == om.MFn.kJoint:
                            return dag.Joint(name)
                        elif mobj.apiType() == om.MFn.kSkinClusterFilter:
                            return dep.SkinCluster(name)
                        elif mobj.hasFn(om.MFn.kAnimCurve):
                            return dep.AnimCurve(name)
                        else:
                            return dep.DependNode(name)

                    # mobjh = om.MObjectHandle(mobj)
                    mobjh = _MFn_MObjectHandle(mobj)
                    mfn = om.MFnDependencyNode(mobj)
                except TypeError:
                    pass
                try:
                    mdag = sellist.getDagPath(0)
                    if cls.__name__ in [dag.Transform.__name__, dag.Joint.__name__]:
                        mfn = om.MFnTransform(mobj)
                    elif cls.__name__ in [dep.SkinCluster.__name__]:
                        mfn = _MFn_MFnSkinCluster(mobj)
                    elif cls.__name__ in [dep.AnimCurve.__name__]:
                        mfn = _MFn_MFnAnimCurve(mobj)
                except TypeError:
                    pass

                _kws = {"_MDagPath":mdag, "_MFn":mfn, "_MObjectHandle":mobjh, "_MObject":mobj}
                return set_api_objects(cls, _kws)


        # Case : Attribute
        #   cls(MPlug)
        #   cls(MPlug, u"aaa")
        elif isinstance(arg0, om.MPlug):
            _plug = arg0
            _mobj = _plug.node()
            mfn = om.MFnDependencyNode(_mobj)
            mobjh = _MFn_MObjectHandle(_mobj)

            #   cls(MPlug)
            if len(args) == 1:
                mplg = _plug

            #   cls(MPlug, u"aaa")
            elif len(args) == 2:
                if _plug.isElement:
                    mplg = _plug.child(mfn.attribute(args[1]))
                elif _plug.isArray:
                    _plug = _plug.elementByLogicalIndex(0)
                    mplg = _plug.child(mfn.attribute(args[1]))
                else:
                    mplg = mfn.findPlug(mfn.attribute(args[1]), False)

            _kws = {"_MPlug":mplg, "_MFn":mfn, "_MObject":mplg.attribute(), "_MObjectHandle":mobjh}
            return set_api_objects(cls, _kws)



    def attr(self, attr):
        self.validCheck()
        attrname = self.name()+u"."+attr
        if cmds.objExists(attrname):
            return Attribute(attrname)
        else:
            raise AttributeError("%r has no attribute or method named '%s'" % (self, attr))

    def __getattr__(self, attr):
        return self.attr(attr)


    def __repr__(self):
            return '{0}("{1}")'.format(self.__class__.__name__, self.__name())

    def __str__(self):
        return self.__repr__()

    def __hash__(self):
        return self._MObjectHandle.hashCode()

    def __eq__(self, other):
        if hasattr(other, "_MObject"):
            return self._MObject == other._MObject
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __name(self):
        if self._MDagPath:
            return self._MDagPath.partialPathName()
        elif self._MFn:
            return self._MFn.name()

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
        # self.validCheck()
        attrname = self.name()+u"."+attr
        if cmds.objExists(attrname):
            return Attribute(attrname)
        else:
            attrname = self.name() + u"." + self._MPlug.partialName() + attr
            if cmds.objExists(attrname):
                return Attribute(attrname)
            else:
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


    def __eq__(self, other):
        if hasattr(other, "_MObject"):
            try:
                _selfindex = self._MPlug.logicalIndex()
            except:
                _selfindex = None
            try:
                _otherindex = other._MPlug.logicalIndex()
            except:
                _otherindex = None
            return self._MObject == other._MObject and _selfindex == _otherindex
        else:
            return False

    def __hash__(self):
        return (self._MObjectHandle.hashCode(), self.longName()).__hash__()

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

    def shortName(self):
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

    def _setDouble(self, plg, value, **kwds):
        # if u"api" in kwds:
        if kwds.get(u"api"):
            plg.setDouble(value)
        else:
            cmds.setAttr(plg.name(), value)

    def _setPlugValue(self, *value, **kwds):
        if u"plug" in kwds:
            # todo: type check
            plug = kwds["plug"]
            _obj = plug.attribute()
        else:
            plug = self._MPlug
            _obj = self._MObject
        _apitype = _obj.apiType()
        _value = value
        _value0 = value[0]

        if len(_value) == 1:
            if isinstance(_value0, (list, tuple)):
                _value = _value0
            elif isinstance(_value0, Vector):
                _value = (_value0.x, _value0.y, _value0.z)

        # print("apitype", _obj.apiTypeStr)

        if _apitype in [om.MFn.kAttribute3Double, om.MFn.kAttribute3Float,
                        om.MFn.kAttribute2Double, om.MFn.kAttribute2Float,
                        om.MFn.kAttribute4Double]:

            if plug.isArray:
                raise MetanRuntimeError(u"The attribute '{0}' is a multi.".format(plug.name()))
            else:
                _count = plug.numChildren()
                if len(_value) != _count:
                    raise MetanArgumentError(u"{0} elements are required for this attribute (given {1})"
                                             .format(_count, len(_value)))
                if not kwds.get("api"):
                    _childtype = plug.child(0).attribute().apiType()
                    if _childtype in [om.MFn.kDoubleLinearAttribute, om.MFn.kFloatLinearAttribute]:
                        distance_unit = om.MDistance.uiUnit()
                        _value = [om.MDistance(_va, om.MDistance.kCentimeters).asUnits(distance_unit) for _va in _value]
                        # _distance = om.MDistance(_value0, om.MDistance.kCentimeters)
                        # _value0 = _distance.asUnits(distance_unit)
                        cmds.setAttr(plug.name(), *_value)

                    elif _childtype in [om.MFn.kDoubleAngleAttribute, om.MFn.kFloatAngleAttribute]:
                        angle_unit = om.MAngle.uiUnit()
                        if angle_unit == om.MAngle.kDegrees:
                            _value = [math.degrees(agl) for agl in _value]
                        cmds.setAttr(plug.name(), *_value)
                    else:
                        cmds.setAttr(plug.name(), *_value)
                    return

                for i in range(_count):
                    _plug = plug.child(i)
                    kwds["plug"] = _plug
                    self._setPlugValue(_value[i], **kwds)


        elif _apitype in [om.MFn.kDoubleLinearAttribute, om.MFn.kFloatLinearAttribute]:
            if kwds.get(u"api"):
                plug.setDouble(_value0)
            else:
                distance_unit = om.MDistance.uiUnit()
                _distance = om.MDistance(_value0, om.MDistance.kCentimeters)
                _value0 = _distance.asUnits(distance_unit)
                cmds.setAttr(plug.name(), _value0)

        elif _apitype == om.MFn.kNumericAttribute:
            _mfnattr = om.MFnNumericAttribute(_obj)
            _type = _mfnattr.numericType()
            # print("numeric type", _type)

            if _type == om.MFnNumericData.kBoolean:
                if kwds.get(u"api"):
                    plug.setBool(_value0)
                    return
            elif _type in [om.MFnNumericData.kShort, om.MFnNumericData.kInt, om.MFnNumericData.kLong, om.MFnNumericData.kByte]:
                if kwds.get(u"api"):
                    plug.setInt(_value0)
                    return
            elif _type in [om.MFnNumericData.kFloat, om.MFnNumericData.kDouble, om.MFnNumericData.kAddr]:
                if kwds.get(u"api"):
                    plug.setDouble(_value0)
                    return
            cmds.setAttr(plug.name(), _value0)

        elif _apitype in [om.MFn.kDoubleAngleAttribute, om.MFn.kFloatAngleAttribute]:
            if kwds.get(u"api"):
                plug.setDouble(_value0)
            else:
                angle_unit = om.MAngle.uiUnit()
                if angle_unit == om.MAngle.kDegrees:
                    _value0 = math.degrees(_value0)
                cmds.setAttr(plug.name(), _value0)

        elif _apitype == om.MFn.kEnumAttribute:
            if kwds.get(u"api"):
                plug.setDouble(_value0)
            else:
                cmds.setAttr(plug.name(), _value0)

        elif _apitype == om.MFn.kTypedAttribute:
            _mfnattr = om.MFnTypedAttribute(_obj)
            _type = _mfnattr.attrType()
            if _type == om.MFnData.kString:
                if kwds.get(u"api"):
                    plug.setString(unicode(_value0))
                else:
                    cmds.setAttr(plug.name(), unicode(_value0), type="string")

            elif _type == om.MFnData.kMatrix:
                if plug.isArray:
                    pass

        elif _apitype == om.MFn.kCompoundAttribute:pass

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

            # _child_apitype = _plug.attribute().apiType()
            # if _count == 3:
            #     if _child_apitype in [om.MFn.kDoubleLinearAttribute, om.MFn.kFloatLinearAttribute]:
            #         return om.MVector(res)
            #     elif _child_apitype in [om.MFn.kDoubleAngleAttribute, om.MFn.kFloatAngleAttribute]:
            #         return om.MVector(res)

            return res

        elif _apitype in [om.MFn.kDoubleAngleAttribute, om.MFn.kFloatAngleAttribute]:
            return plug.asDouble()
            # angle_unit = om.MAngle.uiUnit()
            # if angle_unit == om.MAngle.kDegrees:
            #     return plug.asMAngle().asDegrees()
            # else:
            #     return plug.asDouble()

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
                    return Matrix(om.MFnMatrixData(plug.elementByLogicalIndex(0).asMObject()).matrix())
                return Matrix(om.MFnMatrixData(plug.asMObject()).matrix())

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

    def set(self, *value):
        self._setPlugValue(*value)

    def _set(self, *value):
        self._setPlugValue(*value, api=True)

    def _set_cmd(self, *value):
        cmds.setAttr(self._MPlug.name(), *value)

    def _set_api(self, *value):
        self._MPlug.setDouble(*value)


