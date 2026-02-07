---
id: H28A_KA_Q28
year: H28秋
kamoku: A
number: 28
type: 暗記
field: テクノロジ系 » データベース »データ操作
difficulty: 3
status: 未学習
source: "出典：平成28年秋期 基本情報技術者試験 科目A 問28"
source_url: "https://www.fe-siken.com/kakomon/28_aki/q28.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
関係代数の演算のうち，関係R，Sの直積(R×S)に対応するSELECT文はどれか。ここで，関係R，Sを表R，Sに対応させ，表R及びSにそれぞれ行の重複はないものとする。

## 選択肢
- ア: SELECT * FROM R，S
- イ: SELECT * FROM R EXCEPT SELECT * FROM S
- ウ: SELECT * FROM R UNION SELECT * FROM S
- エ: SELECT * FROM R INTERSECT SELECT * FROM S

## 正解
ア

## 解説
直積は、2つの関係(表)に含まれる要素のすべての組合せから成る表を得る演算です。
R，Sという2つの関係があるとき、R×Sは、関係Rの1つの行に対して関係Sのそれぞれの行を繋ぎ合わせた関係を返します。

### 各選択肢の解説
- ア: 正しい。SQLでは結合条件を指定しない場合や、結合条件が誤っている場合には2つの表を直積結合した結果を返します。
- イ: R EXCEPT S は、R表に存在し、S表に存在しない行から成る表(差集合)を返す演算です。
- ウ: R UNION Sは、2つの表の合わせた集合から重複を除去した表(和集合)で返す演算です。
- エ: R INTERSECT S は、R表とS表に共通する行から成る表(共通集合)を返す演算です。

### 関連概念
- [[EXCEPT]]
- [[INTERSECT]]
- [[UNION]]
