# -*- coding:utf-8 -*-

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
            # obj = to_object(arg)
            # sellist = om.MGlobal.getSelectionListByName(name)
            sellist = om.MSelectionList()
            sellist.add(name)
            try:
                _dagpath = sellist.getDagPath(0)
                _transform = om.MFnTransform(_dagpath.transform())
                mplugs = [_transform.findPlug(_transform.attribute(i), False) for i in range(_transform.attributeCount())]
                # mplugs = [om.MFnAttribute(_transform.attribute(i)) for i in range(_transform.attributeCount())]
                [return_obj.__setattr__(p.name().split(".")[-1], p) for p in mplugs]
                # for i in range(_transform.attributeCount()):
                #     mattr = om.MFnAttribute(_transform.attribute(i))
                #     # setattr(return_obj, mattr.name, mattr)
                #     return_obj.__setattr__(mattr.name, mattr)
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

    def __init__(self, *args, **kws):
        pass

    # def __getattribute__(self, item):
    #     print "__getattribute__",item
