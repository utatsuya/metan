# -*- coding:utf-8 -*-
"""

tmp = '''def {0}(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.{0}(*_args, **kwargs))

'''
for cmdstr in cmds.help("*", list=True):
    if cmdstr in ["exec"]:
        continue
    print(tmp.format(cmdstr))

"""

from __future__ import print_function, absolute_import, division
from maya import cmds as _cmds
from . import wrapclass as _wpc


def ATOMTemplateOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ATOMTemplateOptions(*_args, **kwargs))


def AbortCurrentTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AbortCurrentTool(*_args, **kwargs))


def ActivateGlobalScreenSlider(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ActivateGlobalScreenSlider(*_args, **kwargs))


def ActivateGlobalScreenSliderModeMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ActivateGlobalScreenSliderModeMarkingMenu(*_args, **kwargs))


def ActivateViewport20(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ActivateViewport20(*_args, **kwargs))


def AddAnimationOffset(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddAnimationOffset(*_args, **kwargs))


def AddAnimationOffsetOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddAnimationOffsetOptions(*_args, **kwargs))


def AddAttribute(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddAttribute(*_args, **kwargs))


def AddBlendShape(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddBlendShape(*_args, **kwargs))


def AddBlendShapeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddBlendShapeOptions(*_args, **kwargs))


def AddBoatLocator(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddBoatLocator(*_args, **kwargs))


def AddBoatLocatorOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddBoatLocatorOptions(*_args, **kwargs))


def AddCombinationTarget(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddCombinationTarget(*_args, **kwargs))


def AddCombinationTargetOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddCombinationTargetOptions(*_args, **kwargs))


def AddCurvesToHairSystem(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddCurvesToHairSystem(*_args, **kwargs))


def AddDivisions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddDivisions(*_args, **kwargs))


def AddDivisionsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddDivisionsOptions(*_args, **kwargs))


def AddDynamicBuoy(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddDynamicBuoy(*_args, **kwargs))


def AddDynamicBuoyOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddDynamicBuoyOptions(*_args, **kwargs))


def AddEdgeDivisions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddEdgeDivisions(*_args, **kwargs))


def AddEdgeDivisionsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddEdgeDivisionsOptions(*_args, **kwargs))


def AddFaceDivisions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddFaceDivisions(*_args, **kwargs))


def AddFaceDivisionsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddFaceDivisionsOptions(*_args, **kwargs))


def AddFloorContactPlane(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddFloorContactPlane(*_args, **kwargs))


def AddHolder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddHolder(*_args, **kwargs))


def AddHolderOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddHolderOptions(*_args, **kwargs))


def AddInBetweenTargetShape(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddInBetweenTargetShape(*_args, **kwargs))


def AddInBetweenTargetShapeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddInBetweenTargetShapeOptions(*_args, **kwargs))


def AddInbetween(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddInbetween(*_args, **kwargs))


def AddInfluence(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddInfluence(*_args, **kwargs))


def AddInfluenceOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddInfluenceOptions(*_args, **kwargs))


def AddKeyToolActivate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddKeyToolActivate(*_args, **kwargs))


def AddKeyToolDeactivate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddKeyToolDeactivate(*_args, **kwargs))


def AddKeysTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddKeysTool(*_args, **kwargs))


def AddKeysToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddKeysToolOptions(*_args, **kwargs))


def AddOceanDynamicLocator(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddOceanDynamicLocator(*_args, **kwargs))


def AddOceanDynamicLocatorOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddOceanDynamicLocatorOptions(*_args, **kwargs))


def AddOceanPreviewPlane(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddOceanPreviewPlane(*_args, **kwargs))


def AddOceanSurfaceLocator(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddOceanSurfaceLocator(*_args, **kwargs))


def AddPfxToHairSystem(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddPfxToHairSystem(*_args, **kwargs))


def AddPointsTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddPointsTool(*_args, **kwargs))


def AddPondBoatLocator(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddPondBoatLocator(*_args, **kwargs))


def AddPondBoatLocatorOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddPondBoatLocatorOptions(*_args, **kwargs))


def AddPondDynamicBuoy(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddPondDynamicBuoy(*_args, **kwargs))


def AddPondDynamicBuoyOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddPondDynamicBuoyOptions(*_args, **kwargs))


def AddPondDynamicLocator(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddPondDynamicLocator(*_args, **kwargs))


def AddPondDynamicLocatorOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddPondDynamicLocatorOptions(*_args, **kwargs))


def AddPondSurfaceLocator(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddPondSurfaceLocator(*_args, **kwargs))


def AddSelectionAsCombinationTarget(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddSelectionAsCombinationTarget(*_args, **kwargs))


def AddSelectionAsCombinationTargetOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddSelectionAsCombinationTargetOptions(*_args, **kwargs))


def AddSelectionAsInBetweenTargetShape(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddSelectionAsInBetweenTargetShape(*_args, **kwargs))


def AddSelectionAsInBetweenTargetShapeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddSelectionAsInBetweenTargetShapeOptions(*_args, **kwargs))


def AddSelectionAsTargetShape(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddSelectionAsTargetShape(*_args, **kwargs))


def AddSelectionAsTargetShapeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddSelectionAsTargetShapeOptions(*_args, **kwargs))


def AddShrinkWrapSurfaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddShrinkWrapSurfaces(*_args, **kwargs))


def AddTargetShape(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddTargetShape(*_args, **kwargs))


def AddTargetShapeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddTargetShapeOptions(*_args, **kwargs))


def AddTimeWarp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddTimeWarp(*_args, **kwargs))


def AddToCharacterSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddToCharacterSet(*_args, **kwargs))


def AddToContainer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddToContainer(*_args, **kwargs))


def AddToContainerOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddToContainerOptions(*_args, **kwargs))


def AddToCurrentScene3dsMax(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddToCurrentScene3dsMax(*_args, **kwargs))


def AddToCurrentSceneMotionBuilder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddToCurrentSceneMotionBuilder(*_args, **kwargs))


def AddToCurrentSceneMudbox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddToCurrentSceneMudbox(*_args, **kwargs))


def AddWire(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddWire(*_args, **kwargs))


def AddWireOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddWireOptions(*_args, **kwargs))


def AddWrapInfluence(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AddWrapInfluence(*_args, **kwargs))


def AffectSelectedObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AffectSelectedObject(*_args, **kwargs))


def AimConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AimConstraint(*_args, **kwargs))


def AimConstraintOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AimConstraintOptions(*_args, **kwargs))


def Air(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Air(*_args, **kwargs))


def AirOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AirOptions(*_args, **kwargs))


def AlignCameraToPolygon(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AlignCameraToPolygon(*_args, **kwargs))


def AlignCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AlignCurve(*_args, **kwargs))


def AlignCurveOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AlignCurveOptions(*_args, **kwargs))


def AlignSurfaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AlignSurfaces(*_args, **kwargs))


def AlignSurfacesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AlignSurfacesOptions(*_args, **kwargs))


def AlignUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AlignUV(*_args, **kwargs))


def AlignUVOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AlignUVOptions(*_args, **kwargs))


def AnimLayerRelationshipEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AnimLayerRelationshipEditor(*_args, **kwargs))


def AnimationSnapshot(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AnimationSnapshot(*_args, **kwargs))


def AnimationSnapshotOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AnimationSnapshotOptions(*_args, **kwargs))


def AnimationSweep(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AnimationSweep(*_args, **kwargs))


def AnimationSweepOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AnimationSweepOptions(*_args, **kwargs))


def AnimationTurntable(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AnimationTurntable(*_args, **kwargs))


def AnimationTurntableOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AnimationTurntableOptions(*_args, **kwargs))


def ApexClothingPreview(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ApexClothingPreview(*_args, **kwargs))


def ApexValuesPaintingFloodCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ApexValuesPaintingFloodCmd(*_args, **kwargs))


def AppendToHairCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AppendToHairCache(*_args, **kwargs))


def AppendToHairCacheOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AppendToHairCacheOptions(*_args, **kwargs))


def AppendToPolygonTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AppendToPolygonTool(*_args, **kwargs))


def AppendToPolygonToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AppendToPolygonToolOptions(*_args, **kwargs))


def ApplySettingsToLastStroke(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ApplySettingsToLastStroke(*_args, **kwargs))


def ApplySettingsToSelectedStroke(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ApplySettingsToSelectedStroke(*_args, **kwargs))


def ArcLengthTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ArcLengthTool(*_args, **kwargs))


def ArchiveScene(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ArchiveScene(*_args, **kwargs))


def ArchiveSceneOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ArchiveSceneOptions(*_args, **kwargs))


def Art3dPaintTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Art3dPaintTool(*_args, **kwargs))


def Art3dPaintToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Art3dPaintToolOptions(*_args, **kwargs))


def ArtPaintAttrTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ArtPaintAttrTool(*_args, **kwargs))


def ArtPaintAttrToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ArtPaintAttrToolOptions(*_args, **kwargs))


def ArtPaintBlendShapeWeightsTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ArtPaintBlendShapeWeightsTool(*_args, **kwargs))


def ArtPaintBlendShapeWeightsToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ArtPaintBlendShapeWeightsToolOptions(*_args, **kwargs))


def ArtPaintSelectTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ArtPaintSelectTool(*_args, **kwargs))


def ArtPaintSelectToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ArtPaintSelectToolOptions(*_args, **kwargs))


def ArtPaintSkinWeightsTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ArtPaintSkinWeightsTool(*_args, **kwargs))


def ArtPaintSkinWeightsToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ArtPaintSkinWeightsToolOptions(*_args, **kwargs))


def AssetEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AssetEditor(*_args, **kwargs))


def AssignBrushToHairSystem(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AssignBrushToHairSystem(*_args, **kwargs))


def AssignHairConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AssignHairConstraint(*_args, **kwargs))


def AssignHairConstraintOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AssignHairConstraintOptions(*_args, **kwargs))


def AssignNewMaterial(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AssignNewMaterial(*_args, **kwargs))


def AssignOfflineFile(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AssignOfflineFile(*_args, **kwargs))


def AssignOfflineFileFromRefEd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AssignOfflineFileFromRefEd(*_args, **kwargs))


def AssignOfflineFileFromRefEdOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AssignOfflineFileFromRefEdOptions(*_args, **kwargs))


def AssignOfflineFileOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AssignOfflineFileOptions(*_args, **kwargs))


def AssignTemplate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AssignTemplate(*_args, **kwargs))


def AssignTemplateOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AssignTemplateOptions(*_args, **kwargs))


def AssumePreferredAngle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AssumePreferredAngle(*_args, **kwargs))


def AssumePreferredAngleOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AssumePreferredAngleOptions(*_args, **kwargs))


def AttachBrushToCurves(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AttachBrushToCurves(*_args, **kwargs))


def AttachCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AttachCurve(*_args, **kwargs))


def AttachCurveOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AttachCurveOptions(*_args, **kwargs))


def AttachSelectedAsSourceField(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AttachSelectedAsSourceField(*_args, **kwargs))


def AttachSubdivSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AttachSubdivSurface(*_args, **kwargs))


def AttachSubdivSurfaceOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AttachSubdivSurfaceOptions(*_args, **kwargs))


def AttachSurfaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AttachSurfaces(*_args, **kwargs))


def AttachSurfacesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AttachSurfacesOptions(*_args, **kwargs))


def AttachToPath(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AttachToPath(*_args, **kwargs))


def AttachToPathOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AttachToPathOptions(*_args, **kwargs))


def AttributeEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AttributeEditor(*_args, **kwargs))


def AutoPaintMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AutoPaintMarkingMenu(*_args, **kwargs))


def AutoPaintMarkingMenuPopDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AutoPaintMarkingMenuPopDown(*_args, **kwargs))


def AutoProjection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AutoProjection(*_args, **kwargs))


def AutoProjectionOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AutoProjectionOptions(*_args, **kwargs))


def AutobindContainer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AutobindContainer(*_args, **kwargs))


def AutobindContainerOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AutobindContainerOptions(*_args, **kwargs))


def AveragePolygonNormals(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AveragePolygonNormals(*_args, **kwargs))


def AveragePolygonNormalsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AveragePolygonNormalsOptions(*_args, **kwargs))


def AverageVertex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.AverageVertex(*_args, **kwargs))


def BakeAllNonDefHistory(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BakeAllNonDefHistory(*_args, **kwargs))


def BakeChannel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BakeChannel(*_args, **kwargs))


def BakeChannelOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BakeChannelOptions(*_args, **kwargs))


def BakeCustomPivot(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BakeCustomPivot(*_args, **kwargs))


def BakeCustomPivotOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BakeCustomPivotOptions(*_args, **kwargs))


def BakeDeformerTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BakeDeformerTool(*_args, **kwargs))


def BakeNonDefHistory(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BakeNonDefHistory(*_args, **kwargs))


def BakeNonDefHistoryOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BakeNonDefHistoryOptions(*_args, **kwargs))


def BakeSimulation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BakeSimulation(*_args, **kwargs))


def BakeSimulationOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BakeSimulationOptions(*_args, **kwargs))


def BakeSpringAnimation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BakeSpringAnimation(*_args, **kwargs))


def BakeSpringAnimationOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BakeSpringAnimationOptions(*_args, **kwargs))


def BakeTopologyToTargets(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BakeTopologyToTargets(*_args, **kwargs))


def BaseLevelComponentDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BaseLevelComponentDisplay(*_args, **kwargs))


def BatchBake(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BatchBake(*_args, **kwargs))


def BatchBakeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BatchBakeOptions(*_args, **kwargs))


def BatchRender(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BatchRender(*_args, **kwargs))


def BatchRenderOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BatchRenderOptions(*_args, **kwargs))


def Bend(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Bend(*_args, **kwargs))


def BendCurves(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BendCurves(*_args, **kwargs))


def BendCurvesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BendCurvesOptions(*_args, **kwargs))


def BendOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BendOptions(*_args, **kwargs))


def BestPlaneTexturingTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BestPlaneTexturingTool(*_args, **kwargs))


def Bevel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Bevel(*_args, **kwargs))


def BevelOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BevelOptions(*_args, **kwargs))


def BevelPlus(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BevelPlus(*_args, **kwargs))


def BevelPlusOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BevelPlusOptions(*_args, **kwargs))


def BevelPolygon(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BevelPolygon(*_args, **kwargs))


def BevelPolygonOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BevelPolygonOptions(*_args, **kwargs))


def Birail1(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Birail1(*_args, **kwargs))


def Birail1Options(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Birail1Options(*_args, **kwargs))


def Birail2(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Birail2(*_args, **kwargs))


def Birail2Options(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Birail2Options(*_args, **kwargs))


def Birail3(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Birail3(*_args, **kwargs))


def Birail3Options(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Birail3Options(*_args, **kwargs))


def BlendShapeEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BlendShapeEditor(*_args, **kwargs))


def BlindDataEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BlindDataEditor(*_args, **kwargs))


def BothProxySubdivDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BothProxySubdivDisplay(*_args, **kwargs))


def Boundary(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Boundary(*_args, **kwargs))


def BoundaryOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BoundaryOptions(*_args, **kwargs))


def BreakLightLinks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BreakLightLinks(*_args, **kwargs))


def BreakRigidBodyConnection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BreakRigidBodyConnection(*_args, **kwargs))


def BreakShadowLinks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BreakShadowLinks(*_args, **kwargs))


def BreakTangent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BreakTangent(*_args, **kwargs))


def BreakTangents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BreakTangents(*_args, **kwargs))


def BridgeEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BridgeEdge(*_args, **kwargs))


def BridgeEdgeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BridgeEdgeOptions(*_args, **kwargs))


def BrushAnimationMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BrushAnimationMarkingMenu(*_args, **kwargs))


def BrushAnimationMarkingMenuPopDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BrushAnimationMarkingMenuPopDown(*_args, **kwargs))


def BrushPresetBlend(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BrushPresetBlend(*_args, **kwargs))


def BrushPresetBlendOff(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BrushPresetBlendOff(*_args, **kwargs))


def BrushPresetBlendShading(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BrushPresetBlendShading(*_args, **kwargs))


def BrushPresetBlendShadingOff(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BrushPresetBlendShadingOff(*_args, **kwargs))


def BrushPresetBlendShape(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BrushPresetBlendShape(*_args, **kwargs))


def BrushPresetBlendShapeOff(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BrushPresetBlendShapeOff(*_args, **kwargs))


def BrushPresetReplaceShading(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BrushPresetReplaceShading(*_args, **kwargs))


def BrushPresetReplaceShadingOff(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BrushPresetReplaceShadingOff(*_args, **kwargs))


def BufferCurveSnapshot(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.BufferCurveSnapshot(*_args, **kwargs))


def CVCurveTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CVCurveTool(*_args, **kwargs))


def CVCurveToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CVCurveToolOptions(*_args, **kwargs))


def CVHardness(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CVHardness(*_args, **kwargs))


def CVHardnessOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CVHardnessOptions(*_args, **kwargs))


def CameraModeOrthographic(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CameraModeOrthographic(*_args, **kwargs))


def CameraModePerspective(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CameraModePerspective(*_args, **kwargs))


def CameraModeToggle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CameraModeToggle(*_args, **kwargs))


def CameraSetEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CameraSetEditor(*_args, **kwargs))


def CancelBatchRender(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CancelBatchRender(*_args, **kwargs))


def CenterPivot(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CenterPivot(*_args, **kwargs))


def CenterViewOfSelection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CenterViewOfSelection(*_args, **kwargs))


def ChamferVertex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ChamferVertex(*_args, **kwargs))


def ChamferVertexOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ChamferVertexOptions(*_args, **kwargs))


def ChangeEdgeWidth(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ChangeEdgeWidth(*_args, **kwargs))


def ChangeNormalSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ChangeNormalSize(*_args, **kwargs))


def ChangeUVSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ChangeUVSize(*_args, **kwargs))


def ChangeVertexSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ChangeVertexSize(*_args, **kwargs))


def ChannelControlEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ChannelControlEditor(*_args, **kwargs))


def CharacterAnimationEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CharacterAnimationEditor(*_args, **kwargs))


def CharacterMapper(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CharacterMapper(*_args, **kwargs))


def CharacterSetEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CharacterSetEditor(*_args, **kwargs))


def CircularFillet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CircularFillet(*_args, **kwargs))


def CircularFilletOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CircularFilletOptions(*_args, **kwargs))


def CleanupPolygon(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CleanupPolygon(*_args, **kwargs))


def CleanupPolygonOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CleanupPolygonOptions(*_args, **kwargs))


def ClearCurrentCharacterList(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ClearCurrentCharacterList(*_args, **kwargs))


def ClearCurrentContainer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ClearCurrentContainer(*_args, **kwargs))


def ClearInitialState(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ClearInitialState(*_args, **kwargs))


def ClearPaintEffectsView(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ClearPaintEffectsView(*_args, **kwargs))


def CloseFrontWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CloseFrontWindow(*_args, **kwargs))


def ClosestPointOn(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ClosestPointOn(*_args, **kwargs))


def ClosestPointOnOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ClosestPointOnOptions(*_args, **kwargs))


def CloudImportExport(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CloudImportExport(*_args, **kwargs))


def ClusterCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ClusterCurve(*_args, **kwargs))


def CoarseLevelComponentDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CoarseLevelComponentDisplay(*_args, **kwargs))


def CoarsenSelectedComponents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CoarsenSelectedComponents(*_args, **kwargs))


def CoarserSubdivLevel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CoarserSubdivLevel(*_args, **kwargs))


def CollapseSubdivSurfaceHierarchy(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CollapseSubdivSurfaceHierarchy(*_args, **kwargs))


def CollapseSubdivSurfaceHierarchyOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CollapseSubdivSurfaceHierarchyOptions(*_args, **kwargs))


def ColorPreferencesWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ColorPreferencesWindow(*_args, **kwargs))


def CombinePolygons(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CombinePolygons(*_args, **kwargs))


def CombinePolygonsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CombinePolygonsOptions(*_args, **kwargs))


def CommandShell(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CommandShell(*_args, **kwargs))


def CommandWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CommandWindow(*_args, **kwargs))


def CompleteCurrentTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CompleteCurrentTool(*_args, **kwargs))


def ComponentEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ComponentEditor(*_args, **kwargs))


def ConformPolygon(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConformPolygon(*_args, **kwargs))


def ConformPolygonNormals(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConformPolygonNormals(*_args, **kwargs))


def ConformPolygonOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConformPolygonOptions(*_args, **kwargs))


def ConnectComponents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConnectComponents(*_args, **kwargs))


def ConnectComponentsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConnectComponentsOptions(*_args, **kwargs))


def ConnectJoint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConnectJoint(*_args, **kwargs))


def ConnectJointOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConnectJointOptions(*_args, **kwargs))


def ConnectNodeToIKFK(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConnectNodeToIKFK(*_args, **kwargs))


def ConnectToTime(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConnectToTime(*_args, **kwargs))


def ConnectionEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConnectionEditor(*_args, **kwargs))


def ContentBrowserLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ContentBrowserLayout(*_args, **kwargs))


def ContentBrowserWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ContentBrowserWindow(*_args, **kwargs))


def ConvertInstanceToObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConvertInstanceToObject(*_args, **kwargs))


def ConvertSelectionToContainedEdges(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConvertSelectionToContainedEdges(*_args, **kwargs))


def ConvertSelectionToContainedFaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConvertSelectionToContainedFaces(*_args, **kwargs))


def ConvertSelectionToEdgePerimeter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConvertSelectionToEdgePerimeter(*_args, **kwargs))


def ConvertSelectionToEdges(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConvertSelectionToEdges(*_args, **kwargs))


def ConvertSelectionToFacePerimeter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConvertSelectionToFacePerimeter(*_args, **kwargs))


def ConvertSelectionToFaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConvertSelectionToFaces(*_args, **kwargs))


def ConvertSelectionToShell(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConvertSelectionToShell(*_args, **kwargs))


def ConvertSelectionToShellBorder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConvertSelectionToShellBorder(*_args, **kwargs))


def ConvertSelectionToUVBorder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConvertSelectionToUVBorder(*_args, **kwargs))


def ConvertSelectionToUVEdgeLoop(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConvertSelectionToUVEdgeLoop(*_args, **kwargs))


def ConvertSelectionToUVPerimeter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConvertSelectionToUVPerimeter(*_args, **kwargs))


def ConvertSelectionToUVShell(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConvertSelectionToUVShell(*_args, **kwargs))


def ConvertSelectionToUVShellBorder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConvertSelectionToUVShellBorder(*_args, **kwargs))


def ConvertSelectionToUVs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConvertSelectionToUVs(*_args, **kwargs))


def ConvertSelectionToVertexFaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConvertSelectionToVertexFaces(*_args, **kwargs))


def ConvertSelectionToVertexPerimeter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConvertSelectionToVertexPerimeter(*_args, **kwargs))


def ConvertSelectionToVertices(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConvertSelectionToVertices(*_args, **kwargs))


def ConvertToBreakdown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConvertToBreakdown(*_args, **kwargs))


def ConvertToFrozen(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConvertToFrozen(*_args, **kwargs))


def ConvertToKey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ConvertToKey(*_args, **kwargs))


def CopyFlexor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CopyFlexor(*_args, **kwargs))


def CopyKeys(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CopyKeys(*_args, **kwargs))


def CopyKeysOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CopyKeysOptions(*_args, **kwargs))


def CopyMeshAttributes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CopyMeshAttributes(*_args, **kwargs))


def CopySelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CopySelected(*_args, **kwargs))


def CopySkinWeights(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CopySkinWeights(*_args, **kwargs))


def CopySkinWeightsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CopySkinWeightsOptions(*_args, **kwargs))


def CopyUVs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CopyUVs(*_args, **kwargs))


def CopyUVsToUVSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CopyUVsToUVSet(*_args, **kwargs))


def CopyUVsToUVSetOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CopyUVsToUVSetOptions(*_args, **kwargs))


def CopyVertexSkinWeights(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CopyVertexSkinWeights(*_args, **kwargs))


def CreaseProxyEdgeTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreaseProxyEdgeTool(*_args, **kwargs))


def CreaseProxyEdgeToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreaseProxyEdgeToolOptions(*_args, **kwargs))


def Create2DContainer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Create2DContainer(*_args, **kwargs))


def Create2DContainerEmitter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Create2DContainerEmitter(*_args, **kwargs))


def Create2DContainerEmitterOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Create2DContainerEmitterOptions(*_args, **kwargs))


def Create2DContainerOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Create2DContainerOptions(*_args, **kwargs))


def Create3DContainer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Create3DContainer(*_args, **kwargs))


def Create3DContainerEmitter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Create3DContainerEmitter(*_args, **kwargs))


def Create3DContainerEmitterOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Create3DContainerEmitterOptions(*_args, **kwargs))


def Create3DContainerOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Create3DContainerOptions(*_args, **kwargs))


def CreateActiveRigidBody(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateActiveRigidBody(*_args, **kwargs))


def CreateActiveRigidBodyOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateActiveRigidBodyOptions(*_args, **kwargs))


def CreateAmbientLight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateAmbientLight(*_args, **kwargs))


def CreateAmbientLightOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateAmbientLightOptions(*_args, **kwargs))


def CreateAnnotateNode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateAnnotateNode(*_args, **kwargs))


def CreateAreaLight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateAreaLight(*_args, **kwargs))


def CreateAreaLightOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateAreaLightOptions(*_args, **kwargs))


def CreateBezierCurveTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateBezierCurveTool(*_args, **kwargs))


def CreateBezierCurveToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateBezierCurveToolOptions(*_args, **kwargs))


def CreateBindingSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateBindingSet(*_args, **kwargs))


def CreateBlendShape(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateBlendShape(*_args, **kwargs))


def CreateBlendShapeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateBlendShapeOptions(*_args, **kwargs))


def CreateCameraAim(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateCameraAim(*_args, **kwargs))


def CreateCameraAimOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateCameraAimOptions(*_args, **kwargs))


def CreateCameraAimUp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateCameraAimUp(*_args, **kwargs))


def CreateCameraAimUpOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateCameraAimUpOptions(*_args, **kwargs))


def CreateCameraFromView(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateCameraFromView(*_args, **kwargs))


def CreateCameraOnly(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateCameraOnly(*_args, **kwargs))


def CreateCameraOnlyOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateCameraOnlyOptions(*_args, **kwargs))


def CreateCharacter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateCharacter(*_args, **kwargs))


def CreateCharacterOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateCharacterOptions(*_args, **kwargs))


def CreateClip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateClip(*_args, **kwargs))


def CreateClipOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateClipOptions(*_args, **kwargs))


def CreateCluster(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateCluster(*_args, **kwargs))


def CreateClusterOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateClusterOptions(*_args, **kwargs))


def CreateConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateConstraint(*_args, **kwargs))


def CreateConstraintClip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateConstraintClip(*_args, **kwargs))


def CreateConstraintClipOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateConstraintClipOptions(*_args, **kwargs))


def CreateConstraintOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateConstraintOptions(*_args, **kwargs))


def CreateConstructionPlane(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateConstructionPlane(*_args, **kwargs))


def CreateConstructionPlaneOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateConstructionPlaneOptions(*_args, **kwargs))


def CreateContainer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateContainer(*_args, **kwargs))


def CreateContainerOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateContainerOptions(*_args, **kwargs))


def CreateCreaseSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateCreaseSet(*_args, **kwargs))


def CreateCreaseSetOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateCreaseSetOptions(*_args, **kwargs))


def CreateCurveFromPoly(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateCurveFromPoly(*_args, **kwargs))


def CreateCurveFromPolyOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateCurveFromPolyOptions(*_args, **kwargs))


def CreateDagContainer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateDagContainer(*_args, **kwargs))


def CreateDagContainerOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateDagContainerOptions(*_args, **kwargs))


def CreateDirectionalLight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateDirectionalLight(*_args, **kwargs))


def CreateDirectionalLightOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateDirectionalLightOptions(*_args, **kwargs))


def CreateDiskCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateDiskCache(*_args, **kwargs))


def CreateDiskCacheOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateDiskCacheOptions(*_args, **kwargs))


def CreateEmitter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateEmitter(*_args, **kwargs))


def CreateEmitterOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateEmitterOptions(*_args, **kwargs))


def CreateEmptyGroup(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateEmptyGroup(*_args, **kwargs))


def CreateEmptyUVSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateEmptyUVSet(*_args, **kwargs))


def CreateEmptyUVSetOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateEmptyUVSetOptions(*_args, **kwargs))


def CreateExpressionClip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateExpressionClip(*_args, **kwargs))


def CreateExpressionClipOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateExpressionClipOptions(*_args, **kwargs))


def CreateFlexorWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateFlexorWindow(*_args, **kwargs))


def CreateFluidCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateFluidCache(*_args, **kwargs))


def CreateFluidCacheOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateFluidCacheOptions(*_args, **kwargs))


def CreateGhost(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateGhost(*_args, **kwargs))


def CreateGhostOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateGhostOptions(*_args, **kwargs))


def CreateHair(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateHair(*_args, **kwargs))


def CreateHairCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateHairCache(*_args, **kwargs))


def CreateHairCacheOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateHairCacheOptions(*_args, **kwargs))


def CreateHairOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateHairOptions(*_args, **kwargs))


def CreateIllustratorCurves(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateIllustratorCurves(*_args, **kwargs))


def CreateIllustratorCurvesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateIllustratorCurvesOptions(*_args, **kwargs))


def CreateImagePlane(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateImagePlane(*_args, **kwargs))


def CreateImagePlaneOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateImagePlaneOptions(*_args, **kwargs))


def CreateJiggleDeformer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateJiggleDeformer(*_args, **kwargs))


def CreateJiggleOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateJiggleOptions(*_args, **kwargs))


def CreateLattice(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateLattice(*_args, **kwargs))


def CreateLatticeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateLatticeOptions(*_args, **kwargs))


def CreateLocator(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateLocator(*_args, **kwargs))


def CreateMotionTrail(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateMotionTrail(*_args, **kwargs))


def CreateMotionTrailOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateMotionTrailOptions(*_args, **kwargs))


def CreateNSoftBody(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateNSoftBody(*_args, **kwargs))


def CreateNSoftBodyOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateNSoftBodyOptions(*_args, **kwargs))


def CreateNURBSCircle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateNURBSCircle(*_args, **kwargs))


def CreateNURBSCircleOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateNURBSCircleOptions(*_args, **kwargs))


def CreateNURBSCone(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateNURBSCone(*_args, **kwargs))


def CreateNURBSConeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateNURBSConeOptions(*_args, **kwargs))


def CreateNURBSCube(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateNURBSCube(*_args, **kwargs))


def CreateNURBSCubeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateNURBSCubeOptions(*_args, **kwargs))


def CreateNURBSCylinder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateNURBSCylinder(*_args, **kwargs))


def CreateNURBSCylinderOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateNURBSCylinderOptions(*_args, **kwargs))


def CreateNURBSPlane(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateNURBSPlane(*_args, **kwargs))


def CreateNURBSPlaneOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateNURBSPlaneOptions(*_args, **kwargs))


def CreateNURBSSphere(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateNURBSSphere(*_args, **kwargs))


def CreateNURBSSphereOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateNURBSSphereOptions(*_args, **kwargs))


def CreateNURBSSquare(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateNURBSSquare(*_args, **kwargs))


def CreateNURBSSquareOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateNURBSSquareOptions(*_args, **kwargs))


def CreateNURBSTorus(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateNURBSTorus(*_args, **kwargs))


def CreateNURBSTorusOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateNURBSTorusOptions(*_args, **kwargs))


def CreateNodeWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateNodeWindow(*_args, **kwargs))


def CreateOcean(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateOcean(*_args, **kwargs))


def CreateOceanOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateOceanOptions(*_args, **kwargs))


def CreateOceanWake(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateOceanWake(*_args, **kwargs))


def CreateOceanWakeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateOceanWakeOptions(*_args, **kwargs))


def CreateParticleDiskCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateParticleDiskCache(*_args, **kwargs))


def CreateParticleDiskCacheOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateParticleDiskCacheOptions(*_args, **kwargs))


def CreatePartition(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePartition(*_args, **kwargs))


def CreatePartitionOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePartitionOptions(*_args, **kwargs))


def CreatePassiveRigidBody(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePassiveRigidBody(*_args, **kwargs))


def CreatePassiveRigidBodyOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePassiveRigidBodyOptions(*_args, **kwargs))


def CreatePlatonicSolid(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePlatonicSolid(*_args, **kwargs))


def CreatePlatonicSolidOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePlatonicSolidOptions(*_args, **kwargs))


def CreatePointLight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePointLight(*_args, **kwargs))


def CreatePointLightOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePointLightOptions(*_args, **kwargs))


def CreatePolyFromPreview(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolyFromPreview(*_args, **kwargs))


def CreatePolygonCone(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonCone(*_args, **kwargs))


def CreatePolygonConeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonConeOptions(*_args, **kwargs))


def CreatePolygonCube(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonCube(*_args, **kwargs))


def CreatePolygonCubeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonCubeOptions(*_args, **kwargs))


def CreatePolygonCylinder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonCylinder(*_args, **kwargs))


def CreatePolygonCylinderOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonCylinderOptions(*_args, **kwargs))


def CreatePolygonDisc(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonDisc(*_args, **kwargs))


def CreatePolygonDiscOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonDiscOptions(*_args, **kwargs))


def CreatePolygonGear(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonGear(*_args, **kwargs))


def CreatePolygonGearOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonGearOptions(*_args, **kwargs))


def CreatePolygonHelix(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonHelix(*_args, **kwargs))


def CreatePolygonHelixOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonHelixOptions(*_args, **kwargs))


def CreatePolygonPipe(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonPipe(*_args, **kwargs))


def CreatePolygonPipeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonPipeOptions(*_args, **kwargs))


def CreatePolygonPlane(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonPlane(*_args, **kwargs))


def CreatePolygonPlaneOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonPlaneOptions(*_args, **kwargs))


def CreatePolygonPlatonic(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonPlatonic(*_args, **kwargs))


def CreatePolygonPlatonicOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonPlatonicOptions(*_args, **kwargs))


def CreatePolygonPrism(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonPrism(*_args, **kwargs))


def CreatePolygonPrismOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonPrismOptions(*_args, **kwargs))


def CreatePolygonPyramid(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonPyramid(*_args, **kwargs))


def CreatePolygonPyramidOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonPyramidOptions(*_args, **kwargs))


def CreatePolygonSVG(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonSVG(*_args, **kwargs))


def CreatePolygonSoccerBall(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonSoccerBall(*_args, **kwargs))


def CreatePolygonSoccerBallOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonSoccerBallOptions(*_args, **kwargs))


def CreatePolygonSphere(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonSphere(*_args, **kwargs))


def CreatePolygonSphereOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonSphereOptions(*_args, **kwargs))


def CreatePolygonSphericalHarmonics(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonSphericalHarmonics(*_args, **kwargs))


def CreatePolygonSphericalHarmonicsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonSphericalHarmonicsOptions(*_args, **kwargs))


def CreatePolygonSuperEllipse(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonSuperEllipse(*_args, **kwargs))


def CreatePolygonSuperEllipseOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonSuperEllipseOptions(*_args, **kwargs))


def CreatePolygonTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonTool(*_args, **kwargs))


def CreatePolygonToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonToolOptions(*_args, **kwargs))


def CreatePolygonTorus(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonTorus(*_args, **kwargs))


def CreatePolygonTorusOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonTorusOptions(*_args, **kwargs))


def CreatePolygonType(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonType(*_args, **kwargs))


def CreatePolygonUltraShape(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonUltraShape(*_args, **kwargs))


def CreatePolygonUltraShapeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePolygonUltraShapeOptions(*_args, **kwargs))


def CreatePond(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePond(*_args, **kwargs))


def CreatePondOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePondOptions(*_args, **kwargs))


def CreatePose(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePose(*_args, **kwargs))


def CreatePoseInterpolatorEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePoseInterpolatorEditor(*_args, **kwargs))


def CreatePoseOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreatePoseOptions(*_args, **kwargs))


def CreateQuickSelectSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateQuickSelectSet(*_args, **kwargs))


def CreateReference(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateReference(*_args, **kwargs))


def CreateReferenceOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateReferenceOptions(*_args, **kwargs))


def CreateRigidBodySolver(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateRigidBodySolver(*_args, **kwargs))


def CreateSculptDeformer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateSculptDeformer(*_args, **kwargs))


def CreateSculptDeformerOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateSculptDeformerOptions(*_args, **kwargs))


def CreateSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateSet(*_args, **kwargs))


def CreateSetOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateSetOptions(*_args, **kwargs))


def CreateShot(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateShot(*_args, **kwargs))


def CreateShotOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateShotOptions(*_args, **kwargs))


def CreateShrinkWrap(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateShrinkWrap(*_args, **kwargs))


def CreateShrinkWrapOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateShrinkWrapOptions(*_args, **kwargs))


def CreateSoftBody(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateSoftBody(*_args, **kwargs))


def CreateSoftBodyOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateSoftBodyOptions(*_args, **kwargs))


def CreateSpotLight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateSpotLight(*_args, **kwargs))


def CreateSpotLightOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateSpotLightOptions(*_args, **kwargs))


def CreateSpring(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateSpring(*_args, **kwargs))


def CreateSpringOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateSpringOptions(*_args, **kwargs))


def CreateSubCharacter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateSubCharacter(*_args, **kwargs))


def CreateSubCharacterOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateSubCharacterOptions(*_args, **kwargs))


def CreateSubdivCone(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateSubdivCone(*_args, **kwargs))


def CreateSubdivCube(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateSubdivCube(*_args, **kwargs))


def CreateSubdivCylinder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateSubdivCylinder(*_args, **kwargs))


def CreateSubdivPlane(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateSubdivPlane(*_args, **kwargs))


def CreateSubdivRegion(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateSubdivRegion(*_args, **kwargs))


def CreateSubdivSphere(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateSubdivSphere(*_args, **kwargs))


def CreateSubdivSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateSubdivSurface(*_args, **kwargs))


def CreateSubdivSurfaceOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateSubdivSurfaceOptions(*_args, **kwargs))


def CreateSubdivTorus(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateSubdivTorus(*_args, **kwargs))


def CreateText(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateText(*_args, **kwargs))


def CreateTextOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateTextOptions(*_args, **kwargs))


def CreateTextureDeformer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateTextureDeformer(*_args, **kwargs))


def CreateTextureDeformerOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateTextureDeformerOptions(*_args, **kwargs))


def CreateTextureReferenceObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateTextureReferenceObject(*_args, **kwargs))


def CreateUVShellAlongBorder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateUVShellAlongBorder(*_args, **kwargs))


def CreateUVsBasedOnCamera(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateUVsBasedOnCamera(*_args, **kwargs))


def CreateUVsBasedOnCameraOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateUVsBasedOnCameraOptions(*_args, **kwargs))


def CreateVolumeCone(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateVolumeCone(*_args, **kwargs))


def CreateVolumeCube(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateVolumeCube(*_args, **kwargs))


def CreateVolumeLight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateVolumeLight(*_args, **kwargs))


def CreateVolumeLightOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateVolumeLightOptions(*_args, **kwargs))


def CreateVolumeSphere(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateVolumeSphere(*_args, **kwargs))


def CreateWake(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateWake(*_args, **kwargs))


def CreateWakeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateWakeOptions(*_args, **kwargs))


def CreateWrap(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateWrap(*_args, **kwargs))


def CreateWrapOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CreateWrapOptions(*_args, **kwargs))


def CurlCurves(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CurlCurves(*_args, **kwargs))


def CurlCurvesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CurlCurvesOptions(*_args, **kwargs))


def CurveEditTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CurveEditTool(*_args, **kwargs))


def CurveFillet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CurveFillet(*_args, **kwargs))


def CurveFilletOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CurveFilletOptions(*_args, **kwargs))


def CurveFlow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CurveFlow(*_args, **kwargs))


def CurveFlowOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CurveFlowOptions(*_args, **kwargs))


def CurveSmoothnessCoarse(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CurveSmoothnessCoarse(*_args, **kwargs))


def CurveSmoothnessFine(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CurveSmoothnessFine(*_args, **kwargs))


def CurveSmoothnessMedium(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CurveSmoothnessMedium(*_args, **kwargs))


def CurveSmoothnessRough(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CurveSmoothnessRough(*_args, **kwargs))


def CurveUtilitiesMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CurveUtilitiesMarkingMenu(*_args, **kwargs))


def CurveUtilitiesMarkingMenuPopDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CurveUtilitiesMarkingMenuPopDown(*_args, **kwargs))


def CustomNURBSComponentsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CustomNURBSComponentsOptions(*_args, **kwargs))


def CustomNURBSSmoothness(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CustomNURBSSmoothness(*_args, **kwargs))


def CustomNURBSSmoothnessOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CustomNURBSSmoothnessOptions(*_args, **kwargs))


def CustomPolygonDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CustomPolygonDisplay(*_args, **kwargs))


def CustomPolygonDisplayOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CustomPolygonDisplayOptions(*_args, **kwargs))


def CutCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CutCurve(*_args, **kwargs))


def CutCurveOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CutCurveOptions(*_args, **kwargs))


def CutKeys(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CutKeys(*_args, **kwargs))


def CutKeysOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CutKeysOptions(*_args, **kwargs))


def CutPolygon(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CutPolygon(*_args, **kwargs))


def CutPolygonOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CutPolygonOptions(*_args, **kwargs))


def CutSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CutSelected(*_args, **kwargs))


def CutUVs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CutUVs(*_args, **kwargs))


def CutUVs3D(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CutUVs3D(*_args, **kwargs))


def CutUVsWithoutHotkey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CutUVsWithoutHotkey(*_args, **kwargs))


def CycleBackgroundColor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CycleBackgroundColor(*_args, **kwargs))


def CycleIKHandleStickyState(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CycleIKHandleStickyState(*_args, **kwargs))


def CycleThroughCameras(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.CycleThroughCameras(*_args, **kwargs))


def DeactivateGlobalScreenSlider(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeactivateGlobalScreenSlider(*_args, **kwargs))


def DeactivateGlobalScreenSliderModeMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeactivateGlobalScreenSliderModeMarkingMenu(*_args, **kwargs))


def DecreaseCheckerDensity(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DecreaseCheckerDensity(*_args, **kwargs))


def DecreaseExposureCoarse(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DecreaseExposureCoarse(*_args, **kwargs))


def DecreaseExposureFine(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DecreaseExposureFine(*_args, **kwargs))


def DecreaseGammaCoarse(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DecreaseGammaCoarse(*_args, **kwargs))


def DecreaseGammaFine(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DecreaseGammaFine(*_args, **kwargs))


def DecreaseManipulatorSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DecreaseManipulatorSize(*_args, **kwargs))


def DecrementFluidCenter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DecrementFluidCenter(*_args, **kwargs))


def DefaultQualityDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DefaultQualityDisplay(*_args, **kwargs))


def DeformerSetEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeformerSetEditor(*_args, **kwargs))


def Delete(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Delete(*_args, **kwargs))


def DeleteAllCameras(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllCameras(*_args, **kwargs))


def DeleteAllChannels(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllChannels(*_args, **kwargs))


def DeleteAllClips(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllClips(*_args, **kwargs))


def DeleteAllClusters(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllClusters(*_args, **kwargs))


def DeleteAllConstraints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllConstraints(*_args, **kwargs))


def DeleteAllContainers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllContainers(*_args, **kwargs))


def DeleteAllControllers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllControllers(*_args, **kwargs))


def DeleteAllDynamicConstraints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllDynamicConstraints(*_args, **kwargs))


def DeleteAllExpressions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllExpressions(*_args, **kwargs))


def DeleteAllFluids(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllFluids(*_args, **kwargs))


def DeleteAllFurs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllFurs(*_args, **kwargs))


def DeleteAllHistory(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllHistory(*_args, **kwargs))


def DeleteAllIKHandles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllIKHandles(*_args, **kwargs))


def DeleteAllImagePlanes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllImagePlanes(*_args, **kwargs))


def DeleteAllJoints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllJoints(*_args, **kwargs))


def DeleteAllLattices(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllLattices(*_args, **kwargs))


def DeleteAllLights(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllLights(*_args, **kwargs))


def DeleteAllMotionPaths(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllMotionPaths(*_args, **kwargs))


def DeleteAllNCloths(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllNCloths(*_args, **kwargs))


def DeleteAllNParticles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllNParticles(*_args, **kwargs))


def DeleteAllNRigids(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllNRigids(*_args, **kwargs))


def DeleteAllNonLinearDeformers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllNonLinearDeformers(*_args, **kwargs))


def DeleteAllParticles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllParticles(*_args, **kwargs))


def DeleteAllPoses(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllPoses(*_args, **kwargs))


def DeleteAllRigidBodies(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllRigidBodies(*_args, **kwargs))


def DeleteAllRigidConstraints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllRigidConstraints(*_args, **kwargs))


def DeleteAllSculptObjects(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllSculptObjects(*_args, **kwargs))


def DeleteAllShadingGroupsAndMaterials(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllShadingGroupsAndMaterials(*_args, **kwargs))


def DeleteAllSounds(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllSounds(*_args, **kwargs))


def DeleteAllStaticChannels(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllStaticChannels(*_args, **kwargs))


def DeleteAllStrokes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllStrokes(*_args, **kwargs))


def DeleteAllWires(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAllWires(*_args, **kwargs))


def DeleteAttribute(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteAttribute(*_args, **kwargs))


def DeleteChannels(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteChannels(*_args, **kwargs))


def DeleteChannelsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteChannelsOptions(*_args, **kwargs))


def DeleteConstraints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteConstraints(*_args, **kwargs))


def DeleteCurrentColorSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteCurrentColorSet(*_args, **kwargs))


def DeleteCurrentUVSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteCurrentUVSet(*_args, **kwargs))


def DeleteCurrentWorkspace(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteCurrentWorkspace(*_args, **kwargs))


def DeleteEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteEdge(*_args, **kwargs))


def DeleteEntireHairSystem(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteEntireHairSystem(*_args, **kwargs))


def DeleteExpressions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteExpressions(*_args, **kwargs))


def DeleteExpressionsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteExpressionsOptions(*_args, **kwargs))


def DeleteHair(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteHair(*_args, **kwargs))


def DeleteHairCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteHairCache(*_args, **kwargs))


def DeleteHistory(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteHistory(*_args, **kwargs))


def DeleteKeys(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteKeys(*_args, **kwargs))


def DeleteKeysOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteKeysOptions(*_args, **kwargs))


def DeleteMemoryCaching(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteMemoryCaching(*_args, **kwargs))


def DeleteMotionPaths(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteMotionPaths(*_args, **kwargs))


def DeletePolyElements(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeletePolyElements(*_args, **kwargs))


def DeleteRigidBodies(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteRigidBodies(*_args, **kwargs))


def DeleteSelectedContainers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteSelectedContainers(*_args, **kwargs))


def DeleteStaticChannels(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteStaticChannels(*_args, **kwargs))


def DeleteStaticChannelsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteStaticChannelsOptions(*_args, **kwargs))


def DeleteSurfaceFlow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteSurfaceFlow(*_args, **kwargs))


def DeleteSurfaceFlowOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteSurfaceFlowOptions(*_args, **kwargs))


def DeleteTextureReferenceObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteTextureReferenceObject(*_args, **kwargs))


def DeleteTimeWarp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteTimeWarp(*_args, **kwargs))


def DeleteUVs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteUVs(*_args, **kwargs))


def DeleteUVsWithoutHotkey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteUVsWithoutHotkey(*_args, **kwargs))


def DeleteVertex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeleteVertex(*_args, **kwargs))


def DeltaMush(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeltaMush(*_args, **kwargs))


def DeltaMushOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeltaMushOptions(*_args, **kwargs))


def DetachComponent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DetachComponent(*_args, **kwargs))


def DetachCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DetachCurve(*_args, **kwargs))


def DetachCurveOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DetachCurveOptions(*_args, **kwargs))


def DetachEdgeComponent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DetachEdgeComponent(*_args, **kwargs))


def DetachSkeleton(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DetachSkeleton(*_args, **kwargs))


def DetachSkeletonJoints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DetachSkeletonJoints(*_args, **kwargs))


def DetachSkin(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DetachSkin(*_args, **kwargs))


def DetachSkinOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DetachSkinOptions(*_args, **kwargs))


def DetachSurfaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DetachSurfaces(*_args, **kwargs))


def DetachSurfacesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DetachSurfacesOptions(*_args, **kwargs))


def DetachVertexComponent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DetachVertexComponent(*_args, **kwargs))


def DeviceEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DeviceEditor(*_args, **kwargs))


def DisableAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisableAll(*_args, **kwargs))


def DisableConstraints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisableConstraints(*_args, **kwargs))


def DisableExpressions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisableExpressions(*_args, **kwargs))


def DisableFluids(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisableFluids(*_args, **kwargs))


def DisableGlobalStitch(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisableGlobalStitch(*_args, **kwargs))


def DisableIKSolvers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisableIKSolvers(*_args, **kwargs))


def DisableMemoryCaching(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisableMemoryCaching(*_args, **kwargs))


def DisableParticles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisableParticles(*_args, **kwargs))


def DisableRigidBodies(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisableRigidBodies(*_args, **kwargs))


def DisableSelectedIKHandles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisableSelectedIKHandles(*_args, **kwargs))


def DisableSnapshots(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisableSnapshots(*_args, **kwargs))


def DisableTimeChangeUndoConsolidation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisableTimeChangeUndoConsolidation(*_args, **kwargs))


def DisconnectJoint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisconnectJoint(*_args, **kwargs))


def DisplacementToPolygon(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisplacementToPolygon(*_args, **kwargs))


def DisplayIntermediateObjects(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisplayIntermediateObjects(*_args, **kwargs))


def DisplayLayerEditorWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisplayLayerEditorWindow(*_args, **kwargs))


def DisplayLight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisplayLight(*_args, **kwargs))


def DisplayShaded(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisplayShaded(*_args, **kwargs))


def DisplayShadedAndTextured(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisplayShadedAndTextured(*_args, **kwargs))


def DisplayShadingMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisplayShadingMarkingMenu(*_args, **kwargs))


def DisplayShadingMarkingMenuPopDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisplayShadingMarkingMenuPopDown(*_args, **kwargs))


def DisplaySmoothShaded(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisplaySmoothShaded(*_args, **kwargs))


def DisplayUVShaded(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisplayUVShaded(*_args, **kwargs))


def DisplayUVWireframe(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisplayUVWireframe(*_args, **kwargs))


def DisplayViewport(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisplayViewport(*_args, **kwargs))


def DisplayWireframe(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DisplayWireframe(*_args, **kwargs))


def DistanceTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DistanceTool(*_args, **kwargs))


def DistributeShells(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DistributeShells(*_args, **kwargs))


def DistributeShellsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DistributeShellsOptions(*_args, **kwargs))


def DistributeUVs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DistributeUVs(*_args, **kwargs))


def DistributeUVsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DistributeUVsOptions(*_args, **kwargs))


def DoUnghost(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DoUnghost(*_args, **kwargs))


def DoUnghostOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DoUnghostOptions(*_args, **kwargs))


def DollyTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DollyTool(*_args, **kwargs))


def DopeSheetEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DopeSheetEditor(*_args, **kwargs))


def Drag(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Drag(*_args, **kwargs))


def DragOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DragOptions(*_args, **kwargs))


def Duplicate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Duplicate(*_args, **kwargs))


def DuplicateCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DuplicateCurve(*_args, **kwargs))


def DuplicateCurveOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DuplicateCurveOptions(*_args, **kwargs))


def DuplicateEdges(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DuplicateEdges(*_args, **kwargs))


def DuplicateEdgesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DuplicateEdgesOptions(*_args, **kwargs))


def DuplicateFace(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DuplicateFace(*_args, **kwargs))


def DuplicateFaceOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DuplicateFaceOptions(*_args, **kwargs))


def DuplicateNURBSPatches(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DuplicateNURBSPatches(*_args, **kwargs))


def DuplicateNURBSPatchesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DuplicateNURBSPatchesOptions(*_args, **kwargs))


def DuplicateSpecial(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DuplicateSpecial(*_args, **kwargs))


def DuplicateSpecialOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DuplicateSpecialOptions(*_args, **kwargs))


def DuplicateWithTransform(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DuplicateWithTransform(*_args, **kwargs))


def DynamicRelationshipEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.DynamicRelationshipEditor(*_args, **kwargs))


def EPCurveTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EPCurveTool(*_args, **kwargs))


def EPCurveToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EPCurveToolOptions(*_args, **kwargs))


def EditCharacterAttributes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EditCharacterAttributes(*_args, **kwargs))


def EditFluidResolution(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EditFluidResolution(*_args, **kwargs))


def EditFluidResolutionOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EditFluidResolutionOptions(*_args, **kwargs))


def EditMembershipTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EditMembershipTool(*_args, **kwargs))


def EditOversamplingForCacheSettings(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EditOversamplingForCacheSettings(*_args, **kwargs))


def EditPolygonType(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EditPolygonType(*_args, **kwargs))


def EditTexture(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EditTexture(*_args, **kwargs))


def EmitFluidFromObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EmitFluidFromObject(*_args, **kwargs))


def EmitFluidFromObjectOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EmitFluidFromObjectOptions(*_args, **kwargs))


def EmitFromObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EmitFromObject(*_args, **kwargs))


def EmitFromObjectOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EmitFromObjectOptions(*_args, **kwargs))


def EmptyAnimLayer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EmptyAnimLayer(*_args, **kwargs))


def EnableAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EnableAll(*_args, **kwargs))


def EnableConstraints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EnableConstraints(*_args, **kwargs))


def EnableDynamicConstraints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EnableDynamicConstraints(*_args, **kwargs))


def EnableExpressions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EnableExpressions(*_args, **kwargs))


def EnableFluids(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EnableFluids(*_args, **kwargs))


def EnableGlobalStitch(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EnableGlobalStitch(*_args, **kwargs))


def EnableIKSolvers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EnableIKSolvers(*_args, **kwargs))


def EnableMemoryCaching(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EnableMemoryCaching(*_args, **kwargs))


def EnableNCloths(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EnableNCloths(*_args, **kwargs))


def EnableNParticles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EnableNParticles(*_args, **kwargs))


def EnableNRigids(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EnableNRigids(*_args, **kwargs))


def EnableNucleuses(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EnableNucleuses(*_args, **kwargs))


def EnableParticles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EnableParticles(*_args, **kwargs))


def EnableRigidBodies(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EnableRigidBodies(*_args, **kwargs))


def EnableSelectedIKHandles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EnableSelectedIKHandles(*_args, **kwargs))


def EnableSnapshots(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EnableSnapshots(*_args, **kwargs))


def EnableTimeChangeUndoConsolidation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EnableTimeChangeUndoConsolidation(*_args, **kwargs))


def EnterEditMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EnterEditMode(*_args, **kwargs))


def EnterEditModePress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EnterEditModePress(*_args, **kwargs))


def EnterEditModeRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EnterEditModeRelease(*_args, **kwargs))


def EvaluationToolkit(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.EvaluationToolkit(*_args, **kwargs))


def ExecuteScriptOnFileCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExecuteScriptOnFileCmd(*_args, **kwargs))


def ExpandSelectedComponents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExpandSelectedComponents(*_args, **kwargs))


def Export(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Export(*_args, **kwargs))


def ExportAnimOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExportAnimOptions(*_args, **kwargs))


def ExportDeformerWeights(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExportDeformerWeights(*_args, **kwargs))


def ExportDeformerWeightsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExportDeformerWeightsOptions(*_args, **kwargs))


def ExportOfflineFile(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExportOfflineFile(*_args, **kwargs))


def ExportOfflineFileFromRefEd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExportOfflineFileFromRefEd(*_args, **kwargs))


def ExportOfflineFileFromRefEdOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExportOfflineFileFromRefEdOptions(*_args, **kwargs))


def ExportOfflineFileOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExportOfflineFileOptions(*_args, **kwargs))


def ExportOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExportOptions(*_args, **kwargs))


def ExportProxyContainer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExportProxyContainer(*_args, **kwargs))


def ExportProxyContainerOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExportProxyContainerOptions(*_args, **kwargs))


def ExportSelection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExportSelection(*_args, **kwargs))


def ExportSelectionOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExportSelectionOptions(*_args, **kwargs))


def ExportSkinWeightMaps(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExportSkinWeightMaps(*_args, **kwargs))


def ExportSkinWeightMapsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExportSkinWeightMapsOptions(*_args, **kwargs))


def ExpressionEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExpressionEditor(*_args, **kwargs))


def ExtendCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExtendCurve(*_args, **kwargs))


def ExtendCurveOnSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExtendCurveOnSurface(*_args, **kwargs))


def ExtendCurveOnSurfaceOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExtendCurveOnSurfaceOptions(*_args, **kwargs))


def ExtendCurveOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExtendCurveOptions(*_args, **kwargs))


def ExtendFluid(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExtendFluid(*_args, **kwargs))


def ExtendFluidOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExtendFluidOptions(*_args, **kwargs))


def ExtendSurfaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExtendSurfaces(*_args, **kwargs))


def ExtendSurfacesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExtendSurfacesOptions(*_args, **kwargs))


def ExtractFace(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExtractFace(*_args, **kwargs))


def ExtractFaceOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExtractFaceOptions(*_args, **kwargs))


def ExtractSubdivSurfaceVertices(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExtractSubdivSurfaceVertices(*_args, **kwargs))


def ExtractSubdivSurfaceVerticesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExtractSubdivSurfaceVerticesOptions(*_args, **kwargs))


def Extrude(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Extrude(*_args, **kwargs))


def ExtrudeEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExtrudeEdge(*_args, **kwargs))


def ExtrudeEdgeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExtrudeEdgeOptions(*_args, **kwargs))


def ExtrudeFace(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExtrudeFace(*_args, **kwargs))


def ExtrudeFaceOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExtrudeFaceOptions(*_args, **kwargs))


def ExtrudeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExtrudeOptions(*_args, **kwargs))


def ExtrudeVertex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExtrudeVertex(*_args, **kwargs))


def ExtrudeVertexOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ExtrudeVertexOptions(*_args, **kwargs))


def FBXClose(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXClose(*_args, **kwargs))


def FBXExport(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExport(*_args, **kwargs))


def FBXExportAnimationOnly(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportAnimationOnly(*_args, **kwargs))


def FBXExportApplyConstantKeyReducer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportApplyConstantKeyReducer(*_args, **kwargs))


def FBXExportAudio(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportAudio(*_args, **kwargs))


def FBXExportAxisConversionMethod(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportAxisConversionMethod(*_args, **kwargs))


def FBXExportBakeComplexAnimation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportBakeComplexAnimation(*_args, **kwargs))


def FBXExportBakeComplexEnd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportBakeComplexEnd(*_args, **kwargs))


def FBXExportBakeComplexStart(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportBakeComplexStart(*_args, **kwargs))


def FBXExportBakeComplexStep(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportBakeComplexStep(*_args, **kwargs))


def FBXExportBakeResampleAnimation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportBakeResampleAnimation(*_args, **kwargs))


def FBXExportCacheFile(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportCacheFile(*_args, **kwargs))


def FBXExportCameras(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportCameras(*_args, **kwargs))


def FBXExportColladaFrameRate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportColladaFrameRate(*_args, **kwargs))


def FBXExportColladaSingleMatrix(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportColladaSingleMatrix(*_args, **kwargs))


def FBXExportColladaTriangulate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportColladaTriangulate(*_args, **kwargs))


def FBXExportConstraints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportConstraints(*_args, **kwargs))


def FBXExportConvert2Tif(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportConvert2Tif(*_args, **kwargs))


def FBXExportConvertUnitString(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportConvertUnitString(*_args, **kwargs))


def FBXExportDeleteOriginalTakeOnSplitAnimation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportDeleteOriginalTakeOnSplitAnimation(*_args, **kwargs))


def FBXExportEmbeddedTextures(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportEmbeddedTextures(*_args, **kwargs))


def FBXExportFileVersion(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportFileVersion(*_args, **kwargs))


def FBXExportFinestSubdivLevel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportFinestSubdivLevel(*_args, **kwargs))


def FBXExportGenerateLog(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportGenerateLog(*_args, **kwargs))


def FBXExportHardEdges(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportHardEdges(*_args, **kwargs))


def FBXExportInAscii(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportInAscii(*_args, **kwargs))


def FBXExportIncludeChildren(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportIncludeChildren(*_args, **kwargs))


def FBXExportInputConnections(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportInputConnections(*_args, **kwargs))


def FBXExportInstances(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportInstances(*_args, **kwargs))


def FBXExportLights(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportLights(*_args, **kwargs))


def FBXExportQuaternion(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportQuaternion(*_args, **kwargs))


def FBXExportQuickSelectSetAsCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportQuickSelectSetAsCache(*_args, **kwargs))


def FBXExportReferencedAssetsContent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportReferencedAssetsContent(*_args, **kwargs))


def FBXExportReferencedContainersContent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportReferencedContainersContent(*_args, **kwargs))


def FBXExportScaleFactor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportScaleFactor(*_args, **kwargs))


def FBXExportShapes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportShapes(*_args, **kwargs))


def FBXExportShowUI(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportShowUI(*_args, **kwargs))


def FBXExportSkeletonDefinitions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportSkeletonDefinitions(*_args, **kwargs))


def FBXExportSkins(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportSkins(*_args, **kwargs))


def FBXExportSmoothMesh(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportSmoothMesh(*_args, **kwargs))


def FBXExportSmoothingGroups(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportSmoothingGroups(*_args, **kwargs))


def FBXExportSplitAnimationIntoTakes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportSplitAnimationIntoTakes(*_args, **kwargs))


def FBXExportTangents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportTangents(*_args, **kwargs))


def FBXExportTriangulate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportTriangulate(*_args, **kwargs))


def FBXExportUpAxis(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportUpAxis(*_args, **kwargs))


def FBXExportUseSceneName(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportUseSceneName(*_args, **kwargs))


def FBXExportUseTmpFilePeripheral(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXExportUseTmpFilePeripheral(*_args, **kwargs))


def FBXGetTakeComment(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXGetTakeComment(*_args, **kwargs))


def FBXGetTakeCount(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXGetTakeCount(*_args, **kwargs))


def FBXGetTakeIndex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXGetTakeIndex(*_args, **kwargs))


def FBXGetTakeLocalTimeSpan(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXGetTakeLocalTimeSpan(*_args, **kwargs))


def FBXGetTakeName(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXGetTakeName(*_args, **kwargs))


def FBXGetTakeReferenceTimeSpan(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXGetTakeReferenceTimeSpan(*_args, **kwargs))


def FBXImport(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImport(*_args, **kwargs))


def FBXImportAudio(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportAudio(*_args, **kwargs))


def FBXImportAutoAxisEnable(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportAutoAxisEnable(*_args, **kwargs))


def FBXImportAxisConversionEnable(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportAxisConversionEnable(*_args, **kwargs))


def FBXImportCacheFile(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportCacheFile(*_args, **kwargs))


def FBXImportCameras(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportCameras(*_args, **kwargs))


def FBXImportConstraints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportConstraints(*_args, **kwargs))


def FBXImportConvertDeformingNullsToJoint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportConvertDeformingNullsToJoint(*_args, **kwargs))


def FBXImportConvertUnitString(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportConvertUnitString(*_args, **kwargs))


def FBXImportFillTimeline(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportFillTimeline(*_args, **kwargs))


def FBXImportForcedFileAxis(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportForcedFileAxis(*_args, **kwargs))


def FBXImportGenerateLog(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportGenerateLog(*_args, **kwargs))


def FBXImportHardEdges(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportHardEdges(*_args, **kwargs))


def FBXImportLights(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportLights(*_args, **kwargs))


def FBXImportMergeAnimationLayers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportMergeAnimationLayers(*_args, **kwargs))


def FBXImportMergeBackNullPivots(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportMergeBackNullPivots(*_args, **kwargs))


def FBXImportMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportMode(*_args, **kwargs))


def FBXImportOCMerge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportOCMerge(*_args, **kwargs))


def FBXImportProtectDrivenKeys(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportProtectDrivenKeys(*_args, **kwargs))


def FBXImportQuaternion(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportQuaternion(*_args, **kwargs))


def FBXImportResamplingRateSource(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportResamplingRateSource(*_args, **kwargs))


def FBXImportScaleFactor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportScaleFactor(*_args, **kwargs))


def FBXImportSetLockedAttribute(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportSetLockedAttribute(*_args, **kwargs))


def FBXImportSetMayaFrameRate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportSetMayaFrameRate(*_args, **kwargs))


def FBXImportSetTake(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportSetTake(*_args, **kwargs))


def FBXImportShapes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportShapes(*_args, **kwargs))


def FBXImportShowUI(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportShowUI(*_args, **kwargs))


def FBXImportSkeletonDefinitionsAs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportSkeletonDefinitionsAs(*_args, **kwargs))


def FBXImportSkins(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportSkins(*_args, **kwargs))


def FBXImportUnlockNormals(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportUnlockNormals(*_args, **kwargs))


def FBXImportUpAxis(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXImportUpAxis(*_args, **kwargs))


def FBXLoadExportPresetFile(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXLoadExportPresetFile(*_args, **kwargs))


def FBXLoadImportPresetFile(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXLoadImportPresetFile(*_args, **kwargs))


def FBXLoadMBExportPresetFile(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXLoadMBExportPresetFile(*_args, **kwargs))


def FBXLoadMBImportPresetFile(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXLoadMBImportPresetFile(*_args, **kwargs))


def FBXPopSettings(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXPopSettings(*_args, **kwargs))


def FBXProperties(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXProperties(*_args, **kwargs))


def FBXProperty(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXProperty(*_args, **kwargs))


def FBXPushSettings(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXPushSettings(*_args, **kwargs))


def FBXRead(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXRead(*_args, **kwargs))


def FBXResamplingRate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXResamplingRate(*_args, **kwargs))


def FBXResetExport(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXResetExport(*_args, **kwargs))


def FBXResetImport(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXResetImport(*_args, **kwargs))


def FBXUICallBack(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXUICallBack(*_args, **kwargs))


def FBXUIShowOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FBXUIShowOptions(*_args, **kwargs))


def FilePathEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FilePathEditor(*_args, **kwargs))


def FillHole(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FillHole(*_args, **kwargs))


def FilletBlendTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FilletBlendTool(*_args, **kwargs))


def FilletBlendToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FilletBlendToolOptions(*_args, **kwargs))


def FineLevelComponentDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FineLevelComponentDisplay(*_args, **kwargs))


def Fire(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Fire(*_args, **kwargs))


def FireOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FireOptions(*_args, **kwargs))


def Fireworks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Fireworks(*_args, **kwargs))


def FireworksOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FireworksOptions(*_args, **kwargs))


def FitBSpline(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FitBSpline(*_args, **kwargs))


def FitBSplineOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FitBSplineOptions(*_args, **kwargs))


def Flare(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Flare(*_args, **kwargs))


def FlareOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FlareOptions(*_args, **kwargs))


def FlipContactLayersStateCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FlipContactLayersStateCmd(*_args, **kwargs))


def FlipTriangleEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FlipTriangleEdge(*_args, **kwargs))


def FlipTubeDirection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FlipTubeDirection(*_args, **kwargs))


def FlipUVs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FlipUVs(*_args, **kwargs))


def FlipUVsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FlipUVsOptions(*_args, **kwargs))


def FloatSelectedObjects(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FloatSelectedObjects(*_args, **kwargs))


def FloatSelectedObjectsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FloatSelectedObjectsOptions(*_args, **kwargs))


def FloatSelectedPondObjects(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FloatSelectedPondObjects(*_args, **kwargs))


def FloatSelectedPondObjectsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FloatSelectedPondObjectsOptions(*_args, **kwargs))


def FloodSurfaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FloodSurfaces(*_args, **kwargs))


def FlowPathObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FlowPathObject(*_args, **kwargs))


def FlowPathObjectOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FlowPathObjectOptions(*_args, **kwargs))


def FluidEmitter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FluidEmitter(*_args, **kwargs))


def FluidEmitterOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FluidEmitterOptions(*_args, **kwargs))


def FluidGradients(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FluidGradients(*_args, **kwargs))


def FluidGradientsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FluidGradientsOptions(*_args, **kwargs))


def FourViewArrangement(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FourViewArrangement(*_args, **kwargs))


def FourViewLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FourViewLayout(*_args, **kwargs))


def FrameAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FrameAll(*_args, **kwargs))


def FrameAllInAllViews(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FrameAllInAllViews(*_args, **kwargs))


def FrameSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FrameSelected(*_args, **kwargs))


def FrameSelectedInAllViews(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FrameSelectedInAllViews(*_args, **kwargs))


def FrameSelectedWithoutChildren(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FrameSelectedWithoutChildren(*_args, **kwargs))


def FrameSelectedWithoutChildrenInAllViews(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FrameSelectedWithoutChildrenInAllViews(*_args, **kwargs))


def FreeTangentWeight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FreeTangentWeight(*_args, **kwargs))


def FreeformFillet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FreeformFillet(*_args, **kwargs))


def FreeformFilletOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FreeformFilletOptions(*_args, **kwargs))


def FreezeTransformations(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FreezeTransformations(*_args, **kwargs))


def FreezeTransformationsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FreezeTransformationsOptions(*_args, **kwargs))


def FrontPerspViewLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FrontPerspViewLayout(*_args, **kwargs))


def FullCreaseSubdivSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FullCreaseSubdivSurface(*_args, **kwargs))


def FullHotboxDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.FullHotboxDisplay(*_args, **kwargs))


def GPUBuiltInDeformerControl(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GPUBuiltInDeformerControl(*_args, **kwargs))


def GameExporterWnd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GameExporterWnd(*_args, **kwargs))


def GamePipeline(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GamePipeline(*_args, **kwargs))


def GenerateRagdollCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GenerateRagdollCmd(*_args, **kwargs))


def GeometryConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GeometryConstraint(*_args, **kwargs))


def GeometryConstraintOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GeometryConstraintOptions(*_args, **kwargs))


def GeometryToBoundingBox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GeometryToBoundingBox(*_args, **kwargs))


def GeometryToBoundingBoxOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GeometryToBoundingBoxOptions(*_args, **kwargs))


def GetContactLayersCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GetContactLayersCmd(*_args, **kwargs))


def GetFKIdFromEffectorId(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GetFKIdFromEffectorId(*_args, **kwargs))


def GetFluidExample(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GetFluidExample(*_args, **kwargs))


def GetHIKChildCount(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GetHIKChildCount(*_args, **kwargs))


def GetHIKChildId(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GetHIKChildId(*_args, **kwargs))


def GetHIKEffectorCount(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GetHIKEffectorCount(*_args, **kwargs))


def GetHIKEffectorName(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GetHIKEffectorName(*_args, **kwargs))


def GetHIKMatrixDecomposition(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GetHIKMatrixDecomposition(*_args, **kwargs))


def GetHIKNode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GetHIKNode(*_args, **kwargs))


def GetHIKNodeName(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GetHIKNodeName(*_args, **kwargs))


def GetHIKParentId(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GetHIKParentId(*_args, **kwargs))


def GetHairExample(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GetHairExample(*_args, **kwargs))


def GetOceanPondExample(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GetOceanPondExample(*_args, **kwargs))


def GetProperty2StateAttrNameFromHIKEffectorId(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GetProperty2StateAttrNameFromHIKEffectorId(*_args, **kwargs))


def GetSettingsFromSelectedStroke(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GetSettingsFromSelectedStroke(*_args, **kwargs))


def GetToonExample(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GetToonExample(*_args, **kwargs))


def GhostObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GhostObject(*_args, **kwargs))


def GlobalDiskCacheControl(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GlobalDiskCacheControl(*_args, **kwargs))


def GlobalStitch(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GlobalStitch(*_args, **kwargs))


def GlobalStitchOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GlobalStitchOptions(*_args, **kwargs))


def GoToBindPose(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GoToBindPose(*_args, **kwargs))


def GoToDefaultView(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GoToDefaultView(*_args, **kwargs))


def GoToMaxFrame(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GoToMaxFrame(*_args, **kwargs))


def GoToMinFrame(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GoToMinFrame(*_args, **kwargs))


def GoToNextDrivenKey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GoToNextDrivenKey(*_args, **kwargs))


def GoToPreviousDrivenKey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GoToPreviousDrivenKey(*_args, **kwargs))


def GoToWorkingFrame(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GoToWorkingFrame(*_args, **kwargs))


def Goal(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Goal(*_args, **kwargs))


def GoalOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GoalOptions(*_args, **kwargs))


def GpuCacheExportAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GpuCacheExportAll(*_args, **kwargs))


def GpuCacheExportAllOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GpuCacheExportAllOptions(*_args, **kwargs))


def GpuCacheExportSelection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GpuCacheExportSelection(*_args, **kwargs))


def GpuCacheExportSelectionOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GpuCacheExportSelectionOptions(*_args, **kwargs))


def GpuCacheImport(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GpuCacheImport(*_args, **kwargs))


def GpuCacheImportOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GpuCacheImportOptions(*_args, **kwargs))


def GpuCacheRefreshAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GpuCacheRefreshAll(*_args, **kwargs))


def GraphCopy(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphCopy(*_args, **kwargs))


def GraphCopyOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphCopyOptions(*_args, **kwargs))


def GraphCut(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphCut(*_args, **kwargs))


def GraphCutOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphCutOptions(*_args, **kwargs))


def GraphDelete(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphDelete(*_args, **kwargs))


def GraphDeleteOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphDeleteOptions(*_args, **kwargs))


def GraphEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphEditor(*_args, **kwargs))


def GraphEditorAbsoluteView(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphEditorAbsoluteView(*_args, **kwargs))


def GraphEditorAlwaysDisplayTangents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphEditorAlwaysDisplayTangents(*_args, **kwargs))


def GraphEditorDisableCurveSelection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphEditorDisableCurveSelection(*_args, **kwargs))


def GraphEditorDisplayTangentActive(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphEditorDisplayTangentActive(*_args, **kwargs))


def GraphEditorDisplayValues(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphEditorDisplayValues(*_args, **kwargs))


def GraphEditorEnableCurveSelection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphEditorEnableCurveSelection(*_args, **kwargs))


def GraphEditorFrameAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphEditorFrameAll(*_args, **kwargs))


def GraphEditorFrameCenterView(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphEditorFrameCenterView(*_args, **kwargs))


def GraphEditorFramePlaybackRange(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphEditorFramePlaybackRange(*_args, **kwargs))


def GraphEditorFrameSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphEditorFrameSelected(*_args, **kwargs))


def GraphEditorLockChannel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphEditorLockChannel(*_args, **kwargs))


def GraphEditorNeverDisplayTangents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphEditorNeverDisplayTangents(*_args, **kwargs))


def GraphEditorNormalizedView(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphEditorNormalizedView(*_args, **kwargs))


def GraphEditorStackedView(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphEditorStackedView(*_args, **kwargs))


def GraphEditorUnlockChannel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphEditorUnlockChannel(*_args, **kwargs))


def GraphEditorValueLinesToggle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphEditorValueLinesToggle(*_args, **kwargs))


def GraphPaste(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphPaste(*_args, **kwargs))


def GraphPasteOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphPasteOptions(*_args, **kwargs))


def GraphSnap(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphSnap(*_args, **kwargs))


def GraphSnapOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GraphSnapOptions(*_args, **kwargs))


def Gravity(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Gravity(*_args, **kwargs))


def GravityOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GravityOptions(*_args, **kwargs))


def GreasePencilTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GreasePencilTool(*_args, **kwargs))


def GridOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GridOptions(*_args, **kwargs))


def GridUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GridUV(*_args, **kwargs))


def GridUVOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GridUVOptions(*_args, **kwargs))


def Group(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Group(*_args, **kwargs))


def GroupOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GroupOptions(*_args, **kwargs))


def GroupWithPaintedValuesCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GroupWithPaintedValuesCmd(*_args, **kwargs))


def GrowLoopPolygonSelectionRegion(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GrowLoopPolygonSelectionRegion(*_args, **kwargs))


def GrowPolygonSelectionRegion(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.GrowPolygonSelectionRegion(*_args, **kwargs))


def HIKBodyPartMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HIKBodyPartMode(*_args, **kwargs))


def HIKCharacterControlsTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HIKCharacterControlsTool(*_args, **kwargs))


def HIKComputeReference(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HIKComputeReference(*_args, **kwargs))


def HIKCycleMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HIKCycleMode(*_args, **kwargs))


def HIKFullBodyMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HIKFullBodyMode(*_args, **kwargs))


def HIKGetRemoteCharacterList(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HIKGetRemoteCharacterList(*_args, **kwargs))


def HIKInitAxis(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HIKInitAxis(*_args, **kwargs))


def HIKLiveConnectionTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HIKLiveConnectionTool(*_args, **kwargs))


def HIKPinRotate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HIKPinRotate(*_args, **kwargs))


def HIKPinTranslate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HIKPinTranslate(*_args, **kwargs))


def HIKSelectedMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HIKSelectedMode(*_args, **kwargs))


def HIKSetBodyPartKey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HIKSetBodyPartKey(*_args, **kwargs))


def HIKSetFullBodyKey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HIKSetFullBodyKey(*_args, **kwargs))


def HIKSetSelectionKey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HIKSetSelectionKey(*_args, **kwargs))


def HIKToggleReleasePinning(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HIKToggleReleasePinning(*_args, **kwargs))


def HIKUiControl(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HIKUiControl(*_args, **kwargs))


def HairUVSetLinkingEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HairUVSetLinkingEditor(*_args, **kwargs))


def HardwareRenderBuffer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HardwareRenderBuffer(*_args, **kwargs))


def Help(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Help(*_args, **kwargs))


def HideAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideAll(*_args, **kwargs))


def HideBoundingBox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideBoundingBox(*_args, **kwargs))


def HideCameraManipulators(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideCameraManipulators(*_args, **kwargs))


def HideCameras(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideCameras(*_args, **kwargs))


def HideClusters(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideClusters(*_args, **kwargs))


def HideControllers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideControllers(*_args, **kwargs))


def HideDeformers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideDeformers(*_args, **kwargs))


def HideDeformingGeometry(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideDeformingGeometry(*_args, **kwargs))


def HideDynamicConstraints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideDynamicConstraints(*_args, **kwargs))


def HideFluids(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideFluids(*_args, **kwargs))


def HideFollicles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideFollicles(*_args, **kwargs))


def HideFur(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideFur(*_args, **kwargs))


def HideGeometry(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideGeometry(*_args, **kwargs))


def HideHairSystems(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideHairSystems(*_args, **kwargs))


def HideHotbox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideHotbox(*_args, **kwargs))


def HideIKHandles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideIKHandles(*_args, **kwargs))


def HideIntermediateObjects(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideIntermediateObjects(*_args, **kwargs))


def HideJoints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideJoints(*_args, **kwargs))


def HideKinematics(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideKinematics(*_args, **kwargs))


def HideLattices(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideLattices(*_args, **kwargs))


def HideLightManipulators(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideLightManipulators(*_args, **kwargs))


def HideLights(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideLights(*_args, **kwargs))


def HideManipulators(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideManipulators(*_args, **kwargs))


def HideMarkers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideMarkers(*_args, **kwargs))


def HideNCloths(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideNCloths(*_args, **kwargs))


def HideNParticles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideNParticles(*_args, **kwargs))


def HideNRigids(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideNRigids(*_args, **kwargs))


def HideNURBSCurves(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideNURBSCurves(*_args, **kwargs))


def HideNURBSSurfaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideNURBSSurfaces(*_args, **kwargs))


def HideNonlinears(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideNonlinears(*_args, **kwargs))


def HideObjectGeometry(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideObjectGeometry(*_args, **kwargs))


def HidePlanes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HidePlanes(*_args, **kwargs))


def HidePolygonSurfaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HidePolygonSurfaces(*_args, **kwargs))


def HideSculptObjects(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideSculptObjects(*_args, **kwargs))


def HideSelectedObjects(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideSelectedObjects(*_args, **kwargs))


def HideSmoothSkinInfluences(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideSmoothSkinInfluences(*_args, **kwargs))


def HideStrokeControlCurves(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideStrokeControlCurves(*_args, **kwargs))


def HideStrokePathCurves(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideStrokePathCurves(*_args, **kwargs))


def HideStrokes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideStrokes(*_args, **kwargs))


def HideSubdivSurfaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideSubdivSurfaces(*_args, **kwargs))


def HideTexturePlacements(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideTexturePlacements(*_args, **kwargs))


def HideUIElements(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideUIElements(*_args, **kwargs))


def HideUnselectedCVs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideUnselectedCVs(*_args, **kwargs))


def HideUnselectedObjects(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideUnselectedObjects(*_args, **kwargs))


def HideWrapInfluences(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HideWrapInfluences(*_args, **kwargs))


def HighQualityDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HighQualityDisplay(*_args, **kwargs))


def HoldCurrentKeys(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HoldCurrentKeys(*_args, **kwargs))


def HotkeyPreferencesWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HotkeyPreferencesWindow(*_args, **kwargs))


def HyperGraphPanelRedoViewChange(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HyperGraphPanelRedoViewChange(*_args, **kwargs))


def HyperGraphPanelUndoViewChange(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HyperGraphPanelUndoViewChange(*_args, **kwargs))


def HypergraphDGWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypergraphDGWindow(*_args, **kwargs))


def HypergraphDecreaseDepth(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypergraphDecreaseDepth(*_args, **kwargs))


def HypergraphHierarchyWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypergraphHierarchyWindow(*_args, **kwargs))


def HypergraphIncreaseDepth(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypergraphIncreaseDepth(*_args, **kwargs))


def HypergraphWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypergraphWindow(*_args, **kwargs))


def HypershadeAddOnNodeCreate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeAddOnNodeCreate(*_args, **kwargs))


def HypershadeAdditiveGraphingMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeAdditiveGraphingMode(*_args, **kwargs))


def HypershadeAutoSizeNodes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeAutoSizeNodes(*_args, **kwargs))


def HypershadeCloseActiveTab(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeCloseActiveTab(*_args, **kwargs))


def HypershadeCloseAllTabs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeCloseAllTabs(*_args, **kwargs))


def HypershadeCollapseAsset(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeCollapseAsset(*_args, **kwargs))


def HypershadeConnectSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeConnectSelected(*_args, **kwargs))


def HypershadeConvertPSDToFileTexture(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeConvertPSDToFileTexture(*_args, **kwargs))


def HypershadeConvertPSDToLayeredTexture(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeConvertPSDToLayeredTexture(*_args, **kwargs))


def HypershadeConvertToFileTexture(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeConvertToFileTexture(*_args, **kwargs))


def HypershadeConvertToFileTextureOptionBox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeConvertToFileTextureOptionBox(*_args, **kwargs))


def HypershadeCreateAsset(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeCreateAsset(*_args, **kwargs))


def HypershadeCreateContainerOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeCreateContainerOptions(*_args, **kwargs))


def HypershadeCreateNewTab(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeCreateNewTab(*_args, **kwargs))


def HypershadeCreatePSDFile(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeCreatePSDFile(*_args, **kwargs))


def HypershadeCreateTab(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeCreateTab(*_args, **kwargs))


def HypershadeDeleteAllBakeSets(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDeleteAllBakeSets(*_args, **kwargs))


def HypershadeDeleteAllCamerasAndImagePlanes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDeleteAllCamerasAndImagePlanes(*_args, **kwargs))


def HypershadeDeleteAllLights(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDeleteAllLights(*_args, **kwargs))


def HypershadeDeleteAllShadingGroupsAndMaterials(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDeleteAllShadingGroupsAndMaterials(*_args, **kwargs))


def HypershadeDeleteAllTextures(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDeleteAllTextures(*_args, **kwargs))


def HypershadeDeleteAllUtilities(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDeleteAllUtilities(*_args, **kwargs))


def HypershadeDeleteDuplicateShadingNetworks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDeleteDuplicateShadingNetworks(*_args, **kwargs))


def HypershadeDeleteNodes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDeleteNodes(*_args, **kwargs))


def HypershadeDeleteSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDeleteSelected(*_args, **kwargs))


def HypershadeDeleteUnusedNodes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDeleteUnusedNodes(*_args, **kwargs))


def HypershadeDisplayAllShapes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDisplayAllShapes(*_args, **kwargs))


def HypershadeDisplayAsExtraLargeSwatches(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDisplayAsExtraLargeSwatches(*_args, **kwargs))


def HypershadeDisplayAsIcons(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDisplayAsIcons(*_args, **kwargs))


def HypershadeDisplayAsLargeSwatches(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDisplayAsLargeSwatches(*_args, **kwargs))


def HypershadeDisplayAsList(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDisplayAsList(*_args, **kwargs))


def HypershadeDisplayAsMediumSwatches(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDisplayAsMediumSwatches(*_args, **kwargs))


def HypershadeDisplayAsSmallSwatches(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDisplayAsSmallSwatches(*_args, **kwargs))


def HypershadeDisplayInterestingShapes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDisplayInterestingShapes(*_args, **kwargs))


def HypershadeDisplayNoShapes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDisplayNoShapes(*_args, **kwargs))


def HypershadeDuplicateShadingNetwork(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDuplicateShadingNetwork(*_args, **kwargs))


def HypershadeDuplicateWithConnections(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDuplicateWithConnections(*_args, **kwargs))


def HypershadeDuplicateWithoutNetwork(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeDuplicateWithoutNetwork(*_args, **kwargs))


def HypershadeEditPSDFile(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeEditPSDFile(*_args, **kwargs))


def HypershadeEditTexture(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeEditTexture(*_args, **kwargs))


def HypershadeExpandAsset(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeExpandAsset(*_args, **kwargs))


def HypershadeExportSelectedNetwork(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeExportSelectedNetwork(*_args, **kwargs))


def HypershadeFrameAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeFrameAll(*_args, **kwargs))


def HypershadeFrameSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeFrameSelected(*_args, **kwargs))


def HypershadeGraphAddSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeGraphAddSelected(*_args, **kwargs))


def HypershadeGraphClearGraph(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeGraphClearGraph(*_args, **kwargs))


def HypershadeGraphDownstream(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeGraphDownstream(*_args, **kwargs))


def HypershadeGraphMaterialsOnSelectedObjects(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeGraphMaterialsOnSelectedObjects(*_args, **kwargs))


def HypershadeGraphRearrange(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeGraphRearrange(*_args, **kwargs))


def HypershadeGraphRemoveDownstream(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeGraphRemoveDownstream(*_args, **kwargs))


def HypershadeGraphRemoveSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeGraphRemoveSelected(*_args, **kwargs))


def HypershadeGraphRemoveUnselected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeGraphRemoveUnselected(*_args, **kwargs))


def HypershadeGraphRemoveUpstream(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeGraphRemoveUpstream(*_args, **kwargs))


def HypershadeGraphUpDownstream(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeGraphUpDownstream(*_args, **kwargs))


def HypershadeGraphUpstream(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeGraphUpstream(*_args, **kwargs))


def HypershadeGridToggleSnap(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeGridToggleSnap(*_args, **kwargs))


def HypershadeGridToggleVisibility(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeGridToggleVisibility(*_args, **kwargs))


def HypershadeHideAttributes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeHideAttributes(*_args, **kwargs))


def HypershadeImport(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeImport(*_args, **kwargs))


def HypershadeIncreaseTraversalDepth(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeIncreaseTraversalDepth(*_args, **kwargs))


def HypershadeMoveTabDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeMoveTabDown(*_args, **kwargs))


def HypershadeMoveTabLeft(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeMoveTabLeft(*_args, **kwargs))


def HypershadeMoveTabRight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeMoveTabRight(*_args, **kwargs))


def HypershadeMoveTabUp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeMoveTabUp(*_args, **kwargs))


def HypershadeOpenBinsWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeOpenBinsWindow(*_args, **kwargs))


def HypershadeOpenBrowserWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeOpenBrowserWindow(*_args, **kwargs))


def HypershadeOpenConnectWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeOpenConnectWindow(*_args, **kwargs))


def HypershadeOpenCreateWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeOpenCreateWindow(*_args, **kwargs))


def HypershadeOpenGraphEditorWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeOpenGraphEditorWindow(*_args, **kwargs))


def HypershadeOpenMaterialViewerWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeOpenMaterialViewerWindow(*_args, **kwargs))


def HypershadeOpenModelEditorWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeOpenModelEditorWindow(*_args, **kwargs))


def HypershadeOpenOutlinerWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeOpenOutlinerWindow(*_args, **kwargs))


def HypershadeOpenPropertyEditorWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeOpenPropertyEditorWindow(*_args, **kwargs))


def HypershadeOpenRenderViewWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeOpenRenderViewWindow(*_args, **kwargs))


def HypershadeOpenSpreadSheetWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeOpenSpreadSheetWindow(*_args, **kwargs))


def HypershadeOpenUVEditorWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeOpenUVEditorWindow(*_args, **kwargs))


def HypershadeOutlinerPerspLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeOutlinerPerspLayout(*_args, **kwargs))


def HypershadePerspLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadePerspLayout(*_args, **kwargs))


def HypershadePickWalkDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadePickWalkDown(*_args, **kwargs))


def HypershadePickWalkLeft(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadePickWalkLeft(*_args, **kwargs))


def HypershadePickWalkRight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadePickWalkRight(*_args, **kwargs))


def HypershadePickWalkUp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadePickWalkUp(*_args, **kwargs))


def HypershadePinByDefault(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadePinByDefault(*_args, **kwargs))


def HypershadePinSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadePinSelected(*_args, **kwargs))


def HypershadePublishConnections(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadePublishConnections(*_args, **kwargs))


def HypershadeReduceTraversalDepth(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeReduceTraversalDepth(*_args, **kwargs))


def HypershadeRefreshAllSwatchesOnDisk(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeRefreshAllSwatchesOnDisk(*_args, **kwargs))


def HypershadeRefreshFileListing(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeRefreshFileListing(*_args, **kwargs))


def HypershadeRefreshSelectedSwatches(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeRefreshSelectedSwatches(*_args, **kwargs))


def HypershadeRefreshSelectedSwatchesOnDisk(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeRefreshSelectedSwatchesOnDisk(*_args, **kwargs))


def HypershadeRemoveAsset(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeRemoveAsset(*_args, **kwargs))


def HypershadeRemoveTab(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeRemoveTab(*_args, **kwargs))


def HypershadeRenameActiveTab(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeRenameActiveTab(*_args, **kwargs))


def HypershadeRenameTab(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeRenameTab(*_args, **kwargs))


def HypershadeRenderPerspLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeRenderPerspLayout(*_args, **kwargs))


def HypershadeRenderTextureRange(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeRenderTextureRange(*_args, **kwargs))


def HypershadeRenderTextureRangeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeRenderTextureRangeOptions(*_args, **kwargs))


def HypershadeRestoreLastClosedTab(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeRestoreLastClosedTab(*_args, **kwargs))


def HypershadeRevertSelectedSwatches(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeRevertSelectedSwatches(*_args, **kwargs))


def HypershadeRevertToDefaultTabs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeRevertToDefaultTabs(*_args, **kwargs))


def HypershadeSaveSwatchesToDisk(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeSaveSwatchesToDisk(*_args, **kwargs))


def HypershadeSelectBakeSets(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeSelectBakeSets(*_args, **kwargs))


def HypershadeSelectCamerasAndImagePlanes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeSelectCamerasAndImagePlanes(*_args, **kwargs))


def HypershadeSelectConnected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeSelectConnected(*_args, **kwargs))


def HypershadeSelectDownStream(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeSelectDownStream(*_args, **kwargs))


def HypershadeSelectLights(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeSelectLights(*_args, **kwargs))


def HypershadeSelectMaterialsFromObjects(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeSelectMaterialsFromObjects(*_args, **kwargs))


def HypershadeSelectObjectsWithMaterials(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeSelectObjectsWithMaterials(*_args, **kwargs))


def HypershadeSelectShadingGroupsAndMaterials(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeSelectShadingGroupsAndMaterials(*_args, **kwargs))


def HypershadeSelectTextures(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeSelectTextures(*_args, **kwargs))


def HypershadeSelectUpStream(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeSelectUpStream(*_args, **kwargs))


def HypershadeSelectUtilities(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeSelectUtilities(*_args, **kwargs))


def HypershadeSetLargeNodeSwatchSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeSetLargeNodeSwatchSize(*_args, **kwargs))


def HypershadeSetSmallNodeSwatchSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeSetSmallNodeSwatchSize(*_args, **kwargs))


def HypershadeSetTraversalDepthUnlim(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeSetTraversalDepthUnlim(*_args, **kwargs))


def HypershadeSetTraversalDepthZero(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeSetTraversalDepthZero(*_args, **kwargs))


def HypershadeShapeMenuStateAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeShapeMenuStateAll(*_args, **kwargs))


def HypershadeShapeMenuStateAllExceptShadingGroupMembers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeShapeMenuStateAllExceptShadingGroupMembers(*_args, **kwargs))


def HypershadeShapeMenuStateNoShapes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeShapeMenuStateNoShapes(*_args, **kwargs))


def HypershadeShowAllAttrs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeShowAllAttrs(*_args, **kwargs))


def HypershadeShowConnectedAttrs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeShowConnectedAttrs(*_args, **kwargs))


def HypershadeShowCustomAttrs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeShowCustomAttrs(*_args, **kwargs))


def HypershadeShowDirectoriesAndFiles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeShowDirectoriesAndFiles(*_args, **kwargs))


def HypershadeShowDirectoriesOnly(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeShowDirectoriesOnly(*_args, **kwargs))


def HypershadeSortByName(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeSortByName(*_args, **kwargs))


def HypershadeSortByTime(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeSortByTime(*_args, **kwargs))


def HypershadeSortByType(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeSortByType(*_args, **kwargs))


def HypershadeSortReverseOrder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeSortReverseOrder(*_args, **kwargs))


def HypershadeTestTexture(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeTestTexture(*_args, **kwargs))


def HypershadeTestTextureOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeTestTextureOptions(*_args, **kwargs))


def HypershadeToggleAttrFilter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeToggleAttrFilter(*_args, **kwargs))


def HypershadeToggleCrosshairOnEdgeDragging(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeToggleCrosshairOnEdgeDragging(*_args, **kwargs))


def HypershadeToggleNodeSwatchSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeToggleNodeSwatchSize(*_args, **kwargs))


def HypershadeToggleNodeTitleMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeToggleNodeTitleMode(*_args, **kwargs))


def HypershadeToggleShowNamespace(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeToggleShowNamespace(*_args, **kwargs))


def HypershadeToggleTransformDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeToggleTransformDisplay(*_args, **kwargs))


def HypershadeToggleUseAssetsAndPublishedAttributes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeToggleUseAssetsAndPublishedAttributes(*_args, **kwargs))


def HypershadeToggleZoomIn(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeToggleZoomIn(*_args, **kwargs))


def HypershadeToggleZoomOut(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeToggleZoomOut(*_args, **kwargs))


def HypershadeTransferAttributeValues(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeTransferAttributeValues(*_args, **kwargs))


def HypershadeTransferAttributeValuesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeTransferAttributeValuesOptions(*_args, **kwargs))


def HypershadeUnpinSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeUnpinSelected(*_args, **kwargs))


def HypershadeUpdatePSDNetworks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeUpdatePSDNetworks(*_args, **kwargs))


def HypershadeWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.HypershadeWindow(*_args, **kwargs))


def IKHandleTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.IKHandleTool(*_args, **kwargs))


def IKHandleToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.IKHandleToolOptions(*_args, **kwargs))


def IKSplineHandleTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.IKSplineHandleTool(*_args, **kwargs))


def IKSplineHandleToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.IKSplineHandleToolOptions(*_args, **kwargs))


def IPROptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.IPROptions(*_args, **kwargs))


def IPRRenderIntoNewWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.IPRRenderIntoNewWindow(*_args, **kwargs))


def Import(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Import(*_args, **kwargs))


def ImportAnimOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ImportAnimOptions(*_args, **kwargs))


def ImportDeformerWeights(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ImportDeformerWeights(*_args, **kwargs))


def ImportDeformerWeightsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ImportDeformerWeightsOptions(*_args, **kwargs))


def ImportOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ImportOptions(*_args, **kwargs))


def ImportSkinWeightMaps(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ImportSkinWeightMaps(*_args, **kwargs))


def ImportWorkspaceFiles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ImportWorkspaceFiles(*_args, **kwargs))


def InTangentAuto(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InTangentAuto(*_args, **kwargs))


def InTangentClamped(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InTangentClamped(*_args, **kwargs))


def InTangentFixed(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InTangentFixed(*_args, **kwargs))


def InTangentFlat(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InTangentFlat(*_args, **kwargs))


def InTangentLinear(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InTangentLinear(*_args, **kwargs))


def InTangentPlateau(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InTangentPlateau(*_args, **kwargs))


def InTangentSpline(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InTangentSpline(*_args, **kwargs))


def IncreaseCheckerDensity(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.IncreaseCheckerDensity(*_args, **kwargs))


def IncreaseExposureCoarse(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.IncreaseExposureCoarse(*_args, **kwargs))


def IncreaseExposureFine(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.IncreaseExposureFine(*_args, **kwargs))


def IncreaseGammaCoarse(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.IncreaseGammaCoarse(*_args, **kwargs))


def IncreaseGammaFine(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.IncreaseGammaFine(*_args, **kwargs))


def IncreaseManipulatorSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.IncreaseManipulatorSize(*_args, **kwargs))


def IncrementAndSave(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.IncrementAndSave(*_args, **kwargs))


def IncrementFluidCenter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.IncrementFluidCenter(*_args, **kwargs))


def InitialFluidStates(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InitialFluidStates(*_args, **kwargs))


def InitialFluidStatesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InitialFluidStatesOptions(*_args, **kwargs))


def InsertEdgeLoopTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InsertEdgeLoopTool(*_args, **kwargs))


def InsertEdgeLoopToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InsertEdgeLoopToolOptions(*_args, **kwargs))


def InsertIsoparms(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InsertIsoparms(*_args, **kwargs))


def InsertIsoparmsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InsertIsoparmsOptions(*_args, **kwargs))


def InsertJointTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InsertJointTool(*_args, **kwargs))


def InsertKeyToolActivate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InsertKeyToolActivate(*_args, **kwargs))


def InsertKeyToolDeactivate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InsertKeyToolDeactivate(*_args, **kwargs))


def InsertKeysTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InsertKeysTool(*_args, **kwargs))


def InsertKeysToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InsertKeysToolOptions(*_args, **kwargs))


def InsertKnot(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InsertKnot(*_args, **kwargs))


def InsertKnotOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InsertKnotOptions(*_args, **kwargs))


def InteractiveBindSkin(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InteractiveBindSkin(*_args, **kwargs))


def InteractiveBindSkinOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InteractiveBindSkinOptions(*_args, **kwargs))


def InteractivePlayback(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InteractivePlayback(*_args, **kwargs))


def InteractiveSplitTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InteractiveSplitTool(*_args, **kwargs))


def InteractiveSplitToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InteractiveSplitToolOptions(*_args, **kwargs))


def IntersectCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.IntersectCurve(*_args, **kwargs))


def IntersectCurveOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.IntersectCurveOptions(*_args, **kwargs))


def IntersectSurfaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.IntersectSurfaces(*_args, **kwargs))


def IntersectSurfacesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.IntersectSurfacesOptions(*_args, **kwargs))


def InvertSelection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.InvertSelection(*_args, **kwargs))


def JointTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.JointTool(*_args, **kwargs))


def JointToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.JointToolOptions(*_args, **kwargs))


def KeyBlendShapeTargetsWeight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.KeyBlendShapeTargetsWeight(*_args, **kwargs))


def KeyframeTangentMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.KeyframeTangentMarkingMenu(*_args, **kwargs))


def KeyframeTangentMarkingMenuPopDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.KeyframeTangentMarkingMenuPopDown(*_args, **kwargs))


def LODGenerateMeshes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LODGenerateMeshes(*_args, **kwargs))


def LODGenerateMeshesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LODGenerateMeshesOptions(*_args, **kwargs))


def LassoTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LassoTool(*_args, **kwargs))


def LastActionTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LastActionTool(*_args, **kwargs))


def LatchToNearestSetCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LatchToNearestSetCmd(*_args, **kwargs))


def LatticeDeformKeysTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LatticeDeformKeysTool(*_args, **kwargs))


def LatticeDeformKeysToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LatticeDeformKeysToolOptions(*_args, **kwargs))


def LatticeUVTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LatticeUVTool(*_args, **kwargs))


def LatticeUVToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LatticeUVToolOptions(*_args, **kwargs))


def LaunchViewerCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LaunchViewerCmd(*_args, **kwargs))


def LayerRelationshipEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LayerRelationshipEditor(*_args, **kwargs))


def LayoutUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LayoutUV(*_args, **kwargs))


def LayoutUVAlong(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LayoutUVAlong(*_args, **kwargs))


def LayoutUVAlongOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LayoutUVAlongOptions(*_args, **kwargs))


def LayoutUVOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LayoutUVOptions(*_args, **kwargs))


def LayoutUVRectangle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LayoutUVRectangle(*_args, **kwargs))


def LevelOfDetailGroup(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LevelOfDetailGroup(*_args, **kwargs))


def LevelOfDetailGroupOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LevelOfDetailGroupOptions(*_args, **kwargs))


def LevelOfDetailUngroup(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LevelOfDetailUngroup(*_args, **kwargs))


def LightCentricLightLinkingEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LightCentricLightLinkingEditor(*_args, **kwargs))


def Lightning(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Lightning(*_args, **kwargs))


def LightningOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LightningOptions(*_args, **kwargs))


def LoadHIKCharacterDefinition(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LoadHIKCharacterDefinition(*_args, **kwargs))


def LoadHIKCharacterState(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LoadHIKCharacterState(*_args, **kwargs))


def LoadHIKEffectorSetState(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LoadHIKEffectorSetState(*_args, **kwargs))


def LoadHIKPropertySetState(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LoadHIKPropertySetState(*_args, **kwargs))


def LockCamera(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LockCamera(*_args, **kwargs))


def LockContainer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LockContainer(*_args, **kwargs))


def LockCurveLength(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LockCurveLength(*_args, **kwargs))


def LockNormals(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LockNormals(*_args, **kwargs))


def LockTangentWeight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LockTangentWeight(*_args, **kwargs))


def Loft(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Loft(*_args, **kwargs))


def LoftOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LoftOptions(*_args, **kwargs))


def LongPolygonNormals(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LongPolygonNormals(*_args, **kwargs))


def LookAtSelection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LookAtSelection(*_args, **kwargs))


def LoopBrushAnimation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LoopBrushAnimation(*_args, **kwargs))


def LoopBrushAnimationOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LoopBrushAnimationOptions(*_args, **kwargs))


def LowQualityDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.LowQualityDisplay(*_args, **kwargs))


def MakeBoats(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakeBoats(*_args, **kwargs))


def MakeBoatsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakeBoatsOptions(*_args, **kwargs))


def MakeBrushSpring(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakeBrushSpring(*_args, **kwargs))


def MakeBrushSpringOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakeBrushSpringOptions(*_args, **kwargs))


def MakeCollide(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakeCollide(*_args, **kwargs))


def MakeCollideHair(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakeCollideHair(*_args, **kwargs))


def MakeCollideOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakeCollideOptions(*_args, **kwargs))


def MakeCurvesDynamic(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakeCurvesDynamic(*_args, **kwargs))


def MakeCurvesDynamicOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakeCurvesDynamicOptions(*_args, **kwargs))


def MakeFluidCollide(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakeFluidCollide(*_args, **kwargs))


def MakeFluidCollideOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakeFluidCollideOptions(*_args, **kwargs))


def MakeHoleTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakeHoleTool(*_args, **kwargs))


def MakeHoleToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakeHoleToolOptions(*_args, **kwargs))


def MakeLightLinks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakeLightLinks(*_args, **kwargs))


def MakeLive(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakeLive(*_args, **kwargs))


def MakeMotionField(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakeMotionField(*_args, **kwargs))


def MakeMotorBoats(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakeMotorBoats(*_args, **kwargs))


def MakeMotorBoatsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakeMotorBoatsOptions(*_args, **kwargs))


def MakePaintable(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakePaintable(*_args, **kwargs))


def MakePondBoats(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakePondBoats(*_args, **kwargs))


def MakePondBoatsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakePondBoatsOptions(*_args, **kwargs))


def MakePondMotorBoats(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakePondMotorBoats(*_args, **kwargs))


def MakePondMotorBoatsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakePondMotorBoatsOptions(*_args, **kwargs))


def MakePressureCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakePressureCurve(*_args, **kwargs))


def MakePressureCurveOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakePressureCurveOptions(*_args, **kwargs))


def MakeShadowLinks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakeShadowLinks(*_args, **kwargs))


def MakeUVInstanceCurrent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MakeUVInstanceCurrent(*_args, **kwargs))


def MapUVBorder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MapUVBorder(*_args, **kwargs))


def MapUVBorderOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MapUVBorderOptions(*_args, **kwargs))


def MarkingMenuPopDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MarkingMenuPopDown(*_args, **kwargs))


def MarkingMenuPreferencesWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MarkingMenuPreferencesWindow(*_args, **kwargs))


def MatchPivots(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MatchPivots(*_args, **kwargs))


def MatchRotation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MatchRotation(*_args, **kwargs))


def MatchScaling(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MatchScaling(*_args, **kwargs))


def MatchTransform(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MatchTransform(*_args, **kwargs))


def MatchTranslation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MatchTranslation(*_args, **kwargs))


def MatchUVs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MatchUVs(*_args, **kwargs))


def MatchUVsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MatchUVsOptions(*_args, **kwargs))


def MediumPolygonNormals(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MediumPolygonNormals(*_args, **kwargs))


def MediumQualityDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MediumQualityDisplay(*_args, **kwargs))


def MergeCharacterSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MergeCharacterSet(*_args, **kwargs))


def MergeEdgeTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MergeEdgeTool(*_args, **kwargs))


def MergeEdgeToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MergeEdgeToolOptions(*_args, **kwargs))


def MergeMultipleEdges(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MergeMultipleEdges(*_args, **kwargs))


def MergeMultipleEdgesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MergeMultipleEdgesOptions(*_args, **kwargs))


def MergeToCenter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MergeToCenter(*_args, **kwargs))


def MergeUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MergeUV(*_args, **kwargs))


def MergeUVOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MergeUVOptions(*_args, **kwargs))


def MergeVertexTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MergeVertexTool(*_args, **kwargs))


def MergeVertexToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MergeVertexToolOptions(*_args, **kwargs))


def MergeVertices(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MergeVertices(*_args, **kwargs))


def MergeVerticesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MergeVerticesOptions(*_args, **kwargs))


def MinimizeApplication(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MinimizeApplication(*_args, **kwargs))


def MirrorCutPolygonGeometry(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MirrorCutPolygonGeometry(*_args, **kwargs))


def MirrorCutPolygonGeometryOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MirrorCutPolygonGeometryOptions(*_args, **kwargs))


def MirrorDeformerWeights(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MirrorDeformerWeights(*_args, **kwargs))


def MirrorDeformerWeightsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MirrorDeformerWeightsOptions(*_args, **kwargs))


def MirrorJoint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MirrorJoint(*_args, **kwargs))


def MirrorJointOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MirrorJointOptions(*_args, **kwargs))


def MirrorPolygonGeometry(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MirrorPolygonGeometry(*_args, **kwargs))


def MirrorPolygonGeometryOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MirrorPolygonGeometryOptions(*_args, **kwargs))


def MirrorSkinWeights(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MirrorSkinWeights(*_args, **kwargs))


def MirrorSkinWeightsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MirrorSkinWeightsOptions(*_args, **kwargs))


def MirrorSubdivSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MirrorSubdivSurface(*_args, **kwargs))


def MirrorSubdivSurfaceOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MirrorSubdivSurfaceOptions(*_args, **kwargs))


def ModelingPanelRedoViewChange(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ModelingPanelRedoViewChange(*_args, **kwargs))


def ModelingPanelUndoViewChange(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ModelingPanelUndoViewChange(*_args, **kwargs))


def ModifyConstraintAxis(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ModifyConstraintAxis(*_args, **kwargs))


def ModifyConstraintAxisOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ModifyConstraintAxisOptions(*_args, **kwargs))


def ModifyDisplacementPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ModifyDisplacementPress(*_args, **kwargs))


def ModifyDisplacementRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ModifyDisplacementRelease(*_args, **kwargs))


def ModifyLowerRadiusPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ModifyLowerRadiusPress(*_args, **kwargs))


def ModifyLowerRadiusRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ModifyLowerRadiusRelease(*_args, **kwargs))


def ModifyOpacityPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ModifyOpacityPress(*_args, **kwargs))


def ModifyOpacityRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ModifyOpacityRelease(*_args, **kwargs))


def ModifyPaintValuePress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ModifyPaintValuePress(*_args, **kwargs))


def ModifyPaintValueRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ModifyPaintValueRelease(*_args, **kwargs))


def ModifyStampDepthPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ModifyStampDepthPress(*_args, **kwargs))


def ModifyStampDepthRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ModifyStampDepthRelease(*_args, **kwargs))


def ModifyUVVectorPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ModifyUVVectorPress(*_args, **kwargs))


def ModifyUVVectorRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ModifyUVVectorRelease(*_args, **kwargs))


def ModifyUpperRadiusPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ModifyUpperRadiusPress(*_args, **kwargs))


def ModifyUpperRadiusRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ModifyUpperRadiusRelease(*_args, **kwargs))


def MoveDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MoveDown(*_args, **kwargs))


def MoveIKtoFK(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MoveIKtoFK(*_args, **kwargs))


def MoveInfluence(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MoveInfluence(*_args, **kwargs))


def MoveLeft(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MoveLeft(*_args, **kwargs))


def MoveNearestPickedKeyToolActivate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MoveNearestPickedKeyToolActivate(*_args, **kwargs))


def MoveNearestPickedKeyToolDeactivate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MoveNearestPickedKeyToolDeactivate(*_args, **kwargs))


def MoveNormalTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MoveNormalTool(*_args, **kwargs))


def MoveNormalToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MoveNormalToolOptions(*_args, **kwargs))


def MovePolygonComponent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MovePolygonComponent(*_args, **kwargs))


def MovePolygonComponentOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MovePolygonComponentOptions(*_args, **kwargs))


def MoveRight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MoveRight(*_args, **kwargs))


def MoveRotateScaleTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MoveRotateScaleTool(*_args, **kwargs))


def MoveRotateScaleToolToggleSnapMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MoveRotateScaleToolToggleSnapMode(*_args, **kwargs))


def MoveRotateScaleToolToggleSnapRelativeMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MoveRotateScaleToolToggleSnapRelativeMode(*_args, **kwargs))


def MoveSewUVs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MoveSewUVs(*_args, **kwargs))


def MoveSkinJointsTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MoveSkinJointsTool(*_args, **kwargs))


def MoveSkinJointsToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MoveSkinJointsToolOptions(*_args, **kwargs))


def MoveTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MoveTool(*_args, **kwargs))


def MoveToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MoveToolOptions(*_args, **kwargs))


def MoveUVTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MoveUVTool(*_args, **kwargs))


def MoveUp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.MoveUp(*_args, **kwargs))


def NCreateEmitter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NCreateEmitter(*_args, **kwargs))


def NCreateEmitterOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NCreateEmitterOptions(*_args, **kwargs))


def NEmitFromObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NEmitFromObject(*_args, **kwargs))


def NEmitFromObjectOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NEmitFromObjectOptions(*_args, **kwargs))


def NParticleTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NParticleTool(*_args, **kwargs))


def NParticleToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NParticleToolOptions(*_args, **kwargs))


def NURBSSmoothnessFine(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NURBSSmoothnessFine(*_args, **kwargs))


def NURBSSmoothnessFineOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NURBSSmoothnessFineOptions(*_args, **kwargs))


def NURBSSmoothnessHull(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NURBSSmoothnessHull(*_args, **kwargs))


def NURBSSmoothnessHullOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NURBSSmoothnessHullOptions(*_args, **kwargs))


def NURBSSmoothnessMedium(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NURBSSmoothnessMedium(*_args, **kwargs))


def NURBSSmoothnessMediumOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NURBSSmoothnessMediumOptions(*_args, **kwargs))


def NURBSSmoothnessRough(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NURBSSmoothnessRough(*_args, **kwargs))


def NURBSSmoothnessRoughOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NURBSSmoothnessRoughOptions(*_args, **kwargs))


def NURBSTexturePlacementTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NURBSTexturePlacementTool(*_args, **kwargs))


def NURBSTexturePlacementToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NURBSTexturePlacementToolOptions(*_args, **kwargs))


def NURBSToPolygons(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NURBSToPolygons(*_args, **kwargs))


def NURBSToPolygonsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NURBSToPolygonsOptions(*_args, **kwargs))


def NamespaceEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NamespaceEditor(*_args, **kwargs))


def NewScene(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NewScene(*_args, **kwargs))


def NewSceneOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NewSceneOptions(*_args, **kwargs))


def Newton(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Newton(*_args, **kwargs))


def NewtonOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NewtonOptions(*_args, **kwargs))


def NextFrame(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NextFrame(*_args, **kwargs))


def NextGreasePencilFrame(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NextGreasePencilFrame(*_args, **kwargs))


def NextKey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NextKey(*_args, **kwargs))


def NextManipulatorHandle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NextManipulatorHandle(*_args, **kwargs))


def NextSkinPaintMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NextSkinPaintMode(*_args, **kwargs))


def NextViewArrangement(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NextViewArrangement(*_args, **kwargs))


def NodeEditorAddIterationStatePorts(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorAddIterationStatePorts(*_args, **kwargs))


def NodeEditorAddOnNodeCreate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorAddOnNodeCreate(*_args, **kwargs))


def NodeEditorAdditiveGraphingMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorAdditiveGraphingMode(*_args, **kwargs))


def NodeEditorAutoSizeNodes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorAutoSizeNodes(*_args, **kwargs))


def NodeEditorBackToParent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorBackToParent(*_args, **kwargs))


def NodeEditorCloseActiveTab(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorCloseActiveTab(*_args, **kwargs))


def NodeEditorCloseAllTabs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorCloseAllTabs(*_args, **kwargs))


def NodeEditorConnectNodeOnCreation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorConnectNodeOnCreation(*_args, **kwargs))


def NodeEditorConnectOnDrop(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorConnectOnDrop(*_args, **kwargs))


def NodeEditorConnectSelectedNodes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorConnectSelectedNodes(*_args, **kwargs))


def NodeEditorConnectionStyleBezier(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorConnectionStyleBezier(*_args, **kwargs))


def NodeEditorConnectionStyleCorner(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorConnectionStyleCorner(*_args, **kwargs))


def NodeEditorConnectionStyleSShape(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorConnectionStyleSShape(*_args, **kwargs))


def NodeEditorConnectionStyleStraight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorConnectionStyleStraight(*_args, **kwargs))


def NodeEditorCopy(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorCopy(*_args, **kwargs))


def NodeEditorCopyConnectionsOnPaste(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorCopyConnectionsOnPaste(*_args, **kwargs))


def NodeEditorCreateCompound(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorCreateCompound(*_args, **kwargs))


def NodeEditorCreateDoWhileCompound(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorCreateDoWhileCompound(*_args, **kwargs))


def NodeEditorCreateForEachCompound(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorCreateForEachCompound(*_args, **kwargs))


def NodeEditorCreateIterateCompound(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorCreateIterateCompound(*_args, **kwargs))


def NodeEditorCreateNodePopup(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorCreateNodePopup(*_args, **kwargs))


def NodeEditorCreateTab(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorCreateTab(*_args, **kwargs))


def NodeEditorDeleteNodes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorDeleteNodes(*_args, **kwargs))


def NodeEditorDiveIntoCompound(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorDiveIntoCompound(*_args, **kwargs))


def NodeEditorExplodeCompound(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorExplodeCompound(*_args, **kwargs))


def NodeEditorExtendToShapes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorExtendToShapes(*_args, **kwargs))


def NodeEditorGraphAddSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorGraphAddSelected(*_args, **kwargs))


def NodeEditorGraphAllShapes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorGraphAllShapes(*_args, **kwargs))


def NodeEditorGraphAllShapesExceptShading(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorGraphAllShapesExceptShading(*_args, **kwargs))


def NodeEditorGraphClearGraph(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorGraphClearGraph(*_args, **kwargs))


def NodeEditorGraphDownstream(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorGraphDownstream(*_args, **kwargs))


def NodeEditorGraphNoShapes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorGraphNoShapes(*_args, **kwargs))


def NodeEditorGraphRearrange(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorGraphRearrange(*_args, **kwargs))


def NodeEditorGraphRemoveDownstream(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorGraphRemoveDownstream(*_args, **kwargs))


def NodeEditorGraphRemoveSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorGraphRemoveSelected(*_args, **kwargs))


def NodeEditorGraphRemoveUnselected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorGraphRemoveUnselected(*_args, **kwargs))


def NodeEditorGraphRemoveUpstream(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorGraphRemoveUpstream(*_args, **kwargs))


def NodeEditorGraphUpDownstream(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorGraphUpDownstream(*_args, **kwargs))


def NodeEditorGraphUpstream(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorGraphUpstream(*_args, **kwargs))


def NodeEditorGridToggleCrosshairOnEdgeDragging(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorGridToggleCrosshairOnEdgeDragging(*_args, **kwargs))


def NodeEditorGridToggleSnap(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorGridToggleSnap(*_args, **kwargs))


def NodeEditorGridToggleVisibility(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorGridToggleVisibility(*_args, **kwargs))


def NodeEditorHideAttributes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorHideAttributes(*_args, **kwargs))


def NodeEditorHighlightConnectionsOnNodeSelection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorHighlightConnectionsOnNodeSelection(*_args, **kwargs))


def NodeEditorIncreaseTraversalDepth(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorIncreaseTraversalDepth(*_args, **kwargs))


def NodeEditorLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorLayout(*_args, **kwargs))


def NodeEditorPaste(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorPaste(*_args, **kwargs))


def NodeEditorPickWalkDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorPickWalkDown(*_args, **kwargs))


def NodeEditorPickWalkLeft(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorPickWalkLeft(*_args, **kwargs))


def NodeEditorPickWalkRight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorPickWalkRight(*_args, **kwargs))


def NodeEditorPickWalkUp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorPickWalkUp(*_args, **kwargs))


def NodeEditorPinByDefault(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorPinByDefault(*_args, **kwargs))


def NodeEditorPinSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorPinSelected(*_args, **kwargs))


def NodeEditorPublishCompound(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorPublishCompound(*_args, **kwargs))


def NodeEditorRedockTornOffTab(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorRedockTornOffTab(*_args, **kwargs))


def NodeEditorReduceTraversalDepth(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorReduceTraversalDepth(*_args, **kwargs))


def NodeEditorRenameActiveTab(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorRenameActiveTab(*_args, **kwargs))


def NodeEditorRenderSwatches(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorRenderSwatches(*_args, **kwargs))


def NodeEditorRestoreLastClosedTab(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorRestoreLastClosedTab(*_args, **kwargs))


def NodeEditorSelectConnected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorSelectConnected(*_args, **kwargs))


def NodeEditorSelectDownStream(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorSelectDownStream(*_args, **kwargs))


def NodeEditorSelectUpStream(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorSelectUpStream(*_args, **kwargs))


def NodeEditorSetLargeNodeSwatchSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorSetLargeNodeSwatchSize(*_args, **kwargs))


def NodeEditorSetSmallNodeSwatchSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorSetSmallNodeSwatchSize(*_args, **kwargs))


def NodeEditorSetTraversalDepthUnlim(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorSetTraversalDepthUnlim(*_args, **kwargs))


def NodeEditorSetTraversalDepthZero(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorSetTraversalDepthZero(*_args, **kwargs))


def NodeEditorShapeMenuStateAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorShapeMenuStateAll(*_args, **kwargs))


def NodeEditorShapeMenuStateAllExceptShadingGroupMembers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorShapeMenuStateAllExceptShadingGroupMembers(*_args, **kwargs))


def NodeEditorShapeMenuStateNoShapes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorShapeMenuStateNoShapes(*_args, **kwargs))


def NodeEditorShowAllAttrs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorShowAllAttrs(*_args, **kwargs))


def NodeEditorShowAllCustomAttrs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorShowAllCustomAttrs(*_args, **kwargs))


def NodeEditorShowConnectedAttrs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorShowConnectedAttrs(*_args, **kwargs))


def NodeEditorShowCustomAttrs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorShowCustomAttrs(*_args, **kwargs))


def NodeEditorToggleAttrFilter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorToggleAttrFilter(*_args, **kwargs))


def NodeEditorToggleConsistentNodeNameSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorToggleConsistentNodeNameSize(*_args, **kwargs))


def NodeEditorToggleCreateNodePane(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorToggleCreateNodePane(*_args, **kwargs))


def NodeEditorToggleLockUnlock(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorToggleLockUnlock(*_args, **kwargs))


def NodeEditorToggleNodeSelectedPins(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorToggleNodeSelectedPins(*_args, **kwargs))


def NodeEditorToggleNodeSwatchSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorToggleNodeSwatchSize(*_args, **kwargs))


def NodeEditorToggleNodeTitleMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorToggleNodeTitleMode(*_args, **kwargs))


def NodeEditorToggleShowNamespace(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorToggleShowNamespace(*_args, **kwargs))


def NodeEditorToggleSyncedSelection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorToggleSyncedSelection(*_args, **kwargs))


def NodeEditorToggleUseAssetsAndPublishedAttributes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorToggleUseAssetsAndPublishedAttributes(*_args, **kwargs))


def NodeEditorToggleZoomIn(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorToggleZoomIn(*_args, **kwargs))


def NodeEditorToggleZoomOut(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorToggleZoomOut(*_args, **kwargs))


def NodeEditorTransforms(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorTransforms(*_args, **kwargs))


def NodeEditorUnpinSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorUnpinSelected(*_args, **kwargs))


def NodeEditorWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NodeEditorWindow(*_args, **kwargs))


def NonSacredTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NonSacredTool(*_args, **kwargs))


def NonWeightedTangents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NonWeightedTangents(*_args, **kwargs))


def NormalConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NormalConstraint(*_args, **kwargs))


def NormalConstraintOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NormalConstraintOptions(*_args, **kwargs))


def NormalizeUVs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NormalizeUVs(*_args, **kwargs))


def NormalizeUVsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NormalizeUVsOptions(*_args, **kwargs))


def NvExecuteOnSelection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvExecuteOnSelection(*_args, **kwargs))


def NvExecuteOnTimerCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvExecuteOnTimerCmd(*_args, **kwargs))


def NvSimulationRemoveConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSimulationRemoveConstraint(*_args, **kwargs))


def NvSimulationRemoveRB(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSimulationRemoveRB(*_args, **kwargs))


def NvSolverAnimationEnableDisable(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverAnimationEnableDisable(*_args, **kwargs))


def NvSolverCaptureInitialTransform(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverCaptureInitialTransform(*_args, **kwargs))


def NvSolverContactReports(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverContactReports(*_args, **kwargs))


def NvSolverGetClothingSimulatedVertices(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverGetClothingSimulatedVertices(*_args, **kwargs))


def NvSolverGetConstraintsScaling(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverGetConstraintsScaling(*_args, **kwargs))


def NvSolverGetHardwareAccelerationSupported(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverGetHardwareAccelerationSupported(*_args, **kwargs))


def NvSolverGetMeshData(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverGetMeshData(*_args, **kwargs))


def NvSolverGetMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverGetMode(*_args, **kwargs))


def NvSolverGetMultiThreadSupported(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverGetMultiThreadSupported(*_args, **kwargs))


def NvSolverGetPhysXVersion(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverGetPhysXVersion(*_args, **kwargs))


def NvSolverGetRagdollIconSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverGetRagdollIconSize(*_args, **kwargs))


def NvSolverGetSystemFPS(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverGetSystemFPS(*_args, **kwargs))


def NvSolverIsDisplayConstraints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverIsDisplayConstraints(*_args, **kwargs))


def NvSolverIsDisplayRagdollLocators(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverIsDisplayRagdollLocators(*_args, **kwargs))


def NvSolverIsDisplayRigidBody(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverIsDisplayRigidBody(*_args, **kwargs))


def NvSolverLoopSimulation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverLoopSimulation(*_args, **kwargs))


def NvSolverMomentumEnableDisable(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverMomentumEnableDisable(*_args, **kwargs))


def NvSolverMousePosition(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverMousePosition(*_args, **kwargs))


def NvSolverProcessSpanWithProgress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverProcessSpanWithProgress(*_args, **kwargs))


def NvSolverRagdollRedistributeMass(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverRagdollRedistributeMass(*_args, **kwargs))


def NvSolverReadScriptOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverReadScriptOptions(*_args, **kwargs))


def NvSolverRewindSimulation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverRewindSimulation(*_args, **kwargs))


def NvSolverSetConstraintsScaling(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverSetConstraintsScaling(*_args, **kwargs))


def NvSolverSetDisplayConstraints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverSetDisplayConstraints(*_args, **kwargs))


def NvSolverSetDisplayRagdollLocators(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverSetDisplayRagdollLocators(*_args, **kwargs))


def NvSolverSetDisplayRigidBody(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverSetDisplayRigidBody(*_args, **kwargs))


def NvSolverSetRagdollIconSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverSetRagdollIconSize(*_args, **kwargs))


def NvSolverSetUseHardwareAcceleration(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverSetUseHardwareAcceleration(*_args, **kwargs))


def NvSolverSetUseMultiThread(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverSetUseMultiThread(*_args, **kwargs))


def NvSolverSimulateByTimer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverSimulateByTimer(*_args, **kwargs))


def NvSolverStepSimulation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NvSolverStepSimulation(*_args, **kwargs))


def NxBakeAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NxBakeAll(*_args, **kwargs))


def NxBakeSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NxBakeSelected(*_args, **kwargs))


def NxConnectToFields(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NxConnectToFields(*_args, **kwargs))


def NxCreateActiveRigidBody(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NxCreateActiveRigidBody(*_args, **kwargs))


def NxCreateActiveRigidBodyOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NxCreateActiveRigidBodyOptions(*_args, **kwargs))


def NxCreatePassiveRigidBody(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NxCreatePassiveRigidBody(*_args, **kwargs))


def NxCreatePassiveRigidBodyOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NxCreatePassiveRigidBodyOptions(*_args, **kwargs))


def NxCreateStaticRigidBody(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NxCreateStaticRigidBody(*_args, **kwargs))


def NxDisableShapeCollisions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NxDisableShapeCollisions(*_args, **kwargs))


def NxEnableShapeCollisions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NxEnableShapeCollisions(*_args, **kwargs))


def NxRagdollSaveLoadCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NxRagdollSaveLoadCmd(*_args, **kwargs))


def NxRigidConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NxRigidConstraint(*_args, **kwargs))


def NxRigidConstraintOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NxRigidConstraintOptions(*_args, **kwargs))


def NxSelectAllCloths(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NxSelectAllCloths(*_args, **kwargs))


def NxSelectAllRigidBodies(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NxSelectAllRigidBodies(*_args, **kwargs))


def NxSelectAllRigidConstraints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NxSelectAllRigidConstraints(*_args, **kwargs))


def NxSetInitialConditions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NxSetInitialConditions(*_args, **kwargs))


def NxShowAllShapes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NxShowAllShapes(*_args, **kwargs))


def NxShowNonPhysicsShapes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NxShowNonPhysicsShapes(*_args, **kwargs))


def NxShowPhysicsShapes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.NxShowPhysicsShapes(*_args, **kwargs))


def ObjectCentricLightLinkingEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ObjectCentricLightLinkingEditor(*_args, **kwargs))


def OffsetCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OffsetCurve(*_args, **kwargs))


def OffsetCurveOnSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OffsetCurveOnSurface(*_args, **kwargs))


def OffsetCurveOnSurfaceOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OffsetCurveOnSurfaceOptions(*_args, **kwargs))


def OffsetCurveOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OffsetCurveOptions(*_args, **kwargs))


def OffsetEdgeLoopTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OffsetEdgeLoopTool(*_args, **kwargs))


def OffsetEdgeLoopToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OffsetEdgeLoopToolOptions(*_args, **kwargs))


def OffsetSurfaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OffsetSurfaces(*_args, **kwargs))


def OffsetSurfacesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OffsetSurfacesOptions(*_args, **kwargs))


def OneClickAcknowledge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OneClickAcknowledge(*_args, **kwargs))


def OneClickAcknowledgeCallback(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OneClickAcknowledgeCallback(*_args, **kwargs))


def OneClickDisconnect(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OneClickDisconnect(*_args, **kwargs))


def OneClickDispatch(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OneClickDispatch(*_args, **kwargs))


def OneClickExecute(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OneClickExecute(*_args, **kwargs))


def OneClickFetchRemoteCharacter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OneClickFetchRemoteCharacter(*_args, **kwargs))


def OneClickGetContactingAppName(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OneClickGetContactingAppName(*_args, **kwargs))


def OneClickGetState(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OneClickGetState(*_args, **kwargs))


def OneClickMenuExecute(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OneClickMenuExecute(*_args, **kwargs))


def OneClickMotionBuilderSendToCurrentScene(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OneClickMotionBuilderSendToCurrentScene(*_args, **kwargs))


def OneClickSetCallback(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OneClickSetCallback(*_args, **kwargs))


def OneClickSetupMotionBuilderCharacterStream(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OneClickSetupMotionBuilderCharacterStream(*_args, **kwargs))


def OpenCloseCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OpenCloseCurve(*_args, **kwargs))


def OpenCloseCurveOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OpenCloseCurveOptions(*_args, **kwargs))


def OpenCloseSurfaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OpenCloseSurfaces(*_args, **kwargs))


def OpenCloseSurfacesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OpenCloseSurfacesOptions(*_args, **kwargs))


def OpenScene(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OpenScene(*_args, **kwargs))


def OpenSceneOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OpenSceneOptions(*_args, **kwargs))


def OpenSiShelf(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OpenSiShelf(*_args, **kwargs))


def OpenSiShelfOnMouse(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OpenSiShelfOnMouse(*_args, **kwargs))


def OpenVisorForMeshes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OpenVisorForMeshes(*_args, **kwargs))


def OptimizeScene(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OptimizeScene(*_args, **kwargs))


def OptimizeSceneOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OptimizeSceneOptions(*_args, **kwargs))


def OptimzeUVs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OptimzeUVs(*_args, **kwargs))


def OptimzeUVsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OptimzeUVsOptions(*_args, **kwargs))


def OrientConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OrientConstraint(*_args, **kwargs))


def OrientConstraintOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OrientConstraintOptions(*_args, **kwargs))


def OrientJoint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OrientJoint(*_args, **kwargs))


def OrientJointOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OrientJointOptions(*_args, **kwargs))


def OutTangentAuto(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutTangentAuto(*_args, **kwargs))


def OutTangentClamped(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutTangentClamped(*_args, **kwargs))


def OutTangentFixed(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutTangentFixed(*_args, **kwargs))


def OutTangentFlat(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutTangentFlat(*_args, **kwargs))


def OutTangentLinear(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutTangentLinear(*_args, **kwargs))


def OutTangentPlateau(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutTangentPlateau(*_args, **kwargs))


def OutTangentSpline(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutTangentSpline(*_args, **kwargs))


def OutlinerCollapseAllItems(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerCollapseAllItems(*_args, **kwargs))


def OutlinerCollapseAllSelectedItems(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerCollapseAllSelectedItems(*_args, **kwargs))


def OutlinerDoHide(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerDoHide(*_args, **kwargs))


def OutlinerExpandAllItems(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerExpandAllItems(*_args, **kwargs))


def OutlinerExpandAllSelectedItems(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerExpandAllSelectedItems(*_args, **kwargs))


def OutlinerRenameSelectedItem(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerRenameSelectedItem(*_args, **kwargs))


def OutlinerRevealSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerRevealSelected(*_args, **kwargs))


def OutlinerToggleAssignedMaterials(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerToggleAssignedMaterials(*_args, **kwargs))


def OutlinerToggleAttributes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerToggleAttributes(*_args, **kwargs))


def OutlinerToggleAutoExpandLayers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerToggleAutoExpandLayers(*_args, **kwargs))


def OutlinerToggleConnected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerToggleConnected(*_args, **kwargs))


def OutlinerToggleDAGOnly(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerToggleDAGOnly(*_args, **kwargs))


def OutlinerToggleIgnoreHidden(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerToggleIgnoreHidden(*_args, **kwargs))


def OutlinerToggleIgnoreUseColor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerToggleIgnoreUseColor(*_args, **kwargs))


def OutlinerToggleNamespace(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerToggleNamespace(*_args, **kwargs))


def OutlinerToggleOrganizeByClip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerToggleOrganizeByClip(*_args, **kwargs))


def OutlinerToggleOrganizeByLayer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerToggleOrganizeByLayer(*_args, **kwargs))


def OutlinerToggleReferenceMembers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerToggleReferenceMembers(*_args, **kwargs))


def OutlinerToggleReferenceNodes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerToggleReferenceNodes(*_args, **kwargs))


def OutlinerToggleSetMembers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerToggleSetMembers(*_args, **kwargs))


def OutlinerToggleShapes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerToggleShapes(*_args, **kwargs))


def OutlinerToggleShowMuteInformation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerToggleShowMuteInformation(*_args, **kwargs))


def OutlinerToggleTimeEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerToggleTimeEditor(*_args, **kwargs))


def OutlinerUnhide(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerUnhide(*_args, **kwargs))


def OutlinerWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.OutlinerWindow(*_args, **kwargs))


def PFXUVSetLinkingEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PFXUVSetLinkingEditor(*_args, **kwargs))


def PaintCacheTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintCacheTool(*_args, **kwargs))


def PaintCacheToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintCacheToolOptions(*_args, **kwargs))


def PaintEffectPanelActivate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintEffectPanelActivate(*_args, **kwargs))


def PaintEffectPanelDeactivate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintEffectPanelDeactivate(*_args, **kwargs))


def PaintEffectsGlobalSettings(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintEffectsGlobalSettings(*_args, **kwargs))


def PaintEffectsMeshQuality(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintEffectsMeshQuality(*_args, **kwargs))


def PaintEffectsPanel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintEffectsPanel(*_args, **kwargs))


def PaintEffectsToCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintEffectsToCurve(*_args, **kwargs))


def PaintEffectsToCurveOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintEffectsToCurveOptions(*_args, **kwargs))


def PaintEffectsToNurbs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintEffectsToNurbs(*_args, **kwargs))


def PaintEffectsToNurbsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintEffectsToNurbsOptions(*_args, **kwargs))


def PaintEffectsToPoly(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintEffectsToPoly(*_args, **kwargs))


def PaintEffectsToPolyOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintEffectsToPolyOptions(*_args, **kwargs))


def PaintEffectsTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintEffectsTool(*_args, **kwargs))


def PaintEffectsToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintEffectsToolOptions(*_args, **kwargs))


def PaintEffectsWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintEffectsWindow(*_args, **kwargs))


def PaintFluidsTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintFluidsTool(*_args, **kwargs))


def PaintFluidsToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintFluidsToolOptions(*_args, **kwargs))


def PaintGeomCacheTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintGeomCacheTool(*_args, **kwargs))


def PaintGeomCacheToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintGeomCacheToolOptions(*_args, **kwargs))


def PaintGrid(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintGrid(*_args, **kwargs))


def PaintGridOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintGridOptions(*_args, **kwargs))


def PaintOnPaintableObjects(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintOnPaintableObjects(*_args, **kwargs))


def PaintOnViewPlane(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintOnViewPlane(*_args, **kwargs))


def PaintOperationMarkingMenuPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintOperationMarkingMenuPress(*_args, **kwargs))


def PaintOperationMarkingMenuRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintOperationMarkingMenuRelease(*_args, **kwargs))


def PaintRandom(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintRandom(*_args, **kwargs))


def PaintRandomOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintRandomOptions(*_args, **kwargs))


def PaintReduceWeightsTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintReduceWeightsTool(*_args, **kwargs))


def PaintReduceWeightsToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintReduceWeightsToolOptions(*_args, **kwargs))


def PaintSetMembershipTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintSetMembershipTool(*_args, **kwargs))


def PaintSetMembershipToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintSetMembershipToolOptions(*_args, **kwargs))


def PaintVertexColorTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintVertexColorTool(*_args, **kwargs))


def PaintVertexColorToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PaintVertexColorToolOptions(*_args, **kwargs))


def PanZoomTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PanZoomTool(*_args, **kwargs))


def PanePop(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PanePop(*_args, **kwargs))


def PanelPreferencesWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PanelPreferencesWindow(*_args, **kwargs))


def ParameterTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ParameterTool(*_args, **kwargs))


def Parent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Parent(*_args, **kwargs))


def ParentBaseWire(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ParentBaseWire(*_args, **kwargs))


def ParentBaseWireOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ParentBaseWireOptions(*_args, **kwargs))


def ParentConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ParentConstraint(*_args, **kwargs))


def ParentConstraintOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ParentConstraintOptions(*_args, **kwargs))


def ParentOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ParentOptions(*_args, **kwargs))


def PartialCreaseSubdivSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PartialCreaseSubdivSurface(*_args, **kwargs))


def ParticleCollisionEvents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ParticleCollisionEvents(*_args, **kwargs))


def ParticleFill(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ParticleFill(*_args, **kwargs))


def ParticleFillOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ParticleFillOptions(*_args, **kwargs))


def ParticleInstancer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ParticleInstancer(*_args, **kwargs))


def ParticleInstancerOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ParticleInstancerOptions(*_args, **kwargs))


def ParticleTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ParticleTool(*_args, **kwargs))


def ParticleToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ParticleToolOptions(*_args, **kwargs))


def PartitionEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PartitionEditor(*_args, **kwargs))


def PasteKeys(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PasteKeys(*_args, **kwargs))


def PasteKeysOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PasteKeysOptions(*_args, **kwargs))


def PasteSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PasteSelected(*_args, **kwargs))


def PasteUVs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PasteUVs(*_args, **kwargs))


def PasteVertexSkinWeights(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PasteVertexSkinWeights(*_args, **kwargs))


def PencilCurveTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PencilCurveTool(*_args, **kwargs))


def PencilCurveToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PencilCurveToolOptions(*_args, **kwargs))


def PerPointEmissionRates(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PerPointEmissionRates(*_args, **kwargs))


def PerformanceSettingsWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PerformanceSettingsWindow(*_args, **kwargs))


def PerspGraphHypergraphLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PerspGraphHypergraphLayout(*_args, **kwargs))


def PerspGraphLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PerspGraphLayout(*_args, **kwargs))


def PerspGraphOutlinerLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PerspGraphOutlinerLayout(*_args, **kwargs))


def PerspRelationshipEditorLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PerspRelationshipEditorLayout(*_args, **kwargs))


def PerspTextureLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PerspTextureLayout(*_args, **kwargs))


def PickColorActivate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PickColorActivate(*_args, **kwargs))


def PickColorDeactivate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PickColorDeactivate(*_args, **kwargs))


def PickWalkDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PickWalkDown(*_args, **kwargs))


def PickWalkDownSelect(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PickWalkDownSelect(*_args, **kwargs))


def PickWalkIn(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PickWalkIn(*_args, **kwargs))


def PickWalkLeft(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PickWalkLeft(*_args, **kwargs))


def PickWalkLeftSelect(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PickWalkLeftSelect(*_args, **kwargs))


def PickWalkOut(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PickWalkOut(*_args, **kwargs))


def PickWalkRight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PickWalkRight(*_args, **kwargs))


def PickWalkRightSelect(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PickWalkRightSelect(*_args, **kwargs))


def PickWalkStopAtTransform(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PickWalkStopAtTransform(*_args, **kwargs))


def PickWalkUp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PickWalkUp(*_args, **kwargs))


def PickWalkUpSelect(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PickWalkUpSelect(*_args, **kwargs))


def PickWalkUseController(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PickWalkUseController(*_args, **kwargs))


def PinSelection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PinSelection(*_args, **kwargs))


def PinSelectionOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PinSelectionOptions(*_args, **kwargs))


def PixelMoveDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PixelMoveDown(*_args, **kwargs))


def PixelMoveLeft(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PixelMoveLeft(*_args, **kwargs))


def PixelMoveRight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PixelMoveRight(*_args, **kwargs))


def PixelMoveUp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PixelMoveUp(*_args, **kwargs))


def Planar(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Planar(*_args, **kwargs))


def PlanarOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PlanarOptions(*_args, **kwargs))


def PlaybackBackward(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PlaybackBackward(*_args, **kwargs))


def PlaybackForward(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PlaybackForward(*_args, **kwargs))


def PlaybackStop(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PlaybackStop(*_args, **kwargs))


def PlaybackToggle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PlaybackToggle(*_args, **kwargs))


def PlayblastOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PlayblastOptions(*_args, **kwargs))


def PlayblastWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PlayblastWindow(*_args, **kwargs))


def PluginManager(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PluginManager(*_args, **kwargs))


def PointConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PointConstraint(*_args, **kwargs))


def PointConstraintOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PointConstraintOptions(*_args, **kwargs))


def PointOnCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PointOnCurve(*_args, **kwargs))


def PointOnCurveOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PointOnCurveOptions(*_args, **kwargs))


def PointOnPolyConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PointOnPolyConstraint(*_args, **kwargs))


def PointOnPolyConstraintOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PointOnPolyConstraintOptions(*_args, **kwargs))


def PokePolygon(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PokePolygon(*_args, **kwargs))


def PokePolygonOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PokePolygonOptions(*_args, **kwargs))


def PoleVectorConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PoleVectorConstraint(*_args, **kwargs))


def PoleVectorConstraintOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PoleVectorConstraintOptions(*_args, **kwargs))


def PolyAssignSubdivHole(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyAssignSubdivHole(*_args, **kwargs))


def PolyAssignSubdivHoleOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyAssignSubdivHoleOptions(*_args, **kwargs))


def PolyBrushMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyBrushMarkingMenu(*_args, **kwargs))


def PolyBrushMarkingMenuPopDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyBrushMarkingMenuPopDown(*_args, **kwargs))


def PolyCircularize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyCircularize(*_args, **kwargs))


def PolyCircularizeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyCircularizeOptions(*_args, **kwargs))


def PolyConvertToLoopAndDelete(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyConvertToLoopAndDelete(*_args, **kwargs))


def PolyConvertToLoopAndDuplicate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyConvertToLoopAndDuplicate(*_args, **kwargs))


def PolyConvertToRingAndCollapse(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyConvertToRingAndCollapse(*_args, **kwargs))


def PolyConvertToRingAndSplit(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyConvertToRingAndSplit(*_args, **kwargs))


def PolyCreaseTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyCreaseTool(*_args, **kwargs))


def PolyCreaseToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyCreaseToolOptions(*_args, **kwargs))


def PolyDisplayReset(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyDisplayReset(*_args, **kwargs))


def PolyEditEdgeFlow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyEditEdgeFlow(*_args, **kwargs))


def PolyEditEdgeFlowOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyEditEdgeFlowOptions(*_args, **kwargs))


def PolyExtrude(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyExtrude(*_args, **kwargs))


def PolyExtrudeEdges(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyExtrudeEdges(*_args, **kwargs))


def PolyExtrudeEdgesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyExtrudeEdgesOptions(*_args, **kwargs))


def PolyExtrudeFaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyExtrudeFaces(*_args, **kwargs))


def PolyExtrudeFacesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyExtrudeFacesOptions(*_args, **kwargs))


def PolyExtrudeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyExtrudeOptions(*_args, **kwargs))


def PolyExtrudeVertices(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyExtrudeVertices(*_args, **kwargs))


def PolyExtrudeVerticesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyExtrudeVerticesOptions(*_args, **kwargs))


def PolyMerge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyMerge(*_args, **kwargs))


def PolyMergeEdges(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyMergeEdges(*_args, **kwargs))


def PolyMergeEdgesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyMergeEdgesOptions(*_args, **kwargs))


def PolyMergeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyMergeOptions(*_args, **kwargs))


def PolyMergeVertices(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyMergeVertices(*_args, **kwargs))


def PolyMergeVerticesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyMergeVerticesOptions(*_args, **kwargs))


def PolyRemoveAllCrease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyRemoveAllCrease(*_args, **kwargs))


def PolyRemoveCrease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolyRemoveCrease(*_args, **kwargs))


def PolySelectTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolySelectTool(*_args, **kwargs))


def PolySelectToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolySelectToolOptions(*_args, **kwargs))


def PolySpinEdgeBackward(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolySpinEdgeBackward(*_args, **kwargs))


def PolySpinEdgeForward(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolySpinEdgeForward(*_args, **kwargs))


def PolygonApplyColor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonApplyColor(*_args, **kwargs))


def PolygonApplyColorOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonApplyColorOptions(*_args, **kwargs))


def PolygonBooleanDifference(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonBooleanDifference(*_args, **kwargs))


def PolygonBooleanDifferenceOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonBooleanDifferenceOptions(*_args, **kwargs))


def PolygonBooleanIntersection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonBooleanIntersection(*_args, **kwargs))


def PolygonBooleanIntersectionOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonBooleanIntersectionOptions(*_args, **kwargs))


def PolygonBooleanUnion(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonBooleanUnion(*_args, **kwargs))


def PolygonBooleanUnionOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonBooleanUnionOptions(*_args, **kwargs))


def PolygonClearClipboard(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonClearClipboard(*_args, **kwargs))


def PolygonClearClipboardOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonClearClipboardOptions(*_args, **kwargs))


def PolygonCollapse(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonCollapse(*_args, **kwargs))


def PolygonCollapseEdges(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonCollapseEdges(*_args, **kwargs))


def PolygonCollapseFaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonCollapseFaces(*_args, **kwargs))


def PolygonCopy(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonCopy(*_args, **kwargs))


def PolygonCopyOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonCopyOptions(*_args, **kwargs))


def PolygonHardenEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonHardenEdge(*_args, **kwargs))


def PolygonNormalEditTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonNormalEditTool(*_args, **kwargs))


def PolygonPaste(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonPaste(*_args, **kwargs))


def PolygonPasteOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonPasteOptions(*_args, **kwargs))


def PolygonSelectionConstraints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonSelectionConstraints(*_args, **kwargs))


def PolygonSoftenEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonSoftenEdge(*_args, **kwargs))


def PolygonSoftenHarden(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonSoftenHarden(*_args, **kwargs))


def PolygonSoftenHardenOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PolygonSoftenHardenOptions(*_args, **kwargs))


def PoseEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PoseEditor(*_args, **kwargs))


def PoseInterpolatorNewGroup(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PoseInterpolatorNewGroup(*_args, **kwargs))


def PositionAlongCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PositionAlongCurve(*_args, **kwargs))


def PostInfinityConstant(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PostInfinityConstant(*_args, **kwargs))


def PostInfinityCycle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PostInfinityCycle(*_args, **kwargs))


def PostInfinityCycleOffset(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PostInfinityCycleOffset(*_args, **kwargs))


def PostInfinityLinear(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PostInfinityLinear(*_args, **kwargs))


def PostInfinityOscillate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PostInfinityOscillate(*_args, **kwargs))


def PreInfinityConstant(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PreInfinityConstant(*_args, **kwargs))


def PreInfinityCycle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PreInfinityCycle(*_args, **kwargs))


def PreInfinityCycleOffset(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PreInfinityCycleOffset(*_args, **kwargs))


def PreInfinityLinear(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PreInfinityLinear(*_args, **kwargs))


def PreInfinityOscillate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PreInfinityOscillate(*_args, **kwargs))


def PreferencesWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PreferencesWindow(*_args, **kwargs))


def PrefixHierarchyNames(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PrefixHierarchyNames(*_args, **kwargs))


def PrelightPolygon(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PrelightPolygon(*_args, **kwargs))


def PrelightPolygonOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PrelightPolygonOptions(*_args, **kwargs))


def PreloadReferenceEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PreloadReferenceEditor(*_args, **kwargs))


def PresetBlendingWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PresetBlendingWindow(*_args, **kwargs))


def PrevSkinPaintMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PrevSkinPaintMode(*_args, **kwargs))


def PreviousFrame(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PreviousFrame(*_args, **kwargs))


def PreviousGreasePencilFrame(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PreviousGreasePencilFrame(*_args, **kwargs))


def PreviousKey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PreviousKey(*_args, **kwargs))


def PreviousManipulatorHandle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PreviousManipulatorHandle(*_args, **kwargs))


def PreviousViewArrangement(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PreviousViewArrangement(*_args, **kwargs))


def ProductInformation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ProductInformation(*_args, **kwargs))


def ProfilerTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ProfilerTool(*_args, **kwargs))


def ProfilerToolCategoryView(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ProfilerToolCategoryView(*_args, **kwargs))


def ProfilerToolCpuView(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ProfilerToolCpuView(*_args, **kwargs))


def ProfilerToolHideSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ProfilerToolHideSelected(*_args, **kwargs))


def ProfilerToolHideSelectedRepetition(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ProfilerToolHideSelectedRepetition(*_args, **kwargs))


def ProfilerToolReset(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ProfilerToolReset(*_args, **kwargs))


def ProfilerToolShowAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ProfilerToolShowAll(*_args, **kwargs))


def ProfilerToolShowSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ProfilerToolShowSelected(*_args, **kwargs))


def ProfilerToolShowSelectedRepetition(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ProfilerToolShowSelectedRepetition(*_args, **kwargs))


def ProfilerToolThreadView(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ProfilerToolThreadView(*_args, **kwargs))


def ProfilerToolToggleRecording(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ProfilerToolToggleRecording(*_args, **kwargs))


def ProjectCurveOnMesh(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ProjectCurveOnMesh(*_args, **kwargs))


def ProjectCurveOnMeshOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ProjectCurveOnMeshOptions(*_args, **kwargs))


def ProjectCurveOnSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ProjectCurveOnSurface(*_args, **kwargs))


def ProjectCurveOnSurfaceOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ProjectCurveOnSurfaceOptions(*_args, **kwargs))


def ProjectTangent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ProjectTangent(*_args, **kwargs))


def ProjectTangentOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ProjectTangentOptions(*_args, **kwargs))


def ProjectWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ProjectWindow(*_args, **kwargs))


def ProportionalModificationTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ProportionalModificationTool(*_args, **kwargs))


def PruneCluster(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PruneCluster(*_args, **kwargs))


def PruneLattice(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PruneLattice(*_args, **kwargs))


def PruneSculpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PruneSculpt(*_args, **kwargs))


def PruneSmallWeights(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PruneSmallWeights(*_args, **kwargs))


def PruneSmallWeightsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PruneSmallWeightsOptions(*_args, **kwargs))


def PruneWire(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PruneWire(*_args, **kwargs))


def PublishAttributes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PublishAttributes(*_args, **kwargs))


def PublishAttributesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PublishAttributesOptions(*_args, **kwargs))


def PublishChildAnchor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PublishChildAnchor(*_args, **kwargs))


def PublishChildAnchorOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PublishChildAnchorOptions(*_args, **kwargs))


def PublishConnections(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PublishConnections(*_args, **kwargs))


def PublishConnectionsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PublishConnectionsOptions(*_args, **kwargs))


def PublishNode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PublishNode(*_args, **kwargs))


def PublishParentAnchor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PublishParentAnchor(*_args, **kwargs))


def PublishParentAnchorOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PublishParentAnchorOptions(*_args, **kwargs))


def PublishRootTransform(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PublishRootTransform(*_args, **kwargs))


def PublishRootTransformOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.PublishRootTransformOptions(*_args, **kwargs))


def Quadrangulate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Quadrangulate(*_args, **kwargs))


def QuadrangulateOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.QuadrangulateOptions(*_args, **kwargs))


def QualityDisplayMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.QualityDisplayMarkingMenu(*_args, **kwargs))


def QualityDisplayMarkingMenuPopDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.QualityDisplayMarkingMenuPopDown(*_args, **kwargs))


def QuickRigEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.QuickRigEditor(*_args, **kwargs))


def Quit(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Quit(*_args, **kwargs))


def Radial(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Radial(*_args, **kwargs))


def RadialOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RadialOptions(*_args, **kwargs))


def RaiseApplicationWindows(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RaiseApplicationWindows(*_args, **kwargs))


def RaiseMainWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RaiseMainWindow(*_args, **kwargs))


def RandomizeFollicles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RandomizeFollicles(*_args, **kwargs))


def RandomizeFolliclesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RandomizeFolliclesOptions(*_args, **kwargs))


def RandomizeShells(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RandomizeShells(*_args, **kwargs))


def RandomizeShellsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RandomizeShellsOptions(*_args, **kwargs))


def ReassignBoneLatticeJoint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ReassignBoneLatticeJoint(*_args, **kwargs))


def ReattachSkeleton(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ReattachSkeleton(*_args, **kwargs))


def ReattachSkeletonJoints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ReattachSkeletonJoints(*_args, **kwargs))


def RebuildCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RebuildCurve(*_args, **kwargs))


def RebuildCurveOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RebuildCurveOptions(*_args, **kwargs))


def RebuildSurfaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RebuildSurfaces(*_args, **kwargs))


def RebuildSurfacesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RebuildSurfacesOptions(*_args, **kwargs))


def RecentCommandsWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RecentCommandsWindow(*_args, **kwargs))


def Redo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Redo(*_args, **kwargs))


def RedoPreviousIPRRender(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RedoPreviousIPRRender(*_args, **kwargs))


def RedoPreviousRender(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RedoPreviousRender(*_args, **kwargs))


def RedoViewChange(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RedoViewChange(*_args, **kwargs))


def ReducePolygon(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ReducePolygon(*_args, **kwargs))


def ReducePolygonOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ReducePolygonOptions(*_args, **kwargs))


def ReferenceEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ReferenceEditor(*_args, **kwargs))


def RefineSelectedComponents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RefineSelectedComponents(*_args, **kwargs))


def RegionKeysTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RegionKeysTool(*_args, **kwargs))


def RelaxInitialState(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RelaxInitialState(*_args, **kwargs))


def RelaxInitialStateOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RelaxInitialStateOptions(*_args, **kwargs))


def RelaxUVShell(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RelaxUVShell(*_args, **kwargs))


def RelaxUVShellOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RelaxUVShellOptions(*_args, **kwargs))


def RemoveBindingSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveBindingSet(*_args, **kwargs))


def RemoveBlendShape(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveBlendShape(*_args, **kwargs))


def RemoveBlendShapeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveBlendShapeOptions(*_args, **kwargs))


def RemoveBrushSharing(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveBrushSharing(*_args, **kwargs))


def RemoveConstraintTarget(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveConstraintTarget(*_args, **kwargs))


def RemoveConstraintTargetOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveConstraintTargetOptions(*_args, **kwargs))


def RemoveFromCharacterSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveFromCharacterSet(*_args, **kwargs))


def RemoveFromContainer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveFromContainer(*_args, **kwargs))


def RemoveFromContainerOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveFromContainerOptions(*_args, **kwargs))


def RemoveInbetween(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveInbetween(*_args, **kwargs))


def RemoveInfluence(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveInfluence(*_args, **kwargs))


def RemoveJoint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveJoint(*_args, **kwargs))


def RemoveLatticeTweaks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveLatticeTweaks(*_args, **kwargs))


def RemoveMaterialSoloing(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveMaterialSoloing(*_args, **kwargs))


def RemoveShrinkWrapInnerObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveShrinkWrapInnerObject(*_args, **kwargs))


def RemoveShrinkWrapSurfaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveShrinkWrapSurfaces(*_args, **kwargs))


def RemoveShrinkWrapTarget(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveShrinkWrapTarget(*_args, **kwargs))


def RemoveSubdivProxyMirror(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveSubdivProxyMirror(*_args, **kwargs))


def RemoveSubdivProxyMirrorOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveSubdivProxyMirrorOptions(*_args, **kwargs))


def RemoveWire(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveWire(*_args, **kwargs))


def RemoveWireOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveWireOptions(*_args, **kwargs))


def RemoveWrapInfluence(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RemoveWrapInfluence(*_args, **kwargs))


def RenameAttribute(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RenameAttribute(*_args, **kwargs))


def RenameCurrentColorSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RenameCurrentColorSet(*_args, **kwargs))


def RenameCurrentUVSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RenameCurrentUVSet(*_args, **kwargs))


def RenderDiagnostics(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RenderDiagnostics(*_args, **kwargs))


def RenderFlagsWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RenderFlagsWindow(*_args, **kwargs))


def RenderGlobalsWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RenderGlobalsWindow(*_args, **kwargs))


def RenderIntoNewWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RenderIntoNewWindow(*_args, **kwargs))


def RenderLayerEditorWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RenderLayerEditorWindow(*_args, **kwargs))


def RenderLayerRelationshipEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RenderLayerRelationshipEditor(*_args, **kwargs))


def RenderOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RenderOptions(*_args, **kwargs))


def RenderPassSetEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RenderPassSetEditor(*_args, **kwargs))


def RenderSequence(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RenderSequence(*_args, **kwargs))


def RenderSetupWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RenderSetupWindow(*_args, **kwargs))


def RenderTextureRange(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RenderTextureRange(*_args, **kwargs))


def RenderTextureRangeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RenderTextureRangeOptions(*_args, **kwargs))


def RenderViewNextImage(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RenderViewNextImage(*_args, **kwargs))


def RenderViewPrevImage(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RenderViewPrevImage(*_args, **kwargs))


def RenderViewWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RenderViewWindow(*_args, **kwargs))


def ReorderVertex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ReorderVertex(*_args, **kwargs))


def RepeatLast(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RepeatLast(*_args, **kwargs))


def RepeatLastActionAtMousePosition(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RepeatLastActionAtMousePosition(*_args, **kwargs))


def ReplaceObjects(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ReplaceObjects(*_args, **kwargs))


def ReplaceObjectsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ReplaceObjectsOptions(*_args, **kwargs))


def RerootSkeleton(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RerootSkeleton(*_args, **kwargs))


def ResampleCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ResampleCurve(*_args, **kwargs))


def ResampleCurveOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ResampleCurveOptions(*_args, **kwargs))


def ResetLattice(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ResetLattice(*_args, **kwargs))


def ResetProperty2State(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ResetProperty2State(*_args, **kwargs))


def ResetReflectionOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ResetReflectionOptions(*_args, **kwargs))


def ResetSoftSelectOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ResetSoftSelectOptions(*_args, **kwargs))


def ResetTemplateBrush(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ResetTemplateBrush(*_args, **kwargs))


def ResetTransformations(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ResetTransformations(*_args, **kwargs))


def ResetTransformationsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ResetTransformationsOptions(*_args, **kwargs))


def ResetWeightsToDefault(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ResetWeightsToDefault(*_args, **kwargs))


def ResetWire(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ResetWire(*_args, **kwargs))


def ResetWireOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ResetWireOptions(*_args, **kwargs))


def ResolveInterpenetration(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ResolveInterpenetration(*_args, **kwargs))


def ResolveInterpenetrationOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ResolveInterpenetrationOptions(*_args, **kwargs))


def RestoreUIElements(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RestoreUIElements(*_args, **kwargs))


def RetimeKeysTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RetimeKeysTool(*_args, **kwargs))


def RetimeKeysToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RetimeKeysToolOptions(*_args, **kwargs))


def ReverseCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ReverseCurve(*_args, **kwargs))


def ReverseCurveOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ReverseCurveOptions(*_args, **kwargs))


def ReversePolygonNormals(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ReversePolygonNormals(*_args, **kwargs))


def ReversePolygonNormalsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ReversePolygonNormalsOptions(*_args, **kwargs))


def ReverseSurfaceDirection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ReverseSurfaceDirection(*_args, **kwargs))


def ReverseSurfaceDirectionOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ReverseSurfaceDirectionOptions(*_args, **kwargs))


def Revolve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Revolve(*_args, **kwargs))


def RevolveOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RevolveOptions(*_args, **kwargs))


def RigidBindSkin(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RigidBindSkin(*_args, **kwargs))


def RigidBindSkinOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RigidBindSkinOptions(*_args, **kwargs))


def RigidBodySolver(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RigidBodySolver(*_args, **kwargs))


def RotateTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RotateTool(*_args, **kwargs))


def RotateToolMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RotateToolMarkingMenu(*_args, **kwargs))


def RotateToolMarkingMenuPopDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RotateToolMarkingMenuPopDown(*_args, **kwargs))


def RotateToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RotateToolOptions(*_args, **kwargs))


def RotateToolWithSnapMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RotateToolWithSnapMarkingMenu(*_args, **kwargs))


def RotateToolWithSnapMarkingMenuPopDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RotateToolWithSnapMarkingMenuPopDown(*_args, **kwargs))


def RotateUVTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RotateUVTool(*_args, **kwargs))


def RotateUVs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RotateUVs(*_args, **kwargs))


def RotateUVsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RotateUVsOptions(*_args, **kwargs))


def RoundTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RoundTool(*_args, **kwargs))


def RoundToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.RoundToolOptions(*_args, **kwargs))


def STRSTweakModeOff(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.STRSTweakModeOff(*_args, **kwargs))


def STRSTweakModeOn(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.STRSTweakModeOn(*_args, **kwargs))


def STRSTweakModeToggle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.STRSTweakModeToggle(*_args, **kwargs))


def SaveBrushPreset(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SaveBrushPreset(*_args, **kwargs))


def SaveClothingTemplateCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SaveClothingTemplateCmd(*_args, **kwargs))


def SaveCurrentLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SaveCurrentLayout(*_args, **kwargs))


def SaveCurrentWorkspace(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SaveCurrentWorkspace(*_args, **kwargs))


def SaveFluidStateAs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SaveFluidStateAs(*_args, **kwargs))


def SaveHIKCharacterDefinition(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SaveHIKCharacterDefinition(*_args, **kwargs))


def SavePreferences(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SavePreferences(*_args, **kwargs))


def SaveScene(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SaveScene(*_args, **kwargs))


def SaveSceneAs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SaveSceneAs(*_args, **kwargs))


def SaveSceneAsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SaveSceneAsOptions(*_args, **kwargs))


def SaveSceneOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SaveSceneOptions(*_args, **kwargs))


def ScaleConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ScaleConstraint(*_args, **kwargs))


def ScaleConstraintOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ScaleConstraintOptions(*_args, **kwargs))


def ScaleCurvature(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ScaleCurvature(*_args, **kwargs))


def ScaleCurvatureOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ScaleCurvatureOptions(*_args, **kwargs))


def ScaleKeys(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ScaleKeys(*_args, **kwargs))


def ScaleKeysOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ScaleKeysOptions(*_args, **kwargs))


def ScaleTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ScaleTool(*_args, **kwargs))


def ScaleToolMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ScaleToolMarkingMenu(*_args, **kwargs))


def ScaleToolMarkingMenuPopDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ScaleToolMarkingMenuPopDown(*_args, **kwargs))


def ScaleToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ScaleToolOptions(*_args, **kwargs))


def ScaleToolWithSnapMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ScaleToolWithSnapMarkingMenu(*_args, **kwargs))


def ScaleToolWithSnapMarkingMenuPopDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ScaleToolWithSnapMarkingMenuPopDown(*_args, **kwargs))


def ScaleUVTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ScaleUVTool(*_args, **kwargs))


def ScriptEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ScriptEditor(*_args, **kwargs))


def ScriptPaintTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ScriptPaintTool(*_args, **kwargs))


def ScriptPaintToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ScriptPaintToolOptions(*_args, **kwargs))


def SculptGeometryTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SculptGeometryTool(*_args, **kwargs))


def SculptGeometryToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SculptGeometryToolOptions(*_args, **kwargs))


def SculptMeshActivateBrushSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SculptMeshActivateBrushSize(*_args, **kwargs))


def SculptMeshActivateBrushStrength(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SculptMeshActivateBrushStrength(*_args, **kwargs))


def SculptMeshDeactivateBrushSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SculptMeshDeactivateBrushSize(*_args, **kwargs))


def SculptMeshDeactivateBrushStrength(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SculptMeshDeactivateBrushStrength(*_args, **kwargs))


def SculptMeshFrame(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SculptMeshFrame(*_args, **kwargs))


def SculptMeshInvertFreeze(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SculptMeshInvertFreeze(*_args, **kwargs))


def SculptMeshUnfreezeAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SculptMeshUnfreezeAll(*_args, **kwargs))


def SculptPolygonsTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SculptPolygonsTool(*_args, **kwargs))


def SculptPolygonsToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SculptPolygonsToolOptions(*_args, **kwargs))


def SculptReferenceVectorMarkingMenuPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SculptReferenceVectorMarkingMenuPress(*_args, **kwargs))


def SculptReferenceVectorMarkingMenuRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SculptReferenceVectorMarkingMenuRelease(*_args, **kwargs))


def SculptSubdivsTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SculptSubdivsTool(*_args, **kwargs))


def SculptSubdivsToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SculptSubdivsToolOptions(*_args, **kwargs))


def SculptSurfacesTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SculptSurfacesTool(*_args, **kwargs))


def SculptSurfacesToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SculptSurfacesToolOptions(*_args, **kwargs))


def SelectAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAll(*_args, **kwargs))


def SelectAllAssets(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllAssets(*_args, **kwargs))


def SelectAllBrushes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllBrushes(*_args, **kwargs))


def SelectAllCameras(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllCameras(*_args, **kwargs))


def SelectAllClusters(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllClusters(*_args, **kwargs))


def SelectAllDynamicConstraints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllDynamicConstraints(*_args, **kwargs))


def SelectAllFluids(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllFluids(*_args, **kwargs))


def SelectAllFollicles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllFollicles(*_args, **kwargs))


def SelectAllFurs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllFurs(*_args, **kwargs))


def SelectAllGeometry(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllGeometry(*_args, **kwargs))


def SelectAllHairSystem(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllHairSystem(*_args, **kwargs))


def SelectAllIKHandles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllIKHandles(*_args, **kwargs))


def SelectAllImagePlanes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllImagePlanes(*_args, **kwargs))


def SelectAllInput(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllInput(*_args, **kwargs))


def SelectAllJoints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllJoints(*_args, **kwargs))


def SelectAllLattices(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllLattices(*_args, **kwargs))


def SelectAllLights(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllLights(*_args, **kwargs))


def SelectAllMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllMarkingMenu(*_args, **kwargs))


def SelectAllMarkingMenuPopDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllMarkingMenuPopDown(*_args, **kwargs))


def SelectAllNCloths(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllNCloths(*_args, **kwargs))


def SelectAllNParticles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllNParticles(*_args, **kwargs))


def SelectAllNRigids(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllNRigids(*_args, **kwargs))


def SelectAllNURBSCurves(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllNURBSCurves(*_args, **kwargs))


def SelectAllNURBSSurfaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllNURBSSurfaces(*_args, **kwargs))


def SelectAllOutput(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllOutput(*_args, **kwargs))


def SelectAllParticles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllParticles(*_args, **kwargs))


def SelectAllPolygonGeometry(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllPolygonGeometry(*_args, **kwargs))


def SelectAllRigidBodies(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllRigidBodies(*_args, **kwargs))


def SelectAllRigidConstraints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllRigidConstraints(*_args, **kwargs))


def SelectAllSculptObjects(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllSculptObjects(*_args, **kwargs))


def SelectAllStrokes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllStrokes(*_args, **kwargs))


def SelectAllSubdivGeometry(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllSubdivGeometry(*_args, **kwargs))


def SelectAllTransforms(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllTransforms(*_args, **kwargs))


def SelectAllWires(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectAllWires(*_args, **kwargs))


def SelectBorderEdgeTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectBorderEdgeTool(*_args, **kwargs))


def SelectBrushNames(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectBrushNames(*_args, **kwargs))


def SelectCVsMask(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectCVsMask(*_args, **kwargs))


def SelectComponentToolMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectComponentToolMarkingMenu(*_args, **kwargs))


def SelectComponentToolMarkingMenuPopDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectComponentToolMarkingMenuPopDown(*_args, **kwargs))


def SelectContainerContents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectContainerContents(*_args, **kwargs))


def SelectContiguousEdges(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectContiguousEdges(*_args, **kwargs))


def SelectContiguousEdgesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectContiguousEdgesOptions(*_args, **kwargs))


def SelectCurveCVsAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectCurveCVsAll(*_args, **kwargs))


def SelectCurveCVsFirst(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectCurveCVsFirst(*_args, **kwargs))


def SelectCurveCVsLast(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectCurveCVsLast(*_args, **kwargs))


def SelectEdgeLoop(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectEdgeLoop(*_args, **kwargs))


def SelectEdgeLoopSp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectEdgeLoopSp(*_args, **kwargs))


def SelectEdgeMask(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectEdgeMask(*_args, **kwargs))


def SelectEdgeRing(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectEdgeRing(*_args, **kwargs))


def SelectEdgeRingSp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectEdgeRingSp(*_args, **kwargs))


def SelectFacePath(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectFacePath(*_args, **kwargs))


def SelectFacetMask(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectFacetMask(*_args, **kwargs))


def SelectHierarchy(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectHierarchy(*_args, **kwargs))


def SelectHullsMask(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectHullsMask(*_args, **kwargs))


def SelectIsolate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectIsolate(*_args, **kwargs))


def SelectLightsIlluminatingObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectLightsIlluminatingObject(*_args, **kwargs))


def SelectLightsShadowingObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectLightsShadowingObject(*_args, **kwargs))


def SelectLinesMask(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectLinesMask(*_args, **kwargs))


def SelectMaskToolMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectMaskToolMarkingMenu(*_args, **kwargs))


def SelectMaskToolMarkingMenuPopDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectMaskToolMarkingMenuPopDown(*_args, **kwargs))


def SelectMeshUVShell(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectMeshUVShell(*_args, **kwargs))


def SelectMultiComponentMask(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectMultiComponentMask(*_args, **kwargs))


def SelectNextIntermediatObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectNextIntermediatObject(*_args, **kwargs))


def SelectNone(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectNone(*_args, **kwargs))


def SelectObjectsIlluminatedByLight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectObjectsIlluminatedByLight(*_args, **kwargs))


def SelectObjectsShadowedByLight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectObjectsShadowedByLight(*_args, **kwargs))


def SelectPointsMask(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectPointsMask(*_args, **kwargs))


def SelectPolygonSelectionBoundary(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectPolygonSelectionBoundary(*_args, **kwargs))


def SelectPolygonToolMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectPolygonToolMarkingMenu(*_args, **kwargs))


def SelectPolygonToolMarkingMenuPopDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectPolygonToolMarkingMenuPopDown(*_args, **kwargs))


def SelectPreviousObjects3dsMax(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectPreviousObjects3dsMax(*_args, **kwargs))


def SelectPreviousObjectsMotionBuilder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectPreviousObjectsMotionBuilder(*_args, **kwargs))


def SelectPreviousObjectsMudbox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectPreviousObjectsMudbox(*_args, **kwargs))


def SelectSharedColorInstances(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectSharedColorInstances(*_args, **kwargs))


def SelectSharedUVInstances(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectSharedUVInstances(*_args, **kwargs))


def SelectShortestEdgePathTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectShortestEdgePathTool(*_args, **kwargs))


def SelectSimilar(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectSimilar(*_args, **kwargs))


def SelectSimilarOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectSimilarOptions(*_args, **kwargs))


def SelectSurfacePointsMask(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectSurfacePointsMask(*_args, **kwargs))


def SelectTextureReferenceObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectTextureReferenceObject(*_args, **kwargs))


def SelectTimeWarp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectTimeWarp(*_args, **kwargs))


def SelectToggleMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectToggleMode(*_args, **kwargs))


def SelectTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectTool(*_args, **kwargs))


def SelectToolMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectToolMarkingMenu(*_args, **kwargs))


def SelectToolMarkingMenuPopDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectToolMarkingMenuPopDown(*_args, **kwargs))


def SelectToolOptionsMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectToolOptionsMarkingMenu(*_args, **kwargs))


def SelectToolOptionsMarkingMenuPopDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectToolOptionsMarkingMenuPopDown(*_args, **kwargs))


def SelectUVBackFacingComponents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectUVBackFacingComponents(*_args, **kwargs))


def SelectUVBorder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectUVBorder(*_args, **kwargs))


def SelectUVBorderComponents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectUVBorderComponents(*_args, **kwargs))


def SelectUVFrontFacingComponents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectUVFrontFacingComponents(*_args, **kwargs))


def SelectUVMask(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectUVMask(*_args, **kwargs))


def SelectUVNonOverlappingComponents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectUVNonOverlappingComponents(*_args, **kwargs))


def SelectUVNonOverlappingComponentsPerObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectUVNonOverlappingComponentsPerObject(*_args, **kwargs))


def SelectUVOverlappingComponents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectUVOverlappingComponents(*_args, **kwargs))


def SelectUVOverlappingComponentsPerObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectUVOverlappingComponentsPerObject(*_args, **kwargs))


def SelectUVShell(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectUVShell(*_args, **kwargs))


def SelectUVTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectUVTool(*_args, **kwargs))


def SelectUnmappedFaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectUnmappedFaces(*_args, **kwargs))


def SelectVertexFaceMask(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectVertexFaceMask(*_args, **kwargs))


def SelectVertexMask(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectVertexMask(*_args, **kwargs))


def SelectedAnimLayer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SelectedAnimLayer(*_args, **kwargs))


def SendAsNewScene3dsMax(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SendAsNewScene3dsMax(*_args, **kwargs))


def SendAsNewSceneMotionBuilder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SendAsNewSceneMotionBuilder(*_args, **kwargs))


def SendAsNewSceneMudbox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SendAsNewSceneMudbox(*_args, **kwargs))


def SendAsNewScenePrintStudio(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SendAsNewScenePrintStudio(*_args, **kwargs))


def SendToUnityAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SendToUnityAll(*_args, **kwargs))


def SendToUnitySelection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SendToUnitySelection(*_args, **kwargs))


def SendToUnitySetProject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SendToUnitySetProject(*_args, **kwargs))


def SendToUnrealAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SendToUnrealAll(*_args, **kwargs))


def SendToUnrealSelection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SendToUnrealSelection(*_args, **kwargs))


def SendToUnrealSetProject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SendToUnrealSetProject(*_args, **kwargs))


def SeparatePolygon(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SeparatePolygon(*_args, **kwargs))


def SequenceEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SequenceEditor(*_args, **kwargs))


def SetActiveKey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetActiveKey(*_args, **kwargs))


def SetAsCombinationTarget(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetAsCombinationTarget(*_args, **kwargs))


def SetAsCombinationTargetOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetAsCombinationTargetOptions(*_args, **kwargs))


def SetBreakdownKey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetBreakdownKey(*_args, **kwargs))


def SetBreakdownKeyOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetBreakdownKeyOptions(*_args, **kwargs))


def SetContactLayersToUse(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetContactLayersToUse(*_args, **kwargs))


def SetCurrentColorSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetCurrentColorSet(*_args, **kwargs))


def SetCurrentUVSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetCurrentUVSet(*_args, **kwargs))


def SetCutSewUVTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetCutSewUVTool(*_args, **kwargs))


def SetDrivenKey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetDrivenKey(*_args, **kwargs))


def SetDrivenKeyOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetDrivenKeyOptions(*_args, **kwargs))


def SetEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetEditor(*_args, **kwargs))


def SetFluidAttrFromCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetFluidAttrFromCurve(*_args, **kwargs))


def SetFluidAttrFromCurveOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetFluidAttrFromCurveOptions(*_args, **kwargs))


def SetFocusToCommandLine(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetFocusToCommandLine(*_args, **kwargs))


def SetFocusToNumericInputLine(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetFocusToNumericInputLine(*_args, **kwargs))


def SetFullBodyIKKeys(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetFullBodyIKKeys(*_args, **kwargs))


def SetFullBodyIKKeysAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetFullBodyIKKeysAll(*_args, **kwargs))


def SetFullBodyIKKeysBodyPart(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetFullBodyIKKeysBodyPart(*_args, **kwargs))


def SetFullBodyIKKeysKeyToPin(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetFullBodyIKKeysKeyToPin(*_args, **kwargs))


def SetFullBodyIKKeysOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetFullBodyIKKeysOptions(*_args, **kwargs))


def SetFullBodyIKKeysSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetFullBodyIKKeysSelected(*_args, **kwargs))


def SetIKFKKeyframe(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetIKFKKeyframe(*_args, **kwargs))


def SetInitialState(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetInitialState(*_args, **kwargs))


def SetInitialStateOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetInitialStateOptions(*_args, **kwargs))


def SetKey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetKey(*_args, **kwargs))


def SetKeyAnimated(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetKeyAnimated(*_args, **kwargs))


def SetKeyOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetKeyOptions(*_args, **kwargs))


def SetKeyPath(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetKeyPath(*_args, **kwargs))


def SetKeyRotate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetKeyRotate(*_args, **kwargs))


def SetKeyScale(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetKeyScale(*_args, **kwargs))


def SetKeyTranslate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetKeyTranslate(*_args, **kwargs))


def SetKeyVertexColor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetKeyVertexColor(*_args, **kwargs))


def SetMaxInfluences(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMaxInfluences(*_args, **kwargs))


def SetMeshAmplifyTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshAmplifyTool(*_args, **kwargs))


def SetMeshBulgeTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshBulgeTool(*_args, **kwargs))


def SetMeshCloneTargetTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshCloneTargetTool(*_args, **kwargs))


def SetMeshEraseTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshEraseTool(*_args, **kwargs))


def SetMeshFillTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshFillTool(*_args, **kwargs))


def SetMeshFlattenTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshFlattenTool(*_args, **kwargs))


def SetMeshFoamyTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshFoamyTool(*_args, **kwargs))


def SetMeshFreezeTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshFreezeTool(*_args, **kwargs))


def SetMeshGrabTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshGrabTool(*_args, **kwargs))


def SetMeshGrabUVTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshGrabUVTool(*_args, **kwargs))


def SetMeshImprintTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshImprintTool(*_args, **kwargs))


def SetMeshKnifeTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshKnifeTool(*_args, **kwargs))


def SetMeshMaskTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshMaskTool(*_args, **kwargs))


def SetMeshPinchTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshPinchTool(*_args, **kwargs))


def SetMeshRelaxTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshRelaxTool(*_args, **kwargs))


def SetMeshRepeatTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshRepeatTool(*_args, **kwargs))


def SetMeshScrapeTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshScrapeTool(*_args, **kwargs))


def SetMeshSculptTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshSculptTool(*_args, **kwargs))


def SetMeshSmearTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshSmearTool(*_args, **kwargs))


def SetMeshSmoothTargetTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshSmoothTargetTool(*_args, **kwargs))


def SetMeshSmoothTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshSmoothTool(*_args, **kwargs))


def SetMeshSprayTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshSprayTool(*_args, **kwargs))


def SetMeshWaxTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetMeshWaxTool(*_args, **kwargs))


def SetNClothStartFromMesh(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetNClothStartFromMesh(*_args, **kwargs))


def SetNormalAngle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetNormalAngle(*_args, **kwargs))


def SetPassiveKey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetPassiveKey(*_args, **kwargs))


def SetPreferredAngle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetPreferredAngle(*_args, **kwargs))


def SetPreferredAngleOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetPreferredAngleOptions(*_args, **kwargs))


def SetProject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetProject(*_args, **kwargs))


def SetReFormTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetReFormTool(*_args, **kwargs))


def SetRigidBodyCollision(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetRigidBodyCollision(*_args, **kwargs))


def SetRigidBodyInterpenetration(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetRigidBodyInterpenetration(*_args, **kwargs))


def SetShrinkWrapInnerObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetShrinkWrapInnerObject(*_args, **kwargs))


def SetShrinkWrapTarget(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetShrinkWrapTarget(*_args, **kwargs))


def SetStrokeControlCurves(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetStrokeControlCurves(*_args, **kwargs))


def SetTimecode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetTimecode(*_args, **kwargs))


def SetToFaceNormals(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetToFaceNormals(*_args, **kwargs))


def SetToFaceNormalsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetToFaceNormalsOptions(*_args, **kwargs))


def SetVertexNormal(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetVertexNormal(*_args, **kwargs))


def SetVertexNormalOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetVertexNormalOptions(*_args, **kwargs))


def SetWorkingFrame(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SetWorkingFrame(*_args, **kwargs))


def SewUVs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SewUVs(*_args, **kwargs))


def SewUVs3D(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SewUVs3D(*_args, **kwargs))


def SewUVsWithoutHotkey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SewUVsWithoutHotkey(*_args, **kwargs))


def ShadingGroupAttributeEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShadingGroupAttributeEditor(*_args, **kwargs))


def ShapeEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShapeEditor(*_args, **kwargs))


def ShapeEditorDuplicateTarget(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShapeEditorDuplicateTarget(*_args, **kwargs))


def ShapeEditorNewGroup(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShapeEditorNewGroup(*_args, **kwargs))


def ShapeEditorSelectNone(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShapeEditorSelectNone(*_args, **kwargs))


def ShareColorInstances(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShareColorInstances(*_args, **kwargs))


def ShareOneBrush(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShareOneBrush(*_args, **kwargs))


def ShareUVInstances(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShareUVInstances(*_args, **kwargs))


def Shatter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Shatter(*_args, **kwargs))


def ShatterOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShatterOptions(*_args, **kwargs))


def ShelfPreferencesWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShelfPreferencesWindow(*_args, **kwargs))


def ShortPolygonNormals(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShortPolygonNormals(*_args, **kwargs))


def ShotPlaylistEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShotPlaylistEditor(*_args, **kwargs))


def ShowAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowAll(*_args, **kwargs))


def ShowAllComponents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowAllComponents(*_args, **kwargs))


def ShowAllEditedComponents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowAllEditedComponents(*_args, **kwargs))


def ShowAllPolyComponents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowAllPolyComponents(*_args, **kwargs))


def ShowAllUI(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowAllUI(*_args, **kwargs))


def ShowAnimationUI(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowAnimationUI(*_args, **kwargs))


def ShowAttributeEditorOrChannelBox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowAttributeEditorOrChannelBox(*_args, **kwargs))


def ShowBaseWire(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowBaseWire(*_args, **kwargs))


def ShowBatchRender(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowBatchRender(*_args, **kwargs))


def ShowBoundingBox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowBoundingBox(*_args, **kwargs))


def ShowCameraManipulators(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowCameraManipulators(*_args, **kwargs))


def ShowCameras(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowCameras(*_args, **kwargs))


def ShowClusters(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowClusters(*_args, **kwargs))


def ShowControllers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowControllers(*_args, **kwargs))


def ShowDeformers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowDeformers(*_args, **kwargs))


def ShowDeformingGeometry(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowDeformingGeometry(*_args, **kwargs))


def ShowDynamicConstraints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowDynamicConstraints(*_args, **kwargs))


def ShowDynamicsUI(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowDynamicsUI(*_args, **kwargs))


def ShowFluids(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowFluids(*_args, **kwargs))


def ShowFollicles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowFollicles(*_args, **kwargs))


def ShowFur(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowFur(*_args, **kwargs))


def ShowGeometry(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowGeometry(*_args, **kwargs))


def ShowHairSystems(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowHairSystems(*_args, **kwargs))


def ShowHotbox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowHotbox(*_args, **kwargs))


def ShowIKHandles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowIKHandles(*_args, **kwargs))


def ShowJoints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowJoints(*_args, **kwargs))


def ShowKinematics(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowKinematics(*_args, **kwargs))


def ShowLastHidden(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowLastHidden(*_args, **kwargs))


def ShowLattices(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowLattices(*_args, **kwargs))


def ShowLightManipulators(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowLightManipulators(*_args, **kwargs))


def ShowLights(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowLights(*_args, **kwargs))


def ShowManipulatorTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowManipulatorTool(*_args, **kwargs))


def ShowManipulators(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowManipulators(*_args, **kwargs))


def ShowMarkers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMarkers(*_args, **kwargs))


def ShowMeshAmplifyToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshAmplifyToolOptions(*_args, **kwargs))


def ShowMeshBulgeToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshBulgeToolOptions(*_args, **kwargs))


def ShowMeshCloneTargetToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshCloneTargetToolOptions(*_args, **kwargs))


def ShowMeshEraseToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshEraseToolOptions(*_args, **kwargs))


def ShowMeshFillToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshFillToolOptions(*_args, **kwargs))


def ShowMeshFlattenToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshFlattenToolOptions(*_args, **kwargs))


def ShowMeshFoamyToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshFoamyToolOptions(*_args, **kwargs))


def ShowMeshFreezeToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshFreezeToolOptions(*_args, **kwargs))


def ShowMeshGrabToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshGrabToolOptions(*_args, **kwargs))


def ShowMeshGrabUVToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshGrabUVToolOptions(*_args, **kwargs))


def ShowMeshImprintToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshImprintToolOptions(*_args, **kwargs))


def ShowMeshKnifeToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshKnifeToolOptions(*_args, **kwargs))


def ShowMeshMaskToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshMaskToolOptions(*_args, **kwargs))


def ShowMeshPinchToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshPinchToolOptions(*_args, **kwargs))


def ShowMeshRelaxToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshRelaxToolOptions(*_args, **kwargs))


def ShowMeshRepeatToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshRepeatToolOptions(*_args, **kwargs))


def ShowMeshScrapeToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshScrapeToolOptions(*_args, **kwargs))


def ShowMeshSculptToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshSculptToolOptions(*_args, **kwargs))


def ShowMeshSmearToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshSmearToolOptions(*_args, **kwargs))


def ShowMeshSmoothTargetToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshSmoothTargetToolOptions(*_args, **kwargs))


def ShowMeshSmoothToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshSmoothToolOptions(*_args, **kwargs))


def ShowMeshSprayToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshSprayToolOptions(*_args, **kwargs))


def ShowMeshWaxToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowMeshWaxToolOptions(*_args, **kwargs))


def ShowModelingUI(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowModelingUI(*_args, **kwargs))


def ShowNCloths(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowNCloths(*_args, **kwargs))


def ShowNParticles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowNParticles(*_args, **kwargs))


def ShowNRigids(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowNRigids(*_args, **kwargs))


def ShowNURBSCurves(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowNURBSCurves(*_args, **kwargs))


def ShowNURBSSurfaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowNURBSSurfaces(*_args, **kwargs))


def ShowNonlinears(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowNonlinears(*_args, **kwargs))


def ShowObjectGeometry(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowObjectGeometry(*_args, **kwargs))


def ShowPlanes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowPlanes(*_args, **kwargs))


def ShowPolygonSurfaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowPolygonSurfaces(*_args, **kwargs))


def ShowRenderingUI(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowRenderingUI(*_args, **kwargs))


def ShowResultsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowResultsOptions(*_args, **kwargs))


def ShowRiggingUI(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowRiggingUI(*_args, **kwargs))


def ShowSculptObjects(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowSculptObjects(*_args, **kwargs))


def ShowSelectedObjects(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowSelectedObjects(*_args, **kwargs))


def ShowShadingGroupAttributeEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowShadingGroupAttributeEditor(*_args, **kwargs))


def ShowSmoothSkinInfluences(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowSmoothSkinInfluences(*_args, **kwargs))


def ShowStrokeControlCurves(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowStrokeControlCurves(*_args, **kwargs))


def ShowStrokePathCurves(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowStrokePathCurves(*_args, **kwargs))


def ShowStrokes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowStrokes(*_args, **kwargs))


def ShowSubdivSurfaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowSubdivSurfaces(*_args, **kwargs))


def ShowSurfaceCVs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowSurfaceCVs(*_args, **kwargs))


def ShowTexturePlacements(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowTexturePlacements(*_args, **kwargs))


def ShowUIElements(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowUIElements(*_args, **kwargs))


def ShowWrapInfluences(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShowWrapInfluences(*_args, **kwargs))


def ShrinkLoopPolygonSelectionRegion(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShrinkLoopPolygonSelectionRegion(*_args, **kwargs))


def ShrinkPolygonSelectionRegion(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ShrinkPolygonSelectionRegion(*_args, **kwargs))


def SiShelfXPOP(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SiShelfXPOP(*_args, **kwargs))


def SimplifyCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SimplifyCurve(*_args, **kwargs))


def SimplifyCurveOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SimplifyCurveOptions(*_args, **kwargs))


def SimplifyStrokePathCurves(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SimplifyStrokePathCurves(*_args, **kwargs))


def Sine(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Sine(*_args, **kwargs))


def SineOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SineOptions(*_args, **kwargs))


def SinglePerspectiveViewLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SinglePerspectiveViewLayout(*_args, **kwargs))


def SingleViewArrangement(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SingleViewArrangement(*_args, **kwargs))


def SlideEdgeTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SlideEdgeTool(*_args, **kwargs))


def SlideEdgeToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SlideEdgeToolOptions(*_args, **kwargs))


def Smoke(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Smoke(*_args, **kwargs))


def SmokeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SmokeOptions(*_args, **kwargs))


def SmoothBindSkin(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SmoothBindSkin(*_args, **kwargs))


def SmoothBindSkinOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SmoothBindSkinOptions(*_args, **kwargs))


def SmoothCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SmoothCurve(*_args, **kwargs))


def SmoothCurveOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SmoothCurveOptions(*_args, **kwargs))


def SmoothHairCurves(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SmoothHairCurves(*_args, **kwargs))


def SmoothHairCurvesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SmoothHairCurvesOptions(*_args, **kwargs))


def SmoothPolygon(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SmoothPolygon(*_args, **kwargs))


def SmoothPolygonOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SmoothPolygonOptions(*_args, **kwargs))


def SmoothProxy(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SmoothProxy(*_args, **kwargs))


def SmoothProxyOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SmoothProxyOptions(*_args, **kwargs))


def SmoothSkinWeights(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SmoothSkinWeights(*_args, **kwargs))


def SmoothSkinWeightsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SmoothSkinWeightsOptions(*_args, **kwargs))


def SmoothTangent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SmoothTangent(*_args, **kwargs))


def SmoothingDisplayShowBoth(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SmoothingDisplayShowBoth(*_args, **kwargs))


def SmoothingDisplayToggle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SmoothingDisplayToggle(*_args, **kwargs))


def SmoothingLevelDecrease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SmoothingLevelDecrease(*_args, **kwargs))


def SmoothingLevelIncrease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SmoothingLevelIncrease(*_args, **kwargs))


def Snap2PointsTo2Points(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Snap2PointsTo2Points(*_args, **kwargs))


def Snap2PointsTo2PointsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Snap2PointsTo2PointsOptions(*_args, **kwargs))


def Snap3PointsTo3Points(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Snap3PointsTo3Points(*_args, **kwargs))


def Snap3PointsTo3PointsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Snap3PointsTo3PointsOptions(*_args, **kwargs))


def SnapKeys(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SnapKeys(*_args, **kwargs))


def SnapKeysOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SnapKeysOptions(*_args, **kwargs))


def SnapPointToPoint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SnapPointToPoint(*_args, **kwargs))


def SnapPointToPointOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SnapPointToPointOptions(*_args, **kwargs))


def SnapToCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SnapToCurve(*_args, **kwargs))


def SnapToCurvePress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SnapToCurvePress(*_args, **kwargs))


def SnapToCurveRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SnapToCurveRelease(*_args, **kwargs))


def SnapToGrid(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SnapToGrid(*_args, **kwargs))


def SnapToGridPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SnapToGridPress(*_args, **kwargs))


def SnapToGridRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SnapToGridRelease(*_args, **kwargs))


def SnapToMeshCenter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SnapToMeshCenter(*_args, **kwargs))


def SnapToMeshCenterPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SnapToMeshCenterPress(*_args, **kwargs))


def SnapToMeshCenterRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SnapToMeshCenterRelease(*_args, **kwargs))


def SnapToPixel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SnapToPixel(*_args, **kwargs))


def SnapToPoint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SnapToPoint(*_args, **kwargs))


def SnapToPointPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SnapToPointPress(*_args, **kwargs))


def SnapToPointRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SnapToPointRelease(*_args, **kwargs))


def SoftModDeformer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SoftModDeformer(*_args, **kwargs))


def SoftModDeformerOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SoftModDeformerOptions(*_args, **kwargs))


def SoftModTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SoftModTool(*_args, **kwargs))


def SoftModToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SoftModToolOptions(*_args, **kwargs))


def SoloLastOutput(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SoloLastOutput(*_args, **kwargs))


def SoloMaterial(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SoloMaterial(*_args, **kwargs))


def SplitEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SplitEdge(*_args, **kwargs))


def SplitEdgeRingTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SplitEdgeRingTool(*_args, **kwargs))


def SplitEdgeRingToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SplitEdgeRingToolOptions(*_args, **kwargs))


def SplitMeshWithProjectedCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SplitMeshWithProjectedCurve(*_args, **kwargs))


def SplitMeshWithProjectedCurveOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SplitMeshWithProjectedCurveOptions(*_args, **kwargs))


def SplitPolygonTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SplitPolygonTool(*_args, **kwargs))


def SplitPolygonToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SplitPolygonToolOptions(*_args, **kwargs))


def SplitUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SplitUV(*_args, **kwargs))


def SplitVertex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SplitVertex(*_args, **kwargs))


def SpreadSheetEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SpreadSheetEditor(*_args, **kwargs))


def SquareSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SquareSurface(*_args, **kwargs))


def SquareSurfaceOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SquareSurfaceOptions(*_args, **kwargs))


def Squash(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Squash(*_args, **kwargs))


def SquashOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SquashOptions(*_args, **kwargs))


def StitchEdgesTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.StitchEdgesTool(*_args, **kwargs))


def StitchEdgesToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.StitchEdgesToolOptions(*_args, **kwargs))


def StitchSurfacePoints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.StitchSurfacePoints(*_args, **kwargs))


def StitchSurfacePointsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.StitchSurfacePointsOptions(*_args, **kwargs))


def StitchTogether(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.StitchTogether(*_args, **kwargs))


def StitchTogetherOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.StitchTogetherOptions(*_args, **kwargs))


def StraightenCurves(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.StraightenCurves(*_args, **kwargs))


def StraightenCurvesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.StraightenCurvesOptions(*_args, **kwargs))


def StraightenUVBorder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.StraightenUVBorder(*_args, **kwargs))


def StraightenUVBorderOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.StraightenUVBorderOptions(*_args, **kwargs))


def SubdCutUVs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SubdCutUVs(*_args, **kwargs))


def SubdivProxy(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SubdivProxy(*_args, **kwargs))


def SubdivProxyOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SubdivProxyOptions(*_args, **kwargs))


def SubdivSmoothnessFine(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SubdivSmoothnessFine(*_args, **kwargs))


def SubdivSmoothnessFineOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SubdivSmoothnessFineOptions(*_args, **kwargs))


def SubdivSmoothnessHull(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SubdivSmoothnessHull(*_args, **kwargs))


def SubdivSmoothnessHullOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SubdivSmoothnessHullOptions(*_args, **kwargs))


def SubdivSmoothnessMedium(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SubdivSmoothnessMedium(*_args, **kwargs))


def SubdivSmoothnessMediumOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SubdivSmoothnessMediumOptions(*_args, **kwargs))


def SubdivSmoothnessRough(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SubdivSmoothnessRough(*_args, **kwargs))


def SubdivSmoothnessRoughOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SubdivSmoothnessRoughOptions(*_args, **kwargs))


def SubdivSurfaceCleanTopology(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SubdivSurfaceCleanTopology(*_args, **kwargs))


def SubdivSurfaceHierarchyMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SubdivSurfaceHierarchyMode(*_args, **kwargs))


def SubdivSurfaceMatchTopology(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SubdivSurfaceMatchTopology(*_args, **kwargs))


def SubdivSurfacePolygonProxyMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SubdivSurfacePolygonProxyMode(*_args, **kwargs))


def SubdivToNURBS(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SubdivToNURBS(*_args, **kwargs))


def SubdivToNURBSOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SubdivToNURBSOptions(*_args, **kwargs))


def SubdividePolygon(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SubdividePolygon(*_args, **kwargs))


def SubdividePolygonOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SubdividePolygonOptions(*_args, **kwargs))


def SubstituteGeometry(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SubstituteGeometry(*_args, **kwargs))


def SubstituteGeometryOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SubstituteGeometryOptions(*_args, **kwargs))


def SurfaceBooleanIntersectTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SurfaceBooleanIntersectTool(*_args, **kwargs))


def SurfaceBooleanIntersectToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SurfaceBooleanIntersectToolOptions(*_args, **kwargs))


def SurfaceBooleanSubtractTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SurfaceBooleanSubtractTool(*_args, **kwargs))


def SurfaceBooleanSubtractToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SurfaceBooleanSubtractToolOptions(*_args, **kwargs))


def SurfaceBooleanUnionTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SurfaceBooleanUnionTool(*_args, **kwargs))


def SurfaceBooleanUnionToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SurfaceBooleanUnionToolOptions(*_args, **kwargs))


def SurfaceEditingTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SurfaceEditingTool(*_args, **kwargs))


def SurfaceEditingToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SurfaceEditingToolOptions(*_args, **kwargs))


def SurfaceFlow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SurfaceFlow(*_args, **kwargs))


def SurfaceFlowOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SurfaceFlowOptions(*_args, **kwargs))


def SwapBlendShape(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SwapBlendShape(*_args, **kwargs))


def SwapBlendShapeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SwapBlendShapeOptions(*_args, **kwargs))


def SwapBufferCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SwapBufferCurve(*_args, **kwargs))


def SymmetrizeSelection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SymmetrizeSelection(*_args, **kwargs))


def SymmetrizeUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SymmetrizeUV(*_args, **kwargs))


def SymmetrizeUVBrushSizeOff(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SymmetrizeUVBrushSizeOff(*_args, **kwargs))


def SymmetrizeUVBrushSizeOn(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SymmetrizeUVBrushSizeOn(*_args, **kwargs))


def SymmetrizeUVContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SymmetrizeUVContext(*_args, **kwargs))


def SymmetrizeUVOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SymmetrizeUVOptions(*_args, **kwargs))


def SymmetrizeUVUpdateCommand(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.SymmetrizeUVUpdateCommand(*_args, **kwargs))


def TagAsController(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TagAsController(*_args, **kwargs))


def TagAsControllerParent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TagAsControllerParent(*_args, **kwargs))


def TangentsAuto(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TangentsAuto(*_args, **kwargs))


def TangentsClamped(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TangentsClamped(*_args, **kwargs))


def TangentsFixed(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TangentsFixed(*_args, **kwargs))


def TangentsFlat(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TangentsFlat(*_args, **kwargs))


def TangentsLinear(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TangentsLinear(*_args, **kwargs))


def TangentsPlateau(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TangentsPlateau(*_args, **kwargs))


def TangentsSpline(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TangentsSpline(*_args, **kwargs))


def TangentsStepped(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TangentsStepped(*_args, **kwargs))


def TangetConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TangetConstraint(*_args, **kwargs))


def TangetConstraintOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TangetConstraintOptions(*_args, **kwargs))


def TanimLayer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TanimLayer(*_args, **kwargs))


def TemplateBrushSettings(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TemplateBrushSettings(*_args, **kwargs))


def TemplateObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TemplateObject(*_args, **kwargs))


def Tension(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Tension(*_args, **kwargs))


def TensionOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TensionOptions(*_args, **kwargs))


def TesselateSubdivSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TesselateSubdivSurface(*_args, **kwargs))


def TesselateSubdivSurfaceOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TesselateSubdivSurfaceOptions(*_args, **kwargs))


def TestTexture(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TestTexture(*_args, **kwargs))


def TestTextureOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TestTextureOptions(*_args, **kwargs))


def TexSculptActivateBrushSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TexSculptActivateBrushSize(*_args, **kwargs))


def TexSculptActivateBrushStrength(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TexSculptActivateBrushStrength(*_args, **kwargs))


def TexSculptDeactivateBrushSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TexSculptDeactivateBrushSize(*_args, **kwargs))


def TexSculptDeactivateBrushStrength(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TexSculptDeactivateBrushStrength(*_args, **kwargs))


def TexSculptInvertPin(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TexSculptInvertPin(*_args, **kwargs))


def TexSculptUnpinAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TexSculptUnpinAll(*_args, **kwargs))


def TexSewActivateBrushSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TexSewActivateBrushSize(*_args, **kwargs))


def TexSewDeactivateBrushSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TexSewDeactivateBrushSize(*_args, **kwargs))


def TextureCentricUVLinkingEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TextureCentricUVLinkingEditor(*_args, **kwargs))


def TextureViewWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TextureViewWindow(*_args, **kwargs))


def ThreeBottomSplitViewArrangement(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ThreeBottomSplitViewArrangement(*_args, **kwargs))


def ThreeLeftSplitViewArrangement(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ThreeLeftSplitViewArrangement(*_args, **kwargs))


def ThreePointArcTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ThreePointArcTool(*_args, **kwargs))


def ThreePointArcToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ThreePointArcToolOptions(*_args, **kwargs))


def ThreeRightSplitViewArrangement(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ThreeRightSplitViewArrangement(*_args, **kwargs))


def ThreeTopSplitViewArrangement(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ThreeTopSplitViewArrangement(*_args, **kwargs))


def TimeDraggerToolActivate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeDraggerToolActivate(*_args, **kwargs))


def TimeDraggerToolDeactivate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeDraggerToolDeactivate(*_args, **kwargs))


def TimeEditorAddToSoloSelectedTracks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorAddToSoloSelectedTracks(*_args, **kwargs))


def TimeEditorClipHoldToggle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorClipHoldToggle(*_args, **kwargs))


def TimeEditorClipLoopToggle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorClipLoopToggle(*_args, **kwargs))


def TimeEditorClipRazor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorClipRazor(*_args, **kwargs))


def TimeEditorClipResetTiming(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorClipResetTiming(*_args, **kwargs))


def TimeEditorClipScaleEnd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorClipScaleEnd(*_args, **kwargs))


def TimeEditorClipScaleStart(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorClipScaleStart(*_args, **kwargs))


def TimeEditorClipScaleToggle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorClipScaleToggle(*_args, **kwargs))


def TimeEditorClipTrimEnd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorClipTrimEnd(*_args, **kwargs))


def TimeEditorClipTrimStart(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorClipTrimStart(*_args, **kwargs))


def TimeEditorClipTrimToggle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorClipTrimToggle(*_args, **kwargs))


def TimeEditorCopyClips(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorCopyClips(*_args, **kwargs))


def TimeEditorCreateAdditiveLayer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorCreateAdditiveLayer(*_args, **kwargs))


def TimeEditorCreateAnimTracksAtEnd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorCreateAnimTracksAtEnd(*_args, **kwargs))


def TimeEditorCreateAudioClip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorCreateAudioClip(*_args, **kwargs))


def TimeEditorCreateAudioTracksAtEnd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorCreateAudioTracksAtEnd(*_args, **kwargs))


def TimeEditorCreateClip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorCreateClip(*_args, **kwargs))


def TimeEditorCreateClipOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorCreateClipOptions(*_args, **kwargs))


def TimeEditorCreateGroupFromSelection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorCreateGroupFromSelection(*_args, **kwargs))


def TimeEditorCreateOverrideLayer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorCreateOverrideLayer(*_args, **kwargs))


def TimeEditorCreatePoseClip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorCreatePoseClip(*_args, **kwargs))


def TimeEditorCreatePoseClipOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorCreatePoseClipOptions(*_args, **kwargs))


def TimeEditorCutClips(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorCutClips(*_args, **kwargs))


def TimeEditorDeleteClips(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorDeleteClips(*_args, **kwargs))


def TimeEditorDeleteSelectedTracks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorDeleteSelectedTracks(*_args, **kwargs))


def TimeEditorExplodeGroup(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorExplodeGroup(*_args, **kwargs))


def TimeEditorExportSelection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorExportSelection(*_args, **kwargs))


def TimeEditorExportSelectionOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorExportSelectionOpt(*_args, **kwargs))


def TimeEditorFbxExportAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorFbxExportAll(*_args, **kwargs))


def TimeEditorFrameAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorFrameAll(*_args, **kwargs))


def TimeEditorFrameCenterView(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorFrameCenterView(*_args, **kwargs))


def TimeEditorFramePlaybackRange(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorFramePlaybackRange(*_args, **kwargs))


def TimeEditorFrameSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorFrameSelected(*_args, **kwargs))


def TimeEditorGhostTrackToggle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorGhostTrackToggle(*_args, **kwargs))


def TimeEditorImportAnimation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorImportAnimation(*_args, **kwargs))


def TimeEditorKeepTransitionsTogglePress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorKeepTransitionsTogglePress(*_args, **kwargs))


def TimeEditorKeepTransitionsToggleRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorKeepTransitionsToggleRelease(*_args, **kwargs))


def TimeEditorMuteSelectedTracks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorMuteSelectedTracks(*_args, **kwargs))


def TimeEditorOpenContentBrowser(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorOpenContentBrowser(*_args, **kwargs))


def TimeEditorPasteClips(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorPasteClips(*_args, **kwargs))


def TimeEditorRippleEditTogglePress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorRippleEditTogglePress(*_args, **kwargs))


def TimeEditorRippleEditToggleRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorRippleEditToggleRelease(*_args, **kwargs))


def TimeEditorSceneAuthoringToggle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorSceneAuthoringToggle(*_args, **kwargs))


def TimeEditorSetKey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorSetKey(*_args, **kwargs))


def TimeEditorSetZeroKey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorSetZeroKey(*_args, **kwargs))


def TimeEditorSoloSelectedTracks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorSoloSelectedTracks(*_args, **kwargs))


def TimeEditorToggleMuteSelectedTracks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorToggleMuteSelectedTracks(*_args, **kwargs))


def TimeEditorToggleSnapToClipPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorToggleSnapToClipPress(*_args, **kwargs))


def TimeEditorToggleSnapToClipRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorToggleSnapToClipRelease(*_args, **kwargs))


def TimeEditorToggleSoloSelectedTracks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorToggleSoloSelectedTracks(*_args, **kwargs))


def TimeEditorToggleTimeCursorPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorToggleTimeCursorPress(*_args, **kwargs))


def TimeEditorToggleTimeCursorRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorToggleTimeCursorRelease(*_args, **kwargs))


def TimeEditorUnmuteAllTracks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorUnmuteAllTracks(*_args, **kwargs))


def TimeEditorUnmuteSelectedTracks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorUnmuteSelectedTracks(*_args, **kwargs))


def TimeEditorUnsoloAllTracks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorUnsoloAllTracks(*_args, **kwargs))


def TimeEditorWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TimeEditorWindow(*_args, **kwargs))


def ToggleAnimationDetails(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleAnimationDetails(*_args, **kwargs))


def ToggleAttributeEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleAttributeEditor(*_args, **kwargs))


def ToggleAutoActivateBodyPart(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleAutoActivateBodyPart(*_args, **kwargs))


def ToggleAutoFrame(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleAutoFrame(*_args, **kwargs))


def ToggleAutoSmooth(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleAutoSmooth(*_args, **kwargs))


def ToggleBackfaceCulling(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleBackfaceCulling(*_args, **kwargs))


def ToggleBackfaceGeometry(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleBackfaceGeometry(*_args, **kwargs))


def ToggleBorderEdges(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleBorderEdges(*_args, **kwargs))


def ToggleCVs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleCVs(*_args, **kwargs))


def ToggleCameraNames(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleCameraNames(*_args, **kwargs))


def ToggleCapsLockDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleCapsLockDisplay(*_args, **kwargs))


def ToggleChannelBox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleChannelBox(*_args, **kwargs))


def ToggleChannelsLayers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleChannelsLayers(*_args, **kwargs))


def ToggleCharacterControls(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleCharacterControls(*_args, **kwargs))


def ToggleColorFeedback(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleColorFeedback(*_args, **kwargs))


def ToggleCommandLine(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleCommandLine(*_args, **kwargs))


def ToggleCompIDs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleCompIDs(*_args, **kwargs))


def ToggleContainerCentric(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleContainerCentric(*_args, **kwargs))


def ToggleCreaseEdges(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleCreaseEdges(*_args, **kwargs))


def ToggleCreaseVertices(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleCreaseVertices(*_args, **kwargs))


def ToggleCullingVertices(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleCullingVertices(*_args, **kwargs))


def ToggleCurrentContainerHud(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleCurrentContainerHud(*_args, **kwargs))


def ToggleCurrentFrame(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleCurrentFrame(*_args, **kwargs))


def ToggleCustomNURBSComponents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleCustomNURBSComponents(*_args, **kwargs))


def ToggleDisplacement(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleDisplacement(*_args, **kwargs))


def ToggleDisplayGradient(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleDisplayGradient(*_args, **kwargs))


def ToggleEdgeIDs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleEdgeIDs(*_args, **kwargs))


def ToggleEdgeMetadata(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleEdgeMetadata(*_args, **kwargs))


def ToggleEditPoints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleEditPoints(*_args, **kwargs))


def ToggleEvaluationManagerVisibility(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleEvaluationManagerVisibility(*_args, **kwargs))


def ToggleFaceIDs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleFaceIDs(*_args, **kwargs))


def ToggleFaceMetadata(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleFaceMetadata(*_args, **kwargs))


def ToggleFaceNormalDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleFaceNormalDisplay(*_args, **kwargs))


def ToggleFaceNormals(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleFaceNormals(*_args, **kwargs))


def ToggleFastInteraction(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleFastInteraction(*_args, **kwargs))


def ToggleFkIk(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleFkIk(*_args, **kwargs))


def ToggleFocalLength(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleFocalLength(*_args, **kwargs))


def ToggleFrameRate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleFrameRate(*_args, **kwargs))


def ToggleFullScreenMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleFullScreenMode(*_args, **kwargs))


def ToggleGrid(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleGrid(*_args, **kwargs))


def ToggleHelpLine(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleHelpLine(*_args, **kwargs))


def ToggleHikDetails(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleHikDetails(*_args, **kwargs))


def ToggleHoleFaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleHoleFaces(*_args, **kwargs))


def ToggleHulls(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleHulls(*_args, **kwargs))


def ToggleIKAllowRotation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleIKAllowRotation(*_args, **kwargs))


def ToggleIKHandleSnap(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleIKHandleSnap(*_args, **kwargs))


def ToggleIKSolvers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleIKSolvers(*_args, **kwargs))


def ToggleIsolateSelect(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleIsolateSelect(*_args, **kwargs))


def ToggleKeepHardEdgeCulling(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleKeepHardEdgeCulling(*_args, **kwargs))


def ToggleKeepWireCulling(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleKeepWireCulling(*_args, **kwargs))


def ToggleLatticePoints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleLatticePoints(*_args, **kwargs))


def ToggleLatticeShape(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleLatticeShape(*_args, **kwargs))


def ToggleLayerBar(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleLayerBar(*_args, **kwargs))


def ToggleLocalRotationAxes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleLocalRotationAxes(*_args, **kwargs))


def ToggleMainMenubar(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleMainMenubar(*_args, **kwargs))


def ToggleMaterialLoadingDetailsVisibility(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleMaterialLoadingDetailsVisibility(*_args, **kwargs))


def ToggleMeshEdges(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleMeshEdges(*_args, **kwargs))


def ToggleMeshFaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleMeshFaces(*_args, **kwargs))


def ToggleMeshMaps(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleMeshMaps(*_args, **kwargs))


def ToggleMeshPoints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleMeshPoints(*_args, **kwargs))


def ToggleMeshUVBorders(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleMeshUVBorders(*_args, **kwargs))


def ToggleModelEditorBars(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleModelEditorBars(*_args, **kwargs))


def ToggleModelingToolkit(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleModelingToolkit(*_args, **kwargs))


def ToggleMultiColorFeedback(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleMultiColorFeedback(*_args, **kwargs))


def ToggleNormals(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleNormals(*_args, **kwargs))


def ToggleObjectDetails(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleObjectDetails(*_args, **kwargs))


def ToggleOppositeFlagOfSelectedShapes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleOppositeFlagOfSelectedShapes(*_args, **kwargs))


def ToggleOriginAxis(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleOriginAxis(*_args, **kwargs))


def ToggleOutliner(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleOutliner(*_args, **kwargs))


def TogglePaintAtDepth(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TogglePaintAtDepth(*_args, **kwargs))


def TogglePaintOnPaintableObjects(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TogglePaintOnPaintableObjects(*_args, **kwargs))


def TogglePanZoomPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TogglePanZoomPress(*_args, **kwargs))


def TogglePanZoomRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TogglePanZoomRelease(*_args, **kwargs))


def TogglePanelMenubar(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TogglePanelMenubar(*_args, **kwargs))


def ToggleParticleCount(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleParticleCount(*_args, **kwargs))


def TogglePolyCount(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TogglePolyCount(*_args, **kwargs))


def TogglePolyDisplayEdges(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TogglePolyDisplayEdges(*_args, **kwargs))


def TogglePolyDisplayHardEdges(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TogglePolyDisplayHardEdges(*_args, **kwargs))


def TogglePolyDisplayHardEdgesColor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TogglePolyDisplayHardEdgesColor(*_args, **kwargs))


def TogglePolyDisplayLimitToSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TogglePolyDisplayLimitToSelected(*_args, **kwargs))


def TogglePolyDisplaySoftEdges(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TogglePolyDisplaySoftEdges(*_args, **kwargs))


def TogglePolyNonPlanarFaceDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TogglePolyNonPlanarFaceDisplay(*_args, **kwargs))


def TogglePolyUVsCreateShader(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TogglePolyUVsCreateShader(*_args, **kwargs))


def TogglePolygonFaceCenters(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TogglePolygonFaceCenters(*_args, **kwargs))


def TogglePolygonFaceTriangles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TogglePolygonFaceTriangles(*_args, **kwargs))


def ToggleProxyDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleProxyDisplay(*_args, **kwargs))


def ToggleRangeSlider(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleRangeSlider(*_args, **kwargs))


def ToggleReflection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleReflection(*_args, **kwargs))


def ToggleRotationPivots(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleRotationPivots(*_args, **kwargs))


def ToggleScalePivots(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleScalePivots(*_args, **kwargs))


def ToggleSceneTimecode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleSceneTimecode(*_args, **kwargs))


def ToggleSelectDetails(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleSelectDetails(*_args, **kwargs))


def ToggleSelectionHandles(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleSelectionHandles(*_args, **kwargs))


def ToggleShelf(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleShelf(*_args, **kwargs))


def ToggleShowBufferCurves(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleShowBufferCurves(*_args, **kwargs))


def ToggleShowResults(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleShowResults(*_args, **kwargs))


def ToggleSoftEdges(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleSoftEdges(*_args, **kwargs))


def ToggleStatusLine(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleStatusLine(*_args, **kwargs))


def ToggleSubdDetails(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleSubdDetails(*_args, **kwargs))


def ToggleSurfaceFaceCenters(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleSurfaceFaceCenters(*_args, **kwargs))


def ToggleSurfaceOrigin(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleSurfaceOrigin(*_args, **kwargs))


def ToggleSymmetryDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleSymmetryDisplay(*_args, **kwargs))


def ToggleTangentDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleTangentDisplay(*_args, **kwargs))


def ToggleTextureBorder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleTextureBorder(*_args, **kwargs))


def ToggleTextureBorderEdges(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleTextureBorderEdges(*_args, **kwargs))


def ToggleTimeSlider(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleTimeSlider(*_args, **kwargs))


def ToggleToolMessage(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleToolMessage(*_args, **kwargs))


def ToggleToolSettings(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleToolSettings(*_args, **kwargs))


def ToggleToolbox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleToolbox(*_args, **kwargs))


def ToggleUIElements(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleUIElements(*_args, **kwargs))


def ToggleUVDistortion(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleUVDistortion(*_args, **kwargs))


def ToggleUVEditorIsolateSelectHUD(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleUVEditorIsolateSelectHUD(*_args, **kwargs))


def ToggleUVEditorUVStatisticsHUD(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleUVEditorUVStatisticsHUD(*_args, **kwargs))


def ToggleUVEditorUVStatisticsHUDOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleUVEditorUVStatisticsHUDOptions(*_args, **kwargs))


def ToggleUVIsolateViewSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleUVIsolateViewSelected(*_args, **kwargs))


def ToggleUVShellBorder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleUVShellBorder(*_args, **kwargs))


def ToggleUVTextureImage(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleUVTextureImage(*_args, **kwargs))


def ToggleUVs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleUVs(*_args, **kwargs))


def ToggleUnsharedUVs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleUnsharedUVs(*_args, **kwargs))


def ToggleUseDefaultMaterial(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleUseDefaultMaterial(*_args, **kwargs))


def ToggleVertIDs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleVertIDs(*_args, **kwargs))


def ToggleVertMetadata(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleVertMetadata(*_args, **kwargs))


def ToggleVertexNormalDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleVertexNormalDisplay(*_args, **kwargs))


def ToggleVertices(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleVertices(*_args, **kwargs))


def ToggleViewAxis(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleViewAxis(*_args, **kwargs))


def ToggleViewCube(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleViewCube(*_args, **kwargs))


def ToggleViewportRenderer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleViewportRenderer(*_args, **kwargs))


def ToggleVisibilityAndKeepSelection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleVisibilityAndKeepSelection(*_args, **kwargs))


def ToggleVisibilityAndKeepSelectionOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleVisibilityAndKeepSelectionOptions(*_args, **kwargs))


def ToggleWireframeInArtisan(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleWireframeInArtisan(*_args, **kwargs))


def ToggleZoomInMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToggleZoomInMode(*_args, **kwargs))


def ToolSettingsWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ToolSettingsWindow(*_args, **kwargs))


def TrackTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TrackTool(*_args, **kwargs))


def TransferAttributeValues(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TransferAttributeValues(*_args, **kwargs))


def TransferAttributeValuesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TransferAttributeValuesOptions(*_args, **kwargs))


def TransferAttributes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TransferAttributes(*_args, **kwargs))


def TransferVertexOrder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TransferVertexOrder(*_args, **kwargs))


def TransformNoSelectOffTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TransformNoSelectOffTool(*_args, **kwargs))


def TransformNoSelectOnTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TransformNoSelectOnTool(*_args, **kwargs))


def TransformPolygonComponent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TransformPolygonComponent(*_args, **kwargs))


def TransformPolygonComponentOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TransformPolygonComponentOptions(*_args, **kwargs))


def TranslateToolMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TranslateToolMarkingMenu(*_args, **kwargs))


def TranslateToolMarkingMenuPopDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TranslateToolMarkingMenuPopDown(*_args, **kwargs))


def TranslateToolWithSnapMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TranslateToolWithSnapMarkingMenu(*_args, **kwargs))


def TranslateToolWithSnapMarkingMenuPopDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TranslateToolWithSnapMarkingMenuPopDown(*_args, **kwargs))


def TransplantHair(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TransplantHair(*_args, **kwargs))


def TransplantHairOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TransplantHairOptions(*_args, **kwargs))


def Triangulate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Triangulate(*_args, **kwargs))


def TrimTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TrimTool(*_args, **kwargs))


def TrimToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TrimToolOptions(*_args, **kwargs))


def TruncateHairCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TruncateHairCache(*_args, **kwargs))


def TumbleTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TumbleTool(*_args, **kwargs))


def Turbulence(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Turbulence(*_args, **kwargs))


def TurbulenceOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TurbulenceOptions(*_args, **kwargs))


def Twist(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Twist(*_args, **kwargs))


def TwistOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TwistOptions(*_args, **kwargs))


def TwoPointArcTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TwoPointArcTool(*_args, **kwargs))


def TwoPointArcToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TwoPointArcToolOptions(*_args, **kwargs))


def TwoSideBySideViewArrangement(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TwoSideBySideViewArrangement(*_args, **kwargs))


def TwoStackedViewArrangement(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.TwoStackedViewArrangement(*_args, **kwargs))


def U3DBrushPressureOff(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.U3DBrushPressureOff(*_args, **kwargs))


def U3DBrushPressureOn(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.U3DBrushPressureOn(*_args, **kwargs))


def U3DBrushSizeOff(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.U3DBrushSizeOff(*_args, **kwargs))


def U3DBrushSizeOn(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.U3DBrushSizeOn(*_args, **kwargs))


def UIModeMarkingMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UIModeMarkingMenu(*_args, **kwargs))


def UIModeMarkingMenuPopDown(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UIModeMarkingMenuPopDown(*_args, **kwargs))


def UVAutomaticProjection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVAutomaticProjection(*_args, **kwargs))


def UVAutomaticProjectionOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVAutomaticProjectionOptions(*_args, **kwargs))


def UVCameraBasedProjection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVCameraBasedProjection(*_args, **kwargs))


def UVCameraBasedProjectionOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVCameraBasedProjectionOptions(*_args, **kwargs))


def UVCentricUVLinkingEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVCentricUVLinkingEditor(*_args, **kwargs))


def UVContourStretchProjection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVContourStretchProjection(*_args, **kwargs))


def UVContourStretchProjectionOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVContourStretchProjectionOptions(*_args, **kwargs))


def UVCreateSnapshot(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVCreateSnapshot(*_args, **kwargs))


def UVCylindricProjection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVCylindricProjection(*_args, **kwargs))


def UVCylindricProjectionOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVCylindricProjectionOptions(*_args, **kwargs))


def UVEditorFrameAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVEditorFrameAll(*_args, **kwargs))


def UVEditorFrameSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVEditorFrameSelected(*_args, **kwargs))


def UVEditorInvertPin(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVEditorInvertPin(*_args, **kwargs))


def UVEditorToggleTextureBorderDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVEditorToggleTextureBorderDisplay(*_args, **kwargs))


def UVEditorUnpinAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVEditorUnpinAll(*_args, **kwargs))


def UVGatherShells(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVGatherShells(*_args, **kwargs))


def UVIsolateLoadSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVIsolateLoadSet(*_args, **kwargs))


def UVNormalBasedProjection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVNormalBasedProjection(*_args, **kwargs))


def UVNormalBasedProjectionOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVNormalBasedProjectionOptions(*_args, **kwargs))


def UVOrientShells(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVOrientShells(*_args, **kwargs))


def UVPlanarProjection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVPlanarProjection(*_args, **kwargs))


def UVPlanarProjectionOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVPlanarProjectionOptions(*_args, **kwargs))


def UVSetEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVSetEditor(*_args, **kwargs))


def UVSnapTogether(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVSnapTogether(*_args, **kwargs))


def UVSnapTogetherOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVSnapTogetherOptions(*_args, **kwargs))


def UVSphericalProjection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVSphericalProjection(*_args, **kwargs))


def UVSphericalProjectionOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVSphericalProjectionOptions(*_args, **kwargs))


def UVStackSimilarShells(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVStackSimilarShells(*_args, **kwargs))


def UVStackSimilarShellsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVStackSimilarShellsOptions(*_args, **kwargs))


def UVStraighten(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVStraighten(*_args, **kwargs))


def UVStraightenOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVStraightenOptions(*_args, **kwargs))


def UVUnstackShells(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVUnstackShells(*_args, **kwargs))


def UVUnstackShellsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UVUnstackShellsOptions(*_args, **kwargs))


def UncreaseSubdivSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UncreaseSubdivSurface(*_args, **kwargs))


def Undo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Undo(*_args, **kwargs))


def UndoCanvas(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UndoCanvas(*_args, **kwargs))


def UndoViewChange(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UndoViewChange(*_args, **kwargs))


def Unfold3DContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Unfold3DContext(*_args, **kwargs))


def Unfold3DuvUpdateCommand(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Unfold3DuvUpdateCommand(*_args, **kwargs))


def UnfoldPackUVs3DInCurrentTile(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UnfoldPackUVs3DInCurrentTile(*_args, **kwargs))


def UnfoldPackUVs3DInEmptyTile(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UnfoldPackUVs3DInEmptyTile(*_args, **kwargs))


def UnfoldUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UnfoldUV(*_args, **kwargs))


def UnfoldUVOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UnfoldUVOptions(*_args, **kwargs))


def UnghostObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UnghostObject(*_args, **kwargs))


def Ungroup(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Ungroup(*_args, **kwargs))


def UngroupOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UngroupOptions(*_args, **kwargs))


def Uniform(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Uniform(*_args, **kwargs))


def UniformOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UniformOptions(*_args, **kwargs))


def UnifyTangents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UnifyTangents(*_args, **kwargs))


def UnitizeUVs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UnitizeUVs(*_args, **kwargs))


def UnitizeUVsOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UnitizeUVsOptions(*_args, **kwargs))


def UniversalManip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UniversalManip(*_args, **kwargs))


def UniversalManipOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UniversalManipOptions(*_args, **kwargs))


def UnlockContainer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UnlockContainer(*_args, **kwargs))


def UnlockCurveLength(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UnlockCurveLength(*_args, **kwargs))


def UnlockNormals(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UnlockNormals(*_args, **kwargs))


def UnmirrorSmoothProxy(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UnmirrorSmoothProxy(*_args, **kwargs))


def UnmirrorSmoothProxyOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UnmirrorSmoothProxyOptions(*_args, **kwargs))


def Unparent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Unparent(*_args, **kwargs))


def UnparentOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UnparentOptions(*_args, **kwargs))


def UnpinSelection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UnpinSelection(*_args, **kwargs))


def UnpublishAttributes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UnpublishAttributes(*_args, **kwargs))


def UnpublishChildAnchor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UnpublishChildAnchor(*_args, **kwargs))


def UnpublishNode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UnpublishNode(*_args, **kwargs))


def UnpublishParentAnchor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UnpublishParentAnchor(*_args, **kwargs))


def UnpublishRootTransform(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UnpublishRootTransform(*_args, **kwargs))


def UntemplateObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UntemplateObject(*_args, **kwargs))


def UntrimSurfaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UntrimSurfaces(*_args, **kwargs))


def UntrimSurfacesOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UntrimSurfacesOptions(*_args, **kwargs))


def UpdateBindingSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UpdateBindingSet(*_args, **kwargs))


def UpdateBindingSetOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UpdateBindingSetOptions(*_args, **kwargs))


def UpdateCurrentScene3dsMax(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UpdateCurrentScene3dsMax(*_args, **kwargs))


def UpdateCurrentSceneMotionBuilder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UpdateCurrentSceneMotionBuilder(*_args, **kwargs))


def UpdateCurrentSceneMudbox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UpdateCurrentSceneMudbox(*_args, **kwargs))


def UpdateEraseSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UpdateEraseSurface(*_args, **kwargs))


def UpdateReferenceSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UpdateReferenceSurface(*_args, **kwargs))


def UseSelectedEmitter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.UseSelectedEmitter(*_args, **kwargs))


def VertexNormalEditTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.VertexNormalEditTool(*_args, **kwargs))


def ViewAlongAxisNegativeX(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ViewAlongAxisNegativeX(*_args, **kwargs))


def ViewAlongAxisNegativeY(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ViewAlongAxisNegativeY(*_args, **kwargs))


def ViewAlongAxisNegativeZ(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ViewAlongAxisNegativeZ(*_args, **kwargs))


def ViewAlongAxisX(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ViewAlongAxisX(*_args, **kwargs))


def ViewAlongAxisY(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ViewAlongAxisY(*_args, **kwargs))


def ViewAlongAxisZ(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ViewAlongAxisZ(*_args, **kwargs))


def ViewImage(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ViewImage(*_args, **kwargs))


def ViewSequence(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ViewSequence(*_args, **kwargs))


def VisorWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.VisorWindow(*_args, **kwargs))


def VisualizeMetadataOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.VisualizeMetadataOptions(*_args, **kwargs))


def VolumeAxis(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.VolumeAxis(*_args, **kwargs))


def VolumeAxisOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.VolumeAxisOptions(*_args, **kwargs))


def Vortex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Vortex(*_args, **kwargs))


def VortexOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.VortexOptions(*_args, **kwargs))


def WalkTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.WalkTool(*_args, **kwargs))


def WarpImage(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.WarpImage(*_args, **kwargs))


def WarpImageOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.WarpImageOptions(*_args, **kwargs))


def Wave(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.Wave(*_args, **kwargs))


def WaveOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.WaveOptions(*_args, **kwargs))


def WedgePolygon(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.WedgePolygon(*_args, **kwargs))


def WedgePolygonOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.WedgePolygonOptions(*_args, **kwargs))


def WeightedTangents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.WeightedTangents(*_args, **kwargs))


def WhatsNewHighlightingOff(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.WhatsNewHighlightingOff(*_args, **kwargs))


def WhatsNewHighlightingOn(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.WhatsNewHighlightingOn(*_args, **kwargs))


def WhatsNewStartupDialogOff(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.WhatsNewStartupDialogOff(*_args, **kwargs))


def WhatsNewStartupDialogOn(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.WhatsNewStartupDialogOn(*_args, **kwargs))


def WireDropoffLocator(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.WireDropoffLocator(*_args, **kwargs))


def WireDropoffLocatorOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.WireDropoffLocatorOptions(*_args, **kwargs))


def WireTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.WireTool(*_args, **kwargs))


def WireToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.WireToolOptions(*_args, **kwargs))


def WrinkleTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.WrinkleTool(*_args, **kwargs))


def WrinkleToolOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.WrinkleToolOptions(*_args, **kwargs))


def XgCreateIgSplineEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgCreateIgSplineEditor(*_args, **kwargs))


def XgmCreateInteractiveGroomSplines(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmCreateInteractiveGroomSplines(*_args, **kwargs))


def XgmCreateInteractiveGroomSplinesOption(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmCreateInteractiveGroomSplinesOption(*_args, **kwargs))


def XgmSetClumpBrushTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetClumpBrushTool(*_args, **kwargs))


def XgmSetClumpBrushToolOption(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetClumpBrushToolOption(*_args, **kwargs))


def XgmSetCombBrushTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetCombBrushTool(*_args, **kwargs))


def XgmSetCombBrushToolOption(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetCombBrushToolOption(*_args, **kwargs))


def XgmSetCutBrushTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetCutBrushTool(*_args, **kwargs))


def XgmSetCutBrushToolOption(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetCutBrushToolOption(*_args, **kwargs))


def XgmSetDensityBrushTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetDensityBrushTool(*_args, **kwargs))


def XgmSetDensityBrushToolOption(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetDensityBrushToolOption(*_args, **kwargs))


def XgmSetDirectionBrushTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetDirectionBrushTool(*_args, **kwargs))


def XgmSetDirectionBrushToolOption(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetDirectionBrushToolOption(*_args, **kwargs))


def XgmSetFreezeBrushTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetFreezeBrushTool(*_args, **kwargs))


def XgmSetFreezeBrushToolOption(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetFreezeBrushToolOption(*_args, **kwargs))


def XgmSetGrabBrushTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetGrabBrushTool(*_args, **kwargs))


def XgmSetGrabBrushToolOption(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetGrabBrushToolOption(*_args, **kwargs))


def XgmSetLengthBrushTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetLengthBrushTool(*_args, **kwargs))


def XgmSetLengthBrushToolOption(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetLengthBrushToolOption(*_args, **kwargs))


def XgmSetNoiseBrushTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetNoiseBrushTool(*_args, **kwargs))


def XgmSetNoiseBrushToolOption(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetNoiseBrushToolOption(*_args, **kwargs))


def XgmSetPartBrushTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetPartBrushTool(*_args, **kwargs))


def XgmSetPartBrushToolOption(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetPartBrushToolOption(*_args, **kwargs))


def XgmSetPlaceBrushTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetPlaceBrushTool(*_args, **kwargs))


def XgmSetPlaceBrushToolOption(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetPlaceBrushToolOption(*_args, **kwargs))


def XgmSetSelectBrushTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetSelectBrushTool(*_args, **kwargs))


def XgmSetSelectBrushToolOption(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetSelectBrushToolOption(*_args, **kwargs))


def XgmSetSmoothBrushTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetSmoothBrushTool(*_args, **kwargs))


def XgmSetSmoothBrushToolOption(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetSmoothBrushToolOption(*_args, **kwargs))


def XgmSetWidthBrushTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetWidthBrushTool(*_args, **kwargs))


def XgmSetWidthBrushToolOption(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSetWidthBrushToolOption(*_args, **kwargs))


def XgmSplineCacheCreate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSplineCacheCreate(*_args, **kwargs))


def XgmSplineCacheCreateOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSplineCacheCreateOptions(*_args, **kwargs))


def XgmSplineCacheDelete(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSplineCacheDelete(*_args, **kwargs))


def XgmSplineCacheDeleteNodesAhead(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSplineCacheDeleteNodesAhead(*_args, **kwargs))


def XgmSplineCacheDeleteOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSplineCacheDeleteOptions(*_args, **kwargs))


def XgmSplineCacheDisableSelectedCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSplineCacheDisableSelectedCache(*_args, **kwargs))


def XgmSplineCacheEnableSelectedCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSplineCacheEnableSelectedCache(*_args, **kwargs))


def XgmSplineCacheExport(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSplineCacheExport(*_args, **kwargs))


def XgmSplineCacheExportOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSplineCacheExportOptions(*_args, **kwargs))


def XgmSplineCacheImport(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSplineCacheImport(*_args, **kwargs))


def XgmSplineCacheImportOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSplineCacheImportOptions(*_args, **kwargs))


def XgmSplineCacheReplace(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSplineCacheReplace(*_args, **kwargs))


def XgmSplineCacheReplaceOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSplineCacheReplaceOptions(*_args, **kwargs))


def XgmSplineGeometryConvert(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSplineGeometryConvert(*_args, **kwargs))


def XgmSplinePresetExport(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSplinePresetExport(*_args, **kwargs))


def XgmSplinePresetImport(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSplinePresetImport(*_args, **kwargs))


def XgmSplineSelectConvertToFreeze(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSplineSelectConvertToFreeze(*_args, **kwargs))


def XgmSplineSelectReplaceBySelectedFaces(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.XgmSplineSelectReplaceBySelectedFaces(*_args, **kwargs))


def ZoomTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ZoomTool(*_args, **kwargs))


def aaf2fcp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.aaf2fcp(*_args, **kwargs))


def about(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.about(*_args, **kwargs))


def aboutDialogCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.aboutDialogCmd(*_args, **kwargs))


def abs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.abs(*_args, **kwargs))


def acos(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.acos(*_args, **kwargs))


def acosd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.acosd(*_args, **kwargs))


def acosh(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.acosh(*_args, **kwargs))


def addAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.addAttr(*_args, **kwargs))


def addDynamic(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.addDynamic(*_args, **kwargs))


def addDynamicAttribute(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.addDynamicAttribute(*_args, **kwargs))


def addExtension(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.addExtension(*_args, **kwargs))


def addIK2BsolverCallbacks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.addIK2BsolverCallbacks(*_args, **kwargs))


def addMetadata(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.addMetadata(*_args, **kwargs))


def addPP(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.addPP(*_args, **kwargs))


def adskAsset(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.adskAsset(*_args, **kwargs))


def adskAssetLibrary(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.adskAssetLibrary(*_args, **kwargs))


def adskAssetList(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.adskAssetList(*_args, **kwargs))


def adskAssetListUI(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.adskAssetListUI(*_args, **kwargs))


def adskRepresentation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.adskRepresentation(*_args, **kwargs))


def adskSceneMetadataCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.adskSceneMetadataCmd(*_args, **kwargs))


def affectedNet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.affectedNet(*_args, **kwargs))


def affects(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.affects(*_args, **kwargs))


def agFormatIn(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.agFormatIn(*_args, **kwargs))


def agFormatOut(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.agFormatOut(*_args, **kwargs))


def aimConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.aimConstraint(*_args, **kwargs))


def air(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.air(*_args, **kwargs))


def aliasAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.aliasAttr(*_args, **kwargs))


def align(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.align(*_args, **kwargs))


def alignCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.alignCtx(*_args, **kwargs))


def alignCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.alignCurve(*_args, **kwargs))


def alignSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.alignSurface(*_args, **kwargs))


def allNodeTypes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.allNodeTypes(*_args, **kwargs))


def ambientLight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ambientLight(*_args, **kwargs))


def angle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.angle(*_args, **kwargs))


def angleBetween(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.angleBetween(*_args, **kwargs))


def animCurveEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.animCurveEditor(*_args, **kwargs))


def animDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.animDisplay(*_args, **kwargs))


def animLayer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.animLayer(*_args, **kwargs))


def animView(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.animView(*_args, **kwargs))


def annotate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.annotate(*_args, **kwargs))


def apexClothingImport(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.apexClothingImport(*_args, **kwargs))


def apexClothingMaterialPresetLoad(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.apexClothingMaterialPresetLoad(*_args, **kwargs))


def apexClothingMaterialPresetSave(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.apexClothingMaterialPresetSave(*_args, **kwargs))


def apexClothingPaintRange(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.apexClothingPaintRange(*_args, **kwargs))


def apexClothingPreview(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.apexClothingPreview(*_args, **kwargs))


def appendListItem(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.appendListItem(*_args, **kwargs))


def applyAttrPattern(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.applyAttrPattern(*_args, **kwargs))


def applyMetadata(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.applyMetadata(*_args, **kwargs))


def applyTake(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.applyTake(*_args, **kwargs))


def arcLenDimContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.arcLenDimContext(*_args, **kwargs))


def arcLengthDimension(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.arcLengthDimension(*_args, **kwargs))


def arclen(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.arclen(*_args, **kwargs))


def arrayMapper(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.arrayMapper(*_args, **kwargs))


def art3dPaintCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.art3dPaintCtx(*_args, **kwargs))


def artAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.artAttr(*_args, **kwargs))


def artAttrCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.artAttrCtx(*_args, **kwargs))


def artAttrPaintVertexCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.artAttrPaintVertexCtx(*_args, **kwargs))


def artAttrSkinPaint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.artAttrSkinPaint(*_args, **kwargs))


def artAttrSkinPaintCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.artAttrSkinPaintCmd(*_args, **kwargs))


def artAttrSkinPaintCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.artAttrSkinPaintCtx(*_args, **kwargs))


def artAttrTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.artAttrTool(*_args, **kwargs))


def artBaseCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.artBaseCtx(*_args, **kwargs))


def artBuildPaintMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.artBuildPaintMenu(*_args, **kwargs))


def artFluidAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.artFluidAttr(*_args, **kwargs))


def artFluidAttrCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.artFluidAttrCtx(*_args, **kwargs))


def artPuttyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.artPuttyCtx(*_args, **kwargs))


def artSelect(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.artSelect(*_args, **kwargs))


def artSelectCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.artSelectCtx(*_args, **kwargs))


def artSetPaint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.artSetPaint(*_args, **kwargs))


def artSetPaintCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.artSetPaintCtx(*_args, **kwargs))


def artUserPaintCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.artUserPaintCtx(*_args, **kwargs))


def arubaNurbsToPoly(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.arubaNurbsToPoly(*_args, **kwargs))


def asin(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.asin(*_args, **kwargs))


def asind(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.asind(*_args, **kwargs))


def asinh(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.asinh(*_args, **kwargs))


def assembly(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.assembly(*_args, **kwargs))


def assignCommand(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.assignCommand(*_args, **kwargs))


def assignInputDevice(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.assignInputDevice(*_args, **kwargs))


def assignViewportFactories(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.assignViewportFactories(*_args, **kwargs))


def atan(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.atan(*_args, **kwargs))


def atan2(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.atan2(*_args, **kwargs))


def atan2d(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.atan2d(*_args, **kwargs))


def atand(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.atand(*_args, **kwargs))


def atanh(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.atanh(*_args, **kwargs))


def attachCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.attachCache(*_args, **kwargs))


def attachCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.attachCurve(*_args, **kwargs))


def attachDeviceAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.attachDeviceAttr(*_args, **kwargs))


def attachFluidCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.attachFluidCache(*_args, **kwargs))


def attachGeometryCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.attachGeometryCache(*_args, **kwargs))


def attachNclothCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.attachNclothCache(*_args, **kwargs))


def attachSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.attachSurface(*_args, **kwargs))


def attrColorSliderGrp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.attrColorSliderGrp(*_args, **kwargs))


def attrCompatibility(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.attrCompatibility(*_args, **kwargs))


def attrControlGrp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.attrControlGrp(*_args, **kwargs))


def attrEnumOptionMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.attrEnumOptionMenu(*_args, **kwargs))


def attrEnumOptionMenuGrp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.attrEnumOptionMenuGrp(*_args, **kwargs))


def attrFieldGrp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.attrFieldGrp(*_args, **kwargs))


def attrFieldSliderGrp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.attrFieldSliderGrp(*_args, **kwargs))


def attrNavigationControlGrp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.attrNavigationControlGrp(*_args, **kwargs))


def attributeInfo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.attributeInfo(*_args, **kwargs))


def attributeMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.attributeMenu(*_args, **kwargs))


def attributeName(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.attributeName(*_args, **kwargs))


def attributeQuery(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.attributeQuery(*_args, **kwargs))


def audioTrack(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.audioTrack(*_args, **kwargs))


def autoKeyframe(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.autoKeyframe(*_args, **kwargs))


def autoPlace(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.autoPlace(*_args, **kwargs))


def autoSave(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.autoSave(*_args, **kwargs))


def bakeClip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.bakeClip(*_args, **kwargs))


def bakeDeformer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.bakeDeformer(*_args, **kwargs))


def bakePartialHistory(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.bakePartialHistory(*_args, **kwargs))


def bakeResults(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.bakeResults(*_args, **kwargs))


def bakeSimulation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.bakeSimulation(*_args, **kwargs))


def baseTemplate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.baseTemplate(*_args, **kwargs))


def baseView(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.baseView(*_args, **kwargs))


def batchRender(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.batchRender(*_args, **kwargs))


def besselj0(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.besselj0(*_args, **kwargs))


def besselj1(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.besselj1(*_args, **kwargs))


def besseljn(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.besseljn(*_args, **kwargs))


def besselyn(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.besselyn(*_args, **kwargs))


def bevel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.bevel(*_args, **kwargs))


def bevelPlus(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.bevelPlus(*_args, **kwargs))


def bezierAnchorPreset(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.bezierAnchorPreset(*_args, **kwargs))


def bezierAnchorState(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.bezierAnchorState(*_args, **kwargs))


def bezierCurveToNurbs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.bezierCurveToNurbs(*_args, **kwargs))


def bezierInfo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.bezierInfo(*_args, **kwargs))


def binMembership(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.binMembership(*_args, **kwargs))


def bindSkin(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.bindSkin(*_args, **kwargs))


def blend(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.blend(*_args, **kwargs))


def blend2(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.blend2(*_args, **kwargs))


def blendCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.blendCtx(*_args, **kwargs))


def blendShape(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.blendShape(*_args, **kwargs))


def blendShapeEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.blendShapeEditor(*_args, **kwargs))


def blendShapePanel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.blendShapePanel(*_args, **kwargs))


def blendTwoAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.blendTwoAttr(*_args, **kwargs))


def blindDataType(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.blindDataType(*_args, **kwargs))


def blocksize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.blocksize(*_args, **kwargs))


def boneLattice(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.boneLattice(*_args, **kwargs))


def boundary(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.boundary(*_args, **kwargs))


def boxDollyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.boxDollyCtx(*_args, **kwargs))


def boxZoomCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.boxZoomCtx(*_args, **kwargs))


def bufferCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.bufferCurve(*_args, **kwargs))


def buildBookmarkMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.buildBookmarkMenu(*_args, **kwargs))


def buildKeyframeMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.buildKeyframeMenu(*_args, **kwargs))


def buildSendToBackburnerDialog(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.buildSendToBackburnerDialog(*_args, **kwargs))


def button(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.button(*_args, **kwargs))


def buttonManip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.buttonManip(*_args, **kwargs))


def cMuscleAbout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cMuscleAbout(*_args, **kwargs))


def cMuscleBindSticky(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cMuscleBindSticky(*_args, **kwargs))


def cMuscleCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cMuscleCache(*_args, **kwargs))


def cMuscleCompIndex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cMuscleCompIndex(*_args, **kwargs))


def cMuscleQuery(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cMuscleQuery(*_args, **kwargs))


def cMuscleRayIntersect(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cMuscleRayIntersect(*_args, **kwargs))


def cMuscleRelaxSetup(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cMuscleRelaxSetup(*_args, **kwargs))


def cMuscleSimulate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cMuscleSimulate(*_args, **kwargs))


def cMuscleSplineBind(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cMuscleSplineBind(*_args, **kwargs))


def cMuscleWeight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cMuscleWeight(*_args, **kwargs))


def cMuscleWeightDefault(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cMuscleWeightDefault(*_args, **kwargs))


def cMuscleWeightMirror(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cMuscleWeightMirror(*_args, **kwargs))


def cMuscleWeightPrune(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cMuscleWeightPrune(*_args, **kwargs))


def cMuscleWeightSave(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cMuscleWeightSave(*_args, **kwargs))


def cacheAppend(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cacheAppend(*_args, **kwargs))


def cacheAppendOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cacheAppendOpt(*_args, **kwargs))


def cacheFile(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cacheFile(*_args, **kwargs))


def cacheFileCombine(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cacheFileCombine(*_args, **kwargs))


def cacheFileMerge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cacheFileMerge(*_args, **kwargs))


def cacheFileTrack(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cacheFileTrack(*_args, **kwargs))


def caddyManip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.caddyManip(*_args, **kwargs))


def callbacks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.callbacks(*_args, **kwargs))


def camera(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.camera(*_args, **kwargs))


def cameraSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cameraSet(*_args, **kwargs))


def cameraView(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cameraView(*_args, **kwargs))


def canCreateCaddyManip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.canCreateCaddyManip(*_args, **kwargs))


def canCreateManip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.canCreateManip(*_args, **kwargs))


def canvas(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.canvas(*_args, **kwargs))


def ceil(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ceil(*_args, **kwargs))


def changeSubdivComponentDisplayLevel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.changeSubdivComponentDisplayLevel(*_args, **kwargs))


def changeSubdivRegion(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.changeSubdivRegion(*_args, **kwargs))


def channelBox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.channelBox(*_args, **kwargs))


def character(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.character(*_args, **kwargs))


def characterMap(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.characterMap(*_args, **kwargs))


def characterizationToolUICmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.characterizationToolUICmd(*_args, **kwargs))


def characterize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.characterize(*_args, **kwargs))


def chdir(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.chdir(*_args, **kwargs))


def checkBox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.checkBox(*_args, **kwargs))


def checkBoxGrp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.checkBoxGrp(*_args, **kwargs))


def checkDefaultRenderGlobals(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.checkDefaultRenderGlobals(*_args, **kwargs))


def choice(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.choice(*_args, **kwargs))


def circle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.circle(*_args, **kwargs))


def circularFillet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.circularFillet(*_args, **kwargs))


def clamp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.clamp(*_args, **kwargs))


def clear(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.clear(*_args, **kwargs))


def clearCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.clearCache(*_args, **kwargs))


def clearDynStartState(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.clearDynStartState(*_args, **kwargs))


def clearNClothStartState(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.clearNClothStartState(*_args, **kwargs))


def clearShear(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.clearShear(*_args, **kwargs))


def clip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.clip(*_args, **kwargs))


def clipEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.clipEditor(*_args, **kwargs))


def clipEditorCurrentTimeCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.clipEditorCurrentTimeCtx(*_args, **kwargs))


def clipMatching(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.clipMatching(*_args, **kwargs))


def clipSchedule(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.clipSchedule(*_args, **kwargs))


def clipSchedulerOutliner(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.clipSchedulerOutliner(*_args, **kwargs))


def closeCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.closeCurve(*_args, **kwargs))


def closeSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.closeSurface(*_args, **kwargs))


def cluster(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cluster(*_args, **kwargs))


def cmdFileOutput(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cmdFileOutput(*_args, **kwargs))


def cmdScrollFieldExecuter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cmdScrollFieldExecuter(*_args, **kwargs))


def cmdScrollFieldReporter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cmdScrollFieldReporter(*_args, **kwargs))


def cmdShell(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cmdShell(*_args, **kwargs))


def cmdpipe(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cmdpipe(*_args, **kwargs))


def coarsenSubdivSelectionList(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.coarsenSubdivSelectionList(*_args, **kwargs))


def collision(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.collision(*_args, **kwargs))


def color(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.color(*_args, **kwargs))


def colorAtPoint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.colorAtPoint(*_args, **kwargs))


def colorEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.colorEditor(*_args, **kwargs))


def colorIndex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.colorIndex(*_args, **kwargs))


def colorIndexSliderGrp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.colorIndexSliderGrp(*_args, **kwargs))


def colorInputWidgetGrp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.colorInputWidgetGrp(*_args, **kwargs))


def colorManagementCatalog(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.colorManagementCatalog(*_args, **kwargs))


def colorManagementConvert(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.colorManagementConvert(*_args, **kwargs))


def colorManagementFileRules(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.colorManagementFileRules(*_args, **kwargs))


def colorManagementPrefs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.colorManagementPrefs(*_args, **kwargs))


def colorSliderButtonGrp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.colorSliderButtonGrp(*_args, **kwargs))


def colorSliderGrp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.colorSliderGrp(*_args, **kwargs))


def columnLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.columnLayout(*_args, **kwargs))


def combinationShape(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.combinationShape(*_args, **kwargs))


def commandEcho(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.commandEcho(*_args, **kwargs))


def commandLine(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.commandLine(*_args, **kwargs))


def commandLogging(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.commandLogging(*_args, **kwargs))


def commandPort(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.commandPort(*_args, **kwargs))


def componentBox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.componentBox(*_args, **kwargs))


def componentEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.componentEditor(*_args, **kwargs))


def computePhysicsShapeFromMeshCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.computePhysicsShapeFromMeshCmd(*_args, **kwargs))


def condition(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.condition(*_args, **kwargs))


def cone(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cone(*_args, **kwargs))


def confirmDialog(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.confirmDialog(*_args, **kwargs))


def connectAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.connectAttr(*_args, **kwargs))


def connectControl(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.connectControl(*_args, **kwargs))


def connectDynamic(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.connectDynamic(*_args, **kwargs))


def connectJoint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.connectJoint(*_args, **kwargs))


def connectionInfo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.connectionInfo(*_args, **kwargs))


def constrain(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.constrain(*_args, **kwargs))


def constrainValue(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.constrainValue(*_args, **kwargs))


def constructionHistory(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.constructionHistory(*_args, **kwargs))


def container(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.container(*_args, **kwargs))


def containerBind(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.containerBind(*_args, **kwargs))


def containerProxy(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.containerProxy(*_args, **kwargs))


def containerPublish(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.containerPublish(*_args, **kwargs))


def containerTemplate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.containerTemplate(*_args, **kwargs))


def containerView(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.containerView(*_args, **kwargs))


def contentBrowser(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.contentBrowser(*_args, **kwargs))


def contextInfo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.contextInfo(*_args, **kwargs))


def control(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.control(*_args, **kwargs))


def controller(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.controller(*_args, **kwargs))


def convertBtwConvexHullAndCapsuleCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.convertBtwConvexHullAndCapsuleCmd(*_args, **kwargs))


def convertIffToPsd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.convertIffToPsd(*_args, **kwargs))


def convertSolidTx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.convertSolidTx(*_args, **kwargs))


def convertTessellation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.convertTessellation(*_args, **kwargs))


def convertUnit(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.convertUnit(*_args, **kwargs))


def copyAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.copyAttr(*_args, **kwargs))


def copyDeformerWeights(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.copyDeformerWeights(*_args, **kwargs))


def copyFlexor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.copyFlexor(*_args, **kwargs))


def copyKey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.copyKey(*_args, **kwargs))


def copyNode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.copyNode(*_args, **kwargs))


def copySkinWeights(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.copySkinWeights(*_args, **kwargs))


def cos(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cos(*_args, **kwargs))


def cosd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cosd(*_args, **kwargs))


def cosh(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cosh(*_args, **kwargs))


def crashInfo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.crashInfo(*_args, **kwargs))


def crashInfoCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.crashInfoCmd(*_args, **kwargs))


def createAttrPatterns(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createAttrPatterns(*_args, **kwargs))


def createCurveWarp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createCurveWarp(*_args, **kwargs))


def createDisplayLayer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createDisplayLayer(*_args, **kwargs))


def createEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createEditor(*_args, **kwargs))


def createLayeredPsdFile(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createLayeredPsdFile(*_args, **kwargs))


def createNode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createNode(*_args, **kwargs))


def createNurbsCircleCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createNurbsCircleCtx(*_args, **kwargs))


def createNurbsConeCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createNurbsConeCtx(*_args, **kwargs))


def createNurbsCubeCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createNurbsCubeCtx(*_args, **kwargs))


def createNurbsCylinderCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createNurbsCylinderCtx(*_args, **kwargs))


def createNurbsPlaneCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createNurbsPlaneCtx(*_args, **kwargs))


def createNurbsSphereCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createNurbsSphereCtx(*_args, **kwargs))


def createNurbsSquareCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createNurbsSquareCtx(*_args, **kwargs))


def createNurbsTorusCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createNurbsTorusCtx(*_args, **kwargs))


def createPolyConeCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createPolyConeCtx(*_args, **kwargs))


def createPolyCubeCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createPolyCubeCtx(*_args, **kwargs))


def createPolyCylinderCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createPolyCylinderCtx(*_args, **kwargs))


def createPolyHelixCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createPolyHelixCtx(*_args, **kwargs))


def createPolyPipeCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createPolyPipeCtx(*_args, **kwargs))


def createPolyPlaneCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createPolyPlaneCtx(*_args, **kwargs))


def createPolyPlatonicSolidCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createPolyPlatonicSolidCtx(*_args, **kwargs))


def createPolyPrismCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createPolyPrismCtx(*_args, **kwargs))


def createPolyPyramidCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createPolyPyramidCtx(*_args, **kwargs))


def createPolySoccerBallCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createPolySoccerBallCtx(*_args, **kwargs))


def createPolySphereCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createPolySphereCtx(*_args, **kwargs))


def createPolyTorusCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createPolyTorusCtx(*_args, **kwargs))


def createRenderLayer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createRenderLayer(*_args, **kwargs))


def createSubdivRegion(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.createSubdivRegion(*_args, **kwargs))


def cross(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cross(*_args, **kwargs))


def ctxAbort(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ctxAbort(*_args, **kwargs))


def ctxCompletion(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ctxCompletion(*_args, **kwargs))


def ctxData(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ctxData(*_args, **kwargs))


def ctxEditMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ctxEditMode(*_args, **kwargs))


def ctxTraverse(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ctxTraverse(*_args, **kwargs))


def currentCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.currentCtx(*_args, **kwargs))


def currentTime(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.currentTime(*_args, **kwargs))


def currentTimeCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.currentTimeCtx(*_args, **kwargs))


def currentUnit(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.currentUnit(*_args, **kwargs))


def curve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.curve(*_args, **kwargs))


def curveAddPtCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.curveAddPtCtx(*_args, **kwargs))


def curveBezierCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.curveBezierCtx(*_args, **kwargs))


def curveCVCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.curveCVCtx(*_args, **kwargs))


def curveEPCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.curveEPCtx(*_args, **kwargs))


def curveEditorCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.curveEditorCtx(*_args, **kwargs))


def curveIntersect(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.curveIntersect(*_args, **kwargs))


def curveMoveEPCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.curveMoveEPCtx(*_args, **kwargs))


def curveOnSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.curveOnSurface(*_args, **kwargs))


def curveRGBColor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.curveRGBColor(*_args, **kwargs))


def curveSketchCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.curveSketchCtx(*_args, **kwargs))


def customerInvolvementProgram(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.customerInvolvementProgram(*_args, **kwargs))


def cutKey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cutKey(*_args, **kwargs))


def cycleCheck(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cycleCheck(*_args, **kwargs))


def cylinder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.cylinder(*_args, **kwargs))


def dR_DoCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_DoCmd(*_args, **kwargs))


def dR_activeHandleX(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_activeHandleX(*_args, **kwargs))


def dR_activeHandleXY(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_activeHandleXY(*_args, **kwargs))


def dR_activeHandleXYZ(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_activeHandleXYZ(*_args, **kwargs))


def dR_activeHandleXZ(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_activeHandleXZ(*_args, **kwargs))


def dR_activeHandleY(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_activeHandleY(*_args, **kwargs))


def dR_activeHandleYZ(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_activeHandleYZ(*_args, **kwargs))


def dR_activeHandleZ(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_activeHandleZ(*_args, **kwargs))


def dR_alwaysOnTopTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_alwaysOnTopTGL(*_args, **kwargs))


def dR_autoWeldTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_autoWeldTGL(*_args, **kwargs))


def dR_bevelPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_bevelPress(*_args, **kwargs))


def dR_bevelRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_bevelRelease(*_args, **kwargs))


def dR_bevelTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_bevelTool(*_args, **kwargs))


def dR_bridgePress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_bridgePress(*_args, **kwargs))


def dR_bridgeRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_bridgeRelease(*_args, **kwargs))


def dR_bridgeTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_bridgeTool(*_args, **kwargs))


def dR_cameraToPoly(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_cameraToPoly(*_args, **kwargs))


def dR_conform(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_conform(*_args, **kwargs))


def dR_connectPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_connectPress(*_args, **kwargs))


def dR_connectRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_connectRelease(*_args, **kwargs))


def dR_connectTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_connectTool(*_args, **kwargs))


def dR_contextChanged(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_contextChanged(*_args, **kwargs))


def dR_convertSelectionToEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_convertSelectionToEdge(*_args, **kwargs))


def dR_convertSelectionToFace(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_convertSelectionToFace(*_args, **kwargs))


def dR_convertSelectionToUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_convertSelectionToUV(*_args, **kwargs))


def dR_convertSelectionToVertex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_convertSelectionToVertex(*_args, **kwargs))


def dR_coordSpaceCustom(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_coordSpaceCustom(*_args, **kwargs))


def dR_coordSpaceLocal(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_coordSpaceLocal(*_args, **kwargs))


def dR_coordSpaceObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_coordSpaceObject(*_args, **kwargs))


def dR_coordSpaceWorld(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_coordSpaceWorld(*_args, **kwargs))


def dR_createCameraFromView(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_createCameraFromView(*_args, **kwargs))


def dR_curveSnapPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_curveSnapPress(*_args, **kwargs))


def dR_curveSnapRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_curveSnapRelease(*_args, **kwargs))


def dR_customPivotTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_customPivotTool(*_args, **kwargs))


def dR_customPivotToolPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_customPivotToolPress(*_args, **kwargs))


def dR_customPivotToolRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_customPivotToolRelease(*_args, **kwargs))


def dR_cycleCustomCameras(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_cycleCustomCameras(*_args, **kwargs))


def dR_decreaseManipSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_decreaseManipSize(*_args, **kwargs))


def dR_defLightTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_defLightTGL(*_args, **kwargs))


def dR_disableTexturesTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_disableTexturesTGL(*_args, **kwargs))


def dR_edgedFacesTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_edgedFacesTGL(*_args, **kwargs))


def dR_extrudeBevelPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_extrudeBevelPress(*_args, **kwargs))


def dR_extrudeBevelRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_extrudeBevelRelease(*_args, **kwargs))


def dR_extrudePress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_extrudePress(*_args, **kwargs))


def dR_extrudeRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_extrudeRelease(*_args, **kwargs))


def dR_extrudeTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_extrudeTool(*_args, **kwargs))


def dR_graphEditorTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_graphEditorTGL(*_args, **kwargs))


def dR_gridAllTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_gridAllTGL(*_args, **kwargs))


def dR_gridSnapPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_gridSnapPress(*_args, **kwargs))


def dR_gridSnapRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_gridSnapRelease(*_args, **kwargs))


def dR_hypergraphTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_hypergraphTGL(*_args, **kwargs))


def dR_hypershadeTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_hypershadeTGL(*_args, **kwargs))


def dR_increaseManipSize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_increaseManipSize(*_args, **kwargs))


def dR_loadRecentFile1(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_loadRecentFile1(*_args, **kwargs))


def dR_loadRecentFile2(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_loadRecentFile2(*_args, **kwargs))


def dR_loadRecentFile3(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_loadRecentFile3(*_args, **kwargs))


def dR_loadRecentFile4(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_loadRecentFile4(*_args, **kwargs))


def dR_lockSelTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_lockSelTGL(*_args, **kwargs))


def dR_meshAlphaTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_meshAlphaTGL(*_args, **kwargs))


def dR_meshColorOverrideTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_meshColorOverrideTGL(*_args, **kwargs))


def dR_meshOffsetTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_meshOffsetTGL(*_args, **kwargs))


def dR_modeEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_modeEdge(*_args, **kwargs))


def dR_modeMulti(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_modeMulti(*_args, **kwargs))


def dR_modeObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_modeObject(*_args, **kwargs))


def dR_modePoly(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_modePoly(*_args, **kwargs))


def dR_modeUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_modeUV(*_args, **kwargs))


def dR_modeVert(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_modeVert(*_args, **kwargs))


def dR_movePress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_movePress(*_args, **kwargs))


def dR_moveRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_moveRelease(*_args, **kwargs))


def dR_moveTweakTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_moveTweakTool(*_args, **kwargs))


def dR_mtkPanelTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_mtkPanelTGL(*_args, **kwargs))


def dR_mtkToolTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_mtkToolTGL(*_args, **kwargs))


def dR_multiCutPointCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_multiCutPointCmd(*_args, **kwargs))


def dR_multiCutPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_multiCutPress(*_args, **kwargs))


def dR_multiCutRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_multiCutRelease(*_args, **kwargs))


def dR_multiCutSlicePointCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_multiCutSlicePointCmd(*_args, **kwargs))


def dR_multiCutTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_multiCutTool(*_args, **kwargs))


def dR_nexCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_nexCmd(*_args, **kwargs))


def dR_nexTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_nexTool(*_args, **kwargs))


def dR_objectBackfaceTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_objectBackfaceTGL(*_args, **kwargs))


def dR_objectEdgesOnlyTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_objectEdgesOnlyTGL(*_args, **kwargs))


def dR_objectHideTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_objectHideTGL(*_args, **kwargs))


def dR_objectTemplateTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_objectTemplateTGL(*_args, **kwargs))


def dR_objectXrayTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_objectXrayTGL(*_args, **kwargs))


def dR_outlinerTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_outlinerTGL(*_args, **kwargs))


def dR_overlayAppendMeshTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_overlayAppendMeshTGL(*_args, **kwargs))


def dR_paintPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_paintPress(*_args, **kwargs))


def dR_paintRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_paintRelease(*_args, **kwargs))


def dR_pointSnapPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_pointSnapPress(*_args, **kwargs))


def dR_pointSnapRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_pointSnapRelease(*_args, **kwargs))


def dR_preferencesTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_preferencesTGL(*_args, **kwargs))


def dR_quadDrawClearDots(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_quadDrawClearDots(*_args, **kwargs))


def dR_quadDrawPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_quadDrawPress(*_args, **kwargs))


def dR_quadDrawRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_quadDrawRelease(*_args, **kwargs))


def dR_quadDrawTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_quadDrawTool(*_args, **kwargs))


def dR_renderGlobalsTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_renderGlobalsTGL(*_args, **kwargs))


def dR_renderLastTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_renderLastTGL(*_args, **kwargs))


def dR_rotatePress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_rotatePress(*_args, **kwargs))


def dR_rotateRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_rotateRelease(*_args, **kwargs))


def dR_rotateTweakTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_rotateTweakTool(*_args, **kwargs))


def dR_safeFrameTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_safeFrameTGL(*_args, **kwargs))


def dR_scalePress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_scalePress(*_args, **kwargs))


def dR_scaleRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_scaleRelease(*_args, **kwargs))


def dR_scaleTweakTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_scaleTweakTool(*_args, **kwargs))


def dR_selConstraintAngle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_selConstraintAngle(*_args, **kwargs))


def dR_selConstraintBorder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_selConstraintBorder(*_args, **kwargs))


def dR_selConstraintEdgeLoop(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_selConstraintEdgeLoop(*_args, **kwargs))


def dR_selConstraintEdgeRing(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_selConstraintEdgeRing(*_args, **kwargs))


def dR_selConstraintElement(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_selConstraintElement(*_args, **kwargs))


def dR_selConstraintOff(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_selConstraintOff(*_args, **kwargs))


def dR_selConstraintUVEdgeLoop(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_selConstraintUVEdgeLoop(*_args, **kwargs))


def dR_selectAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_selectAll(*_args, **kwargs))


def dR_selectInvert(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_selectInvert(*_args, **kwargs))


def dR_selectModeDisableTweakMarquee(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_selectModeDisableTweakMarquee(*_args, **kwargs))


def dR_selectModeHybrid(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_selectModeHybrid(*_args, **kwargs))


def dR_selectModeMarquee(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_selectModeMarquee(*_args, **kwargs))


def dR_selectModeRaycast(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_selectModeRaycast(*_args, **kwargs))


def dR_selectModeTweakMarquee(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_selectModeTweakMarquee(*_args, **kwargs))


def dR_selectPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_selectPress(*_args, **kwargs))


def dR_selectRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_selectRelease(*_args, **kwargs))


def dR_selectSimilar(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_selectSimilar(*_args, **kwargs))


def dR_selectTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_selectTool(*_args, **kwargs))


def dR_setExtendBorder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_setExtendBorder(*_args, **kwargs))


def dR_setExtendEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_setExtendEdge(*_args, **kwargs))


def dR_setExtendLoop(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_setExtendLoop(*_args, **kwargs))


def dR_setRelaxAffectsAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_setRelaxAffectsAll(*_args, **kwargs))


def dR_setRelaxAffectsAuto(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_setRelaxAffectsAuto(*_args, **kwargs))


def dR_setRelaxAffectsBorders(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_setRelaxAffectsBorders(*_args, **kwargs))


def dR_setRelaxAffectsInterior(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_setRelaxAffectsInterior(*_args, **kwargs))


def dR_showAbout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_showAbout(*_args, **kwargs))


def dR_showHelp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_showHelp(*_args, **kwargs))


def dR_showOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_showOptions(*_args, **kwargs))


def dR_slideEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_slideEdge(*_args, **kwargs))


def dR_slideOff(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_slideOff(*_args, **kwargs))


def dR_slideSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_slideSurface(*_args, **kwargs))


def dR_snapToBackfacesTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_snapToBackfacesTGL(*_args, **kwargs))


def dR_softSelDistanceTypeGlobal(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_softSelDistanceTypeGlobal(*_args, **kwargs))


def dR_softSelDistanceTypeObject(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_softSelDistanceTypeObject(*_args, **kwargs))


def dR_softSelDistanceTypeSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_softSelDistanceTypeSurface(*_args, **kwargs))


def dR_softSelDistanceTypeVolume(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_softSelDistanceTypeVolume(*_args, **kwargs))


def dR_softSelStickyPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_softSelStickyPress(*_args, **kwargs))


def dR_softSelStickyRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_softSelStickyRelease(*_args, **kwargs))


def dR_softSelToolTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_softSelToolTGL(*_args, **kwargs))


def dR_symmetrize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_symmetrize(*_args, **kwargs))


def dR_symmetryFlip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_symmetryFlip(*_args, **kwargs))


def dR_symmetryTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_symmetryTGL(*_args, **kwargs))


def dR_targetWeldPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_targetWeldPress(*_args, **kwargs))


def dR_targetWeldRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_targetWeldRelease(*_args, **kwargs))


def dR_targetWeldTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_targetWeldTool(*_args, **kwargs))


def dR_testCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_testCmd(*_args, **kwargs))


def dR_timeConfigTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_timeConfigTGL(*_args, **kwargs))


def dR_tweakPress(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_tweakPress(*_args, **kwargs))


def dR_tweakRelease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_tweakRelease(*_args, **kwargs))


def dR_vertLockSelected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_vertLockSelected(*_args, **kwargs))


def dR_vertSelectLocked(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_vertSelectLocked(*_args, **kwargs))


def dR_vertUnlockAll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_vertUnlockAll(*_args, **kwargs))


def dR_viewBack(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_viewBack(*_args, **kwargs))


def dR_viewBottom(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_viewBottom(*_args, **kwargs))


def dR_viewFront(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_viewFront(*_args, **kwargs))


def dR_viewGridTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_viewGridTGL(*_args, **kwargs))


def dR_viewJointsTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_viewJointsTGL(*_args, **kwargs))


def dR_viewLeft(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_viewLeft(*_args, **kwargs))


def dR_viewLightsTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_viewLightsTGL(*_args, **kwargs))


def dR_viewPersp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_viewPersp(*_args, **kwargs))


def dR_viewRight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_viewRight(*_args, **kwargs))


def dR_viewTop(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_viewTop(*_args, **kwargs))


def dR_viewXrayTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_viewXrayTGL(*_args, **kwargs))


def dR_visorTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_visorTGL(*_args, **kwargs))


def dR_wireframeSmoothTGL(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dR_wireframeSmoothTGL(*_args, **kwargs))


def dagCommandWrapper(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dagCommandWrapper(*_args, **kwargs))


def dagObjectCompare(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dagObjectCompare(*_args, **kwargs))


def dagObjectHit(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dagObjectHit(*_args, **kwargs))


def dagPose(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dagPose(*_args, **kwargs))


def dataStructure(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dataStructure(*_args, **kwargs))


def date(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.date(*_args, **kwargs))


def dbcount(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dbcount(*_args, **kwargs))


def dbfootprint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dbfootprint(*_args, **kwargs))


def dbmessage(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dbmessage(*_args, **kwargs))


def dbpeek(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dbpeek(*_args, **kwargs))


def dbtrace(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dbtrace(*_args, **kwargs))


def debug(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.debug(*_args, **kwargs))


def debugNamespace(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.debugNamespace(*_args, **kwargs))


def debugVar(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.debugVar(*_args, **kwargs))


def defaultLightListCheckBox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.defaultLightListCheckBox(*_args, **kwargs))


def defaultNavigation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.defaultNavigation(*_args, **kwargs))


def defineDataServer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.defineDataServer(*_args, **kwargs))


def defineVirtualDevice(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.defineVirtualDevice(*_args, **kwargs))


def deformer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.deformer(*_args, **kwargs))


def deformerEvaluator(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.deformerEvaluator(*_args, **kwargs))


def deformerWeights(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.deformerWeights(*_args, **kwargs))


def deg_to_rad(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.deg_to_rad(*_args, **kwargs))


def delete(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.delete(*_args, **kwargs))


def deleteAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.deleteAttr(*_args, **kwargs))


def deleteAttrPattern(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.deleteAttrPattern(*_args, **kwargs))


def deleteExtension(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.deleteExtension(*_args, **kwargs))


def deleteGeometryCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.deleteGeometryCache(*_args, **kwargs))


def deleteHistoryAheadOfGeomCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.deleteHistoryAheadOfGeomCache(*_args, **kwargs))


def deleteNclothCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.deleteNclothCache(*_args, **kwargs))


def deleteUI(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.deleteUI(*_args, **kwargs))


def delrandstr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.delrandstr(*_args, **kwargs))


def deltaMush(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.deltaMush(*_args, **kwargs))


def detachCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.detachCurve(*_args, **kwargs))


def detachDeviceAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.detachDeviceAttr(*_args, **kwargs))


def detachSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.detachSurface(*_args, **kwargs))


def deviceEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.deviceEditor(*_args, **kwargs))


def deviceManager(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.deviceManager(*_args, **kwargs))


def devicePanel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.devicePanel(*_args, **kwargs))


def dgControl(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dgControl(*_args, **kwargs))


def dgInfo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dgInfo(*_args, **kwargs))


def dgPerformance(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dgPerformance(*_args, **kwargs))


def dgcontrol(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dgcontrol(*_args, **kwargs))


def dgdebug(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dgdebug(*_args, **kwargs))


def dgdirty(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dgdirty(*_args, **kwargs))


def dgeval(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dgeval(*_args, **kwargs))


def dgfilter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dgfilter(*_args, **kwargs))


def dgmodified(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dgmodified(*_args, **kwargs))


def dgstats(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dgstats(*_args, **kwargs))


def dgtimer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dgtimer(*_args, **kwargs))


def dimWhen(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dimWhen(*_args, **kwargs))


def directConnectPath(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.directConnectPath(*_args, **kwargs))


def directKeyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.directKeyCtx(*_args, **kwargs))


def directionalLight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.directionalLight(*_args, **kwargs))


def dirmap(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dirmap(*_args, **kwargs))


def disable(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.disable(*_args, **kwargs))


def disableIncorrectNameWarning(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.disableIncorrectNameWarning(*_args, **kwargs))


def disconnectAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.disconnectAttr(*_args, **kwargs))


def disconnectJoint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.disconnectJoint(*_args, **kwargs))


def diskCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.diskCache(*_args, **kwargs))


def displacementToPoly(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.displacementToPoly(*_args, **kwargs))


def displayAffected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.displayAffected(*_args, **kwargs))


def displayColor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.displayColor(*_args, **kwargs))


def displayCull(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.displayCull(*_args, **kwargs))


def displayLevelOfDetail(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.displayLevelOfDetail(*_args, **kwargs))


def displayPref(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.displayPref(*_args, **kwargs))


def displayRGBColor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.displayRGBColor(*_args, **kwargs))


def displaySmoothness(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.displaySmoothness(*_args, **kwargs))


def displayStats(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.displayStats(*_args, **kwargs))


def displayString(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.displayString(*_args, **kwargs))


def displaySurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.displaySurface(*_args, **kwargs))


def distanceDimContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.distanceDimContext(*_args, **kwargs))


def distanceDimension(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.distanceDimension(*_args, **kwargs))


def dnoise(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dnoise(*_args, **kwargs))


def doBlur(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.doBlur(*_args, **kwargs))


def dockControl(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dockControl(*_args, **kwargs))


def dolly(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dolly(*_args, **kwargs))


def dollyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dollyCtx(*_args, **kwargs))


def dopeSheetEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dopeSheetEditor(*_args, **kwargs))


def dot(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dot(*_args, **kwargs))


def doubleProfileBirailSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.doubleProfileBirailSurface(*_args, **kwargs))


def dpBirailCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dpBirailCtx(*_args, **kwargs))


def drag(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.drag(*_args, **kwargs))


def dragAttrContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dragAttrContext(*_args, **kwargs))


def draggerContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.draggerContext(*_args, **kwargs))


def drawExtrudeFacetCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.drawExtrudeFacetCtx(*_args, **kwargs))


def dropoffLocator(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dropoffLocator(*_args, **kwargs))


def duplicate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.duplicate(*_args, **kwargs))


def duplicateCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.duplicateCurve(*_args, **kwargs))


def duplicateSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.duplicateSurface(*_args, **kwargs))


def dx11Shader(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dx11Shader(*_args, **kwargs))


def dynCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dynCache(*_args, **kwargs))


def dynControl(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dynControl(*_args, **kwargs))


def dynExport(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dynExport(*_args, **kwargs))


def dynExpression(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dynExpression(*_args, **kwargs))


def dynGlobals(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dynGlobals(*_args, **kwargs))


def dynPaintCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dynPaintCtx(*_args, **kwargs))


def dynPaintEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dynPaintEditor(*_args, **kwargs))


def dynParticleCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dynParticleCtx(*_args, **kwargs))


def dynPref(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dynPref(*_args, **kwargs))


def dynSelectCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dynSelectCtx(*_args, **kwargs))


def dynTestData(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dynTestData(*_args, **kwargs))


def dynWireCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dynWireCtx(*_args, **kwargs))


def dynamicConstraintRemove(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dynamicConstraintRemove(*_args, **kwargs))


def dynamicLoad(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.dynamicLoad(*_args, **kwargs))


def editDisplayLayerGlobals(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.editDisplayLayerGlobals(*_args, **kwargs))


def editDisplayLayerMembers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.editDisplayLayerMembers(*_args, **kwargs))


def editImportedStatus(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.editImportedStatus(*_args, **kwargs))


def editMetadata(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.editMetadata(*_args, **kwargs))


def editRenderLayerAdjustment(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.editRenderLayerAdjustment(*_args, **kwargs))


def editRenderLayerGlobals(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.editRenderLayerGlobals(*_args, **kwargs))


def editRenderLayerMembers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.editRenderLayerMembers(*_args, **kwargs))


def editor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.editor(*_args, **kwargs))


def editorTemplate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.editorTemplate(*_args, **kwargs))


def effector(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.effector(*_args, **kwargs))


def emit(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.emit(*_args, **kwargs))


def emitter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.emitter(*_args, **kwargs))


def enableDevice(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.enableDevice(*_args, **kwargs))


def encodeString(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.encodeString(*_args, **kwargs))


def env(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.env(*_args, **kwargs))


def erf(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.erf(*_args, **kwargs))


def erfc(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.erfc(*_args, **kwargs))


def error(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.error(*_args, **kwargs))


def eval(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.eval(*_args, **kwargs))


def evalContinue(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.evalContinue(*_args, **kwargs))


def evalDeferred(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.evalDeferred(*_args, **kwargs))


def evalEcho(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.evalEcho(*_args, **kwargs))


def evalNoSelectNotify(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.evalNoSelectNotify(*_args, **kwargs))


def evaluationManager(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.evaluationManager(*_args, **kwargs))


def evaluator(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.evaluator(*_args, **kwargs))


def event(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.event(*_args, **kwargs))


def exactWorldBoundingBox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.exactWorldBoundingBox(*_args, **kwargs))


def exclusiveLightCheckBox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.exclusiveLightCheckBox(*_args, **kwargs))


def exists(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.exists(*_args, **kwargs))


def exp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.exp(*_args, **kwargs))


def expm1(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.expm1(*_args, **kwargs))


def exportEdits(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.exportEdits(*_args, **kwargs))


def expression(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.expression(*_args, **kwargs))


def expressionEditorListen(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.expressionEditorListen(*_args, **kwargs))


def extendCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.extendCurve(*_args, **kwargs))


def extendFluid(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.extendFluid(*_args, **kwargs))


def extendSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.extendSurface(*_args, **kwargs))


def extrude(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.extrude(*_args, **kwargs))


def falloffCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.falloffCurve(*_args, **kwargs))


def falloffCurveAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.falloffCurveAttr(*_args, **kwargs))


def fcheck(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fcheck(*_args, **kwargs))


def fclose(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fclose(*_args, **kwargs))


def feof(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.feof(*_args, **kwargs))


def fflush(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fflush(*_args, **kwargs))


def fgetline(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fgetline(*_args, **kwargs))


def fgetword(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fgetword(*_args, **kwargs))


def file(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.file(*_args, **kwargs))


def fileBrowserDialog(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fileBrowserDialog(*_args, **kwargs))


def fileDialog(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fileDialog(*_args, **kwargs))


def fileDialog2(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fileDialog2(*_args, **kwargs))


def fileInfo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fileInfo(*_args, **kwargs))


def filePathEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.filePathEditor(*_args, **kwargs))


def filetest(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.filetest(*_args, **kwargs))


def filletCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.filletCurve(*_args, **kwargs))


def filter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.filter(*_args, **kwargs))


def filterCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.filterCurve(*_args, **kwargs))


def filterExpand(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.filterExpand(*_args, **kwargs))


def findDeformers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.findDeformers(*_args, **kwargs))


def findKeyframe(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.findKeyframe(*_args, **kwargs))


def findType(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.findType(*_args, **kwargs))


def fitBspline(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fitBspline(*_args, **kwargs))


def flagTest(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.flagTest(*_args, **kwargs))


def flexor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.flexor(*_args, **kwargs))


def floatField(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.floatField(*_args, **kwargs))


def floatFieldGrp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.floatFieldGrp(*_args, **kwargs))


def floatScrollBar(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.floatScrollBar(*_args, **kwargs))


def floatSlider(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.floatSlider(*_args, **kwargs))


def floatSlider2(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.floatSlider2(*_args, **kwargs))


def floatSliderButtonGrp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.floatSliderButtonGrp(*_args, **kwargs))


def floatSliderGrp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.floatSliderGrp(*_args, **kwargs))


def floor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.floor(*_args, **kwargs))


def flow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.flow(*_args, **kwargs))


def flowLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.flowLayout(*_args, **kwargs))


def fluidAppend(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fluidAppend(*_args, **kwargs))


def fluidAppendOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fluidAppendOpt(*_args, **kwargs))


def fluidCacheInfo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fluidCacheInfo(*_args, **kwargs))


def fluidDeleteCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fluidDeleteCache(*_args, **kwargs))


def fluidDeleteCacheFrames(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fluidDeleteCacheFrames(*_args, **kwargs))


def fluidDeleteCacheFramesOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fluidDeleteCacheFramesOpt(*_args, **kwargs))


def fluidDeleteCacheOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fluidDeleteCacheOpt(*_args, **kwargs))


def fluidEmitter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fluidEmitter(*_args, **kwargs))


def fluidMergeCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fluidMergeCache(*_args, **kwargs))


def fluidMergeCacheOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fluidMergeCacheOpt(*_args, **kwargs))


def fluidReplaceCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fluidReplaceCache(*_args, **kwargs))


def fluidReplaceCacheOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fluidReplaceCacheOpt(*_args, **kwargs))


def fluidReplaceFrames(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fluidReplaceFrames(*_args, **kwargs))


def fluidReplaceFramesOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fluidReplaceFramesOpt(*_args, **kwargs))


def fluidVoxelInfo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fluidVoxelInfo(*_args, **kwargs))


def flushIdleQueue(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.flushIdleQueue(*_args, **kwargs))


def flushThumbnailCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.flushThumbnailCache(*_args, **kwargs))


def flushUndo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.flushUndo(*_args, **kwargs))


def fmod(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fmod(*_args, **kwargs))


def fontAttributes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fontAttributes(*_args, **kwargs))


def fontDialog(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fontDialog(*_args, **kwargs))


def fopen(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fopen(*_args, **kwargs))


def formLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.formLayout(*_args, **kwargs))


def format(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.format(*_args, **kwargs))


def fprint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fprint(*_args, **kwargs))


def frameBufferName(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.frameBufferName(*_args, **kwargs))


def frameLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.frameLayout(*_args, **kwargs))


def fread(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fread(*_args, **kwargs))


def freadAllLines(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.freadAllLines(*_args, **kwargs))


def freadAllText(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.freadAllText(*_args, **kwargs))


def freadint64(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.freadint64(*_args, **kwargs))


def freeFormFillet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.freeFormFillet(*_args, **kwargs))


def freezeOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.freezeOptions(*_args, **kwargs))


def frewind(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.frewind(*_args, **kwargs))


def fwrite(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fwrite(*_args, **kwargs))


def fwriteAllLines(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fwriteAllLines(*_args, **kwargs))


def fwriteAllText(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fwriteAllText(*_args, **kwargs))


def fwriteint64(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.fwriteint64(*_args, **kwargs))


def gameExporter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.gameExporter(*_args, **kwargs))


def gamma(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.gamma(*_args, **kwargs))


def gauss(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.gauss(*_args, **kwargs))


def geomBind(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.geomBind(*_args, **kwargs))


def geomToBBox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.geomToBBox(*_args, **kwargs))


def geometryAppendCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.geometryAppendCache(*_args, **kwargs))


def geometryAppendCacheOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.geometryAppendCacheOpt(*_args, **kwargs))


def geometryCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.geometryCache(*_args, **kwargs))


def geometryCacheOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.geometryCacheOpt(*_args, **kwargs))


def geometryConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.geometryConstraint(*_args, **kwargs))


def geometryDeleteCacheFrames(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.geometryDeleteCacheFrames(*_args, **kwargs))


def geometryDeleteCacheFramesOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.geometryDeleteCacheFramesOpt(*_args, **kwargs))


def geometryDeleteCacheOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.geometryDeleteCacheOpt(*_args, **kwargs))


def geometryExportCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.geometryExportCache(*_args, **kwargs))


def geometryExportCacheOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.geometryExportCacheOpt(*_args, **kwargs))


def geometryMergeCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.geometryMergeCache(*_args, **kwargs))


def geometryMergeCacheOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.geometryMergeCacheOpt(*_args, **kwargs))


def geometryReplaceCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.geometryReplaceCache(*_args, **kwargs))


def geometryReplaceCacheFrames(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.geometryReplaceCacheFrames(*_args, **kwargs))


def geometryReplaceCacheFramesOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.geometryReplaceCacheFramesOpt(*_args, **kwargs))


def geometryReplaceCacheOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.geometryReplaceCacheOpt(*_args, **kwargs))


def getAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.getAttr(*_args, **kwargs))


def getClassification(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.getClassification(*_args, **kwargs))


def getDefaultBrush(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.getDefaultBrush(*_args, **kwargs))


def getFileList(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.getFileList(*_args, **kwargs))


def getFluidAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.getFluidAttr(*_args, **kwargs))


def getInputDeviceRange(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.getInputDeviceRange(*_args, **kwargs))


def getLastError(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.getLastError(*_args, **kwargs))


def getMetadata(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.getMetadata(*_args, **kwargs))


def getModifiers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.getModifiers(*_args, **kwargs))


def getModulePath(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.getModulePath(*_args, **kwargs))


def getPanel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.getPanel(*_args, **kwargs))


def getParticleAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.getParticleAttr(*_args, **kwargs))


def getProcArguments(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.getProcArguments(*_args, **kwargs))


def getRenderDependencies(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.getRenderDependencies(*_args, **kwargs))


def getRenderTasks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.getRenderTasks(*_args, **kwargs))


def getenv(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.getenv(*_args, **kwargs))


def getpid(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.getpid(*_args, **kwargs))


def glRender(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.glRender(*_args, **kwargs))


def glRenderEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.glRenderEditor(*_args, **kwargs))


def globalStitch(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.globalStitch(*_args, **kwargs))


def gmatch(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.gmatch(*_args, **kwargs))


def goal(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.goal(*_args, **kwargs))


def gpuCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.gpuCache(*_args, **kwargs))


def grabColor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.grabColor(*_args, **kwargs))


def gradientControl(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.gradientControl(*_args, **kwargs))


def gradientControlNoAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.gradientControlNoAttr(*_args, **kwargs))


def graphDollyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.graphDollyCtx(*_args, **kwargs))


def graphSelectContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.graphSelectContext(*_args, **kwargs))


def graphTrackCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.graphTrackCtx(*_args, **kwargs))


def gravity(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.gravity(*_args, **kwargs))


def greasePencil(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.greasePencil(*_args, **kwargs))


def greasePencilCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.greasePencilCtx(*_args, **kwargs))


def greasePencilHelper(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.greasePencilHelper(*_args, **kwargs))


def greaseRenderPlane(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.greaseRenderPlane(*_args, **kwargs))


def grid(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.grid(*_args, **kwargs))


def gridLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.gridLayout(*_args, **kwargs))


def group(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.group(*_args, **kwargs))


def groupParts(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.groupParts(*_args, **kwargs))


def hardenPointCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hardenPointCurve(*_args, **kwargs))


def hardware(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hardware(*_args, **kwargs))


def hardwareRenderPanel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hardwareRenderPanel(*_args, **kwargs))


def hasMetadata(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hasMetadata(*_args, **kwargs))


def headsUpDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.headsUpDisplay(*_args, **kwargs))


def headsUpMessage(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.headsUpMessage(*_args, **kwargs))


def help(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.help(*_args, **kwargs))


def helpLine(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.helpLine(*_args, **kwargs))


def hermite(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hermite(*_args, **kwargs))


def hide(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hide(*_args, **kwargs))


def hikBodyPart(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hikBodyPart(*_args, **kwargs))


def hikCharacterToolWidget(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hikCharacterToolWidget(*_args, **kwargs))


def hikCustomRigToolWidget(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hikCustomRigToolWidget(*_args, **kwargs))


def hikGetEffectorIdFromName(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hikGetEffectorIdFromName(*_args, **kwargs))


def hikGetNodeCount(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hikGetNodeCount(*_args, **kwargs))


def hikGetNodeIdFromName(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hikGetNodeIdFromName(*_args, **kwargs))


def hikGlobals(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hikGlobals(*_args, **kwargs))


def hikManip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hikManip(*_args, **kwargs))


def hikRigAlign(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hikRigAlign(*_args, **kwargs))


def hikRigSync(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hikRigSync(*_args, **kwargs))


def hilite(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hilite(*_args, **kwargs))


def hitTest(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hitTest(*_args, **kwargs))


def hotBox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hotBox(*_args, **kwargs))


def hotkey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hotkey(*_args, **kwargs))


def hotkeyCheck(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hotkeyCheck(*_args, **kwargs))


def hotkeyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hotkeyCtx(*_args, **kwargs))


def hotkeyEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hotkeyEditor(*_args, **kwargs))


def hotkeyEditorPanel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hotkeyEditorPanel(*_args, **kwargs))


def hotkeyMapSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hotkeyMapSet(*_args, **kwargs))


def hotkeySet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hotkeySet(*_args, **kwargs))


def hsv_to_rgb(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hsv_to_rgb(*_args, **kwargs))


def hudButton(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hudButton(*_args, **kwargs))


def hudSlider(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hudSlider(*_args, **kwargs))


def hudSliderButton(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hudSliderButton(*_args, **kwargs))


def hwReflectionMap(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hwReflectionMap(*_args, **kwargs))


def hwRender(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hwRender(*_args, **kwargs))


def hwRenderLoad(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hwRenderLoad(*_args, **kwargs))


def hyperGraph(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hyperGraph(*_args, **kwargs))


def hyperPanel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hyperPanel(*_args, **kwargs))


def hyperShade(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hyperShade(*_args, **kwargs))


def hypot(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.hypot(*_args, **kwargs))


def iconTextButton(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.iconTextButton(*_args, **kwargs))


def iconTextCheckBox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.iconTextCheckBox(*_args, **kwargs))


def iconTextRadioButton(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.iconTextRadioButton(*_args, **kwargs))


def iconTextRadioCollection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.iconTextRadioCollection(*_args, **kwargs))


def iconTextScrollList(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.iconTextScrollList(*_args, **kwargs))


def iconTextStaticLabel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.iconTextStaticLabel(*_args, **kwargs))


def ikHandle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ikHandle(*_args, **kwargs))


def ikHandleCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ikHandleCtx(*_args, **kwargs))


def ikHandleDisplayScale(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ikHandleDisplayScale(*_args, **kwargs))


def ikSolver(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ikSolver(*_args, **kwargs))


def ikSplineHandleCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ikSplineHandleCtx(*_args, **kwargs))


def ikSpringSolverCallbacks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ikSpringSolverCallbacks(*_args, **kwargs))


def ikSpringSolverRestPose(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ikSpringSolverRestPose(*_args, **kwargs))


def ikSystem(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ikSystem(*_args, **kwargs))


def ikSystemInfo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ikSystemInfo(*_args, **kwargs))


def ikfkDisplayMethod(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ikfkDisplayMethod(*_args, **kwargs))


def illustratorCurves(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.illustratorCurves(*_args, **kwargs))


def image(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.image(*_args, **kwargs))


def imagePlane(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.imagePlane(*_args, **kwargs))


def imageWindowEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.imageWindowEditor(*_args, **kwargs))


def imfPlugins(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.imfPlugins(*_args, **kwargs))


def inViewEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.inViewEditor(*_args, **kwargs))


def inViewMessage(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.inViewMessage(*_args, **kwargs))


def inheritTransform(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.inheritTransform(*_args, **kwargs))


def insertJoint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.insertJoint(*_args, **kwargs))


def insertJointCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.insertJointCtx(*_args, **kwargs))


def insertKeyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.insertKeyCtx(*_args, **kwargs))


def insertKnotCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.insertKnotCurve(*_args, **kwargs))


def insertKnotSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.insertKnotSurface(*_args, **kwargs))


def insertListItem(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.insertListItem(*_args, **kwargs))


def insertListItemBefore(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.insertListItemBefore(*_args, **kwargs))


def instance(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.instance(*_args, **kwargs))


def instanceable(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.instanceable(*_args, **kwargs))


def instancer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.instancer(*_args, **kwargs))


def intField(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.intField(*_args, **kwargs))


def intFieldGrp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.intFieldGrp(*_args, **kwargs))


def intScrollBar(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.intScrollBar(*_args, **kwargs))


def intSlider(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.intSlider(*_args, **kwargs))


def intSliderGrp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.intSliderGrp(*_args, **kwargs))


def interactionStyle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.interactionStyle(*_args, **kwargs))


def internalVar(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.internalVar(*_args, **kwargs))


def intersect(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.intersect(*_args, **kwargs))


def invertShape(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.invertShape(*_args, **kwargs))


def iprEngine(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.iprEngine(*_args, **kwargs))


def isApexLoaded(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.isApexLoaded(*_args, **kwargs))


def isConnected(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.isConnected(*_args, **kwargs))


def isDescendentPulling(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.isDescendentPulling(*_args, **kwargs))


def isDirty(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.isDirty(*_args, **kwargs))


def isTrue(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.isTrue(*_args, **kwargs))


def isolateSelect(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.isolateSelect(*_args, **kwargs))


def itemFilter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.itemFilter(*_args, **kwargs))


def itemFilterAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.itemFilterAttr(*_args, **kwargs))


def itemFilterRender(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.itemFilterRender(*_args, **kwargs))


def itemFilterType(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.itemFilterType(*_args, **kwargs))


def iterOnNurbs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.iterOnNurbs(*_args, **kwargs))


def joint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.joint(*_args, **kwargs))


def jointCluster(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.jointCluster(*_args, **kwargs))


def jointCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.jointCtx(*_args, **kwargs))


def jointDisplayScale(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.jointDisplayScale(*_args, **kwargs))


def jointLattice(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.jointLattice(*_args, **kwargs))


def journal(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.journal(*_args, **kwargs))


def keyTangent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.keyTangent(*_args, **kwargs))


def keyframe(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.keyframe(*_args, **kwargs))


def keyframeOutliner(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.keyframeOutliner(*_args, **kwargs))


def keyframeRegionCurrentTimeCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.keyframeRegionCurrentTimeCtx(*_args, **kwargs))


def keyframeRegionDirectKeyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.keyframeRegionDirectKeyCtx(*_args, **kwargs))


def keyframeRegionDollyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.keyframeRegionDollyCtx(*_args, **kwargs))


def keyframeRegionInsertKeyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.keyframeRegionInsertKeyCtx(*_args, **kwargs))


def keyframeRegionMoveKeyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.keyframeRegionMoveKeyCtx(*_args, **kwargs))


def keyframeRegionScaleKeyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.keyframeRegionScaleKeyCtx(*_args, **kwargs))


def keyframeRegionSelectKeyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.keyframeRegionSelectKeyCtx(*_args, **kwargs))


def keyframeRegionSetKeyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.keyframeRegionSetKeyCtx(*_args, **kwargs))


def keyframeRegionTrackCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.keyframeRegionTrackCtx(*_args, **kwargs))


def keyframeStats(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.keyframeStats(*_args, **kwargs))


def keyingGroup(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.keyingGroup(*_args, **kwargs))


def lassoContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.lassoContext(*_args, **kwargs))


def lattice(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.lattice(*_args, **kwargs))


def latticeDeformKeyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.latticeDeformKeyCtx(*_args, **kwargs))


def launch(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.launch(*_args, **kwargs))


def launchImageEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.launchImageEditor(*_args, **kwargs))


def layerButton(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.layerButton(*_args, **kwargs))


def layeredShaderPort(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.layeredShaderPort(*_args, **kwargs))


def layeredTexturePort(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.layeredTexturePort(*_args, **kwargs))


def layout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.layout(*_args, **kwargs))


def layoutDialog(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.layoutDialog(*_args, **kwargs))


def license(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.license(*_args, **kwargs))


def licenseCheck(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.licenseCheck(*_args, **kwargs))


def lightList(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.lightList(*_args, **kwargs))


def lightlink(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.lightlink(*_args, **kwargs))


def linearPrecision(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.linearPrecision(*_args, **kwargs))


def linstep(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.linstep(*_args, **kwargs))


def listAnimatable(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.listAnimatable(*_args, **kwargs))


def listAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.listAttr(*_args, **kwargs))


def listAttrPatterns(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.listAttrPatterns(*_args, **kwargs))


def listCameras(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.listCameras(*_args, **kwargs))


def listConnections(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.listConnections(*_args, **kwargs))


def listDeviceAttachments(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.listDeviceAttachments(*_args, **kwargs))


def listHistory(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.listHistory(*_args, **kwargs))


def listInputDeviceAxes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.listInputDeviceAxes(*_args, **kwargs))


def listInputDeviceButtons(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.listInputDeviceButtons(*_args, **kwargs))


def listInputDevices(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.listInputDevices(*_args, **kwargs))


def listNodeTypes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.listNodeTypes(*_args, **kwargs))


def listNodesWithIncorrectNames(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.listNodesWithIncorrectNames(*_args, **kwargs))


def listRelatives(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.listRelatives(*_args, **kwargs))


def listSets(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.listSets(*_args, **kwargs))


def loadFluid(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.loadFluid(*_args, **kwargs))


def loadModule(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.loadModule(*_args, **kwargs))


def loadPlugin(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.loadPlugin(*_args, **kwargs))


def loadPrefObjects(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.loadPrefObjects(*_args, **kwargs))


def loadUI(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.loadUI(*_args, **kwargs))


def lockNode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.lockNode(*_args, **kwargs))


def loft(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.loft(*_args, **kwargs))


def log(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.log(*_args, **kwargs))


def log10(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.log10(*_args, **kwargs))


def log1p(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.log1p(*_args, **kwargs))


def lookThru(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.lookThru(*_args, **kwargs))


def ls(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ls(*_args, **kwargs))


def lsThroughFilter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.lsThroughFilter(*_args, **kwargs))


def lsUI(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.lsUI(*_args, **kwargs))


def mag(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.mag(*_args, **kwargs))


def makeIdentity(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.makeIdentity(*_args, **kwargs))


def makeLive(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.makeLive(*_args, **kwargs))


def makePaintable(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.makePaintable(*_args, **kwargs))


def makeSingleSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.makeSingleSurface(*_args, **kwargs))


def makebot(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.makebot(*_args, **kwargs))


def manipComponentPivot(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.manipComponentPivot(*_args, **kwargs))


def manipMoveContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.manipMoveContext(*_args, **kwargs))


def manipMoveLimitsCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.manipMoveLimitsCtx(*_args, **kwargs))


def manipOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.manipOptions(*_args, **kwargs))


def manipPivot(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.manipPivot(*_args, **kwargs))


def manipRotateContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.manipRotateContext(*_args, **kwargs))


def manipRotateLimitsCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.manipRotateLimitsCtx(*_args, **kwargs))


def manipScaleContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.manipScaleContext(*_args, **kwargs))


def manipScaleLimitsCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.manipScaleLimitsCtx(*_args, **kwargs))


def marker(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.marker(*_args, **kwargs))


def match(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.match(*_args, **kwargs))


def matchTransform(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.matchTransform(*_args, **kwargs))


def mateCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.mateCtx(*_args, **kwargs))


def max(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.max(*_args, **kwargs))


def maxfloat(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.maxfloat(*_args, **kwargs))


def maxint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.maxint(*_args, **kwargs))


def mayaDpiSetting(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.mayaDpiSetting(*_args, **kwargs))


def mayaDpiSettingAction(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.mayaDpiSettingAction(*_args, **kwargs))


def mayaPreviewRenderIntoNewWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.mayaPreviewRenderIntoNewWindow(*_args, **kwargs))


def melInfo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.melInfo(*_args, **kwargs))


def melOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.melOptions(*_args, **kwargs))


def memory(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.memory(*_args, **kwargs))


def memoryDiag(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.memoryDiag(*_args, **kwargs))


def menu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.menu(*_args, **kwargs))


def menuBarLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.menuBarLayout(*_args, **kwargs))


def menuEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.menuEditor(*_args, **kwargs))


def menuItem(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.menuItem(*_args, **kwargs))


def menuSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.menuSet(*_args, **kwargs))


def menuSetPref(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.menuSetPref(*_args, **kwargs))


def meshIntersectTest(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.meshIntersectTest(*_args, **kwargs))


def meshRemap(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.meshRemap(*_args, **kwargs))


def meshRemapContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.meshRemapContext(*_args, **kwargs))


def meshReorder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.meshReorder(*_args, **kwargs))


def meshReorderContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.meshReorderContext(*_args, **kwargs))


def messageLine(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.messageLine(*_args, **kwargs))


def min(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.min(*_args, **kwargs))


def minfloat(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.minfloat(*_args, **kwargs))


def minimizeApp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.minimizeApp(*_args, **kwargs))


def minint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.minint(*_args, **kwargs))


def mirrorJoint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.mirrorJoint(*_args, **kwargs))


def mirrorShape(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.mirrorShape(*_args, **kwargs))


def modelCurrentTimeCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.modelCurrentTimeCtx(*_args, **kwargs))


def modelEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.modelEditor(*_args, **kwargs))


def modelPanel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.modelPanel(*_args, **kwargs))


def modelingToolkitSuperCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.modelingToolkitSuperCtx(*_args, **kwargs))


def moduleDetectionLogic(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.moduleDetectionLogic(*_args, **kwargs))


def moduleInfo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.moduleInfo(*_args, **kwargs))


def mouldMesh(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.mouldMesh(*_args, **kwargs))


def mouldSrf(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.mouldSrf(*_args, **kwargs))


def mouldSubdiv(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.mouldSubdiv(*_args, **kwargs))


def mouse(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.mouse(*_args, **kwargs))


def movIn(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.movIn(*_args, **kwargs))


def movOut(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.movOut(*_args, **kwargs))


def move(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.move(*_args, **kwargs))


def moveKeyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.moveKeyCtx(*_args, **kwargs))


def moveVertexAlongDirection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.moveVertexAlongDirection(*_args, **kwargs))


def movieCompressor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.movieCompressor(*_args, **kwargs))


def movieInfo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.movieInfo(*_args, **kwargs))


def mpBirailCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.mpBirailCtx(*_args, **kwargs))


def mrMapVisualizer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.mrMapVisualizer(*_args, **kwargs))


def mrShaderManager(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.mrShaderManager(*_args, **kwargs))


def mtkQuadDrawPoint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.mtkQuadDrawPoint(*_args, **kwargs))


def mtkShrinkWrap(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.mtkShrinkWrap(*_args, **kwargs))


def multiProfileBirailSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.multiProfileBirailSurface(*_args, **kwargs))


def multiTouch(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.multiTouch(*_args, **kwargs))


def mute(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.mute(*_args, **kwargs))


def myTestCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.myTestCmd(*_args, **kwargs))


def nBase(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nBase(*_args, **kwargs))


def nClothAppend(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nClothAppend(*_args, **kwargs))


def nClothAppendOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nClothAppendOpt(*_args, **kwargs))


def nClothCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nClothCache(*_args, **kwargs))


def nClothCacheOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nClothCacheOpt(*_args, **kwargs))


def nClothCreate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nClothCreate(*_args, **kwargs))


def nClothCreateOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nClothCreateOptions(*_args, **kwargs))


def nClothDeleteCacheFrames(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nClothDeleteCacheFrames(*_args, **kwargs))


def nClothDeleteCacheFramesOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nClothDeleteCacheFramesOpt(*_args, **kwargs))


def nClothDeleteCacheOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nClothDeleteCacheOpt(*_args, **kwargs))


def nClothDeleteHistory(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nClothDeleteHistory(*_args, **kwargs))


def nClothDeleteHistoryOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nClothDeleteHistoryOpt(*_args, **kwargs))


def nClothMakeCollide(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nClothMakeCollide(*_args, **kwargs))


def nClothMakeCollideOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nClothMakeCollideOptions(*_args, **kwargs))


def nClothMergeCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nClothMergeCache(*_args, **kwargs))


def nClothMergeCacheOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nClothMergeCacheOpt(*_args, **kwargs))


def nClothRemove(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nClothRemove(*_args, **kwargs))


def nClothReplaceCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nClothReplaceCache(*_args, **kwargs))


def nClothReplaceCacheOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nClothReplaceCacheOpt(*_args, **kwargs))


def nClothReplaceFrames(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nClothReplaceFrames(*_args, **kwargs))


def nClothReplaceFramesOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nClothReplaceFramesOpt(*_args, **kwargs))


def nParticle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nParticle(*_args, **kwargs))


def nSoft(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nSoft(*_args, **kwargs))


def nameCommand(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nameCommand(*_args, **kwargs))


def nameField(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nameField(*_args, **kwargs))


def namespace(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.namespace(*_args, **kwargs))


def namespaceInfo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.namespaceInfo(*_args, **kwargs))


def newton(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.newton(*_args, **kwargs))


def nexConnectContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nexConnectContext(*_args, **kwargs))


def nexConnectCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nexConnectCtx(*_args, **kwargs))


def nexCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nexCtx(*_args, **kwargs))


def nexMultiCutContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nexMultiCutContext(*_args, **kwargs))


def nexMultiCutCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nexMultiCutCtx(*_args, **kwargs))


def nexOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nexOpt(*_args, **kwargs))


def nexQuadDrawContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nexQuadDrawContext(*_args, **kwargs))


def nexQuadDrawCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nexQuadDrawCtx(*_args, **kwargs))


def nexTRSContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nexTRSContext(*_args, **kwargs))


def nodeCast(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nodeCast(*_args, **kwargs))


def nodeEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nodeEditor(*_args, **kwargs))


def nodeGrapher(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nodeGrapher(*_args, **kwargs))


def nodeIconButton(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nodeIconButton(*_args, **kwargs))


def nodeOutliner(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nodeOutliner(*_args, **kwargs))


def nodePreset(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nodePreset(*_args, **kwargs))


def nodeTreeLister(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nodeTreeLister(*_args, **kwargs))


def nodeType(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nodeType(*_args, **kwargs))


def noise(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.noise(*_args, **kwargs))


def nonLinear(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nonLinear(*_args, **kwargs))


def nop(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nop(*_args, **kwargs))


def normalConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.normalConstraint(*_args, **kwargs))


def notifyPostRedo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.notifyPostRedo(*_args, **kwargs))


def notifyPostUndo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.notifyPostUndo(*_args, **kwargs))


def nucleusDisplayDynamicConstraintNodes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nucleusDisplayDynamicConstraintNodes(*_args, **kwargs))


def nucleusDisplayMaterialNodes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nucleusDisplayMaterialNodes(*_args, **kwargs))


def nucleusDisplayNComponentNodes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nucleusDisplayNComponentNodes(*_args, **kwargs))


def nucleusDisplayOtherNodes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nucleusDisplayOtherNodes(*_args, **kwargs))


def nucleusDisplayTextureNodes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nucleusDisplayTextureNodes(*_args, **kwargs))


def nucleusDisplayTransformNodes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nucleusDisplayTransformNodes(*_args, **kwargs))


def nucleusGetEffectsAsset(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nucleusGetEffectsAsset(*_args, **kwargs))


def nucleusGetnClothExample(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nucleusGetnClothExample(*_args, **kwargs))


def nucleusGetnParticleExample(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nucleusGetnParticleExample(*_args, **kwargs))


def nurbsBoolean(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nurbsBoolean(*_args, **kwargs))


def nurbsCopyUVSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nurbsCopyUVSet(*_args, **kwargs))


def nurbsCube(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nurbsCube(*_args, **kwargs))


def nurbsCurveRebuildPref(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nurbsCurveRebuildPref(*_args, **kwargs))


def nurbsCurveToBezier(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nurbsCurveToBezier(*_args, **kwargs))


def nurbsEditUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nurbsEditUV(*_args, **kwargs))


def nurbsPlane(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nurbsPlane(*_args, **kwargs))


def nurbsSelect(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nurbsSelect(*_args, **kwargs))


def nurbsSquare(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nurbsSquare(*_args, **kwargs))


def nurbsToPoly(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nurbsToPoly(*_args, **kwargs))


def nurbsToPolygonsPref(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nurbsToPolygonsPref(*_args, **kwargs))


def nurbsToSubdiv(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nurbsToSubdiv(*_args, **kwargs))


def nurbsToSubdivPref(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nurbsToSubdivPref(*_args, **kwargs))


def nurbsUVSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nurbsUVSet(*_args, **kwargs))


def nxBuildGetDate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nxBuildGetDate(*_args, **kwargs))


def nxBuildIsDebug(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nxBuildIsDebug(*_args, **kwargs))


def nxDeleteRigidBody(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nxDeleteRigidBody(*_args, **kwargs))


def nxFlushCacheDataFromSelection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nxFlushCacheDataFromSelection(*_args, **kwargs))


def nxGetLargestIndex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nxGetLargestIndex(*_args, **kwargs))


def nxParent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nxParent(*_args, **kwargs))


def nxReplaceDuplicatedRigidBody(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nxReplaceDuplicatedRigidBody(*_args, **kwargs))


def nxRigidBody(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nxRigidBody(*_args, **kwargs))


def nxRigidConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nxRigidConstraint(*_args, **kwargs))


def nxVisualDebugger(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.nxVisualDebugger(*_args, **kwargs))


def objExists(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.objExists(*_args, **kwargs))


def objectCenter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.objectCenter(*_args, **kwargs))


def objectType(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.objectType(*_args, **kwargs))


def objectTypeUI(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.objectTypeUI(*_args, **kwargs))


def offsetCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.offsetCurve(*_args, **kwargs))


def offsetCurveOnSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.offsetCurveOnSurface(*_args, **kwargs))


def offsetSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.offsetSurface(*_args, **kwargs))


def ogs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ogs(*_args, **kwargs))


def ogsRender(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ogsRender(*_args, **kwargs))


def ogsdebug(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ogsdebug(*_args, **kwargs))


def openGLExtension(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.openGLExtension(*_args, **kwargs))


def openMayaPref(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.openMayaPref(*_args, **kwargs))


def optionMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.optionMenu(*_args, **kwargs))


def optionMenuGrp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.optionMenuGrp(*_args, **kwargs))


def optionVar(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.optionVar(*_args, **kwargs))


def orbit(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.orbit(*_args, **kwargs))


def orbitCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.orbitCtx(*_args, **kwargs))


def orientConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.orientConstraint(*_args, **kwargs))


def outlinerEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.outlinerEditor(*_args, **kwargs))


def outlinerPanel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.outlinerPanel(*_args, **kwargs))


def overrideModifier(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.overrideModifier(*_args, **kwargs))


def paint3d(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.paint3d(*_args, **kwargs))


def paintEffectsDisplay(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.paintEffectsDisplay(*_args, **kwargs))


def pairBlend(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.pairBlend(*_args, **kwargs))


def palettePort(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.palettePort(*_args, **kwargs))


def panZoom(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.panZoom(*_args, **kwargs))


def panZoomCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.panZoomCtx(*_args, **kwargs))


def paneLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.paneLayout(*_args, **kwargs))


def panel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.panel(*_args, **kwargs))


def panelConfiguration(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.panelConfiguration(*_args, **kwargs))


def panelHistory(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.panelHistory(*_args, **kwargs))


def paramDimContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.paramDimContext(*_args, **kwargs))


def paramDimension(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.paramDimension(*_args, **kwargs))


def paramLocator(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.paramLocator(*_args, **kwargs))


def parent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.parent(*_args, **kwargs))


def parentConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.parentConstraint(*_args, **kwargs))


def particle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.particle(*_args, **kwargs))


def particleExists(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.particleExists(*_args, **kwargs))


def particleFill(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.particleFill(*_args, **kwargs))


def particleInstancer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.particleInstancer(*_args, **kwargs))


def particleRenderInfo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.particleRenderInfo(*_args, **kwargs))


def partition(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.partition(*_args, **kwargs))


def pasteKey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.pasteKey(*_args, **kwargs))


def pathAnimation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.pathAnimation(*_args, **kwargs))


def pause(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.pause(*_args, **kwargs))


def pclose(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.pclose(*_args, **kwargs))


def perCameraVisibility(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.perCameraVisibility(*_args, **kwargs))


def percent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.percent(*_args, **kwargs))


def performanceOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.performanceOptions(*_args, **kwargs))


def pfxstrokes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.pfxstrokes(*_args, **kwargs))


def pickWalk(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.pickWalk(*_args, **kwargs))


def picture(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.picture(*_args, **kwargs))


def pixelMove(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.pixelMove(*_args, **kwargs))


def planarSrf(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.planarSrf(*_args, **kwargs))


def plane(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.plane(*_args, **kwargs))


def play(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.play(*_args, **kwargs))


def playbackOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.playbackOptions(*_args, **kwargs))


def playblast(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.playblast(*_args, **kwargs))


def pluginDisplayFilter(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.pluginDisplayFilter(*_args, **kwargs))


def pluginInfo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.pluginInfo(*_args, **kwargs))


def pointConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.pointConstraint(*_args, **kwargs))


def pointCurveConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.pointCurveConstraint(*_args, **kwargs))


def pointLight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.pointLight(*_args, **kwargs))


def pointOnCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.pointOnCurve(*_args, **kwargs))


def pointOnPolyConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.pointOnPolyConstraint(*_args, **kwargs))


def pointOnSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.pointOnSurface(*_args, **kwargs))


def pointPosition(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.pointPosition(*_args, **kwargs))


def poleVectorConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.poleVectorConstraint(*_args, **kwargs))


def polyAppend(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyAppend(*_args, **kwargs))


def polyAppendFacetCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyAppendFacetCtx(*_args, **kwargs))


def polyAppendVertex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyAppendVertex(*_args, **kwargs))


def polyAutoProjection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyAutoProjection(*_args, **kwargs))


def polyAverageNormal(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyAverageNormal(*_args, **kwargs))


def polyAverageVertex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyAverageVertex(*_args, **kwargs))


def polyBevel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyBevel(*_args, **kwargs))


def polyBevel3(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyBevel3(*_args, **kwargs))


def polyBlendColor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyBlendColor(*_args, **kwargs))


def polyBlindData(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyBlindData(*_args, **kwargs))


def polyBoolOp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyBoolOp(*_args, **kwargs))


def polyBridgeEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyBridgeEdge(*_args, **kwargs))


def polyCBoolOp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCBoolOp(*_args, **kwargs))


def polyCacheMonitor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCacheMonitor(*_args, **kwargs))


def polyCanBridgeEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCanBridgeEdge(*_args, **kwargs))


def polyCheck(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCheck(*_args, **kwargs))


def polyChipOff(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyChipOff(*_args, **kwargs))


def polyCircularize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCircularize(*_args, **kwargs))


def polyCircularizeEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCircularizeEdge(*_args, **kwargs))


def polyCircularizeFace(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCircularizeFace(*_args, **kwargs))


def polyClean(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyClean(*_args, **kwargs))


def polyClipboard(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyClipboard(*_args, **kwargs))


def polyCloseBorder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCloseBorder(*_args, **kwargs))


def polyCollapseEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCollapseEdge(*_args, **kwargs))


def polyCollapseFacet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCollapseFacet(*_args, **kwargs))


def polyCollapseTweaks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCollapseTweaks(*_args, **kwargs))


def polyColorBlindData(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyColorBlindData(*_args, **kwargs))


def polyColorDel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyColorDel(*_args, **kwargs))


def polyColorMod(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyColorMod(*_args, **kwargs))


def polyColorPerVertex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyColorPerVertex(*_args, **kwargs))


def polyColorSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyColorSet(*_args, **kwargs))


def polyColorSetCmdWrapper(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyColorSetCmdWrapper(*_args, **kwargs))


def polyCompare(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCompare(*_args, **kwargs))


def polyCone(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCone(*_args, **kwargs))


def polyConnectComponents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyConnectComponents(*_args, **kwargs))


def polyContourProjection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyContourProjection(*_args, **kwargs))


def polyCopyUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCopyUV(*_args, **kwargs))


def polyCrease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCrease(*_args, **kwargs))


def polyCreaseCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCreaseCtx(*_args, **kwargs))


def polyCreateFacet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCreateFacet(*_args, **kwargs))


def polyCreateFacetCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCreateFacetCtx(*_args, **kwargs))


def polyCube(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCube(*_args, **kwargs))


def polyCut(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCut(*_args, **kwargs))


def polyCutCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCutCtx(*_args, **kwargs))


def polyCutUVCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCutUVCtx(*_args, **kwargs))


def polyCylinder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCylinder(*_args, **kwargs))


def polyCylindricalProjection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyCylindricalProjection(*_args, **kwargs))


def polyDelEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyDelEdge(*_args, **kwargs))


def polyDelFacet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyDelFacet(*_args, **kwargs))


def polyDelVertex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyDelVertex(*_args, **kwargs))


def polyDisc(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyDisc(*_args, **kwargs))


def polyDuplicateAndConnect(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyDuplicateAndConnect(*_args, **kwargs))


def polyDuplicateEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyDuplicateEdge(*_args, **kwargs))


def polyEditEdgeFlow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyEditEdgeFlow(*_args, **kwargs))


def polyEditUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyEditUV(*_args, **kwargs))


def polyEditUVShell(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyEditUVShell(*_args, **kwargs))


def polyEvaluate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyEvaluate(*_args, **kwargs))


def polyExtrudeEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyExtrudeEdge(*_args, **kwargs))


def polyExtrudeFacet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyExtrudeFacet(*_args, **kwargs))


def polyExtrudeVertex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyExtrudeVertex(*_args, **kwargs))


def polyFlipEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyFlipEdge(*_args, **kwargs))


def polyFlipUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyFlipUV(*_args, **kwargs))


def polyForceUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyForceUV(*_args, **kwargs))


def polyGear(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyGear(*_args, **kwargs))


def polyGeoSampler(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyGeoSampler(*_args, **kwargs))


def polyHelix(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyHelix(*_args, **kwargs))


def polyHole(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyHole(*_args, **kwargs))


def polyInfo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyInfo(*_args, **kwargs))


def polyInstallAction(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyInstallAction(*_args, **kwargs))


def polyIterOnPoly(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyIterOnPoly(*_args, **kwargs))


def polyLayoutUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyLayoutUV(*_args, **kwargs))


def polyListComponentConversion(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyListComponentConversion(*_args, **kwargs))


def polyMapCut(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyMapCut(*_args, **kwargs))


def polyMapDel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyMapDel(*_args, **kwargs))


def polyMapSew(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyMapSew(*_args, **kwargs))


def polyMapSewMove(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyMapSewMove(*_args, **kwargs))


def polyMergeEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyMergeEdge(*_args, **kwargs))


def polyMergeEdgeCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyMergeEdgeCtx(*_args, **kwargs))


def polyMergeFacet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyMergeFacet(*_args, **kwargs))


def polyMergeFacetCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyMergeFacetCtx(*_args, **kwargs))


def polyMergeUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyMergeUV(*_args, **kwargs))


def polyMergeVertex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyMergeVertex(*_args, **kwargs))


def polyMirrorFace(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyMirrorFace(*_args, **kwargs))


def polyMoveEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyMoveEdge(*_args, **kwargs))


def polyMoveFacet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyMoveFacet(*_args, **kwargs))


def polyMoveFacetUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyMoveFacetUV(*_args, **kwargs))


def polyMoveUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyMoveUV(*_args, **kwargs))


def polyMoveVertex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyMoveVertex(*_args, **kwargs))


def polyMultiLayoutUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyMultiLayoutUV(*_args, **kwargs))


def polyNormal(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyNormal(*_args, **kwargs))


def polyNormalPerVertex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyNormalPerVertex(*_args, **kwargs))


def polyNormalizeUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyNormalizeUV(*_args, **kwargs))


def polyOptUvs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyOptUvs(*_args, **kwargs))


def polyOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyOptions(*_args, **kwargs))


def polyOutput(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyOutput(*_args, **kwargs))


def polyPinUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyPinUV(*_args, **kwargs))


def polyPipe(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyPipe(*_args, **kwargs))


def polyPlanarProjection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyPlanarProjection(*_args, **kwargs))


def polyPlane(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyPlane(*_args, **kwargs))


def polyPlatonic(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyPlatonic(*_args, **kwargs))


def polyPlatonicSolid(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyPlatonicSolid(*_args, **kwargs))


def polyPoke(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyPoke(*_args, **kwargs))


def polyPrimitive(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyPrimitive(*_args, **kwargs))


def polyPrimitiveMisc(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyPrimitiveMisc(*_args, **kwargs))


def polyPrism(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyPrism(*_args, **kwargs))


def polyProjectCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyProjectCurve(*_args, **kwargs))


def polyProjection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyProjection(*_args, **kwargs))


def polyPyramid(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyPyramid(*_args, **kwargs))


def polyQuad(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyQuad(*_args, **kwargs))


def polyQueryBlindData(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyQueryBlindData(*_args, **kwargs))


def polyReduce(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyReduce(*_args, **kwargs))


def polyRemesh(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyRemesh(*_args, **kwargs))


def polyRetopo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyRetopo(*_args, **kwargs))


def polyRetopoCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyRetopoCtx(*_args, **kwargs))


def polySelect(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySelect(*_args, **kwargs))


def polySelectConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySelectConstraint(*_args, **kwargs))


def polySelectConstraintMonitor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySelectConstraintMonitor(*_args, **kwargs))


def polySelectCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySelectCtx(*_args, **kwargs))


def polySelectEditCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySelectEditCtx(*_args, **kwargs))


def polySelectEditCtxDataCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySelectEditCtxDataCmd(*_args, **kwargs))


def polySelectSp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySelectSp(*_args, **kwargs))


def polySeparate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySeparate(*_args, **kwargs))


def polySetToFaceNormal(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySetToFaceNormal(*_args, **kwargs))


def polySetVertices(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySetVertices(*_args, **kwargs))


def polySewEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySewEdge(*_args, **kwargs))


def polyShortestPathCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyShortestPathCtx(*_args, **kwargs))


def polySlideEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySlideEdge(*_args, **kwargs))


def polySlideEdgeCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySlideEdgeCtx(*_args, **kwargs))


def polySmooth(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySmooth(*_args, **kwargs))


def polySoftEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySoftEdge(*_args, **kwargs))


def polySphere(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySphere(*_args, **kwargs))


def polySphericalProjection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySphericalProjection(*_args, **kwargs))


def polySpinEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySpinEdge(*_args, **kwargs))


def polySplit(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySplit(*_args, **kwargs))


def polySplitCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySplitCtx(*_args, **kwargs))


def polySplitCtx2(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySplitCtx2(*_args, **kwargs))


def polySplitEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySplitEdge(*_args, **kwargs))


def polySplitRing(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySplitRing(*_args, **kwargs))


def polySplitVertex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySplitVertex(*_args, **kwargs))


def polyStraightenUVBorder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyStraightenUVBorder(*_args, **kwargs))


def polySubdivideEdge(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySubdivideEdge(*_args, **kwargs))


def polySubdivideFacet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySubdivideFacet(*_args, **kwargs))


def polySuperCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySuperCtx(*_args, **kwargs))


def polySuperShape(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polySuperShape(*_args, **kwargs))


def polyTestPop(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyTestPop(*_args, **kwargs))


def polyToCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyToCurve(*_args, **kwargs))


def polyToSubdiv(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyToSubdiv(*_args, **kwargs))


def polyTorus(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyTorus(*_args, **kwargs))


def polyTransfer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyTransfer(*_args, **kwargs))


def polyTriangulate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyTriangulate(*_args, **kwargs))


def polyUVCoverage(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyUVCoverage(*_args, **kwargs))


def polyUVOverlap(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyUVOverlap(*_args, **kwargs))


def polyUVRectangle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyUVRectangle(*_args, **kwargs))


def polyUVSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyUVSet(*_args, **kwargs))


def polyUVStackSimilarShells(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyUVStackSimilarShells(*_args, **kwargs))


def polyUVStackSimilarShellsCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyUVStackSimilarShellsCmd(*_args, **kwargs))


def polyUnite(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyUnite(*_args, **kwargs))


def polyUniteSkinned(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyUniteSkinned(*_args, **kwargs))


def polyVertexNormalCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyVertexNormalCtx(*_args, **kwargs))


def polyWarpImage(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyWarpImage(*_args, **kwargs))


def polyWedgeFace(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.polyWedgeFace(*_args, **kwargs))


def popListItem(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.popListItem(*_args, **kwargs))


def popPinning(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.popPinning(*_args, **kwargs))


def popen(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.popen(*_args, **kwargs))


def popupMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.popupMenu(*_args, **kwargs))


def pose(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.pose(*_args, **kwargs))


def poseEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.poseEditor(*_args, **kwargs))


def poseInterpolator(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.poseInterpolator(*_args, **kwargs))


def posePanel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.posePanel(*_args, **kwargs))


def pow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.pow(*_args, **kwargs))


def preferredRenderer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.preferredRenderer(*_args, **kwargs))


def preloadRefEd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.preloadRefEd(*_args, **kwargs))


def prepareRender(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.prepareRender(*_args, **kwargs))


def prependListItem(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.prependListItem(*_args, **kwargs))


def print(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.print(*_args, **kwargs))


def printStudio(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.printStudio(*_args, **kwargs))


def profiler(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.profiler(*_args, **kwargs))


def profilerTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.profilerTool(*_args, **kwargs))


def progressBar(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.progressBar(*_args, **kwargs))


def progressWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.progressWindow(*_args, **kwargs))


def projectCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.projectCurve(*_args, **kwargs))


def projectTangent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.projectTangent(*_args, **kwargs))


def projectionContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.projectionContext(*_args, **kwargs))


def projectionManip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.projectionManip(*_args, **kwargs))


def promptDialog(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.promptDialog(*_args, **kwargs))


def propModCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.propModCtx(*_args, **kwargs))


def propMove(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.propMove(*_args, **kwargs))


def psdChannelOutliner(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.psdChannelOutliner(*_args, **kwargs))


def psdConvSolidTxOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.psdConvSolidTxOptions(*_args, **kwargs))


def psdEditTextureFile(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.psdEditTextureFile(*_args, **kwargs))


def psdExport(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.psdExport(*_args, **kwargs))


def psdTextureFile(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.psdTextureFile(*_args, **kwargs))


def pushPinning(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.pushPinning(*_args, **kwargs))


def putenv(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.putenv(*_args, **kwargs))


def pwd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.pwd(*_args, **kwargs))


def python(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.python(*_args, **kwargs))


def querySubdiv(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.querySubdiv(*_args, **kwargs))


def quit(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.quit(*_args, **kwargs))


def rad_to_deg(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.rad_to_deg(*_args, **kwargs))


def radial(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.radial(*_args, **kwargs))


def radioButton(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.radioButton(*_args, **kwargs))


def radioButtonGrp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.radioButtonGrp(*_args, **kwargs))


def radioCollection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.radioCollection(*_args, **kwargs))


def radioMenuItemCollection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.radioMenuItemCollection(*_args, **kwargs))


def rampColorPort(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.rampColorPort(*_args, **kwargs))


def rampWidget(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.rampWidget(*_args, **kwargs))


def rampWidgetAttrless(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.rampWidgetAttrless(*_args, **kwargs))


def rand(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.rand(*_args, **kwargs))


def randstate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.randstate(*_args, **kwargs))


def rangeControl(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.rangeControl(*_args, **kwargs))


def readPDC(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.readPDC(*_args, **kwargs))


def readTake(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.readTake(*_args, **kwargs))


def rebuildCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.rebuildCurve(*_args, **kwargs))


def rebuildSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.rebuildSurface(*_args, **kwargs))


def recordAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.recordAttr(*_args, **kwargs))


def recordDevice(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.recordDevice(*_args, **kwargs))


def redo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.redo(*_args, **kwargs))


def reference(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.reference(*_args, **kwargs))


def referenceEdit(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.referenceEdit(*_args, **kwargs))


def referenceQuery(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.referenceQuery(*_args, **kwargs))


def refineSubdivSelectionList(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.refineSubdivSelectionList(*_args, **kwargs))


def refresh(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.refresh(*_args, **kwargs))


def refreshEditorTemplates(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.refreshEditorTemplates(*_args, **kwargs))


def regionSelectKeyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.regionSelectKeyCtx(*_args, **kwargs))


def regmatch(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.regmatch(*_args, **kwargs))


def rehash(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.rehash(*_args, **kwargs))


def relationship(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.relationship(*_args, **kwargs))


def reloadImage(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.reloadImage(*_args, **kwargs))


def removeJoint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.removeJoint(*_args, **kwargs))


def removeListItem(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.removeListItem(*_args, **kwargs))


def removeMultiInstance(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.removeMultiInstance(*_args, **kwargs))


def rename(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.rename(*_args, **kwargs))


def renameAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renameAttr(*_args, **kwargs))


def renameUI(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renameUI(*_args, **kwargs))


def render(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.render(*_args, **kwargs))


def renderGlobalsNode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renderGlobalsNode(*_args, **kwargs))


def renderInfo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renderInfo(*_args, **kwargs))


def renderLayerMembers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renderLayerMembers(*_args, **kwargs))


def renderLayerPostProcess(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renderLayerPostProcess(*_args, **kwargs))


def renderManip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renderManip(*_args, **kwargs))


def renderPartition(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renderPartition(*_args, **kwargs))


def renderPassRegistry(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renderPassRegistry(*_args, **kwargs))


def renderQualityNode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renderQualityNode(*_args, **kwargs))


def renderSettings(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renderSettings(*_args, **kwargs))


def renderSetup(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renderSetup(*_args, **kwargs))


def renderSetupFind(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renderSetupFind(*_args, **kwargs))


def renderSetupHighlight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renderSetupHighlight(*_args, **kwargs))


def renderSetupLegacyLayer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renderSetupLegacyLayer(*_args, **kwargs))


def renderSetupLocalOverride(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renderSetupLocalOverride(*_args, **kwargs))


def renderSetupPostApply(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renderSetupPostApply(*_args, **kwargs))


def renderSetupSelect(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renderSetupSelect(*_args, **kwargs))


def renderSetupSwitchVisibleRenderLayer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renderSetupSwitchVisibleRenderLayer(*_args, **kwargs))


def renderThumbnailUpdate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renderThumbnailUpdate(*_args, **kwargs))


def renderWindowEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renderWindowEditor(*_args, **kwargs))


def renderWindowSelectContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renderWindowSelectContext(*_args, **kwargs))


def renderer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.renderer(*_args, **kwargs))


def reorder(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.reorder(*_args, **kwargs))


def reorderContainer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.reorderContainer(*_args, **kwargs))


def reorderDeformers(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.reorderDeformers(*_args, **kwargs))


def repeatLast(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.repeatLast(*_args, **kwargs))


def replaceCacheFrames(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.replaceCacheFrames(*_args, **kwargs))


def replaceCacheFramesOpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.replaceCacheFramesOpt(*_args, **kwargs))


def requires(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.requires(*_args, **kwargs))


def reroot(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.reroot(*_args, **kwargs))


def resampleFluid(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.resampleFluid(*_args, **kwargs))


def resetTool(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.resetTool(*_args, **kwargs))


def resolutionNode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.resolutionNode(*_args, **kwargs))


def resourceManager(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.resourceManager(*_args, **kwargs))


def retimeHelper(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.retimeHelper(*_args, **kwargs))


def retimeKeyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.retimeKeyCtx(*_args, **kwargs))


def reverseCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.reverseCurve(*_args, **kwargs))


def reverseSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.reverseSurface(*_args, **kwargs))


def revolve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.revolve(*_args, **kwargs))


def rgb_to_hsv(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.rgb_to_hsv(*_args, **kwargs))


def rigidBody(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.rigidBody(*_args, **kwargs))


def rigidSolver(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.rigidSolver(*_args, **kwargs))


def roll(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.roll(*_args, **kwargs))


def rollCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.rollCtx(*_args, **kwargs))


def rot(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.rot(*_args, **kwargs))


def rotate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.rotate(*_args, **kwargs))


def rotationInterpolation(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.rotationInterpolation(*_args, **kwargs))


def roundCRCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.roundCRCtx(*_args, **kwargs))


def roundConstantRadius(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.roundConstantRadius(*_args, **kwargs))


def rowColumnLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.rowColumnLayout(*_args, **kwargs))


def rowLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.rowLayout(*_args, **kwargs))


def runTimeCommand(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.runTimeCommand(*_args, **kwargs))


def runup(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.runup(*_args, **kwargs))


def sampleImage(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.sampleImage(*_args, **kwargs))


def saveAllShelves(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.saveAllShelves(*_args, **kwargs))


def saveFluid(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.saveFluid(*_args, **kwargs))


def saveImage(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.saveImage(*_args, **kwargs))


def saveInitialState(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.saveInitialState(*_args, **kwargs))


def saveMenu(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.saveMenu(*_args, **kwargs))


def savePrefObjects(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.savePrefObjects(*_args, **kwargs))


def savePrefs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.savePrefs(*_args, **kwargs))


def saveShelf(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.saveShelf(*_args, **kwargs))


def saveToolSettings(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.saveToolSettings(*_args, **kwargs))


def saveViewportSettings(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.saveViewportSettings(*_args, **kwargs))


def scale(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.scale(*_args, **kwargs))


def scaleComponents(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.scaleComponents(*_args, **kwargs))


def scaleConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.scaleConstraint(*_args, **kwargs))


def scaleKey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.scaleKey(*_args, **kwargs))


def scaleKeyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.scaleKeyCtx(*_args, **kwargs))


def sceneEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.sceneEditor(*_args, **kwargs))


def sceneUIReplacement(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.sceneUIReplacement(*_args, **kwargs))


def scmh(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.scmh(*_args, **kwargs))


def scriptCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.scriptCtx(*_args, **kwargs))


def scriptEditorInfo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.scriptEditorInfo(*_args, **kwargs))


def scriptJob(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.scriptJob(*_args, **kwargs))


def scriptNode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.scriptNode(*_args, **kwargs))


def scriptTable(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.scriptTable(*_args, **kwargs))


def scriptedPanel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.scriptedPanel(*_args, **kwargs))


def scriptedPanelType(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.scriptedPanelType(*_args, **kwargs))


def scrollField(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.scrollField(*_args, **kwargs))


def scrollLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.scrollLayout(*_args, **kwargs))


def sculpt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.sculpt(*_args, **kwargs))


def sculptMeshCacheChangeCloneSource(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.sculptMeshCacheChangeCloneSource(*_args, **kwargs))


def sculptMeshCacheCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.sculptMeshCacheCtx(*_args, **kwargs))


def sculptTarget(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.sculptTarget(*_args, **kwargs))


def seed(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.seed(*_args, **kwargs))


def selLoadSettings(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.selLoadSettings(*_args, **kwargs))


def select(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.select(*_args, **kwargs))


def selectContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.selectContext(*_args, **kwargs))


def selectKey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.selectKey(*_args, **kwargs))


def selectKeyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.selectKeyCtx(*_args, **kwargs))


def selectKeyframe(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.selectKeyframe(*_args, **kwargs))


def selectKeyframeRegionCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.selectKeyframeRegionCtx(*_args, **kwargs))


def selectMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.selectMode(*_args, **kwargs))


def selectPref(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.selectPref(*_args, **kwargs))


def selectPriority(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.selectPriority(*_args, **kwargs))


def selectType(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.selectType(*_args, **kwargs))


def selectedNodes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.selectedNodes(*_args, **kwargs))


def selectionConnection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.selectionConnection(*_args, **kwargs))


def separator(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.separator(*_args, **kwargs))


def sequenceManager(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.sequenceManager(*_args, **kwargs))


def setAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setAttr(*_args, **kwargs))


def setAttrMapping(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setAttrMapping(*_args, **kwargs))


def setDefaultShadingGroup(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setDefaultShadingGroup(*_args, **kwargs))


def setDrivenKeyframe(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setDrivenKeyframe(*_args, **kwargs))


def setDynStartState(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setDynStartState(*_args, **kwargs))


def setDynamic(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setDynamic(*_args, **kwargs))


def setEditCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setEditCtx(*_args, **kwargs))


def setFluidAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setFluidAttr(*_args, **kwargs))


def setFocus(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setFocus(*_args, **kwargs))


def setInfinity(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setInfinity(*_args, **kwargs))


def setInputDeviceMapping(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setInputDeviceMapping(*_args, **kwargs))


def setKeyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setKeyCtx(*_args, **kwargs))


def setKeyPath(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setKeyPath(*_args, **kwargs))


def setKeyframe(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setKeyframe(*_args, **kwargs))


def setKeyframeBlendshapeTargetWts(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setKeyframeBlendshapeTargetWts(*_args, **kwargs))


def setMenuMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setMenuMode(*_args, **kwargs))


def setNClothStartState(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setNClothStartState(*_args, **kwargs))


def setNodeTypeFlag(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setNodeTypeFlag(*_args, **kwargs))


def setParent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setParent(*_args, **kwargs))


def setParticleAttr(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setParticleAttr(*_args, **kwargs))


def setRenderPassType(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setRenderPassType(*_args, **kwargs))


def setStartupMessage(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setStartupMessage(*_args, **kwargs))


def setToolTo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setToolTo(*_args, **kwargs))


def setUITemplate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setUITemplate(*_args, **kwargs))


def setXformManip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.setXformManip(*_args, **kwargs))


def sets(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.sets(*_args, **kwargs))


def shaderfx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.shaderfx(*_args, **kwargs))


def shadingConnection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.shadingConnection(*_args, **kwargs))


def shadingGeometryRelCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.shadingGeometryRelCtx(*_args, **kwargs))


def shadingLightRelCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.shadingLightRelCtx(*_args, **kwargs))


def shadingNetworkCompare(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.shadingNetworkCompare(*_args, **kwargs))


def shadingNode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.shadingNode(*_args, **kwargs))


def shapeCompare(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.shapeCompare(*_args, **kwargs))


def shapeEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.shapeEditor(*_args, **kwargs))


def shapePanel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.shapePanel(*_args, **kwargs))


def shelfButton(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.shelfButton(*_args, **kwargs))


def shelfLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.shelfLayout(*_args, **kwargs))


def shelfTabLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.shelfTabLayout(*_args, **kwargs))


def shot(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.shot(*_args, **kwargs))


def shotRipple(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.shotRipple(*_args, **kwargs))


def shotTrack(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.shotTrack(*_args, **kwargs))


def showHelp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.showHelp(*_args, **kwargs))


def showHidden(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.showHidden(*_args, **kwargs))


def showManipCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.showManipCtx(*_args, **kwargs))


def showMetadata(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.showMetadata(*_args, **kwargs))


def showSelectionInTitle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.showSelectionInTitle(*_args, **kwargs))


def showShadingGroupAttrEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.showShadingGroupAttrEditor(*_args, **kwargs))


def showWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.showWindow(*_args, **kwargs))


def sign(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.sign(*_args, **kwargs))


def simplify(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.simplify(*_args, **kwargs))


def simulationSets(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.simulationSets(*_args, **kwargs))


def sin(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.sin(*_args, **kwargs))


def sind(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.sind(*_args, **kwargs))


def singleProfileBirailSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.singleProfileBirailSurface(*_args, **kwargs))


def sinh(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.sinh(*_args, **kwargs))


def size(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.size(*_args, **kwargs))


def sizeBytes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.sizeBytes(*_args, **kwargs))


def skeletonEmbed(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.skeletonEmbed(*_args, **kwargs))


def skinBindCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.skinBindCtx(*_args, **kwargs))


def skinCluster(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.skinCluster(*_args, **kwargs))


def skinPercent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.skinPercent(*_args, **kwargs))


def smoothCurve(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.smoothCurve(*_args, **kwargs))


def smoothTangentSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.smoothTangentSurface(*_args, **kwargs))


def smoothstep(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.smoothstep(*_args, **kwargs))


def snapKey(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.snapKey(*_args, **kwargs))


def snapMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.snapMode(*_args, **kwargs))


def snapTogetherCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.snapTogetherCtx(*_args, **kwargs))


def snapshot(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.snapshot(*_args, **kwargs))


def snapshotBeadContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.snapshotBeadContext(*_args, **kwargs))


def snapshotBeadCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.snapshotBeadCtx(*_args, **kwargs))


def snapshotModifyKeyCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.snapshotModifyKeyCtx(*_args, **kwargs))


def soft(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.soft(*_args, **kwargs))


def softMod(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.softMod(*_args, **kwargs))


def softModContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.softModContext(*_args, **kwargs))


def softModCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.softModCtx(*_args, **kwargs))


def softSelect(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.softSelect(*_args, **kwargs))


def softSelectOptionsCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.softSelectOptionsCtx(*_args, **kwargs))


def soloMaterial(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.soloMaterial(*_args, **kwargs))


def sort(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.sort(*_args, **kwargs))


def sortCaseInsensitive(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.sortCaseInsensitive(*_args, **kwargs))


def sound(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.sound(*_args, **kwargs))


def soundControl(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.soundControl(*_args, **kwargs))


def spBirailCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.spBirailCtx(*_args, **kwargs))


def spaceLocator(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.spaceLocator(*_args, **kwargs))


def sphere(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.sphere(*_args, **kwargs))


def sphrand(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.sphrand(*_args, **kwargs))


def spotLight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.spotLight(*_args, **kwargs))


def spotLightPreviewPort(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.spotLightPreviewPort(*_args, **kwargs))


def spreadSheetEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.spreadSheetEditor(*_args, **kwargs))


def spring(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.spring(*_args, **kwargs))


def sqrt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.sqrt(*_args, **kwargs))


def squareSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.squareSurface(*_args, **kwargs))


def srtContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.srtContext(*_args, **kwargs))


def stackTrace(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.stackTrace(*_args, **kwargs))


def stitchSurface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.stitchSurface(*_args, **kwargs))


def stitchSurfaceCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.stitchSurfaceCtx(*_args, **kwargs))


def stitchSurfacePoints(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.stitchSurfacePoints(*_args, **kwargs))


def strcmp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.strcmp(*_args, **kwargs))


def stringArrayIntersector(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.stringArrayIntersector(*_args, **kwargs))


def stringArrayRemove(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.stringArrayRemove(*_args, **kwargs))


def stroke(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.stroke(*_args, **kwargs))


def subdAutoProjection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.subdAutoProjection(*_args, **kwargs))


def subdCleanTopology(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.subdCleanTopology(*_args, **kwargs))


def subdCollapse(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.subdCollapse(*_args, **kwargs))


def subdDisplayMode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.subdDisplayMode(*_args, **kwargs))


def subdDuplicateAndConnect(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.subdDuplicateAndConnect(*_args, **kwargs))


def subdEditUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.subdEditUV(*_args, **kwargs))


def subdLayoutUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.subdLayoutUV(*_args, **kwargs))


def subdListComponentConversion(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.subdListComponentConversion(*_args, **kwargs))


def subdMapCut(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.subdMapCut(*_args, **kwargs))


def subdMapSewMove(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.subdMapSewMove(*_args, **kwargs))


def subdMatchTopology(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.subdMatchTopology(*_args, **kwargs))


def subdMirror(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.subdMirror(*_args, **kwargs))


def subdPlanarProjection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.subdPlanarProjection(*_args, **kwargs))


def subdToBlind(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.subdToBlind(*_args, **kwargs))


def subdToNurbs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.subdToNurbs(*_args, **kwargs))


def subdToPoly(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.subdToPoly(*_args, **kwargs))


def subdTransferUVsToCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.subdTransferUVsToCache(*_args, **kwargs))


def subdiv(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.subdiv(*_args, **kwargs))


def subdivCrease(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.subdivCrease(*_args, **kwargs))


def subdivDisplaySmoothness(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.subdivDisplaySmoothness(*_args, **kwargs))


def subgraph(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.subgraph(*_args, **kwargs))


def substitute(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.substitute(*_args, **kwargs))


def substituteGeometry(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.substituteGeometry(*_args, **kwargs))


def substring(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.substring(*_args, **kwargs))


def suitePrefs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.suitePrefs(*_args, **kwargs))


def superCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.superCtx(*_args, **kwargs))


def surface(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.surface(*_args, **kwargs))


def surfaceSampler(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.surfaceSampler(*_args, **kwargs))


def surfaceShaderList(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.surfaceShaderList(*_args, **kwargs))


def swatchDisplayPort(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.swatchDisplayPort(*_args, **kwargs))


def swatchRefresh(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.swatchRefresh(*_args, **kwargs))


def switchTable(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.switchTable(*_args, **kwargs))


def symbolButton(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.symbolButton(*_args, **kwargs))


def symbolCheckBox(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.symbolCheckBox(*_args, **kwargs))


def symmetricModelling(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.symmetricModelling(*_args, **kwargs))


def symmetrizeUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.symmetrizeUV(*_args, **kwargs))


def syncSculptCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.syncSculptCache(*_args, **kwargs))


def sysFile(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.sysFile(*_args, **kwargs))


def system(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.system(*_args, **kwargs))


def tabLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.tabLayout(*_args, **kwargs))


def tan(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.tan(*_args, **kwargs))


def tand(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.tand(*_args, **kwargs))


def tangentConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.tangentConstraint(*_args, **kwargs))


def tanh(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.tanh(*_args, **kwargs))


def targetWeldCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.targetWeldCtx(*_args, **kwargs))


def tension(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.tension(*_args, **kwargs))


def testPa(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.testPa(*_args, **kwargs))


def testPassContribution(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.testPassContribution(*_args, **kwargs))


def texCutContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.texCutContext(*_args, **kwargs))


def texLatticeDeformContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.texLatticeDeformContext(*_args, **kwargs))


def texManipContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.texManipContext(*_args, **kwargs))


def texMoveContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.texMoveContext(*_args, **kwargs))


def texMoveUVShellContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.texMoveUVShellContext(*_args, **kwargs))


def texRotateContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.texRotateContext(*_args, **kwargs))


def texScaleContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.texScaleContext(*_args, **kwargs))


def texSculptCacheContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.texSculptCacheContext(*_args, **kwargs))


def texSculptCacheSync(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.texSculptCacheSync(*_args, **kwargs))


def texSelectContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.texSelectContext(*_args, **kwargs))


def texSelectShortestPathCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.texSelectShortestPathCtx(*_args, **kwargs))


def texSmoothContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.texSmoothContext(*_args, **kwargs))


def texSmudgeUVContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.texSmudgeUVContext(*_args, **kwargs))


def texTweakUVContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.texTweakUVContext(*_args, **kwargs))


def texWinToolCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.texWinToolCtx(*_args, **kwargs))


def text(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.text(*_args, **kwargs))


def textCurves(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.textCurves(*_args, **kwargs))


def textField(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.textField(*_args, **kwargs))


def textFieldButtonGrp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.textFieldButtonGrp(*_args, **kwargs))


def textFieldGrp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.textFieldGrp(*_args, **kwargs))


def textManip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.textManip(*_args, **kwargs))


def textScrollList(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.textScrollList(*_args, **kwargs))


def textureDeformer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.textureDeformer(*_args, **kwargs))


def textureLassoContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.textureLassoContext(*_args, **kwargs))


def texturePlacementContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.texturePlacementContext(*_args, **kwargs))


def textureWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.textureWindow(*_args, **kwargs))


def threadCount(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.threadCount(*_args, **kwargs))


def threePointArcCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.threePointArcCtx(*_args, **kwargs))


def thumbnailCaptureComponent(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.thumbnailCaptureComponent(*_args, **kwargs))


def timeCode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.timeCode(*_args, **kwargs))


def timeControl(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.timeControl(*_args, **kwargs))


def timeEditor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.timeEditor(*_args, **kwargs))


def timeEditorAnimSource(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.timeEditorAnimSource(*_args, **kwargs))


def timeEditorBakeClips(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.timeEditorBakeClips(*_args, **kwargs))


def timeEditorClip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.timeEditorClip(*_args, **kwargs))


def timeEditorClipLayer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.timeEditorClipLayer(*_args, **kwargs))


def timeEditorClipOffset(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.timeEditorClipOffset(*_args, **kwargs))


def timeEditorComposition(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.timeEditorComposition(*_args, **kwargs))


def timeEditorPanel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.timeEditorPanel(*_args, **kwargs))


def timeEditorTracks(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.timeEditorTracks(*_args, **kwargs))


def timeField(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.timeField(*_args, **kwargs))


def timeFieldGrp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.timeFieldGrp(*_args, **kwargs))


def timePort(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.timePort(*_args, **kwargs))


def timeWarp(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.timeWarp(*_args, **kwargs))


def timer(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.timer(*_args, **kwargs))


def timerX(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.timerX(*_args, **kwargs))


def toggle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.toggle(*_args, **kwargs))


def toggleAxis(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.toggleAxis(*_args, **kwargs))


def toggleDisplacement(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.toggleDisplacement(*_args, **kwargs))


def toggleWindowVisibility(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.toggleWindowVisibility(*_args, **kwargs))


def tokenize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.tokenize(*_args, **kwargs))


def tolerance(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.tolerance(*_args, **kwargs))


def tolower(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.tolower(*_args, **kwargs))


def toolBar(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.toolBar(*_args, **kwargs))


def toolButton(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.toolButton(*_args, **kwargs))


def toolCollection(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.toolCollection(*_args, **kwargs))


def toolDropped(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.toolDropped(*_args, **kwargs))


def toolHasOptions(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.toolHasOptions(*_args, **kwargs))


def toolPropertyWindow(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.toolPropertyWindow(*_args, **kwargs))


def torus(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.torus(*_args, **kwargs))


def toupper(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.toupper(*_args, **kwargs))


def trace(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.trace(*_args, **kwargs))


def track(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.track(*_args, **kwargs))


def trackCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.trackCtx(*_args, **kwargs))


def transferAttributes(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.transferAttributes(*_args, **kwargs))


def transferShadingSets(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.transferShadingSets(*_args, **kwargs))


def transformCompare(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.transformCompare(*_args, **kwargs))


def transformLimits(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.transformLimits(*_args, **kwargs))


def translator(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.translator(*_args, **kwargs))


def treeLister(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.treeLister(*_args, **kwargs))


def treeView(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.treeView(*_args, **kwargs))


def trim(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.trim(*_args, **kwargs))


def trimCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.trimCtx(*_args, **kwargs))


def trunc(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.trunc(*_args, **kwargs))


def truncateFluidCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.truncateFluidCache(*_args, **kwargs))


def truncateHairCache(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.truncateHairCache(*_args, **kwargs))


def tumble(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.tumble(*_args, **kwargs))


def tumbleCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.tumbleCtx(*_args, **kwargs))


def turbulence(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.turbulence(*_args, **kwargs))


def twoPointArcCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.twoPointArcCtx(*_args, **kwargs))


def u3dAutoSeam(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.u3dAutoSeam(*_args, **kwargs))


def u3dLayout(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.u3dLayout(*_args, **kwargs))


def u3dOptimize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.u3dOptimize(*_args, **kwargs))


def u3dTopoValid(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.u3dTopoValid(*_args, **kwargs))


def u3dUnfold(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.u3dUnfold(*_args, **kwargs))


def ubercam(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ubercam(*_args, **kwargs))


def uiTemplate(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.uiTemplate(*_args, **kwargs))


def unapplyOverride(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.unapplyOverride(*_args, **kwargs))


def unassignInputDevice(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.unassignInputDevice(*_args, **kwargs))


def undo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.undo(*_args, **kwargs))


def undoInfo(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.undoInfo(*_args, **kwargs))


def unfold(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.unfold(*_args, **kwargs))


def ungroup(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.ungroup(*_args, **kwargs))


def uniform(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.uniform(*_args, **kwargs))


def unit(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.unit(*_args, **kwargs))


def unknownNode(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.unknownNode(*_args, **kwargs))


def unknownPlugin(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.unknownPlugin(*_args, **kwargs))


def unloadPlugin(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.unloadPlugin(*_args, **kwargs))


def untangleUV(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.untangleUV(*_args, **kwargs))


def untrim(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.untrim(*_args, **kwargs))


def upAxis(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.upAxis(*_args, **kwargs))


def userCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.userCtx(*_args, **kwargs))


def uvLink(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.uvLink(*_args, **kwargs))


def uvSnapshot(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.uvSnapshot(*_args, **kwargs))


def vectorize(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.vectorize(*_args, **kwargs))


def vectornum(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.vectornum(*_args, **kwargs))


def view2dToolCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.view2dToolCtx(*_args, **kwargs))


def viewCamera(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.viewCamera(*_args, **kwargs))


def viewClipPlane(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.viewClipPlane(*_args, **kwargs))


def viewFit(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.viewFit(*_args, **kwargs))


def viewHeadOn(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.viewHeadOn(*_args, **kwargs))


def viewLookAt(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.viewLookAt(*_args, **kwargs))


def viewManip(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.viewManip(*_args, **kwargs))


def viewPlace(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.viewPlace(*_args, **kwargs))


def viewSet(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.viewSet(*_args, **kwargs))


def visor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.visor(*_args, **kwargs))


def volumeAxis(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.volumeAxis(*_args, **kwargs))


def volumeBind(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.volumeBind(*_args, **kwargs))


def vortex(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.vortex(*_args, **kwargs))


def waitCursor(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.waitCursor(*_args, **kwargs))


def walkCtx(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.walkCtx(*_args, **kwargs))


def warning(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.warning(*_args, **kwargs))


def webBrowser(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.webBrowser(*_args, **kwargs))


def webBrowserPrefs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.webBrowserPrefs(*_args, **kwargs))


def webView(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.webView(*_args, **kwargs))


def webViewCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.webViewCmd(*_args, **kwargs))


def weightEditorCmd(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.weightEditorCmd(*_args, **kwargs))


def wfnum(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.wfnum(*_args, **kwargs))


def whatIs(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.whatIs(*_args, **kwargs))


def whatsNewHighlight(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.whatsNewHighlight(*_args, **kwargs))


def window(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.window(*_args, **kwargs))


def windowPref(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.windowPref(*_args, **kwargs))


def wire(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.wire(*_args, **kwargs))


def wireContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.wireContext(*_args, **kwargs))


def workspace(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.workspace(*_args, **kwargs))


def workspaceControl(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.workspaceControl(*_args, **kwargs))


def workspaceControlState(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.workspaceControlState(*_args, **kwargs))


def workspaceLayoutManager(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.workspaceLayoutManager(*_args, **kwargs))


def workspacePanel(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.workspacePanel(*_args, **kwargs))


def wrinkle(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.wrinkle(*_args, **kwargs))


def wrinkleContext(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.wrinkleContext(*_args, **kwargs))


def writeTake(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.writeTake(*_args, **kwargs))


def xform(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.xform(*_args, **kwargs))


def xformConstraint(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.xformConstraint(*_args, **kwargs))


def xpmPicker(*args, **kwargs):
    _args = _wpc.to_string(args)
    return _wpc.to_object(_cmds.xpmPicker(*_args, **kwargs))




