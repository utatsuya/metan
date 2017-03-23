# -*- coding:utf-8 -*-
from __future__ import print_function, absolute_import, division
import maya.cmds as cmds
import maya.api.OpenMaya as om
from .import attribute as att
from . import dag as dag


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

    def __new__(cls, *args, **kws):

        _api_objects = dict([(k, None) for k in ["_mDagPath", "_mDependNode", "_mObject", "_mHandle"]])
        _newobj = super(cls.__class__, cls).__new__(cls)

        if not len(args):
            # todo: create?
            return _newobj

        arg = args[0]
        if isinstance(arg, (str, unicode)):
            name = arg
            sellist = om.MSelectionList()
            sellist.add(name)
            try:
                # _dagpath = sellist.getDagPath(0)
                _api_objects["_mDagPath"] = sellist.getDagPath(0)
                _api_objects["_mObject"] = _api_objects["_mDagPath"].node()
                if _api_objects["_mObject"].apiType() == om.MFn.kTransform and cls.__name__ == MetanObject.__name__:
                    return dag.Transform(name)
                elif _api_objects["_mObject"].apiType() == om.MFn.kJoint and cls.__name__ == MetanObject.__name__:
                    return dag.Joint(name)
                _api_objects["_mHandle"] = om.MObjectHandle(_api_objects["_mObject"])
                # _transform = om.MFnTransform(_dagpath.transform())
            except TypeError:
                pass
            try:
                # _mo = sellist.getDependNode(0)
                _api_objects["_mObject"] = sellist.getDependNode(0)
                _api_objects["_mHandle"] = om.MObjectHandle(_api_objects["_mObject"])
                _api_objects["_mDependNode"] = om.MFnDependencyNode(_api_objects["_mObject"])
            except TypeError:
                pass

            for k, v in _api_objects.items():
                _newobj.__setattr__(k, v)

        return _newobj

    def attr(self, attr):
        attrname = self.name()+u"."+attr
        if cmds.objExists(attrname):
            return att.Attribute(self._mDependNode, attr)
            # return self._mDependNode.findPlug(self._mDependNode.attribute(attr), False)
        else:
            # except AttributeError:
            raise AttributeError("%r has no attribute or method named '%s'" % (self, attr))

    def __getattr__(self, attr):
        return self.attr(attr)

    def __init__(self, *args, **kws):
        pass

    def __repr__(self):
        if self.metan_class:
            return '<Meta> {0}("{1}", type="{2}")'.format(self.__class__.__name__, self.name(), self.nodeType())
        else:
            return '<Standard> {0}("{1}", type="{2}")'.format(self.__class__.__name__, self.name(), self.nodeType())

    def __str__(self):
        return self.__repr__()

    def nodeType(self):
        if self._mDependNode:
            return self._mDependNode.typeName

    def name(self):
        if not self.isValid():
            raise RuntimeError

        if self._mDagPath:
            return self._mDagPath.partialPathName()
        elif self._mDependNode:
            return self._mDependNode.name()

    def isValid(self):
        return self._mHandle.isValid()

class DependNode(MetanObject):
    pass

class MetanClass(MetanObject):

    def testn(self):
        pass


class OrgMetaNode(MetanClass):

    def testn(self):
        pass
