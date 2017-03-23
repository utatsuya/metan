# -*- coding:utf-8 -*-
from __future__ import print_function, absolute_import, division
import maya.cmds as cmds
import maya.api.OpenMaya as om
from metan.wrapclass import MetanObject, DependNode

class DagNode(DependNode):
    def testn(self):
        print(self.__class__)

class Transform(DagNode):
    def testn(self):
        print(self.__class__)

class Joint(Transform):
    def testn(self):
        print(self.__class__)
