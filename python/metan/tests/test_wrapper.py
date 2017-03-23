# -*- coding:utf-8 -*-
import unittest
import maya.cmds as cmds
import metan


class TestScene(unittest.TestCase):

    def test_getset(self):
        cmds.file(new=True, f=True)
        cube = cmds.polyCube()[0]
        print cube
        m = metan.M(u"pCube1")
        print 'm.t.get()', m.t.get()
        print 'm.translate.get()', m.translate.get()
        print 'm.tx.get()', m.tx.get()
        print 'm.translateX.get()', m.translateX.get()
        print 'm.t.x.get()', m.t.x.get()
        print 'm.translate.x.get()', m.translate.x.get()
        print 'm.t.tx.get()', m.t.tx.get()
        print 'm.translate.translateX.get()', m.translate.translateX.get()
        print " "
        print 'm.attr("t").get()', m.attr("t").get()
        print 'm.attr("translate").get()', m.attr("translate").get()
        print 'm.attr("tx").get()', m.attr("tx").get()
        print 'm.attr("translateX").get()', m.attr("translateX").get()
        print 'm.attr("t").x.get()', m.attr("t").x.get()
        print 'm.attr("translate").x.get()', m.attr("translate").x.get()
        print 'm.attr("t").tx.get()', m.attr("t").tx.get()
        print 'm.attr("translate").tx.get()', m.attr("translate").tx.get()
        print 'm.attr("t").attr("x").get()', m.attr("t").attr("x").get()
        print 'm.attr("translate").attr("x").get()', m.attr("translate").attr("x").get()
        print 'm.attr("t").attr("tx").get()', m.attr("t").attr("tx").get()
        print 'm.attr("translate").attr("translateX").get()', m.attr("translate").attr("translateX").get()
        print " "
        print 'm.m.get()', m.m.get()
        print 'm.matrix.get()', m.matrix.get()
        print 'm.pim.get()', m.pim.get()
        print 'm.parentInverseMatrix.get()', m.parentInverseMatrix.get()
        print 'm.pim[0].get()', m.pim[0].get()
        print 'm.parentInverseMatrix[0].get()', m.parentInverseMatrix[0].get()
        print 'm.attr("pim").get()', m.attr("pim").get()
        print 'm.attr("parentInverseMatrix").get()', m.attr("parentInverseMatrix").get()
        print 'm.attr("pim")[0].get()', m.attr("pim")[0].get()
        print 'm.attr("parentInverseMatrix")[0].get()', m.attr("parentInverseMatrix")[0].get()
        print 'm.attr("pim[0]").get()', m.attr("pim[0]").get()
        print 'm.attr("parentInverseMatrix[0]").get()', m.attr("parentInverseMatrix[0]").get()
        print "="*20

        cmds.circle()
        m = metan.M(u"nurbsCircleShape1")
        assert(m.wn.get() == [[0.0, 0.0, 1.0]])
        assert(m.attr("wn").get() == [[0.0, 0.0, 1.0]])
        assert(m.worldNormal.get() == [[0.0, 0.0, 1.0]])
        assert(m.attr("worldNormal").get() == [[0.0, 0.0, 1.0]])
        assert(m.wn[0].get() == [0.0, 0.0, 1.0])
        assert(m.attr("wn")[0].get() == [0.0, 0.0, 1.0])
        assert(m.attr("wn[0]").get() == [0.0, 0.0, 1.0])
        assert(m.worldNormal[0].get() == [0.0, 0.0, 1.0])
        assert(m.attr("worldNormal")[0].get() == [0.0, 0.0, 1.0])
        assert(m.attr("worldNormal[0]").get() == [0.0, 0.0, 1.0])
        assert(m.wn.wnx.get() == 0.0)
        assert(m.attr("wn").wnx.get() == 0.0)
        assert(m.attr("wn").attr("wnx").get() == 0.0)
        assert(m.worldNormal.wnx.get() == 0.0)
        assert(m.attr("worldNormal").wnx.get() == 0.0)
        assert(m.attr("worldNormal").attr("wnx").get() == 0.0)
        assert(m.worldNormal.worldNormalX.get() == 0.0)
        assert(m.attr("worldNormal").worldNormalX.get() == 0.0)
        assert(m.attr("worldNormal").attr("worldNormalX").get() == 0.0)
        assert(m.wn.x.get() == 0.0)
        assert(m.attr("wn").x.get() == 0.0)
        assert(m.attr("wn").attr("x").get() == 0.0)
        assert(m.worldNormal.x.get() == 0.0)
        assert(m.attr("worldNormal").x.get() == 0.0)
        assert(m.attr("worldNormal").attr("x").get() == 0.0)
        assert(m.worldNormal[0].wnx.get() == 0.0)
        assert(m.attr("worldNormal")[0].wnx.get() == 0.0)
        assert(m.attr("worldNormal")[0].attr("wnx").get() == 0.0)
        assert(m.attr("worldNormal[0]").wnx.get() == 0.0)
        assert(m.attr("worldNormal[0]").attr("wnx").get() == 0.0)
        assert(m.worldNormal[0].x.get() == 0.0)
        assert(m.attr("worldNormal")[0].x.get() == 0.0)
        assert(m.attr("worldNormal")[0].attr("x").get() == 0.0)
        assert(m.attr("worldNormal[0]").x.get() == 0.0)
        assert(m.attr("worldNormal[0]").attr("x").get() == 0.0)
        assert(m.worldNormal[0].worldNormalX.get() == 0.0)
        assert(m.attr("worldNormal")[0].worldNormalX.get() == 0.0)
        assert(m.attr("worldNormal")[0].attr("worldNormalX").get() == 0.0)
        assert(m.attr("worldNormal[0]").worldNormalX.get() == 0.0)
        assert(m.attr("worldNormal[0]").attr("worldNormalX").get() == 0.0)
        assert(m.mmv.get() == [0.0, 8.0])
        assert(m.minMaxValue.get() == [0.0, 8.0])
        assert(m.obcc.get() == [0.0, 0.0, 0.0])
        assert(m.attr("obcc").get() == [0.0, 0.0, 0.0])
        assert(m.objectColorRGB.get() == [0.0, 0.0, 0.0])
        assert(m.attr("objectColorRGB").get() == [0.0, 0.0, 0.0])
        assert(m.obcc.obcr.get() == 0.0)
        assert(m.attr("obcc").obcr.get() == 0.0)
        assert(m.attr("obcc").attr("obcr").get() == 0.0)
        assert(m.objectColorRGB.obcr.get() == 0.0)
        assert(m.attr("objectColorRGB").obcr.get() == 0.0)
        assert(m.attr("objectColorRGB").attr("obcr").get() == 0.0)
        assert(m.objectColorRGB.objectColorR.get() == 0.0)
        assert(m.attr("objectColorRGB").attr("objectColorR").get() == 0.0)
        assert(m.objectColorR.get() == 0.0)
        assert(m.attr("objectColorR").get() == 0.0)

        m = metan.M(u"pCubeShape1")
        assert(m.vertexColor[0].vertexFaceColor[0].get() == [[0.0, 0.0, 0.0], 1.0])
        assert(m.attr("vertexColor")[0].vertexFaceColor[0].get() == [[0.0, 0.0, 0.0], 1.0])
        assert(m.attr("vertexColor")[0].attr("vertexFaceColor")[0].get() == [[0.0, 0.0, 0.0], 1.0])
        assert(m.attr("vertexColor[0]").attr("vertexFaceColor")[0].get() == [[0.0, 0.0, 0.0], 1.0])
        # assert(m.attr("vertexColor[0]").attr("vertexFaceColor[0]").get() == [[0.0, 0.0, 0.0], 1.0])
        assert(m.vertexColor[0].vertexFaceColor[0].vertexFaceColorRGB.get() == [0.0, 0.0, 0.0])
        assert(m.vertexColor[0].vertexFaceColor[0].attr("vertexFaceColorRGB").get() == [0.0, 0.0, 0.0])
        assert(m.vertexColor[0].attr("vertexFaceColor")[0].vertexFaceColorRGB.get() == [0.0, 0.0, 0.0])
        assert(m.attr("vertexColor")[0].vertexFaceColor[0].vertexFaceColorRGB.get() == [0.0, 0.0, 0.0])
        assert(m.attr("vertexColor")[0].attr("vertexFaceColor")[0].vertexFaceColorRGB.get() == [0.0, 0.0, 0.0])
        assert(m.attr("vertexColor")[0].attr("vertexFaceColor")[0].attr("vertexFaceColorRGB").get() == [0.0, 0.0, 0.0])
        assert(m.attr("vertexColor[0]").attr("vertexFaceColor")[0].attr("vertexFaceColorRGB").get() == [0.0, 0.0, 0.0])
        # assert(m.attr("vertexColor[0]").attr("vertexFaceColor[0]").attr("vertexFaceColorRGB").get() == [0.0, 0.0, 0.0])

        # assert(m.vertexColor[0].vertexFaceColor[0].vertexFaceColorRGB.vertexFaceColorB.get() == 0.0)

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

