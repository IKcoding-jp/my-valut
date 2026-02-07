---
id: H30H_KA_Q08
year: H30春
kamoku: A
number: 8
type: 暗記
field: テクノロジ系 » アルゴリズムとプログラミング »その他の言語
difficulty: 3
status: 未学習
source: "出典：平成30年春期 基本情報技術者試験 科目A 問8"
source_url: "https://www.fe-siken.com/kakomon/30_haru/q8.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
XML文書のDTDに記述するものはどれか。

## 選択肢
- ア: 使用する文字コード
- イ: データ
- ウ: バージョン情報
- エ: 文書型の定義

## 正解
エ

## 解説
XMLでは、文書作成者が自由に要素名や属性名を付け文章構造を構築することができます。
DTD
(Document Type Definition)とは、XMLなどのマークアップ言語において文書構造を定義するスキーマ言語の一つです。
DTDには、記述可能な要素名、属性名や発生順序・発生回数など文書作成のルールを定義でき、XML文書側では文書型宣言"<!DOCTYPE …>"で使用するDTDを指定できます。作成された文書がDTDに適合するかどうかを検証することで、処理の正確性や安全性を高められます。

### 各選択肢の解説
- ア: 使用する文字コードはXML文書のXML宣言内で指定します。
- イ: 実データはXML文書内に記述します。
- ウ: バージョン情報はXML文書のXML宣言内で指定します。
- エ: 正しい。DTDには文書構造の定義を記述します。

### 関連概念
- [[DOCTYPE]]
- [[DTD]]
