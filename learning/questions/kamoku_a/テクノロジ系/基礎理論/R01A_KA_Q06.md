---
id: R01A_KA_Q06
year: R01秋
kamoku: A
number: 6
type: 混合
field: テクノロジ系 » 基礎理論 »応用数学
difficulty: 3
status: 未学習
source: "出典：令和元年秋期 基本情報技術者試験 科目A 問6"
source_url: "https://www.fe-siken.com/kakomon/01_aki/q6.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
Random(n)は，0以上n未満の整数を一様な確率で返す関数である。整数型の変数A，B及びCに対して次の一連の手続を実行したとき，Cの値が0になる確率はどれか。

A＝Random(10)
B＝Random(10)
C＝A－B

## 選択肢
- ア: 1100
- イ: 120
- ウ: 110
- エ: 15

## 正解
ウ

## 解説
Random(10)の返す値は整数0～9なので、Aがとり得る値は10種類、Bも同様に10種類となります。これより、確率の分母となるAとBの組合せ総数は次のように計算できます。
10通り×10通り＝100通り
Cの値が0、すなわち「A－B＝0」となるのは、AとBが同じ値のときのみです。これは、A=B=0，A=B=1，…，A=B=9 というように全部で10通りあります。
したがって、Cの値が0になる確率は、
10通り／100通り＝1／10
となります。

### 関連概念
