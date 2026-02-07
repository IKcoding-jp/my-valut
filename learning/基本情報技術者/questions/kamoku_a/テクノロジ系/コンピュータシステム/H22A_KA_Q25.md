---
id: H22A_KA_Q25
year: H22秋
kamoku: A
number: 25
type: 暗記
field: テクノロジ系 » ハードウェア »ハードウェア
difficulty: 3
status: 未学習
source: "出典：平成22年秋期 基本情報技術者試験 科目A 問25"
source_url: "https://www.fe-siken.com/kakomon/22_aki/q25.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
次の条件を満足する論理回路はどれか。

〔条件〕
階段の上下にあるスイッチA又はBで，一つの照明を点灯・消灯する。すなわち，一方のスイッチの状態にかかわらず，他方のスイッチで照明を点灯・消灯できる。![25.png/image-size:247×47](https://www.fe-siken.com/kakomon/22_aki/img/25.png)

## 選択肢
- ア: AND
- イ: NAND
- ウ: NOR
- エ: XOR

## 正解
エ

## 解説
階段の上と下に設置されているスイッチを思い浮かべてみればわかるように、各スイッチにはON/OFFの区別があるわけではなく、どちらのスイッチ押しても現在の照明の状態を変えることができます。
つまりスイッチを押すと(1を入力すると)相手スイッチ状態(0または1)にかかわらず、照明の状態を反転する(0→1, 1→0)ことが求められます。
XOR回路には、
特定のビットと1でXORをとると、そのビットを反転できる
という特徴があり、この目的に合う論理回路として最適です。

### 関連概念
- [[ON/OFF]]
