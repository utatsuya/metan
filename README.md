# metan

Autodesk Maya Python API2.0 をPyMelライクに利用するためのラッパーライブラリを作成中です

#### 現時点でできること

  * オブジェクト生成
  * アトリビュートの値の取得

#### まだできないこと

  * 値の設定全般
  * その他多くのことができません
  
#### プロファイル結果

  ```
  import metan.debug as dbg
  import pymel.core as pm
  cmds.polyCube()[0]
  
  # cubeのtranslateXの値を1000回取得
  # pymel:0.09s, metan:0.015s
  
  func = pm.PyNode(u"pCube1").t.tx.get
  print dbg.run_profile(func, count=1000)()
  func = mtn.M(u"pCube1").t.tx.get
  print dbg.run_profile(func, count=1000)()
  
  
  # cubeのmatrixの値を1000回取得
  # pymel:1.56s, metan:0.023s
  
  func = pm.PyNode(u"pCube1").m.get
  print dbg.run_profile(func, count=1000)()
  func = mtn.M(u"pCube1").m.get
  print dbg.run_profile(func, count=1000)()
  
  
  ```
  
#### 記述例
  ```
  import metan.core as mtn
  import maya.cmds as cmds
  cube = cmds.polyCube()[0]
  m = mtn.M(cube)
  
  m.t.name()
  m.attr("t").name()
  m.attr("translate").name()
  mtn.M(u"pCube1.t").name()
  mtn.M(u"pCube1.translate").name()
  # Rsult: u'pCube1.translate' # 
  
  m.tx.name()
  m.t.tx.name()
  m.t.x.name()
  mtn.M(u"pCube1.t.tx").name()
  mtn.M(u"pCube1.translate.translateX").name()
  mtn.M(u"pCube1.translateX").name()
  m.attr("t.tx").name()
  m.attr("translate.tx").name()
  m.attr("translate.translateX").name()
  # Result: u'pCube1.translateX' # 
  
  m.t.get()
  # Result: [0, 0, 0] # 
  
  m.tx.get()
  # result : 0.0 # 
  
  m.wm.name()
  m.worldMatrix.name()
  m.attr("wm").name()
  # Result: u'pCube1.worldMatrix' # 
  
  m.wm[0].name()
  m.worldMatrix[0].name()
  m.attr("wm[0]").name()
  m.attr("wm")[0].name()
  # Result: u'pCube1.worldMatrix[0]' # 
  
  m.wm.get()
  m.wm[0].get()
  # Result: maya.api.OpenMaya.MMatrix(((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))) # 
  ```
  
  詳しくは、テストコード（
[test_wrapper.py](/tests/test_wrapper.py)
）を確認してください

```
# Mayaシーン上でテストコードを実行する
import metan.tests
metan.tests.run()
```
