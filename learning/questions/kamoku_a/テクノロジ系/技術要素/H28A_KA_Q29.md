---
id: H28A_KA_Q29
year: H28秋
kamoku: A
number: 29
type: 暗記
field: テクノロジ系 » データベース »データ操作
difficulty: 3
status: 未学習
source: "出典：平成28年秋期 基本情報技術者試験 科目A 問29"
source_url: "https://www.fe-siken.com/kakomon/28_aki/q29.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
"社員"表と"部門"表に対し，次のSQL文を実行したときの結果はどれか。![29.png/image-size:359×319](https://www.fe-siken.com/kakomon/28_aki/img/29.png)

## 選択肢
- ア: 1
- イ: 2
- ウ: 3
- エ: 4

## 正解
ウ

## 解説
まずWHERE句にあるように、社員表と部門表を所属列と部門名列をキー列として結合します。結合処理を行うとフロア列が追加された次のような中間表になります。
そして結合された表中でフロア列の値が"2"である行(部門.フロア＝2)の数を、COUNT(*)で集計しています。下表で示すようにフロア列の値が"2"の行は3行あるので、SQL文を実行した結果は
3
になります。

### 関連概念
