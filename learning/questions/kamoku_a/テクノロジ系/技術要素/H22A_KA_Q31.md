---
id: H22A_KA_Q31
year: H22秋
kamoku: A
number: 31
type: 暗記
field: テクノロジ系 » データベース »データ操作
difficulty: 3
status: 未学習
source: "出典：平成22年秋期 基本情報技術者試験 科目A 問31"
source_url: "https://www.fe-siken.com/kakomon/22_aki/q31.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
"商品"表に対してデータの更新処理が正しく実行できるUPDATE文はどれか。ここで，"商品"表は次のCREATE文で定義されている。![31.png/image-size:463×238](https://www.fe-siken.com/kakomon/22_aki/img/31.png)

## 選択肢
- ア: ![31a.png/image-size:455×15](https://www.fe-siken.com/kakomon/22_aki/img/31a.png)
- イ: ![31i.png/image-size:455×15](https://www.fe-siken.com/kakomon/22_aki/img/31i.png)
- ウ: ![31u.png/image-size:455×15](https://www.fe-siken.com/kakomon/22_aki/img/31u.png)
- エ: ![31e.png/image-size:455×16](https://www.fe-siken.com/kakomon/22_aki/img/31e.png)

## 正解
エ

## 解説
UPDATE文は、表中のデータを変更するSQLです。
UPDATE 表名 SET 列名 = 変更値 (WHERE 条件)
SETで変更したい列と変更後の値を指定し、WHERE句では変更したい行を抽出する条件を指定します。
この問題では、表生成のCREATE文が示されていて、「PRIMARY KEY (商品番号)」の部分から主キーは"商品番号"だということがわかります。問題のUPDATE文が主キーの一意性を保つことができるかに着目してみましょう。

### 各選択肢の解説
- ア: 商品番号"S002"の行の商品番号を"S001"にすると、商品番号"S001"の行が二つになり主キーの一意性を満たさなくなってしまうので誤りです。
- イ: 商品名がCの二つの行"S004","S005"の両方が、同じ商品番号"S006"になってしまうと主キーの一意性を満たさなくなってしまうので誤りです。
- ウ: 主キーである商品番号にNULL(空値)をセットすることはできません。
- エ: 正しい。商品番号"S003"の行は、上から３番目のみで商品名"B"を"D"に変更することが可能です。

### 関連概念
- [[KEY]]
- [[PRIMARY]]
- [[SET]]
- [[UPDATE]]
- [[WHERE]]
