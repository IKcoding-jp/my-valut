---
id: H26H_KA_Q06
year: H26春
kamoku: A
number: 6
type: 暗記
field: テクノロジ系 » アルゴリズムとプログラミング »アルゴリズム
difficulty: 3
status: 未学習
source: "出典：平成26年春期 基本情報技術者試験 科目A 問6"
source_url: "https://www.fe-siken.com/kakomon/26_haru/q6.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
2分木の各ノードがもつ記号を出力する再帰的なプログラムProc(n)の定義は，次のとおりである。このプログラムを，図の2分木の根(最上位のノード)に適用したときの出力はどれか。

Proc(ノードn){
nに左の子lがあればProc(l)を呼び出す
nに右の子rがあればProc(r)を呼び出す
nに書かれた記号を出力する
}![06.png/image-size:124×148](https://www.fe-siken.com/kakomon/26_haru/img/06.png)

## 選択肢
- ア: ＋a*－bcd
- イ: a＋b－c*d
- ウ: abc－d*＋
- エ: b－c*d＋a

## 正解
ウ

## 解説
与えられたプログラムを設問の2分木に適用すると次のようになります。
出力された記号を順番に並べると「abc－d*＋」になります。

### 各選択肢の解説
最初に2分木の根である"+"から始まります。[proc(+)]"+"の左には"a"があるので、Proc(a)が呼び出されます。
[Proc(a)]"a"の左右にはノードがないので、aを出力し、Proc(+)の処理に戻ります。
"+"の右には"*"があるので、Proc(*)が呼び出されます。
[Proc(*)]"*"の左には"-"があるので、Proc(-)が呼び出されます。
[Proc(-)]"-"の左には"b"があるので、Proc(b)が呼び出されます。
[Proc(b)]"b"の左右にはノードがないので、bを出力し、Proc(-)の処理に戻ります。
"-"の右には"c"があるので、Proc(c)が呼び出されます。
[Proc(c)]"c"の左右にはノードがないので、cを出力し、Proc(-)の処理に戻ります。
Proc(-)は、-を出力し、Proc(*)に戻ります。
"*"の右には"d"があるので、Proc(d)が呼び出されます。
[Proc(d)]"d"の左右にはノードがないので、dを出力し、Proc(*)の処理に戻ります。
Proc(*)は、*を出力し、Proc(+)に戻ります。
Proc(+)は、+を出力し、処理が終了します。

### 関連概念
