---
id: R01H_KA_Q43
year: R01春
kamoku: A
number: 43
type: 暗記
field: テクノロジ系 » セキュリティ »セキュリティ実装技術
difficulty: 3
status: 未学習
source: "出典：令和元年春期 基本情報技術者試験 科目A 問43"
source_url: "https://www.fe-siken.com/kakomon/31_haru/q43.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
OSI基本参照モデルのネットワーク層で動作し，"認証ヘッダー(AH)"と"暗号ペイロード(ESP)"の二つのプロトコルを含むものはどれか。

## 選択肢
- ア: IPsec
- イ: S/MIME
- ウ: SSH
- エ: XML暗号

## 正解
ア

## 解説
IPsec
(IP Security)は、IP(Internet Protocol)を拡張してセキュリティを高めたプロトコルで、改ざんの検知、通信データの暗号化、送信元の認証などの機能をOSI基本参照モデルのネットワーク層レベル(TCP/IPモデルではIP層)で提供します。IPsecを用いれば上層のアプリケーションに依存せずに暗号化通信を行えるため、VPNの構築に利用されます。
IPsecはプロトコル群の総称であり、認証、暗号化、鍵交換などの複数のプロトコルを含みます。そのうち、認証を担うプロトコルが
AH
(Authentication Header)、認証と暗号化を担うプロトコルが
ESP
(Encapsulated Security Payload)です。
どの規格もデータの暗号化を担いますが、ネットワーク層で動作するのはIPsecだけです。したがって「ア」が正解です。

### 各選択肢の解説
- ア: 正しい。
- イ: Secure MIMEの略。公開鍵暗号技術を使用して「認証」「改ざん検出」「暗号化」などの機能を電子メールソフトに提供する規格です。
- ウ: Secure Shellの略。公開鍵暗号や認証の技術を用いて、遠隔地にあるコンピュータ（リモートコンピュータ）との間で安全にリモート通信をするためのプロトコルです。
- エ: XML暗号は、XML文書の一部分を暗号化するための規格です。

### 関連概念
- [[AH]]
- [[ESP]]
- [[IP]]
- [[TCP/IP]]
- [[ネットワーク]]
