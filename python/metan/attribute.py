# -*- coding:utf-8 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om


class MetanAttr(object):

    def __new__(cls, *args, **kws):
        _api_objects = dict([(k, None) for k in ["_mPlug", "_mObject", "_mHandle"]])
        newobj = super(cls.__class__, cls).__new__(cls)
        _dependnode = args[0]
        _attrname = args[1]

        _plug = _dependnode.findPlug(_dependnode.attribute(_attrname), False)
        _api_objects["_mPlug"] = _plug

        for k, v in _api_objects.items():
            newobj.__setattr__(k, v)

        return newobj

    def __repr__(self):
        return '{0}("{1}")'.format(self.__class__.__name__, self.name())

    def __str__(self):
        return self.__repr__()

    def name(self):
        return self._mPlug.name().split(".")[-1]

    def get(self):
        return

    def set(self, value):
        pass
