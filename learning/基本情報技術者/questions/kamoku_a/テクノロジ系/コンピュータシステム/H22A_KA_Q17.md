---
id: H22A_KA_Q17
year: H22秋
kamoku: A
number: 17
type: 混合
field: テクノロジ系 » システム構成要素 »システムの評価指標
difficulty: 3
status: 未学習
source: "出典：平成22年秋期 基本情報技術者試験 科目A 問17"
source_url: "https://www.fe-siken.com/kakomon/22_aki/q17.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
システムが時間とともに図のように故障と回復を繰り返した。このとき、RASISの信頼性(Reliability)と可用性(Availability)を表す指標の組合せとして、適切なものはどれか。ここで、![17_1.png/image-size:157×28](https://www.fe-siken.com/kakomon/22_aki/img/17_1.png)とする。![17_2.png/image-size:309×108](https://www.fe-siken.com/kakomon/22_aki/img/17_2.png)

## 選択肢


## 正解
イ

## 解説
RASIS
(レイシス)とは、システムの信頼性を評価する５つの概念の頭文字を合わせた言葉です。
Reliability…信頼性故障を起こしにくいさの度合い。MTBF(平均故障間隔)が指標として用いられる。Availability…可用性必要な時にシステムが使用可能状態である度合い。稼働率が指標として用いられる。Serviceability…保守性システム障害の時に修理がしやすさの度合いIntegrity…保全性保存されているデータの完全であるかどうかの度合いSecurity…安全性保存されているデータが、災害や障害などに対してもつ耐性の度合い。機密性とも呼ばれる。
この問題では、これら信頼性を評価するときの指標を表すの式が求められてるので、上記で書いたように
信頼性はMTBF
、
可用性は稼働率
を表す式がどれかを考えればよいことになります。
問題文の図を見ると、t1,t2…tn が正常に稼働していた時間、s1,s2…sn が障害が起こってから回復するまでに要した時間を表していることがわかります。
信頼性の指標であるMTBFは、故障が回復してから次の故障が起こるまでの平均時間なので、
(t1＋t2＋ … tn)／n→
T
可用性の指標である稼働率は、MTBF／(MTBF＋MTTR) の式で求められます。
MTTRは、故障からの回復に要した平均時間なので、
(s1＋s2＋ … sn)／n　→ S
MTBFが
T
、MTTRが
S
とわかったので、これらをそのまま稼働率の式に当てはめると、
稼働率＝
T／(T＋S)
信頼性の指標であるMTBFが
T
,、可用性の指標である稼働率が
T／(T＋S)
なので正しい組合せは「イ」となります。

### 関連概念
- [[MTBF]]
- [[RASIS]]
- [[稼働率]]
