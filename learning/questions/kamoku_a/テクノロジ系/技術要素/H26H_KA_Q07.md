---
id: H26H_KA_Q07
year: H26春
kamoku: A
number: 7
type: 暗記
field: テクノロジ系 » アルゴリズムとプログラミング »データ構造
difficulty: 3
status: 未学習
source: "出典：平成26年春期 基本情報技術者試験 科目A 問7"
source_url: "https://www.fe-siken.com/kakomon/26_haru/q7.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
空の状態のキューとスタックの二つのデータ構造がある。次の手続を順に実行した場合，変数xに代入されるデータはどれか。ここで，手続きに引用している関数は，次のとおりとする。

〔関数の定義〕
push(y)：データyをスタックに積む。pop()：データをスタックから取り出して，その値を返す。enq(y)：データyをキューに挿入する。deq()：データをキューから取り出して，その値を返す。
〔手続〕
push(a)push(b)enq(pop())enq(c)push(d)push(deq())x ← pop()

## 選択肢
- ア: a
- イ: b
- ウ: c
- エ: d

## 正解
イ

## 解説
スタック
は後入先出し、
キュー
は先入先出しのデータ構造です。設問の手続きの実行するとスタックとキューの内容は次のように変化していきます。
したがってxに代入されるデータは
b
になります。

### 各選択肢の解説
push(a)…aをスタックに挿入する
push(b)…bをスタックに挿入する
enq(pop())…スタックから取り出したデータ(b)をキューに挿入する
enq(c)…cをキューに挿入する
push(d)…dをスタックに挿入する
push(deq())…キューから取り出したデータ(b)をスタックに挿入する
x←pop()…スタックから取り出したデータ(b)をxに代入する

### 関連概念
