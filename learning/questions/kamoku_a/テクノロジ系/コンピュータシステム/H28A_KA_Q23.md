---
id: H28A_KA_Q23
year: H28秋
kamoku: A
number: 23
type: 混合
field: テクノロジ系 » ハードウェア »ハードウェア
difficulty: 3
status: 未学習
source: "出典：平成28年秋期 基本情報技術者試験 科目A 問23"
source_url: "https://www.fe-siken.com/kakomon/28_aki/q23.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
真理値表に示す3入力多数決回路はどれか。![23.png/image-size:151×196](https://www.fe-siken.com/kakomon/28_aki/img/23.png)

## 選択肢
- ア: ![23a.png/image-size:176×99](https://www.fe-siken.com/kakomon/28_aki/img/23a.png)
- イ: ![23i.png/image-size:173×99](https://www.fe-siken.com/kakomon/28_aki/img/23i.png)
- ウ: ![23u.png/image-size:175×99](https://www.fe-siken.com/kakomon/28_aki/img/23u.png)
- エ: ![23e.png/image-size:174×99](https://www.fe-siken.com/kakomon/28_aki/img/23e.png)

## 正解
ア

## 解説
3入力多数決回路なので、真理値表にあるように3つの入力中2つ以上が"1"（＝"1"が多数）であれば結果に"1"を出力、そして2つ以上が"0"（＝"0"が多数）であれば結果に"0"を出力するものになっている必要があります。
回路ごとにA、B、Cの値を与えた場合の出力を照合していくと、正しいのは「ア」の回路とわかります。
「ア」の回路は、論理的には次のような演算を行う回路と考えられます。

### 各選択肢の解説
まず「A，B」「A，C」「B，C」それぞれの論理積を求める。
3つの論理積演算の結果に"1"が現れれば、3つの入力中に"1"が2つ以上あることが確定する。逆に"1"が現れなければ3つの入力中の"1"の個数は1以下ということになる。
3つの論理積演算の結果の中に少なくとも"1"が1つ以上ある場合には"1"(可決)、そうでなければ"0"(否決)を出力すればよいので、3つの演算結果を論理和演算した結果を最終的な出力とする。
- ア: 正しい。
- イ: この回路図は真理値表は以下のようになるため誤りです。
- ウ: この回路図は真理値表は以下のようになるため誤りです。
- エ: この回路図は真理値表は以下のようになるため誤りです。

### 関連概念
