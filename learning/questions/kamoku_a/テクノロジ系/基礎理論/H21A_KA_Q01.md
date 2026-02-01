---
id: H21A_KA_Q01
year: H21秋
kamoku: A
number: 1
type: 混合
field: テクノロジ系 » 基礎理論 »応用数学
difficulty: 3
status: 未学習
source: "出典：平成21年秋期 基本情報技術者試験 科目A 問1"
source_url: "https://www.fe-siken.com/kakomon/21_aki/q1.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
N個の観測値の平均値を算出する式はどれか。ここで，SはN個の観測値の和(ただし，S＞0)とし，[X]は X以下で最大の整数とする。また，平均値は，小数第1位を四捨五入して整数値として求める。

## 選択肢
- ア: ![01a.png/image-size:55×34](https://www.fe-siken.com/kakomon/21_aki/img/01a.png)
- イ: ![01i.png/image-size:55×34](https://www.fe-siken.com/kakomon/21_aki/img/01i.png)
- ウ: ![01u.png/image-size:55×34](https://www.fe-siken.com/kakomon/21_aki/img/01u.png)
- エ: ![01e.png/image-size:55×34](https://www.fe-siken.com/kakomon/21_aki/img/01e.png)

## 正解
エ

## 解説
通常平均値を求めるには、観測値の和÷観測値の個数(S／N)となるのですが、平均値を四捨五入して整数値で求めるので計算に工夫が必要になります。具体的には小数第1位を四捨五入して、整数値で求めるということなので、小数部分が5以上の時は切り上げ、4以下は切り下げの処理を行うことが求められます。
このようなことを行うには普通に計算された平均値(S／N)に0.5を足してから小数部分を切り捨てます。これにより四捨五入と同様の効果を得ることができます。
例)小数第1位が 6, 5, 4の場合
2.6＋0.5＝3.1 (小数部分を切り捨て)→ 3
2.5＋0.5＝3
2.4＋0.5＝2.9 (小数部分を切り捨て)→ 2
上の例を見ると四捨五入が行われ、整数での解になることが確認できます。
したがって適切な式は「エ」になります。

### 関連概念
