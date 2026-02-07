---
id: H23T_KA_Q06
year: H23特
kamoku: A
number: 6
type: 理解
field: テクノロジ系 » アルゴリズムとプログラミング »アルゴリズム
difficulty: 3
status: 未学習
source: "出典：平成23年特別 基本情報技術者試験 科目A 問6"
source_url: "https://www.fe-siken.com/kakomon/23_toku/q6.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
関数 ƒ(x，y)が次のように定義されているとき，ƒ(775，527)の値は幾らか。ここで，x mod yはxをyで割った余りを返す。ƒ(x, y): if y = 0 then return x else return ƒ(y,  x mod y)

## 選択肢
- ア: 0
- イ: 31
- ウ: 248
- エ: 527

## 正解
イ

## 解説
再帰関数になっているので、段階的に計算していきます。
したがって、関数ƒ(775, 527)によって返却される数値は
31
になります。

### 各選択肢の解説
ƒ(775, 527)＝ƒ(527, 775 mod 527)※775÷527＝1 余り 248
ƒ(527, 248)＝ƒ(248, 527 mod 248)※527÷248＝2 余り 31
ƒ(248, 31)＝ƒ(31, 248 mod 31)※248÷31＝8 余り 0
ƒ(31, 0)＝（y=0なので）xを返却

### 関連概念
