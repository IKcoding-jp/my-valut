---
id: H24H_KA_Q52
year: H24春
kamoku: A
number: 52
type: 混合
field: マネジメント系 » プロジェクトマネジメント »プロジェクトの時間
difficulty: 3
status: 未学習
source: "出典：平成24年春期 基本情報技術者試験 科目A 問52"
source_url: "https://www.fe-siken.com/kakomon/24_haru/q52.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
プロジェクトのタイムマネジメントのために次のアローダイアグラムを作成した。クリティカルパスはどれか。![52.png/image-size:323×173](https://www.fe-siken.com/kakomon/24_haru/img/52.png)

## 選択肢
- ア: A→C→E→F
- イ: A→D→G
- ウ: B→E→F
- エ: B→E→G

## 正解
ウ

## 解説
プロジェクト開始から完了に至るまでに存在する工程の流れには、以下の5通りがあります。
これらすべての経路について所要日数を求め、その中で所要日数が最大となる経路がクリティカルパスです。※点線で表されるダミー作業は作業日数0日として計算します。
[A→D→G]1＋3＋4＝8日[A→C→E→(ダミー作業)→G]1＋3＋4＋0＋4＝12日[A→C→E→F]1＋3＋4＋5＝13日[B→E→(ダミー作業)→G]5＋4＋0＋4＝13日[B→E→F]5＋4＋5＝14日
したがって、最も日数を要する「B→E→F」がクリティカルパスとなります。

### 各選択肢の解説
A→D→G
A→C→E→(ダミー作業)→G
A→C→E→F
B→E→(ダミー作業)→G　※選択肢「エ」では単にB→E→Gとして表記
B→E→F

### 関連概念
