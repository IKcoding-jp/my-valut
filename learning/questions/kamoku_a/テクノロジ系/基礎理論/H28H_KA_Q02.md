---
id: H28H_KA_Q02
year: H28春
kamoku: A
number: 2
type: 暗記
field: テクノロジ系 » 基礎理論 »情報に関する理論
difficulty: 3
status: 未学習
source: "出典：平成28年春期 基本情報技術者試験 科目A 問2"
source_url: "https://www.fe-siken.com/kakomon/28_haru/q2.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
次の状態遷移図で表現されるオートマトンで受理されるビット列はどれか。ここで，ビット列は左から順に読み込まれるものとする。![02.png/image-size:258×71](https://www.fe-siken.com/kakomon/28_haru/img/02.png)

## 選択肢
- ア: 0000
- イ: 0111
- ウ: 1010
- エ: 1111

## 正解
ウ

## 解説
設問のオートマトンでビット列が受理されるまでの流れは、
となります。(下図参照)
(2)と(4)の手順に注目すると、"1"の後には必ず1つ以上の"0"が含まれなければならないことがわかります。したがって選択肢のうち受理可能なビット列は「1010」のみです。

### 各選択肢の解説
"0"を0回以上繰り返す
"1"を出力する
"1"を0回以上繰り返す
"0"を出力する
"0"又は"1"を0回以上繰り返した後、受理される

### 関連概念
