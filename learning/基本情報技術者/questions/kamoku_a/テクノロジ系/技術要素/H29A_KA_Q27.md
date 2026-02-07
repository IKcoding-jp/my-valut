---
id: H29A_KA_Q27
year: H29秋
kamoku: A
number: 27
type: 暗記
field: テクノロジ系 » データベース »データベース設計
difficulty: 3
status: 未学習
source: "出典：平成29年秋期 基本情報技術者試験 科目A 問27"
source_url: "https://www.fe-siken.com/kakomon/29_aki/q27.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
SQL文においてFOREIGN KEYとREFERENCESを用いて指定する制約はどれか。

## 選択肢
- ア: キー制約
- イ: 検査制約
- ウ: 参照制約
- エ: 表明

## 正解
ウ

## 解説
参照制約
は、外部キーを持つ表にレコードを追加する場合に、その外部キー列の値は参照先の表の主キーとして存在するものでなければならない、また、別表から主キーの値を参照されている行は削除することができないという制限を課す制約です。
参照制約は、関係データベースの整合性を保つために設定され、その指定には次のように"FOREIGN KEY"と"REFERENCES"が使われます。
FOREIGN KEY 列リスト REFERENCES 親テーブル(列リスト)
したがって正解は「ウ」です。

### 各選択肢の解説
- ア: キー制約は、PRIMARY KEY句やFOREIGN KEY句を用いて指定します。
- イ: 検査制約は、CHECK句を用いて指定します。
- ウ: 正しい。参照制約は、FOREIGN KEYとREFERENCESを用いて指定します。
- エ: 表明は、整合性制約の一種でCREATE ASSERTION句で指定します。

### 関連概念
- [[CREATE]]
- [[FOREIGN]]
- [[KEY]]
- [[PRIMARY]]
- [[REFERENCES]]
