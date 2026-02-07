---
id: R01H_KA_Q28
year: R01春
kamoku: A
number: 28
type: 暗記
field: テクノロジ系 » データベース »データ操作
difficulty: 3
status: 未学習
source: "出典：令和元年春期 基本情報技術者試験 科目A 問28"
source_url: "https://www.fe-siken.com/kakomon/31_haru/q28.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
関係モデルにおいて表Xから表Yを得る関係演算はどれか。![28.png/image-size:427×166](https://www.fe-siken.com/kakomon/31_haru/img/28.png)

## 選択肢
- ア: 結合(join)
- イ: 射影(projection)
- ウ: 選択(selection)
- エ: 併合(merge)

## 正解
イ

## 解説
関係データベースの理論である関係モデルでは、表を集合演算及び関係演算によって操作します。関係演算には、結合、射影、選択、商があり、それぞれ以下の操作を行うものです（"併合"という演算は存在しません）。
結合複数の表を共通する属性で結合して1つの表にする操作射影表から指定された列を抽出する操作選択表から指定された行を抽出する操作商表Rのうち表Sの全ての項目を含む行の集合を返す演算
表Yは、表Xから"商品番号"列と"数量"列を取り出してできた表なので、適切な演算名は「射影」になります。

### 関連概念
- [[データベース]]
