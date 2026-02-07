---
id: H21H_KA_Q33
year: H21春
kamoku: A
number: 33
type: 暗記
field: テクノロジ系 » データベース »データ操作
difficulty: 3
status: 未学習
source: "出典：平成21年春期 基本情報技術者試験 科目A 問33"
source_url: "https://www.fe-siken.com/kakomon/21_haru/q33.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
関係データベースの"製品"表と"売上"表から，売上報告のビュー表を定義するSQL文中のaに入るものはどれか。![33.png/image-size:455×204](https://www.fe-siken.com/kakomon/21_haru/img/33.png)

## 選択肢
- ア: GRANT
- イ: INSERT
- ウ: SCHEMA
- エ: SELECT

## 正解
エ

## 解説
関係データベースの
ビュー
は、実表の一部、または複数の実表から関係演算(選択、射影、結合など)によって得られた結果を1つの表に見せかけた仮想の表です。ビュー表はCREATE VIEW文によって定義され、対象となる実表からSELECT文をもちいて列と行を抜き出すという方法で定義されます。
したがって
a
に入るのは、"SELECT"です。

### 各選択肢の解説
- ア: GRANTは、特定のユーザーに表などのオブジェクトに対する権限を付与するときに使う文です。
- イ: INSERTは、表に行を挿入するときに使うSQL文です。
- ウ: SCHEMAは、データベースに名前空間を定義するCREATE SCHEMA文の一部です。
- エ: 正しい。ビュー表は、SELECTを使って表示するデータを定義します。

### 関連概念
- [[CREATE]]
- [[データベース]]
