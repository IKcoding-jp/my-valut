---
id: H23T_KA_Q44
year: H23特
kamoku: A
number: 44
type: 混合
field: テクノロジ系 » セキュリティ »セキュリティ実装技術
difficulty: 3
status: 未学習
source: "出典：平成23年特別 基本情報技術者試験 科目A 問44"
source_url: "https://www.fe-siken.com/kakomon/23_toku/q44.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
社内ネットワークとインターネットの接続点にパケットフィルタリング型ファイアウォールを設置して，社内ネットワーク上のPCからインターネット上のWebサーバ(ポート番号80) にアクセスできるようにするとき，フィルタリングで許可するルールの適切な組合せはどれか。

## 選択肢
- ア: ![44a.png/image-size:275×78](https://www.fe-siken.com/kakomon/23_toku/img/44a.png)
- イ: ![44i.png/image-size:276×77](https://www.fe-siken.com/kakomon/23_toku/img/44i.png)
- ウ: ![44u.png/image-size:276×77](https://www.fe-siken.com/kakomon/23_toku/img/44u.png)
- エ: ![44e.png/image-size:275×77](https://www.fe-siken.com/kakomon/23_toku/img/44e.png)

## 正解
ウ

## 解説
パケットフィルタリング
では、パケットのヘッダー情報内のIPアドレス及びポート番号を基準にパケット通過の可否を決定します。
ポート番号
は、通信をする際にあて先のプログラムを特定するための0～65535(16ビット符号無し整数)の番号です。IPアドレスが建物の住所だとすれば、ポート番号は部屋番号ということになります。0～1023までは「WELL KNOWN PORT NUMBERS」と言い、よく利用されるアプリケーション用に予約されています。
(HTTP:TCP/80、FTP:20,21/TCP,、SMTP:25/TCPなど)
インターネット通信に使われるプロトコルは
HTTP
(HyperText Transfer Protocol)で、ポート番号は80です。このため、インターネット上のWebサーバにアクセスできるようにするには、内部からWebサーバの80番ポートに向けた発信パケット(HTTPリクエスト)、および逆向きの、Webサーバのポート80からクライアントPCの1024番以上に向けた応答パケット(HTTPレスポンス)の通過を許可する必要があります。
したがって適切なルール設定は「ウ」です。

### 関連概念
- [[HTTP]]
- [[KNOWN]]
- [[PORT]]
- [[WELL]]
- [[ネットワーク]]
