---
id: H21H_KA_Q17
year: H21春
kamoku: A
number: 17
type: 混合
field: テクノロジ系 » システム構成要素 »システムの評価指標
difficulty: 3
status: 未学習
source: "出典：平成21年春期 基本情報技術者試験 科目A 問17"
source_url: "https://www.fe-siken.com/kakomon/21_haru/q17.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
システムの信頼性を表す指標であるRASのうち，可用性(Availability)を表す尺度はどれか。

## 選択肢
- ア: 稼働率(MTBFMTBF＋MTTR)
- イ: 全運転時間(MTBF＋MTTR)
- ウ: 平均故障間隔(MTBF)
- エ: 平均修理時間(MTTR)

## 正解
ア

## 解説
RAS
は、R(Reliability：信頼性)、A(Availability：可用性)、S(Serviceability：保守性)の頭文字を合わせたもので、システムの信頼性を表す指標です。このうち可用性とは、システムの必要な機能を必要なだけに使うことができるかどうか度合いを表します。
稼働率は、全運転時間に占める正常に稼動していた時間の割合で、一般的に可用性の指標として用いられます。稼働率は、MTBF（システムの修復が完了し正常に稼働し始めてから、次回故障するまでの平均故障間隔）とMTTR（システムの故障を修理するために要した平均修復時間）を使った次の式で表されます。
稼働率＝
MTBFMTBF＋MTTR
したがって「ア」が正解です。

### 各選択肢の解説
- ア: 正しい。稼働率は可用性を表す尺度です。
- イ: 全運転時間は、特に何の尺度に対応するということはありません。
- ウ: MTBFは信頼性を表す尺度です。
- エ: MTTRは保守性を表す尺度です。

### 関連概念
- [[MTTR]]
- [[RAS]]
- [[稼働率]]
