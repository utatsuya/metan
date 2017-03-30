# -*- coding:utf-8 -*-
from __future__ import print_function, absolute_import, division
import maya.api.OpenMaya as om

__all__ = [u"Matrix"]

class Matrix(om.MMatrix):
    def __repr__(self):
        return u'{0}{1}'.format(self.__class__.__name__, str(self))
