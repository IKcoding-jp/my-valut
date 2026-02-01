---
id: R01H_KA_Q33
year: R01春
kamoku: A
number: 33
type: 暗記
field: テクノロジ系 » ネットワーク »通信プロトコル
difficulty: 3
status: 未学習
source: "出典：令和元年春期 基本情報技術者試験 科目A 問33"
source_url: "https://www.fe-siken.com/kakomon/31_haru/q33.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
トランスポート層のプロトコルであり，信頼性よりもリアルタイム性が重視される場合に用いられるものはどれか。

## 選択肢
- ア: HTTP
- イ: IP
- ウ: TCP
- エ: UDP

## 正解
エ

## 解説
UDP
(User Datagram Protocol)は、TCP/IPの通信処理で使われる伝送制御プロトコルの一つで、TCPと同じトランスポート層に位置します。
TCPでは通信の信頼性を担保するために、コネクション確立、再送処理、輻輳処理などの様々な仕組みが取り入れられていますが、その分だけ通信のオーバーヘッドは増加してしまいます。TCPから信頼性を確保する機能を取り除き、ヘッダー構成の簡素化によりデータ比率を高めることで、軽量で効率性の高い通信を実現するプロトコルが「UDP」です。UDPは、信頼性よりも効率性やリアルタイム性が重視される音声や画像のストリーム配信、および、DNS、DHCP、NTPなどのアプリケーション層プロトコルで用いられています。
したがって「エ」が正解です。

### 各選択肢の解説
TCP… 信頼性重視
UDP… 通信効率、リアルタイム性重視
- ア: Hypertext Transfer Protocolの略。アプリケーション層のプロトコルです。
- イ: Internet Protocolの略。ネットワーク層のプロトコルです。
- ウ: Transmission Control Protocolの略。トランスポート層のプロトコルですが、通信の信頼性を重視する通信に用いられます。
- エ: 正しい。UDPは、リアルタイム性重視のトランスポート層のプロトコルです。

### 関連概念
- [[TCP/IP]]
- [[UDP]]
- [[ネットワーク]]
- [[プロトコル]]
