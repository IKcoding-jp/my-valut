---
id: H29H_KA_Q03
year: H29春
kamoku: A
number: 3
type: 混合
field: テクノロジ系 » 基礎理論 »離散数学
difficulty: 3
status: 未学習
source: "出典：平成29年春期 基本情報技術者試験 科目A 問3"
source_url: "https://www.fe-siken.com/kakomon/29_haru/q3.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
XとYの否定論理積 X NAND Yは，NOT(X AND Y)として定義される。X OR YをNANDだけを使って表した論理式はどれか。

## 選択肢
- ア: ((X NAND Y) NAND X) NAND Y
- イ: (X NAND X) NAND (Y NAND Y)
- ウ: (X NAND Y) NAND (X NAND Y)
- エ: X NAND (Y NAND (X NAND Y))

## 正解
イ

## 解説
否定論理積
(NAND)は、2つの入力がともに1の場合にだけ結果が0、その他の場合は1となる論理演算です。
X OR Yは、下の真理値表で表される論理演算なので、これをもとに各選択肢のXとYに0または1を代入してOR演算と同様の結果になるかどうかを検証します。
まずX＝0，Y＝0のときに演算結果が0になるかを検証します。
次に正しい可能性のある「イ」と「ウ」について、X＝1，Y＝0のときに演算結果が1になるか検証します。
したがって残った「イ」が答えとして適切です。
また4つの論理式をベン図で表すと次のようになります。
こちらの方法でも正解を導くことが可能です。

### 各選択肢の解説
- ア: ((0 NAND 0)NAND 0)NAND 0＝(1 NAND 0) NAND 0＝1 NAND 0＝1結果が0ではないので誤りとわかります。
- イ: (0 NAND 0)NAND(0 NAND 0)＝1 NAND 1＝0結果が0なので正しい可能性があります。
- ウ: (0 NAND 0)NAND(0 NAND 0)＝1 NAND 1＝0結果が0なので正しい可能性があります。
- エ: 0 NAND(0 NAND(0 NAND 0))＝0 NAND (0 NAND 1)＝0 NAND 1＝1結果が0ではないので誤りとわかります。
「イ」(1 NAND 1) NAND (0 NAND 0)＝0 NAND 1＝1
「ウ」(1 NAND 0) NAND (1 NAND 0)＝1 NAND 1＝0結果が1ではないので誤りとわかります。

### 関連概念
- [[NAND]]
