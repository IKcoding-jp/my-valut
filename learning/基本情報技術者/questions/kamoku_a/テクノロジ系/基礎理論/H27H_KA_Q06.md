---
id: H27H_KA_Q06
year: H27春
kamoku: A
number: 6
type: 混合
field: テクノロジ系 » アルゴリズムとプログラミング »アルゴリズム
difficulty: 3
status: 未学習
source: "出典：平成27年春期 基本情報技術者試験 科目A 問6"
source_url: "https://www.fe-siken.com/kakomon/27_haru/q6.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
整列されたn個のデータの中から，求める要素を2分探索法で探索する。この処理の計算量のオーダーを表す式はどれか。

## 選択肢
- ア: log n
- イ: n
- ウ: n2
- エ: n log n

## 正解
ア

## 解説
2分探索法
は、要素が昇順または降順に整列された集合に対して、探索範囲を1／2に狭めて探索することを再帰的に繰り返して目的のデータを探索するアルゴリズムです。
2分探索法では、データの個数 n と計算量 x の関係は下表のようになっています。
この関係を立式すると
n＝2
x
2を底として対数(log)をとると、
log
2
n＝x
つまり計算量のオーダーは
O
(log n) になります。

### 関連概念
- [[アルゴリズム]]
