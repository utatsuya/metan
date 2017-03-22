# -*- coding:utf-8 -*-
import os
import unittest


def module_path_gen(directory, prefix=None):
    pathlist = []
    _, root = os.path.split(directory)
    for f in os.listdir(directory):
        if f.endswith(".pyc"):
            continue
        if f.startswith("__init__"):
            continue
        if f == "tests":
            continue
        if f.startswith("."):
            continue

        if prefix:
            pathlist.append(prefix + "." + root + "." + f.split(".")[0])
        else:
            pathlist.append(root + "." + f.split(".")[0])
    return pathlist


def reloader():
    _tests, _ = os.path.split(__file__)
    _metan, _ = os.path.split(_tests)
    modpath = module_path_gen(_metan) + module_path_gen(_tests, prefix="metan")
    for mp in modpath:
        mod = __import__(mp, globals(), locals(), ["*"])
        reload(mod)


def run():
    import metan.tests.test_wrapper
    reloader()
    suite = unittest.TestSuite()
    suite.addTest(metan.tests.test_wrapper.TestScene())
    suite.addTest(metan.tests.test_wrapper.TestScene2())
    unittest.TextTestRunner().run(suite)
