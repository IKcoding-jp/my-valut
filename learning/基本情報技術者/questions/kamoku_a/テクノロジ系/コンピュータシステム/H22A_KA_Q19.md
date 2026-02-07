---
id: H22A_KA_Q19
year: H22秋
kamoku: A
number: 19
type: 混合
field: テクノロジ系 » システム構成要素 »システムの評価指標
difficulty: 3
status: 未学習
source: "出典：平成22年秋期 基本情報技術者試験 科目A 問19"
source_url: "https://www.fe-siken.com/kakomon/22_aki/q19.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
四つの装置A～Dで構成されるシステム全体の稼働率として，最も近いものはどれか。ここで，個々の稼働率は，AとCが0.9，BとDが0.8とする。また，並列接続部分については，いずれか一方が稼働しているとき，当該並列部分は稼働しているものとする。![19.png/image-size:160×76](https://www.fe-siken.com/kakomon/22_aki/img/19.png)

## 選択肢
- ア: 0.72
- イ: 0.92
- ウ: 0.93
- エ: 0.95

## 正解
エ

## 解説
計算手順としては、AとCで構成される左側、次にBとDで構成される右側を計算し、最後に二つのシステムを直接につないだ時の稼働率を計算していきます。
[左側 AとC]
1－(1－0.9)
2
＝1－0.1
2
＝0.99
[右側 BとD]
1―(1－0.8)
2
＝1－0.2
2
＝0.96
[全体 A,C と B,D]
0.99×0.96＝0.9504≒
0.95
よって正解は
0.95
となります。

### 関連概念
- [[稼働率]]
