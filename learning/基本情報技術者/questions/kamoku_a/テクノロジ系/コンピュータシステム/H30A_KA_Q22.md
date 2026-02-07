---
id: H30A_KA_Q22
year: H30秋
kamoku: A
number: 22
type: 暗記
field: テクノロジ系 » ハードウェア »ハードウェア
difficulty: 3
status: 未学習
source: "出典：平成30年秋期 基本情報技術者試験 科目A 問22"
source_url: "https://www.fe-siken.com/kakomon/30_aki/q22.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
2入力NAND素子を用いて4入力NAND回路を構成したものはどれか。

## 選択肢
- ア: ![22a.png/image-size:95×72](https://www.fe-siken.com/kakomon/30_aki/img/22a.png)
- イ: ![22i.png/image-size:139×71](https://www.fe-siken.com/kakomon/30_aki/img/22i.png)
- ウ: ![22u.png/image-size:195×164](https://www.fe-siken.com/kakomon/30_aki/img/22u.png)
- エ: ![22e.png/image-size:225×161](https://www.fe-siken.com/kakomon/30_aki/img/22e.png)

## 正解
イ

## 解説
否定論理積(2入力NAND)は、2つの入力がともに1のときにだけ結果が0、その他の場合は1となる論理演算です。NAND素子を組み合わせることによってAND、OR、XOR、NOT、NORなどの回路を構成することができます。
そして、多入力NANDは入力が1つでも"0"なら"1"を返す論理回路です。本問では4入力NANDを構成することになっているので、4つの入力のいずれかが"0"であるときに"1"を出力する、または全ての入力が"1"のときに"0"を出力する論理回路になっていればよい訳です。
まず、4つの入力に"1"を設定したときに"0"を出力するか否かによって正しい論理回路図を選別していきます。
この時点で「ア」と「ウ」は不適切であると判断できます。残った「イ」と「エ」について検証を続けます。ここでは4つの入力に"1010"を与えた場合の出力を見てみます。
消去法により「イ」が4入力NAND回路と判断できます。なお「エ」は4入力NOR回路です。

### 関連概念
