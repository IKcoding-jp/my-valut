---
id: R01H_KA_Q29
year: R01春
kamoku: A
number: 29
type: 暗記
field: テクノロジ系 » データベース »データ操作
difficulty: 3
status: 未学習
source: "出典：令和元年春期 基本情報技術者試験 科目A 問29"
source_url: "https://www.fe-siken.com/kakomon/31_haru/q29.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
"学生"表と"学部"表に対して次のSQL文を実行した結果として，正しいものはどれか。![29.png/image-size:416×145](https://www.fe-siken.com/kakomon/31_haru/img/29.png)〔SQL文〕SELECT 氏名 FROM 学生, 学部
WHERE 所属 = 学部名 AND 学部.住所 = '新宿'

## 選択肢
- ア: ![29a.png/image-size:75×38](https://www.fe-siken.com/kakomon/31_haru/img/29a.png)
- イ: ![29i.png/image-size:75×63](https://www.fe-siken.com/kakomon/31_haru/img/29i.png)
- ウ: ![29u.png/image-size:76×63](https://www.fe-siken.com/kakomon/31_haru/img/29u.png)
- エ: ![29e.png/image-size:75×89](https://www.fe-siken.com/kakomon/31_haru/img/29e.png)

## 正解
ウ

## 解説
設問のSQL文は「"学生"表と"学部"表を"所属"列と"学部名"列で結合し、"学部"表の"住所"列の値が"新宿"である行を選択し、その中から"氏名"列を抜きだす」と解釈できます。
結果を得るまでの手順を以下に示します。

### 各選択肢の解説
まず、"学生"表と"学部"表を、"所属"列と"学部名"列の値が同じ行同士で結合します。
その中で"学部"表の"住所"列の値が"新宿"である行だけを選択します。
最後に"氏名"列を抜き出すと「ウ」の結果が得られます。

### 関連概念
- [[FROM]]
- [[SELECT]]
- [[WHERE]]
