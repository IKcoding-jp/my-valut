---
id: R01H_KA_Q27
year: R01春
kamoku: A
number: 27
type: 暗記
field: テクノロジ系 » データベース »データ操作
difficulty: 3
status: 未学習
source: "出典：令和元年春期 基本情報技術者試験 科目A 問27"
source_url: "https://www.fe-siken.com/kakomon/31_haru/q27.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
"中間テスト"表からクラスごと，教科ごとの平均点を求め，クラス名，教科名の昇順に表示するSQL文中のaに入れる字句はどれか。

中間テスト（クラス名，教科名，学生番号，名前，点数）

〔SQL文〕SELECT クラス名，教科名，AVG(点数) AS 平均点
FROM 中間テスト
a

## 選択肢
- ア: GROUP BY クラス名，教科名 ORDER BY クラス名，AVG(点数)
- イ: GROUP BY クラス名，教科名 ORDER BY クラス名，教科名
- ウ: GROUP BY クラス名，教科名，学生番号 ORDER BY クラス名，教科名，平均点
- エ: GROUP BY クラス名，平均点 ORDER BY クラス名，教科名

## 正解
イ

## 解説
クラスごと、教科ごとの平均点を求めるので、
GROUP BY クラス名，教科名
でグループ化します。さらに表示はクラス名、教科名の昇順に行うので、
ORDER BY クラス名，教科名
というように整列優先順位の高い属性順に指定します。

### 各選択肢の解説
- ア: 表示順が、クラス名、平均点の順になってしまうため誤りです。
- イ: 正しい。
- ウ: GROUP BY句に学生番号を指定すると、クラス・教科・学生ごとの集計になってしまうため誤りです。
- エ: クラス名でしかグループ化していないので、教科ごとの集計ができません。また、GROUP BY句で未指定の"教科名"列をSELECT句で指定しているため構文エラーとなります。

### 関連概念
- [[FROM]]
- [[GROUP]]
- [[ORDER]]
- [[SELECT]]
- [[テスト]]
