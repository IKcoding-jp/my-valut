---
id: H22H_KA_Q31
year: H22春
kamoku: A
number: 31
type: 暗記
field: テクノロジ系 » データベース »データ操作
difficulty: 3
status: 未学習
source: "出典：平成22年春期 基本情報技術者試験 科目A 問31"
source_url: "https://www.fe-siken.com/kakomon/22_haru/q31.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
"商品"表，"在庫"表に対する次のSQL文と，同じ結果が得られるSQL文はどれか。ここで，下線部は主キーを表す。![31.png/image-size:443×97](https://www.fe-siken.com/kakomon/22_haru/img/31.png)

## 選択肢
- ア: ![31a.png/image-size:454×33](https://www.fe-siken.com/kakomon/22_haru/img/31a.png)
- イ: ![31i.png/image-size:454×32](https://www.fe-siken.com/kakomon/22_haru/img/31i.png)
- ウ: ![31u.png/image-size:454×48](https://www.fe-siken.com/kakomon/22_haru/img/31u.png)
- エ: ![31e.png/image-size:454×48](https://www.fe-siken.com/kakomon/22_haru/img/31e.png)

## 正解
エ

## 解説
まず設問のSQL文ですが、(SELECT 商品番号 FROM 在庫)の副問合せで"在庫"表の商品番号列に存在する値のリストを作成し、それを"商品"表の商品番号列と比較しています。比較演算子は
NOT IN
なので、"商品"表の商品番号列の中で、"在庫"表の商品番号列に存在しない商品番号のリストが得られます。
EXISTS
は、親表の行を1行ずつ処理し、続く相関副問合せによって返された結果行が1つ以上存在すれば真、1つもなければ偽を返す句です。INとEXISTSは異なる意味ですが、使い方を工夫することで同じ結果を返すことが可能です。

### 各選択肢の解説
- ア: "在庫"表の商品番号のうち、"商品"表の商品番号列の値として存在する行が得られます。上記の例でいえば、商品番号{101, 105, 102, 104}が返されます。
- イ: "在庫"表の商品番号のうち、"商品"表の商品番号列の値として存在しない行が得られます。上記の例でいえば、"結果なし"が返されます。
- ウ: 副問合せは、現在処理中の"商品"表の商品番号が、"在庫"表の商品番号として存在する場合に1行以上を返します。"EXISTS = 真"となる行は、両表に含まれる商品番号になります。上記の例でいえば、商品番号{101, 102, 104, 105}が返されます。
- エ: 正しい。副問合せは、現在の"商品"表の商品番号が"在庫"表の商品番号として存在する場合に1行以上を返します。"NOT EXISTS = 真"となる行は、"商品"表に商品番号があるが、"在庫"表にはその商品番号がない行になります。上記の例でいえば、商品番号{103, 106}が返されます。

### 関連概念
- [[EXISTS]]
- [[FROM]]
- [[SELECT]]
