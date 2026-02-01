---
id: H26A_KA_Q43
year: H26秋
kamoku: A
number: 43
type: 暗記
field: テクノロジ系 » セキュリティ »情報セキュリティ対策
difficulty: 3
status: 未学習
source: "出典：平成26年秋期 基本情報技術者試験 科目A 問43"
source_url: "https://www.fe-siken.com/kakomon/26_aki/q43.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
HTTPS(HTTP over SSL/TLS)の機能を用いて実現できるものはどれか。

## 選択肢
- ア: SQLインジェクションによるWebサーバへの攻撃を防ぐ。
- イ: TCPポート80番と443番以外の通信を遮断する。
- ウ: Webサーバとブラウザの間の通信を暗号化する。
- エ: Webサーバへの不正なアクセスをネットワーク層でのパケットフィルタリングによって制限する。

## 正解
ウ

## 解説
HTTPS
は、WebサーバとWebブラウザがデータを安全に送受信するために、SSL/TLSプロトコルによって生成されるセキュアな接続上でデータのやり取り(HTTP通信)を行う方式です。
HTTPは、平文のままで情報をやり取りするため個人情報の送信や電子決済などセキュリティが重要となる通信に使うことは危険が伴います。HTTPSではこの問題に対処するためSSL/TLSから提供される通信の暗号化，ノードの認証，改ざん検出などの機能を使用し、「なりすまし」や「盗聴」による攻撃から通信を保護できるようになっています。

### 各選択肢の解説
- ア: WAF(Web Application Firewall)の機能です。
- イ: ファイアウォールの機能です。
- ウ: 正しい。HTTPSの機能です。
- エ: ファイアウォールの機能です。

### 関連概念
- [[HTTP]]
- [[HTTPS]]
- [[SSL/TLS]]
- [[ファイアウォール]]
- [[プロトコル]]
