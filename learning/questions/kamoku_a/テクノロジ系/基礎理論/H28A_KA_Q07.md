---
id: H28A_KA_Q07
year: H28秋
kamoku: A
number: 7
type: 理解
field: テクノロジ系 » アルゴリズムとプログラミング »アルゴリズム
difficulty: 3
status: 未学習
source: "出典：平成28年秋期 基本情報技術者試験 科目A 問7"
source_url: "https://www.fe-siken.com/kakomon/28_aki/q7.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
整数x，y(x＞y≧0)に対して，次のように定義された関数F(x，y)がある。F(231，15)の値は幾らか。ここで，x mod y はxをyで割った余りである。![07.png/image-size:251×37](https://www.fe-siken.com/kakomon/28_aki/img/07.png)

## 選択肢
- ア: 2
- イ: 3
- ウ: 5
- エ: 7

## 正解
イ

## 解説
「y＞0 のとき F(x，y) = F(y，x mod y) 」と決められているということは、左辺を右辺の形に変換できるということです。すなわち、右辺の第1引数には左辺の第2引数(y)を与え、右辺の第2引数には x mod y を与えて計算すればよいわけです。
最初の F(231，15) … x＝231、y＝15の場合、231 mod 15 = 6 ですから F(231，15) = F(15，6) です。これを繰り返しながら最終的な値を求めていきます。
F(231，15)
＝F(15，231 mod 15)＝F(15，6)
＝F(6，15 mod 6)＝F(6，3)
＝F(3，6 mod 3)＝F(3，0)
＝3
したがって正解は「3」になります。

### 関連概念
