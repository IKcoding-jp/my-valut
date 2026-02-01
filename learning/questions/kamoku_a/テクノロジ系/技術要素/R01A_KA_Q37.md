---
id: R01A_KA_Q37
year: R01秋
kamoku: A
number: 37
type: 混合
field: テクノロジ系 » セキュリティ »セキュリティ実装技術
difficulty: 3
status: 未学習
source: "出典：令和元年秋期 基本情報技術者試験 科目A 問37"
source_url: "https://www.fe-siken.com/kakomon/01_aki/q37.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
WPA3はどれか。

## 選択肢
- ア: HTTP通信の暗号化規格
- イ: TCP/IP通信の暗号化規格
- ウ: Webサーバで使用するデジタル証明書の規格
- エ: 無線LANのセキュリティ規格

## 正解
エ

## 解説
WPA3
(Wi-Fi Protected Access 3)は、無線LANのセキュリティプロトコルWPA2の後継となる次期バージョンです。WPA2には2017年11月に「KRACKs」と呼ばれる4ウェイハンドシェイク時における深刻な脆弱性が見つかっており、翌2018年に発表されたWPA3ではセキュリティのさらなる強化が図られています。具体的には、管理フレーム暗号化を行うPMF機能の使用を必須とするほか、パーソナルモード、エンタープライズモードそれぞれで変更が行われています。
WPA3-Personal楕円曲線暗号を使用してクライアントとアクセスポイント間の鍵共有を行うSAE(Simultaneous Authentication of Equals)を認証時に追加し、辞書攻撃、総当たり攻撃から保護する。→「KRACKs」の無効化WPA3-Enterprise暗号化アルゴリズムとして、WPA2のCCMP(AES128ビット)よりも強度の高いCNSA準拠の192ビットブロック暗号を選択可能になった。

### 各選択肢の解説
- ア: TLS(Transport Layer Security)、またはHTTPS(Hypertext Transfer Protocol Secure)の説明です。
- イ: IPsec(IP Security Architecture)の説明です。
- ウ: ITU-T X.509の説明です。
- エ: 正しい。WPA3の説明です。

### 関連概念
- [[IP]]
- [[アルゴリズム]]
- [[プロトコル]]
- [[暗号化]]
- [[認証]]
