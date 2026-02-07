---
id: H29H_KA_Q22
year: H29春
kamoku: A
number: 22
type: 混合
field: テクノロジ系 » ハードウェア »ハードウェア
difficulty: 3
status: 未学習
source: "出典：平成29年春期 基本情報技術者試験 科目A 問22"
source_url: "https://www.fe-siken.com/kakomon/29_haru/q22.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
図に示す，1桁の2進数xとyを加算して，z(和の1桁目)及びc(桁上げ)を出力する半加算器において，AとBの素子の組合せとして，適切なものはどれか。![22.png/image-size:292×63](https://www.fe-siken.com/kakomon/29_haru/img/22.png)

## 選択肢


## 正解
ア

## 解説
桁上げの出力cは入力される2つの数値がともに"1"のときにだけ"1"を出力します。この関係はAND回路(論理積)の真理値表と一致します。
また和の1桁目zは、入力される2つの数値が同じ場合に"0"、異なる場合には"1"が出力されます。この関係はXOR回路(排他的論理和)の真理値表と一致します。
したがって、zを決定するAの回路は
排他的論理和
(XOR)、cを決定するBの回路は
論理積
（AND）です。

### 関連概念
