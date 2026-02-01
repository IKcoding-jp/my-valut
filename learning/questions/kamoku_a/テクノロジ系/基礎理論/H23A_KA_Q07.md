---
id: H23A_KA_Q07
year: H23秋
kamoku: A
number: 7
type: 暗記
field: テクノロジ系 » アルゴリズムとプログラミング »アルゴリズム
difficulty: 3
status: 未学習
source: "出典：平成23年秋期 基本情報技術者試験 科目A 問7"
source_url: "https://www.fe-siken.com/kakomon/23_aki/q7.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
要素番号が0から始まる配列 TANGO がある。n個の単語が TANGO[1] から TANGO[n] に入っている。図は，n番目の単語を TANGO[1] に移動するために，TANGO[1] から TANGO[n－1] の単語を順に一つずつ後ろにずらして単語表を再構成する流れ図である。aに入れる処理として，適切なものはどれか。![07.png/image-size:347×217](https://www.fe-siken.com/kakomon/23_aki/img/07.png)

## 選択肢
- ア: TANGO[i]→TANGO[i＋1]
- イ: TANGO[i]→TANGO[n－i]
- ウ: TANGO[i＋1]→TANGO[n－i]
- エ: TANGO[n－i]→TANGO[i]

## 正解
ア

## 解説
最後の要素である TANGO[n] を TANGO[1] に移動する場合を考えてみます。
まず、ループ処理の前に TANGO[n] のデータを TANGO[0] にコピーします。
次のループ処理で単語を順に一つずつ後ろにずらすには、TANGO[4]→TANGO[5]，TANGO[3]→TANGO[4] というように前の1つ前の配列要素のデータをコピーしていく処理が必要です。
ループ処理は、変数iが、n－1(配列要素のうち最後の1つ前) から 0(最初) まで続きます。aに入る処理をループ変数iで表すと、現在の配列要素 TANGO[i] を値を1つ後ろの配列要素 TANGO[i＋1] にコピーする TANGO[i]→TANGO[i＋1] が適切です。

### 関連概念
- [[TANGO]]
