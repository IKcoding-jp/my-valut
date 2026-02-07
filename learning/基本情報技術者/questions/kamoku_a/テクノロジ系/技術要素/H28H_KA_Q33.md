---
id: H28H_KA_Q33
year: H28春
kamoku: A
number: 33
type: 混合
field: テクノロジ系 » ネットワーク »ネットワーク方式
difficulty: 3
status: 未学習
source: "出典：平成28年春期 基本情報技術者試験 科目A 問33"
source_url: "https://www.fe-siken.com/kakomon/28_haru/q33.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
プライベートIPアドレスの複数の端末が，一つのグローバルIPアドレスを使ってインターネット接続を利用する仕組みを実現するものはどれか。

## 選択肢
- ア: DHCP
- イ: DNS
- ウ: NAPT
- エ: RADIUS

## 正解
ウ

## 解説
NAPT
(Network Address Port Translation)は、プライベートIPアドレスとグローバルIPアドレスを1対1で相互変換するNATの考え方に、ポート番号でのクライアント識別を組み合わせた技術です。1つのグローバルIPアドレスで複数のプライベートIPアドレスを持つノードを同時にインターネットに接続させることが可能です。IPマスカレードとも呼ばれます。

### 各選択肢の解説
- ア: Dynamic Host Configuration Protocolの略。TCP/IPネットワークで、ネットワークに接続するノードへのIPアドレスの割り当てをアドレスプールから自動的に行うプロトコルです。
- イ: Domain Name Systemの略。ドメイン名とIPアドレスを結びつけて変換する(名前解決する)仕組みです。
- ウ: 正しい。NAPTは、1つのグローバルIPアドレスで複数のクライアントをインターネットに接続させることができる仕組みです。
- エ: Remote Authentication Dial In User Serviceの略。認証情報と認証手続き、および利用ログの記録(アカウンティング)をネットワーク上のサーバに一元化することを目的としたシステムです。

### 関連概念
- [[NAPT]]
- [[TCP/IP]]
- [[ネットワーク]]
- [[プロトコル]]
- [[認証]]
