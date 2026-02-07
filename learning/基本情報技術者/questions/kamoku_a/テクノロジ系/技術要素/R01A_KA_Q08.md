---
id: R01A_KA_Q08
year: R01秋
kamoku: A
number: 8
type: 暗記
field: テクノロジ系 » アルゴリズムとプログラミング »データ構造
difficulty: 3
status: 未学習
source: "出典：令和元年秋期 基本情報技術者試験 科目A 問8"
source_url: "https://www.fe-siken.com/kakomon/01_aki/q8.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
A，C，K，S，Tの順に文字が入力される。スタックを利用して，S，T，A，C，Kという順に文字を出力するために，最小限必要となるスタックは何個か。ここで，どのスタックにおいてもポップ操作が実行されたときには必ず文字を出力する。また，スタック間の文字の移動は行わない。

## 選択肢
- ア: 1
- イ: 2
- ウ: 3
- エ: 4

## 正解
ウ

## 解説
スタック
は、データ追加のときは最後尾にデータを追加し、データ取り出しのときはデータの最後尾から取り出す
後入れ先出し
(LIFO:Last-in First-out)のデータ構造です。
スタックでは、データを追加するPUSH命令、データを取り出すPOP命令を使用してデータ操作を行います。
まず、スタック構造の動作を確認する意味を含めて1つの場合で試してみます。※[]の中を各スタックの内容として考えてください。一番右が最後尾のデータです。
STに続いてAが出力できないので無理です。
次にスタックを2つ用意した場合を考えてみます。
AをCより先にpopするには、CをAとは別のスタックに積む必要があります。その後、Kを積むと、AとCをKより先に出力することができなくなってしまうので、目的の順番で出力できません。
スタックを3つ用意すると、CKよりも先に出力したいAを退避させておくことができます。
したがって、S、T、A、C、Kという順に文字を出力するためには、少なくとも3個のスタックが必要です。

### 各選択肢の解説
push A：[A]
push C：[A，C]
push K：[A，C，K]
push S：[A，C，K，S]
pop 　：[A，C，K] → Sを出力
push T：[A，C，K，T]
pop　 ：[A，C，K] → Tを出力
pop 　：[A，C，K] → Kを出力 //×
push A：[A]　[]
push C：[A]　[C]
push K：[A，K]　[C] または [A]　[C，K] //×
…
push A：[A]　[]　[]
push C：[A]　[C]　[]
push K：[A]　[C]　[K]
push S：[A]　[C]　[K，S]
pop 　：[A]　[C]　[K] → Sを出力
push T：[A]　[C]　[K，T]
pop 　：[A]　[C]　[K] → Tを出力
pop 　：[]　[C]　[K] → Aを出力
pop 　：[]　[]　[K] → Cを出力
pop 　：[]　[]　[] → Kを出力

### 関連概念
