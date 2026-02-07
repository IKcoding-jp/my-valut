---
id: H27A_KA_Q23
year: H27秋
kamoku: A
number: 23
type: 混合
field: テクノロジ系 » ハードウェア »ハードウェア
difficulty: 3
status: 未学習
source: "出典：平成27年秋期 基本情報技術者試験 科目A 問23"
source_url: "https://www.fe-siken.com/kakomon/27_aki/q23.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
図のNANDゲートの組合せ回路で，入力A，B，C，Dに対する出力Xの論理式はどれか。ここで，論理式中の"・"は論理積，"＋"は論理和を表す。![23.png/image-size:182×92](https://www.fe-siken.com/kakomon/27_aki/img/23.png)

## 選択肢
- ア: (A＋B)・(C＋D)
- イ: A＋B＋C＋D
- ウ: A・B＋C・D
- エ: A・B・C・D

## 正解
ウ

## 解説
NAND回路
のNANDは"
NOT AND
"を表していて、AND回路の出力を反転させた回路です。したがって、二つの入力が共に1の時だけ0を出力し、その他の場合は1を出力します。
論理回路から導いた論理式を変形する方法と、ベン図を使用する方法の2通りでの解法を説明します。
[論理式を使う方法]
NAND回路を論理式で表すと「
A・B
」となるため、設問の組合せ回路は、
A・B・C・D
と表すことができます。これをド・モルガン則を利用して変形すると、
A・B・C・D
＝
A・B
＋
C・D
//A・B＝A＋Bを適用
＝
A・B＋C・D
//A＝Aを適用
[ベン図を使う方法]

### 関連概念
