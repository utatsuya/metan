# -*- coding:utf-8 -*-
from __future__ import print_function, absolute_import, division
import maya.cmds as cmds
import maya.api.OpenMaya as om
import metan.attribute as att
from metan.exception import *


def to_object(name):
    sellist = om.MGlobal.getSelectionListByName(name)
    try:
        return sellist.getDagPath(0)
    except TypeError:
        mo = sellist.getDependNode(0)
        return om.MFnDependencyNode(mo)


class MetanObject(object):
    u"""
    """

    metan_class = None
    # _api_objects_ = {}

    def __new__(cls, *args, **kws):
        import metan.dag as dag

        _api_objects = dict([(k, None) for k in ["_ApiCls", "_MFn", "_MDagPath", "_MObject",
                                                 "_MObjectHandle", "_mDependNode"]])
        _newobj = super(cls.__class__, cls).__new__(cls)

        if len(args) == 0:
            raise MetanArgumentError("{0}() takes one or more arguments (0 given)".format(cls.__name__))

        arg = args[0]
        if isinstance(arg, basestring):
            name = arg
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
                # _transform = om.MFnTransform(_dagpath.transform())
            except TypeError:
                pass
            try:
                # _mo = sellist.getDependNode(0)
                _api_objects["_MObject"] = sellist.getDependNode(0)
                _api_objects["_MObjectHandle"] = om.MObjectHandle(_api_objects["_MObject"])
                _api_objects["_mDependNode"] = om.MFnDependencyNode(_api_objects["_MObject"])
                _api_objects["_MFn"] = om.MFnDependencyNode(_api_objects["_MObject"])
            except TypeError:
                pass

            for k, v in _api_objects.items():
                _newobj.__setattr__(k, v)

        return _newobj

    def attr(self, attr):
        self.validCheck()
        attrname = self.name()+u"."+attr
        if cmds.objExists(attrname):
            return att.Attribute(self._mDependNode, attr)
        else:
            raise AttributeError("%r has no attribute or method named '%s'" % (self, attr))

    def __getattr__(self, attr):
        return self.attr(attr)

    def __init__(self, *args, **kws):
        pass

    def __repr__(self):
        if self.metan_class:
            return '<Meta> {0}("{1}", type="{2}")'.format(self.__class__.__name__, self.__name(), self.nodeType())
        else:
            return '<Standard> {0}("{1}", type="{2}")'.format(self.__class__.__name__, self.__name(), self.nodeType())

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

