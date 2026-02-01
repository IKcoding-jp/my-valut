---
id: H22H_KA_Q32
year: H22春
kamoku: A
number: 32
type: 混合
field: テクノロジ系 » データベース »トランザクション処理
difficulty: 3
status: 未学習
source: "出典：平成22年春期 基本情報技術者試験 科目A 問32"
source_url: "https://www.fe-siken.com/kakomon/22_haru/q32.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
DBMS において，同じデータを複数のプログラムが同時に更新しようとしたときに，データの矛盾が起きないようにするための仕組みはどれか。

## 選択肢
- ア: アクセス権限
- イ: 機密保護
- ウ: 排他制御
- エ: リカバリ制御

## 正解
ウ

## 解説
排他制御
は、トランザクションの整合性を保つために1つのタスクがトランザクションを実行中は、その処理が終わるまで他のタスクからのトランザクション要求を待機させる方法です。
排他制御を実現する方式としては、占有ロックや時刻印アルゴリズムなどがあります。

### 関連概念
- [[DBMS]]
- [[アルゴリズム]]
- [[トランザクション]]
