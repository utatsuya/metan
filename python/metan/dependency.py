# -*- coding:utf-8 -*-
from __future__ import print_function, absolute_import, division
from metan.wrapclass import MetanObject

class DependNode(MetanObject):
    u""""""

    def nodeType(self):
        if self._MFn:
            return self._MFn.typeName

class AnimCurve(DependNode):pass
class SkinCluster(DependNode):pass
