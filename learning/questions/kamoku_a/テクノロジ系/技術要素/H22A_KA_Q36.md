---
id: H22A_KA_Q36
year: H22秋
kamoku: A
number: 36
type: 混合
field: テクノロジ系 » ネットワーク »データ通信と制御
difficulty: 3
status: 未学習
source: "出典：平成22年秋期 基本情報技術者試験 科目A 問36"
source_url: "https://www.fe-siken.com/kakomon/22_aki/q36.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
ルータがパケットの経路決定に用いる情報として，最も適切なものはどれか。

## 選択肢
- ア: あて先IPアドレス
- イ: あて先MACアドレス
- ウ: 発信元IPアドレス
- エ: 発信元MACアドレス

## 正解
ア

## 解説
ルータ
(Router)は、異なる2つのネットワークをOSI基本参照モデルのネットワーク層で接続し、通過するパケットのIPアドレスを見てパケットを最適な経路に中継する通信装置です。
ルータは、パケットを受信すると、そのヘッダー情報に含まれる
宛先IPアドレス
を確認します。そして自身が持つルーティングテーブルと照合して、適切なインタフェースからパケットを送出します。
したがって「ア」が正解です。

### 関連概念
- [[ネットワーク]]
