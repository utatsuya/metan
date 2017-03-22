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
        print 'm.t.x.get()', m.t.x.get()
        print 'm.t.tx.get()', m.t.tx.get()
        print 'm.tx.get()', m.tx.get()
        print 'm.t.get()', m.t.get()
        print 'm.attr("t").get()', m.attr("t").get()
        print 'm.attr("tx").get()', m.attr("tx").get()
        print 'm.attr("t").x.get()', m.attr("t").x.get()
        print 'm.attr("t").tx.get()', m.attr("t").tx.get()
        print 'm.attr("t").attr("x").get()', m.attr("t").attr("x").get()
        print 'm.attr("t").attr("tx").get()', m.attr("t").attr("tx").get()

    def runTest(self):
        self.test_getset()
