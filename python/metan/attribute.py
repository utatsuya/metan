# -*- coding:utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import maya.cmds as cmds
import maya.api.OpenMaya as om


class MetanAttr(object):

    def __new__(cls, *args, **kws):
        _api_objects = dict([(k, None) for k in ["_mDependNode", "_mPlug", "_mObject", "_mHandle"]])
        _cache = dict([(k, None) for k in ["_isCompound", "_numChildren", "_apiType", "_apiTypeStr"]])
        newobj = super(cls.__class__, cls).__new__(cls)

        _attrname = args[1]
        # if args[0].type() == om.MFn.kDependencyNode:
        if isinstance(args[0], om.MFnDependencyNode):
            _dependnode = args[0]
            _plug = _dependnode.findPlug(_dependnode.attribute(_attrname), False)
            _api_objects["_mDependNode"] = _dependnode

        # elif isinstance(args[0], om.MPlug):
        elif isinstance(args[0], MetanAttr):
            _pplug = args[0]
            _dependnode = _pplug._mDependNode
            _plug = _dependnode.findPlug(_dependnode.attribute(_attrname), False)

        _attribute = _plug.attribute()

        _api_objects["_mPlug"] = _plug
        _api_objects["_mObject"] = _attribute
        _cache["_isCompound"] = _plug.isCompound
        if _cache["_isCompound"]:
            _cache["_numChildren"] = _plug.numChildren()
        _cache["_apiType"] = _attribute.apiType()
        _cache["_apiTypeStr"] = _attribute.apiTypeStr

        for k, v in _api_objects.items():
            newobj.__setattr__(k, v)

        for k, v in _cache.items():
            newobj.__setattr__(k, v)

        return newobj

    def __getattr__(self, attr):
        # todo: refactor
        attrname = self._mPlug.name().split(".")[0] + "." + self._mPlug.partialName()+"."+attr
        attrname_ = self._mPlug.name().split(".")[0] + "." + self._mPlug.partialName()+attr
        # print attr
        # print attrname
        if cmds.objExists(attrname):
            return MetanAttr(self, attr)
        elif cmds.objExists(attrname_):
            _attr = self._mPlug.partialName()+attr
            return MetanAttr(self, _attr)
        else:
            # except AttributeError:
            raise AttributeError("%r has no attribute or method named '%s'" % (self, attr))

    def __repr__(self):
        return '{0}("{1}")'.format(self.__class__.__name__, self.name())

    def __str__(self):
        return self.__repr__()

    def name(self):
        return self._mPlug.name().split(".")[-1]

    def get(self):
        # todo: 型に応じて適切な値をget
        return self._mPlug.asDouble()

    def set(self, value):
        self.set_by_cmds(value)
        # self.set_by_api(value)

    def set_by_cmds(self, value):
        # todo: 型に応じて適切な値をset cmds.setAttr()を利用する
        cmds.setAttr(self._mPlug.name(), value)

    def set_by_api(self, value):
        # todo: 型に応じて適切な値をset apiでsetする undo非サポート
        self._mPlug.setDouble(value)

    # def valid(self):
    #     return self._mHandle.isValid()

