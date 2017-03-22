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
        print "="*20
        print 'm.m.get()', m.m.get()
        print 'm.pim.get()', m.pim.get()
        print 'm.pim[0].get()', m.pim[0].get()
        print 'm.attr("pim").get()', m.attr("pim").get()
        print 'm.attr("pim")[0].get()', m.attr("pim")[0].get()
        print 'm.attr("pim[0]").get()', m.attr("pim[0]").get()

    def runTest(self):
        self.test_getset()


class TestScene2(unittest.TestCase):

    def test_getset(self):
        cmds.file(new=True, f=True)
        cube = cmds.polyCube()[0]
        print cube
        m = metan.M("pCube1")
        print 'm.t.x.get()', m.t.x.get()

    def runTest(self):
        self.test_getset()

