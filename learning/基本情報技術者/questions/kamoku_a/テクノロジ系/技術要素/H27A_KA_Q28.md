---
id: H27A_KA_Q28
year: H27秋
kamoku: A
number: 28
type: 混合
field: テクノロジ系 » データベース »データ操作
difficulty: 3
status: 未学習
source: "出典：平成27年秋期 基本情報技術者試験 科目A 問28"
source_url: "https://www.fe-siken.com/kakomon/27_aki/q28.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
"出庫記録"表に対するSQL文のうち，最も大きな値が得られるものはどれか。![28.png/image-size:197×129](https://www.fe-siken.com/kakomon/27_aki/img/28.png)

## 選択肢
- ア: ![28a.png/image-size:482×14](https://www.fe-siken.com/kakomon/27_aki/img/28a.png)
- イ: ![28i.png/image-size:482×14](https://www.fe-siken.com/kakomon/27_aki/img/28i.png)
- ウ: ![28u.png/image-size:482×14](https://www.fe-siken.com/kakomon/27_aki/img/28u.png)
- エ: ![28e.png/image-size:482×14](https://www.fe-siken.com/kakomon/27_aki/img/28e.png)

## 正解
イ

## 解説
したがって最も大きな値が得られるSQL文は「イ」になります。

### 各選択肢の解説
- ア: AVG()は、平均を計算する集計関数です。商品番号が"NP200"は4個ありレコード数は2なので、平均値として2が得られます。
- イ: COUNT()は、行数を数える集計関数です。"出庫記録"は4行からなっているので、4が得られます。
- ウ: MAX()は、最大値を得る集計関数です。"出庫記録"のレコードの中で"数量"列の最大値である3が得られます。
- エ: SUM()は、合計値を計算する集計関数です。日付が"2015-10-11"であるレコードは3,4行目なので、2つの行の"数量"の値を合計した3が得られます。

### 関連概念
