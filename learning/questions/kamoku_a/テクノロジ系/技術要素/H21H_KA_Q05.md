---
id: H21H_KA_Q05
year: H21春
kamoku: A
number: 5
type: 暗記
field: テクノロジ系 » アルゴリズムとプログラミング »データ構造
difficulty: 3
status: 未学習
source: "出典：平成21年春期 基本情報技術者試験 科目A 問5"
source_url: "https://www.fe-siken.com/kakomon/21_haru/q5.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
関数や手続を呼び出す際に，戻り番地や処理途中のデータを一時的に保存するのに適したデータ構造はどれか。

## 選択肢
- ア: 2分探索木
- イ: キュー
- ウ: スタック
- エ: 双方向連結リスト

## 正解
ウ

## 解説
スタック
は、LIFO(Last in First Out，後入れ先出し)のデータ構造で、メインルーチンからサブルーチンを呼び出すときにメインルーチンの戻り番地や変数の値を一時的に格納しておくときなどに使われます。
ローカル変数やもとの手続きの呼び出し位置などをスタックに積んでいき、関数が終了するたびに前のデータをスタックから取り出して手続きを復帰させます。

### 関連概念
