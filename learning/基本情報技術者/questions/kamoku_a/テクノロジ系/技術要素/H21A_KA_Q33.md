---
id: H21A_KA_Q33
year: H21秋
kamoku: A
number: 33
type: 暗記
field: テクノロジ系 » データベース »データ操作
difficulty: 3
status: 未学習
source: "出典：平成21年秋期 基本情報技術者試験 科目A 問33"
source_url: "https://www.fe-siken.com/kakomon/21_aki/q33.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
SQLの構文として，正しいものはどれか。

## 選択肢
- ア: SELECT 注文日, AVG(数量)
FROM 注文明細
- イ: SELECT 注文日, AVG(数量)
FROM 注文明細
GROUP BY 注文日
- ウ: SELECT 注文日, AVG(SUM(数量))
FROM 注文明細
GROUP BY 注文日
- エ: SELECT 注文日
FROM 注文明細
WHERE SUM(数量) > 1000
GROUP BY 注文日

## 正解
イ

## 解説
### 各選択肢の解説
- ア: 注文日がGROUP BY句で指定されていないのに、SELECTで注文日と集計関数が使用されているので不適切です。
- イ: 正しい。注文日ごとの数量が出力されるSQL文です。
- ウ: AVG関数は引数が列名でなければならないので不適切です。
- エ: WHERE句はグループ化前に行を制限するので、集計関数を条件指定に使用することはできません。

### 関連概念
- [[GROUP]]
