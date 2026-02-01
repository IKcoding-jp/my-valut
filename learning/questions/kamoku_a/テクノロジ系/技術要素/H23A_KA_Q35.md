---
id: H23A_KA_Q35
year: H23秋
kamoku: A
number: 35
type: 暗記
field: テクノロジ系 » データベース »データ操作
difficulty: 3
status: 未学習
source: "出典：平成23年秋期 基本情報技術者試験 科目A 問35"
source_url: "https://www.fe-siken.com/kakomon/23_aki/q35.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
関係データベースの操作の説明のうち，適切なものはどれか。

## 選択肢
- ア: 結合は，二つ以上の表を連結して，一つの表を生成することをいう。
- イ: 射影は，表の中から条件に合致した行を取り出すことをいう。
- ウ: 選択は，表の中から特定の列を取り出すことをいう。
- エ: 挿入は，表に対して特定の列を挿入することをいう。

## 正解
ア

## 解説
### 各選択肢の解説
- ア: 正しい。結合は、2つの表がもつ共通の属性(列)で結合を行い新しい表を作り出す操作です。SQLではJOIN句による方法とWHERE句による方法があります。//JOIN句SELECT * FROM tblA INNER JOIN tblB ON tblA.id = tblB.id//WHERE句WHERE tblA.id = tblB.id
- イ: 射影は、表の中から特定の列を取り出す操作です。SQLのSELECT文がこの操作に対応します。SELECT name, age FROM users
- ウ: 選択は、表の中から条件に合致した行を取り出す操作です。SQLのWHERE句等がこの操作に対応します。SELECT * FROM usersWHERE age > 20 AND city = 'Tokyo'
- エ: 挿入は、表に対して特定の行を差し込む操作です。SQLのINSERT文がこの操作に対応します。列の挿入はSQLのADD句で行われるため、操作名としては「追加」が適当です。INSERT INTO users (name, age) VALUES ('Alice', 30)

### 関連概念
- [[FROM]]
- [[INNER]]
- [[INSERT]]
- [[INTO]]
- [[JOIN]]
