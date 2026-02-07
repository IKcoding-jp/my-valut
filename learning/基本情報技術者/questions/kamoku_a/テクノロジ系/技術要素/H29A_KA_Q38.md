---
id: H29A_KA_Q38
year: H29秋
kamoku: A
number: 38
type: 暗記
field: テクノロジ系 » セキュリティ »情報セキュリティ
difficulty: 3
status: 未学習
source: "出典：平成29年秋期 基本情報技術者試験 科目A 問38"
source_url: "https://www.fe-siken.com/kakomon/29_aki/q38.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
非常に大きな数の素因数分解が困難なことを利用した公開鍵暗号方式はどれか。

## 選択肢
- ア: AES
- イ: DH
- ウ: DSA
- エ: RSA

## 正解
エ

## 解説
RSA暗号
(Rivest Shamir Adleman)は、桁数が大きい合成数の素因数分解が困難であることを安全性の根拠とした公開鍵暗号の一つです。数字の桁数がそのまま安全強度につながるため、実際のRSAでは合成数の元となる2つの数に300～1,000桁の非常に大きな素数が使用されます。
RSAという名称は、開発者であるRivest，Shamir，Adlemanの頭文字をとって名付けられました。

### 各選択肢の解説
- ア: Advanced Encryption Standardの略。アメリカ合衆国の次世代暗号方式として規格化された共通鍵暗号方式です。
- イ: Diffie-Hellmanの略。事前の秘密情報の共有なしに暗号化鍵の共有を安全に行える鍵交換方式です。TLSなどで使用されています。
- ウ: Digital Signature Algorithmの略。離散対数問題を安全性の根拠とするElGamal署名を改良して開発された、デジタル署名方式の一つです。
- エ: 正しい。RSAは、非常に大きな数の素因数分解が困難なことを安全性の根拠としています。

### 関連概念
- [[公開鍵]]
- [[共通鍵]]
- [[暗号化]]
- [[署名]]
