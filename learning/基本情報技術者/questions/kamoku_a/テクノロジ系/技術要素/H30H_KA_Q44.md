---
id: H30H_KA_Q44
year: H30春
kamoku: A
number: 44
type: 暗記
field: テクノロジ系 » セキュリティ »情報セキュリティ対策
difficulty: 3
status: 未学習
source: "出典：平成30年春期 基本情報技術者試験 科目A 問44"
source_url: "https://www.fe-siken.com/kakomon/30_haru/q44.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
社内ネットワークとインターネットの接続点に，ステートフルインスペクション機能をもたない，静的なパケットフィルタリング型のファイアウォールを設置している。このネットワーク構成において，社内のPCからインターネット上のSMTPサーバに電子メールを送信できるようにするとき，ファイアウォールで通過を許可するTCPパケットのポート番号の組合せはどれか。ここで，SMTP通信には，デフォルトのポート番号を使うものとする。

## 選択肢


## 正解
ウ

## 解説
SMTP
(Simple Mail Transfer Protocol)は、電子メールを転送するプロトコルで通信に
TCP/25
ポートを使用します。
電子メールを送信するのに必要となる通信は、
の2つです。PC(クライアント)は"well-knownポート"ではない1024番以降のポートを通信に使用するので、
という2種類のパケットだけを通過許可すればSMTP通信を行うことができます。したがって「ウ」の設定が適切となります。
なお表に登場するTCP/110は、メール受信のPOP(Post Office Protocol)で使用するポート番号です。

### 各選択肢の解説
PCからSMTPサーバへの発信パケット
SMTPサーバからPCへの応答パケット
PC(1024以上)→SMTPサーバ(25)
SMTPサーバ(25)→PC(1024以上)

### 関連概念
- [[SMTP]]
- [[ネットワーク]]
- [[ファイアウォール]]
- [[プロトコル]]
