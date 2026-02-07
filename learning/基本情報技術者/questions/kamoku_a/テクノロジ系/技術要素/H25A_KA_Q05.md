---
id: H25A_KA_Q05
year: H25秋
kamoku: A
number: 5
type: 暗記
field: テクノロジ系 » アルゴリズムとプログラミング »データ構造
difficulty: 3
status: 未学習
source: "出典：平成25年秋期 基本情報技術者試験 科目A 問5"
source_url: "https://www.fe-siken.com/kakomon/25_aki/q5.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
待ち行列に対する操作を，次のとおり定義する。

ENQ n:待ち行列にデータnを挿入する。
DEQ :待ち行列からデータを取り出す。

空の待ち行列に対し，ENQ1，ENQ2，ENQ3，DEQ，ENQ4，ENQ5，DEQ，ENQ6，DEQ，DEQの操作を行った。次にDEQ操作を行ったとき，取り出される値はどれか。

## 選択肢
- ア: 1
- イ: 2
- ウ: 5
- エ: 6

## 正解
ウ

## 解説
待ち行列
(キュー)は、先に入ったものから先に取り出す「先入先出し方式」のデータ構造です。左を待ち行列の入口、右を出口として操作の流れを考えます。
[ENQ1]　1
[ENQ2]　21
[ENQ3]　321
[DEQ] 　32 →1
[ENQ4]　432
[ENQ5]　5432
[DEQ] 　543 →2
[ENQ6]　6543
[DEQ] 　654 →3
[DEQ] 　65 →4
次に行われるDEQ操作で取り出される値が答えとなります。
[DEQ] 　6 →
5
したがって答えは「5」が適切です。

### 関連概念
- [[DEQ]]
- [[ENQ]]
