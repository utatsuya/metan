# -*- coding:utf-8 -*-
import unittest
import maya.cmds as cmds
import metan


class TestScene(unittest.TestCase):

    def test_getset(self):
        cmds.file(new=True, f=True)
        cube = cmds.polyCube()[0]
        print cube
        m = metan.M("pCube1")
        print m.t.x.get()
        print m.t.tx.get()
        print m.tx.get()

    def runTest(self):
        self.test_getset()
