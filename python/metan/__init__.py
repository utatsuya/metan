# -*- coding:utf-8 -*-
from __future__ import print_function, absolute_import, division
import maya.cmds as cmds
from . import wrapclass as wc
from metan.dag import Transform, DagNode, Joint

# M = wc.MetanClass

def M(nodeName):
    nodetype = cmds.nodeType(nodeName)
    if nodetype == u"transform":
        return Transform(nodeName)
    elif nodetype == u"joint":
        return Joint(nodeName)
    else:
        return wc.MetanObject(nodeName)

