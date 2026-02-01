---
id: H29A_KA_Q05
year: H29秋
kamoku: A
number: 5
type: 暗記
field: テクノロジ系 » アルゴリズムとプログラミング »データ構造
difficulty: 3
status: 未学習
source: "出典：平成29年秋期 基本情報技術者試験 科目A 問5"
source_url: "https://www.fe-siken.com/kakomon/29_aki/q5.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
A，B，C，Dの順に到着するデータに対して，一つのスタックだけを用いて出力可能なデータ列はどれか。

## 選択肢
- ア: A，D，B，C
- イ: B，D，A，C
- ウ: C，B，D，A
- エ: D，C，A，B

## 正解
ウ

## 解説
スタック
は後入れ先出し(LIFO)のデータ構造で、PUSH命令とPOP命令によってデータを操作します。"後入れ先出し"ですので、スタックに先に入れたデータは、後から入れたデータよりも先に出力することができません。
選択肢の出力順をひとつずつ試していけばわかるのですが、4つのデータ列の中で出力可能なのは「C，B，D，A」で、その出力の過程は以下の通りです。
各出力を試みた場合、以下のようになります。※[]はスタックを表し、左の要素ほど昔に格納されたことを意味します。

### 各選択肢の解説
PUSH(A)
PUSH(B)
PUSH(C)
POP(C)
POP(B)
PUSH(D)
POP(D)
POP(A)
- ア: PUSH(A)　[A]POP(A)　[] ※Aを出力PUSH(B)　[B]PUSH(C)　[BC]PUSH(D)　[BCD]POP(D)　[BC] ※Dを出力BはCより先にスタックに格納されたので、Cより先にBを出力することができません。
- イ: PUSH(A)　[A]PUSH(B)　[AB]POP(B)　[A] ※Bを出力PUSH(C)　[AC]PUSH(D)　[ACD]POP(D)　[AC] ※Dを出力AはCより先にスタックに格納されたので、Cより先にAを出力することができません。
- ウ: 正しい。
- エ: PUSH(A)　[A]PUSH(B)　[AB]PUSH(C)　[ABC]PUSH(D)　[ABCD]POP(D)　[ABC] ※Dを出力POP(C)　[AB] ※Cを出力AはBより先にスタックに格納されたので、Bより先にAを出力することができません。

### 関連概念
