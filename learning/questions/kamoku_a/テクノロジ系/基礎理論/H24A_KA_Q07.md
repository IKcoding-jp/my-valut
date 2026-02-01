---
id: H24A_KA_Q07
year: H24秋
kamoku: A
number: 7
type: 混合
field: テクノロジ系 » アルゴリズムとプログラミング »アルゴリズム
difficulty: 3
status: 未学習
source: "出典：平成24年秋期 基本情報技術者試験 科目A 問7"
source_url: "https://www.fe-siken.com/kakomon/24_aki/q7.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
n!の値を，次の関数F(n)によって計算する。乗算の回数を表す式はどれか。![07.png/image-size:199×49](https://www.fe-siken.com/kakomon/24_aki/img/07.png)

## 選択肢
- ア: n－1
- イ: n
- ウ: n2
- エ: n!

## 正解
イ

## 解説
仮の値として5!で確かめてみると、
F(5)＝5×F(4)
＝5×4×F(3)
＝5×4×3×F(2)
＝5×4×3×2×F(1)
＝5×4×3×2×1×F(0)
＝5×4×3×2×1×1
関数の引数である5に対して乗算の回数は5回なので、引数がnである場合の乗算の回数はn回になるとわかります。

### 関連概念
