---
id: H24A_KA_Q22
year: H24秋
kamoku: A
number: 22
type: 混合
field: テクノロジ系 » ハードウェア »ハードウェア
difficulty: 3
status: 未学習
source: "出典：平成24年秋期 基本情報技術者試験 科目A 問22"
source_url: "https://www.fe-siken.com/kakomon/24_aki/q22.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
NAND素子を用いた次の組合せ回路の出力Zを表す式はどれか。ここで，論理式中の"・"は論理積，"＋"は論理和，"X"はXの否定を表す。![22.png/image-size:233×90](https://www.fe-siken.com/kakomon/24_aki/img/22.png)

## 選択肢
- ア: X・Y
- イ: X＋Y
- ウ: X・Y
- エ: X＋Y

## 正解
イ

## 解説
NAND回路
は、NAND(Not AND)の名称どおりAND回路の逆を出力する回路で、2つの入力がともに"1"のときだけ"0"を出力し、それ以外の入力では"1"を出力します。
設問の回路に入力値XとYのすべての組合せ（X=0,Y=0・X=1,Y=0・X=0,Y=1・X=1, Y=1）を試すと、それぞれ以下の出力が得られます。
上記結果の入力値XとYおよび出力値Zの関係を整理すると、次の真理値表が得られます。
この真理値表より、設問の回路は2つの入力の論理和を得るOR回路と等価であることがわかるので、正解は「X＋Y」です。
【別解】
回路図を論理式で表し、その論理式を変形することで答えを導く解く方法もあります。
Z＝
X・X・Y・Y
＝
X・X
＋
Y・Y
//ド・モルガンの法則を適用
＝X・X＋Y・Y
//A＝A
＝X＋Y
//A・A＝A

### 関連概念
