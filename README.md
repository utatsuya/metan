# metan

Autodesk Maya Python API2.0 をPyMelライクに利用するためのラッパーライブラリを作成中です

#### 現時点でできること

  * アトリビュートの値の取得
  * アトリビュートへ値を設定
  * オブジェクト同士の比較 
  * metan.core.selected()
  * DependNode.listAttrStr(), _listAttr() [issues#9](https://github.com/utatsuya/metan/issues/9)
  * DependNode.hasAttr() [issues#10](https://github.com/utatsuya/metan/issues/10)
  * Attribute()をキャッシュして高速化 [issues#5](https://github.com/utatsuya/metan/issues/5)
  * MetanObject.listConnections(),inputs(),outputs() [issues#11](https://github.com/utatsuya/metan/issues/11)
  * アトリビュートの接続・解除（Attribute.connnect(),disconnect()）
  * コネクションの取得（Attribute.inputs(),outputs(),connections(),isConnected()）

※getsetは内部単位で扱います。例えば、回転値はUI上ではDegreeとなっていてもmetanでは常にRadianです。
  
#### まだできないこと（未実装なもの）

  * SRT関係のメソッド（Transform.getTranslation()など）
  * ノードタイプ固有のメソッド（DagNode.getShapes(),など）
  * その他もろもろ(addAttr,deleteAttr,addChild,getChildren,hasChild,numChildren,hasParent,getParent,setParent....

#### プロファイル結果

  ```
  import maya.cmds as cmds
  import pymel.core as pm
  import pymel.core.datatypes as dt
  import metan.debug as dbg

  cmds.polyCube()[0]

  # cubeのtranslateXの値を1000回取得
  # pymel:0.09s, metan:0.015s

  func = pm.PyNode(u"pCube1").t.tx.get
  print dbg.run_profile(func, count=1000)()
  func = mtn.M(u"pCube1").t.tx.get
  print dbg.run_profile(func, count=1000)()


  # cubeのmatrixの値を1000回取得
  # pymel:1.56s, metan:0.031s

  func = pm.PyNode(u"pCube1").m.get
  print dbg.run_profile(func, count=1000)()
  func = mtn.M(u"pCube1").m.get
  print dbg.run_profile(func, count=1000)()


  # cubeのtranslateXに1000回設定
  # pymel:0.112s, metan(cmds):0.074s, metan(api):0.027s

  print dbg.run_profile(pm.PyNode(u"pCube1").tx.set, count=1000)(1)
  print dbg.run_profile(mtn.M(u"pCube1").tx.set, count=1000)(1)
  print dbg.run_profile(mtn.M(u"pCube1").tx._set, count=1000)(1) #APIを利用したsetのためundo不可


  # cubeのtranslateに1000回設定 その１
  # pymel:0.136s, metan(cmds):0.084s, metan(api):0.067s

  print dbg.run_profile(pm.PyNode(u"pCube1").t.set, count=1000)(1,2,3)
  print dbg.run_profile(mtn.M(u"pCube1").t.set, count=1000)(1,2,3)
  print dbg.run_profile(mtn.M(u"pCube1").t._set, count=1000)(1,2,3) #APIを利用したsetのためundo不可


  # cubeのtranslateに1000回設定 その２
  # pymel:0.244s, metan(cmds):0.087s, metan(api):0.050s

  print dbg.run_profile(pm.PyNode(u"pCube1").t.set, count=1000)([1,2,3])
  print dbg.run_profile(mtn.M(u"pCube1").t.set, count=1000)([1,2,3])
  print dbg.run_profile(mtn.M(u"pCube1").t._set, count=1000)([1,2,3]) #APIを利用したsetのためundo不可


  # cubeのtranslateに1000回設定 その３
  # pymel:0.181s, metan(cmds):0.098s, metan(api):0.063s

  print dbg.run_profile(pm.PyNode(u"pCube1").t.set, count=1000)(dt.Vector(1,2,3))
  print dbg.run_profile(mtn.M(u"pCube1").t.set, count=1000)(mtn.Vector(1,2,3))
  print dbg.run_profile(mtn.M(u"pCube1").t._set, count=1000)(mtn.Vector(1,2,3)) #APIを利用したsetのためundo不可


  # addMatrixのinput[0]にMatrixを100回設定
  # pymel:1.367s, metan(cmds):0.026s, metan(api):0.011s

  cmds.createNode(u"addMatrix")
  print dbg.run_profile(pm.PyNode(u"addMatrix1").i[0].set, count=100)(dt.Matrix())
  print dbg.run_profile(mtn.M(u"addMatrix1").i[0].set, count=100)(mtn.Matrix(mtn.Matrix()))
  print dbg.run_profile(mtn.M(u"addMatrix1").i[0]._set, count=100)(mtn.Matrix()) #APIを利用したsetのためundo不可
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
  
  m.tx.set(1.0)
  m.t.set(mtn.Vector(1,1,1))
  m.r.set(mtn.EulerRotation(1,1,1))
  m.s.set(1.5, 1.5, 1.5)
  
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
  # Result: Matrix(((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))) # 

  # インスタンスの異なるオブジェクト同士の比較
  mtn.M(u"pCube1").t.tx == mtn.M(u"pCube1.tx") # True
  mtn.M(u"pCube1").attr("t.tx") == mtn.M(u"pCube1").attr("translate").attr("translateX") # True
  mtn.M(u"pCube1").wm == mtn.M(u"pCube1").wm[0] #False
  ```
  
  詳しくは、テストコード（
[test_wrapper.py](/python/metan/tests/test_wrapper.py)
）を確認してください

```
# Mayaシーン上でテストコードを実行する
import metan.tests
metan.tests.run()
```
