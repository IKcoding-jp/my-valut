---
id: H30A_KA_Q05
year: H30秋
kamoku: A
number: 5
type: 暗記
field: テクノロジ系 » アルゴリズムとプログラミング »データ構造
difficulty: 3
status: 未学習
source: "出典：平成30年秋期 基本情報技術者試験 科目A 問5"
source_url: "https://www.fe-siken.com/kakomon/30_aki/q5.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
待ち行列に対する操作を，次のとおり定義する。
ENQ n:待ち行列にデータnを挿入する。DEQ :待ち行列からデータを取り出す。空の待ち行列に対し，ENQ1，ENQ2，ENQ3，DEQ，ENQ4，ENQ5，DEQ，ENQ6，DEQ，DEQの操作を行った。次にDEQ操作を行ったとき，取り出されるデータはどれか。

## 選択肢
- ア: 1
- イ: 2
- ウ: 5
- エ: 6

## 正解
ウ

## 解説
待ち行列
(キュー構造)は、先に入ったものから先に取り出す「先入先出し方式」のデータ構造です。左を待ち行列の入口、右を出口として操作に伴う待ち行列の変化を追っておきます。
ENQ1：　[1]
ENQ2：　[2][1]
ENQ3：　[3][2][1]
DEQ： 　[3][2] → [1]
ENQ4：　[4][3][2]
ENQ5：　[5][4][3][2]
DEQ： 　[5][4][3] → [2]
ENQ6：　[6][5][4][3]
DEQ：　 [6][5][4] → [3]
DEQ：　 [6][5] → [4]
次に行われるDEQ操作で取り出される値が答えとなります。
DEQ：　 [6] →[
5
]
したがって答えは「5」が適切です。

### 関連概念
- [[DEQ]]
- [[ENQ]]
