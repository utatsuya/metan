# -*- coding:utf-8 -*-
from __future__ import print_function, absolute_import, division
from metan.dependency import DependNode

class DagNode(DependNode):
    u""""""

class Transform(DagNode):
    u""""""

class Joint(Transform):
    u""""""

class Mesh(DagNode):pass
class Camera(DagNode):pass
class NurbsCurve(DagNode):pass
class NurbsSurface(DagNode):pass
class ObjectSet(DagNode):pass
class AnimLayer(ObjectSet):pass
class Constraint(Transform):pass
class IkEffector(Transform):pass
class IkHandle(Transform):pass



