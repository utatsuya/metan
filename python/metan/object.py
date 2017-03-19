# -*- coding:utf-8 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om


def to_object(name):
    sellist = om.MGlobal.getSelectionListByName(name)
    try:
        return sellist.getDagPath(0)
    except TypeError:
        mo = sellist.getDependNode(0)
        return om.MFnDependencyNode(mo)


class MetanObject(object):
    def __new__(cls, *args, **kws):

        _dagpath = None
        _dependnode = None
        _transform = None
        return_obj = super(cls.__class__, cls).__new__(cls)
        if not len(args):
            return return_obj
        arg = args[0]
        if isinstance(arg, str):
            name = arg
            sellist = om.MSelectionList()
            sellist.add(name)
            try:
                _dagpath = sellist.getDagPath(0)
                _transform = om.MFnTransform(_dagpath.transform())
            except TypeError:
                pass
            try:
                _mo = sellist.getDependNode(0)
                _dependnode = om.MFnDependencyNode(_mo)
            except TypeError:
                pass

            setattr(return_obj, "_dagpath", _dagpath)
            setattr(return_obj, "_transform", _transform)
            setattr(return_obj, "_dependnode", _dependnode)

        return return_obj

    def __getattr__(self, attr):
        attrname = self._transform.name()+"."+attr
        if cmds.objExists(attrname):
            return self._transform.findPlug(self._transform.attribute(attr), False)
        else:
            # except AttributeError:
            raise AttributeError("%r has no attribute or method named '%s'" % (self, attr))

    def __init__(self, *args, **kws):
        pass


class MayaNode(MetanObject):

    def __repr__(self):
        # return '{0}.{1}("{2}")'.format(self.__class__.__module__, self.__class__.__name__, self.name())
        return '{0}("{1}", type="{2}")'.format(self.__class__.__name__, self.name(), self.nodetype())
        return "{0} <node_type '{1}'> <node_name '{2}'>".format(self.__class__, self.nodetype(), self.name())
        return "%s(Wrapped Standard MayaNode, node: '%s')" % (self.__class__, self.name())

        return '<Wrapped MayaNode. type:{3}> {0}.{1}("{2}")'.format(self.__class__.__module__,
                                                                    self.__class__.__name__,
                                                                    self.name(),
                                                                    self.nodetype())

    def __str__(self):
        return self.__repr__()

    def nodetype(self):
        if self._dependnode:
            return self._dependnode.typeName

    def name(self):
        if self._dagpath:
            return self._dagpath.partialPathName()
        if self._dependnode:
            return self._dependnode.name()


class MetaNode(MayaNode):
    pass