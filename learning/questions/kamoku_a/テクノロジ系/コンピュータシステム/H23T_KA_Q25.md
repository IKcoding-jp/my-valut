---
id: H23T_KA_Q25
year: H23特
kamoku: A
number: 25
type: 混合
field: テクノロジ系 » ハードウェア »ハードウェア
difficulty: 3
status: 未学習
source: "出典：平成23年特別 基本情報技術者試験 科目A 問25"
source_url: "https://www.fe-siken.com/kakomon/23_toku/q25.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
図に示す1けたの2進数xとyを加算し，z(和の1けた目)及びc(けた上げ)を出力する半加算器において，AとBの素子の組合せとして，適切なものはどれか。![25.png/image-size:268×57](https://www.fe-siken.com/kakomon/23_toku/img/25.png)

## 選択肢


## 正解
ア

## 解説
桁上げの出力cは入力される2つの数値がともに"1"のときにだけ"1"を出力します。この関係はAND回路(論理積)の真理値表と一致します。
また和の1桁目zは、入力される2つの数値が同じ場合に"0"、異なる場合には"1"が出力されます。この関係はXOR回路(排他的論理和)の真理値表と一致します。
したがって、Aの回路は
排他的論理和
(XOR)、Bの回路は
論理積
（AND）です。

### 関連概念
