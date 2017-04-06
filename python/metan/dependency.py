# -*- coding:utf-8 -*-
from __future__ import print_function, absolute_import, division
import maya.cmds as cmds
from metan.wrapclass import MetanObject, Attribute

class DependNode(MetanObject):
    u""""""

    def listAttrStr(self, *args, **kwds):
        _name = self.name()
        attrnames = []
        if args:
            attrnames = cmds.listAttr([_name+"."+attr.split(".")[-1] for attr in args], **kwds)
        else:
            attrnames = cmds.listAttr(_name, **kwds)

        if not attrnames:
            return []
        else:
            return attrnames

    def _listAttr(self, *args, **kwds):
        if kwds or args:
            _name = self.name()
            return [Attribute(_name+"."+attr) for attr in self.listAttrStr(*args, **kwds)]
        else:
            return [Attribute(self._MFn.findPlug(self._MFn.attribute(i), False))
                    for i in range(self._MFn.attributeCount())]

    def nodeType(self):
        if self._MFn:
            return self._MFn.typeName

    def hasAttr(self, attr):
        if isinstance(attr, basestring):
            if u"[" in attr or u"." in attr:
                return cmds.objExists(self.name()+"."+attr)
            else:
                return self._MFn.hasAttribute(attr)
        elif attr.__class__.__name__ ==  Attribute.__name__:
            return self._MFn.hasAttribute(attr.attrName())


class AnimCurve(DependNode):pass
class SkinCluster(DependNode):pass
