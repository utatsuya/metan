# -*- coding:utf-8 -*-
from __future__ import print_function, absolute_import, division
from maya.api import OpenMaya as om
from metan.dependency import DependNode
from metan.datatype.vector import Vector
from metan.datatype.quaternion import Quaternion

_MTransformationMatrix_ = om.MTransformationMatrix


class DagNode(DependNode):
    u""""""
    def fullPathName(self):
        self.validCheck()
        return self._MDagPath.fullPathName()

    def parent(self):
        # TODO: MetanObjectの呼び出し方これで大丈夫？
        # TODO: 最初の要素しか返していない
        import metan.wrapclass
        return metan.wrapclass.MetanObject(self._MFn.parent(0))

    def child(self):
        # TODO: MetanObjectの呼び出し方これで大丈夫？
        # TODO: 最初の要素しか返していない
        import metan.wrapclass
        return metan.wrapclass.MetanObject(self._MFn.child(0))


class Transform(DagNode):
    u""""""
    def getT(self, **kwargs):
        kwg_ws = kwargs.get(u'ws', False)
        if kwg_ws:
            m = self.attr(u'wm[0]').get()
            return Vector(m[12], m[13], m[14])
            # return self._MFn.translation(om.MSpace.kWorld)
        else:
            return Vector(self._MFn.translation())
            # m = self.attr(u'm').get()
            # return Vector(m[12], m[13], m[14])

    def getQ(self, **kwargs):
        kwg_ws = kwargs.get(u'ws', False)
        if kwg_ws:
            m = self.attr(u'wm[0]').get()
            tm = _MTransformationMatrix_(m)
            return Quaternion(tm.rotation(asQuaternion=True))
        else:
            return Quaternion(self._MFn.rotation(asQuaternion=True))

    def setQ(self, quat, **kwargs):
        kwg_ws = kwargs.get('ws', False)
        kwg_api = kwargs.get('api', False)
        tm = _MTransformationMatrix_()
        tm.setRotation(quat)
        if kwg_ws:
            # TODO:
            pass 
        else:
            if kwg_api:
                self._MFn.setRotation(quat, om.MSpace.kTransform)
            else:
                self._MFn.setRotation(quat, om.MSpace.kTransform)
                # TODO:
                # cmds.setAttr()


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



