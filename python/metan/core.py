# -*- coding:utf-8 -*-
from __future__ import print_function, absolute_import, division
import maya.cmds as cmds
from metan.datatype.euler import EulerRotation
from metan.datatype.matrix import Matrix
from metan.datatype.quaternion import Quaternion
from metan.datatype.vector import Vector
from metan.wrapclass import MetanObject, Attribute
from metan.dag import Transform, DagNode, Joint
from metan.dependency import DependNode, AnimCurve, SkinCluster

M = MetanObject


def selected(*args, **kwds):
    kwds["sl"]=True
    items = cmds.ls(**kwds)
    if items:
        return [MetanObject(name) for name in items]
    else:
        return []
