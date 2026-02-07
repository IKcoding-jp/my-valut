---
id: R01A_KA_Q26
year: R01秋
kamoku: A
number: 26
type: 暗記
field: テクノロジ系 » データベース »データ操作
difficulty: 3
status: 未学習
source: "出典：令和元年秋期 基本情報技術者試験 科目A 問26"
source_url: "https://www.fe-siken.com/kakomon/01_aki/q26.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
"得点"表から，学生ごとに全科目の点数の平均を算出し，平均が80点以上の学生の学生番号とその平均点を求める。aに入れる適切な字句はどれか。ここで，実線の下線は主キーを表す。

得点（学生番号，科目，点数）

〔SQL文〕
SELECT 学生番号，AVG(点数)
FROM 得点
GROUP BYa

## 選択肢
- ア: 科目 HAVING AVG(点数) >= 80
- イ: 科目 WHERE 点数 >= 80
- ウ: 学生番号 HAVING AVG(点数) >= 80
- エ: 学生番号 WHERE 点数 >= 80

## 正解
ウ

## 解説
GROUP BY句でグループ化した後にグループを絞るにはHAVING句を使用します。本問では学生ごとに全科目の平均を算出したいので、「GROUP BY 学生番号」でレコードを学生番号ごとにグルーピングした後、点数の平均が80以上の学生を「HAVING AVG(点数) >= 80」で選択することになります。
「イ」と「エ」では、GROUP BY句の後にWHERE句を記述しているので構文エラーとなります。各句の記述順は、
と決まっていて、グループ化したものを条件で絞り込むにはHAVING句を使用しなければなりません。また「ア」は科目ごとにグループ化しているので、科目ごとの平均点を集計してしまうことになります。
したがって「ウ」が正解です。

### 各選択肢の解説
WHERE句 … 条件を指定してレコードを絞る
GROUP BY句 … 指定した属性でレコードをグループ化する
HAVING句 …  条件を指定してグループを絞る
ORDER BY句 … レコードの表示順を指定する

### 関連概念
- [[FROM]]
- [[GROUP]]
- [[HAVING]]
- [[ORDER]]
- [[SELECT]]
