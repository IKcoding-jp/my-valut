---
id: H26H_KA_Q05
year: H26春
kamoku: A
number: 5
type: 暗記
field: テクノロジ系 » 基礎理論 »情報に関する理論
difficulty: 3
status: 未学習
source: "出典：平成26年春期 基本情報技術者試験 科目A 問5"
source_url: "https://www.fe-siken.com/kakomon/26_haru/q5.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
次の表は，文字列を検査するための状態遷移表である。検査では，初期状態をaとし，文字列の検査中に状態がeになれば不合格とする。
解答群で示される文字列のうち，不合格となるものはどれか。ここで，文字列は左端から検査し，解答群中の△は空白を表す。![05.png/image-size:313×119](https://www.fe-siken.com/kakomon/26_haru/img/05.png)

## 選択肢
- ア: ＋0010
- イ: －1
- ウ: 12.2
- エ: 9.△

## 正解
ウ

## 解説
### 各選択肢の解説
- ア: c(符号)→b(数字)→b(数字)→b(数字)→b(数字)と遷移するので問題ありません。
- イ: c(符号)→b(数字)と遷移するので問題ありません。
- ウ: b(数字)→b(数字)→d(小数点)と遷移し、現在の状態がdであり次の文字が数字であるのでeに遷移します。したがって不合格となります。
- エ: b(数字)→d(小数点)→a(空白)と遷移するので問題ありません。

### 関連概念
