---
id: H22A_KA_Q05
year: H22秋
kamoku: A
number: 5
type: 暗記
field: テクノロジ系 » アルゴリズムとプログラミング »データ構造
difficulty: 3
status: 未学習
source: "出典：平成22年秋期 基本情報技術者試験 科目A 問5"
source_url: "https://www.fe-siken.com/kakomon/22_aki/q5.html"
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
スタックは後入れ先出し(LIFO)のデータ構造です。
ひとつずつ試していけばわかるのですが、４つのデータ列の中で出力可能なのは「C、B、D、A」で、出力の過程は以下の通りです。

### 各選択肢の解説
PUSH(A)
PUSH(B)
PUSH(C)
POP(C)
POP(B)
PUSH(D)
POP(D)
POP(A)
- ア: Cの前にBを出力することができません。
- イ: Cの前にAを出力することができません。
- ウ: 正しい。
- エ: Bの前にAを出力することができません。

### 関連概念
