---
id: H28A_KA_Q15
year: H28秋
kamoku: A
number: 15
type: 理解
field: テクノロジ系 » システム構成要素 »システムの評価指標
difficulty: 3
status: 未学習
source: "出典：平成28年秋期 基本情報技術者試験 科目A 問15"
source_url: "https://www.fe-siken.com/kakomon/28_aki/q15.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
2台のコンピュータを並列に接続して使うシステムがある。それぞれのMTBFとMTTRを次の表に示す。どちらか1台が稼働していればよい場合，システム全体の稼働率は何%か。![15.png/image-size:228×68](https://www.fe-siken.com/kakomon/28_aki/img/15.png)

## 選択肢
- ア: 91.2
- イ: 95.5
- ウ: 96.5
- エ: 99.8

## 正解
エ

## 解説
まず各コンピュータの稼働率を求めます。稼働率を求める公式は「MTBF／(MTBF＋MTTR)」です。
[コンピュータA]
480／(480＋20)＝0.96
[コンピュータB]
950／(950＋50)＝0.95
どちらか1台が稼働していればシステムは正常であるため並列接続の稼働率を計算する公式「1－(1－R
A
)(1－R
B
)」に各稼働率を代入して答えを導きます。
1－(1－0.96)(1－0.95)
＝1－(0.04×0.05)
＝1－0.002
＝0.998＝
99.8
(%)
したがって「エ」が正解です。

### 関連概念
- [[稼働率]]
