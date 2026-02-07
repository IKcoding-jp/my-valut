---
id: H25H_KA_Q29
year: H25春
kamoku: A
number: 29
type: 暗記
field: テクノロジ系 » データベース »データ操作
difficulty: 3
status: 未学習
source: "出典：平成25年春期 基本情報技術者試験 科目A 問29"
source_url: "https://www.fe-siken.com/kakomon/25_haru/q29.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
"BOOKS"表から書名に"UNIX"を含む行を全て探すために次のSQL文を用いる。aに指定する文字列として，適切なものはどれか。ここで，書名は"BOOKS"表の"書名"列に格納されている。

SELECT * FROM BOOKS WHERE 書名 LIKE 'a'

## 選択肢
- ア: %UNIX
- イ: %UNIX%
- ウ: UNIX
- エ: UNIX%

## 正解
イ

## 解説
LIKE句
は、0文字以上の任意の文字列にマッチする「%」、任意の1文字にマッチする「_」などのワイルドカードと呼ばれる文字を使用して、文字列パターンを条件に指定可能にする句です。
書名に"UNIX"が含まれている行を抽出したいので、文字以上の任意の文字列にマッチする「%」を前後に付加した「%UNIX%」を指定するのが適切です。

### 各選択肢の解説
- ア: 書名が"UNIX"で終わる場合にマッチします。
- イ: 正しい。
- ウ: 書名が"UNIX"の場合にだけマッチします。
- エ: 書名が"UNIX"で始まる場合にマッチします。

### 関連概念
- [[BOOKS]]
- [[FROM]]
- [[LIKE]]
- [[SELECT]]
- [[WHERE]]
