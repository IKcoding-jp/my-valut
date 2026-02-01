---
id: H27A_KA_Q19
year: H27秋
kamoku: A
number: 19
type: 暗記
field: テクノロジ系 » 基礎理論 »情報に関する理論
difficulty: 3
status: 未学習
source: "出典：平成27年秋期 基本情報技術者試験 科目A 問19"
source_url: "https://www.fe-siken.com/kakomon/27_aki/q19.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
コンパイラで構文解析した結果の表現方法の一つに四つ組形式がある。
(演算子，被演算子1，被演算子2，結果)
この形式は，被演算子1と被演算子2に演算子を作用させたものが結果であることを表す。次の一連の四つ組は，どの式を構文解析した結果か。ここで，T1，T2，T3は一時変数を表す。(＊，B，C，T1)
(／，T1，D，T2)
(＋，A，T2，T3)

## 選択肢
- ア: A＋B＊C／D
- イ: A＋B＊C／T2
- ウ: B＊C＋A／D
- エ: B＊C＋T1／D

## 正解
ア

## 解説
3つ目の式には被演算子としてT
1
とT
2
が使われていて、2つ目の式には被演算子としてT
1
が使われているので、上の式から順に展開していくことになります。
(＊，B，C，T1)T1は、"B"と"C"を"＊"で演算した結果T1=B＊C(／，T1，D，T2)T1= B ＊ C なので、T2は、"B＊C"と"D"を"／"で演算した結果T2=B＊C／D(＋，A，T2，T3)T2 = B＊C／D なので、T3は、"A"と"B＊C／D"を"＋"で演算した結果T3=A＋B＊C／D
したがって、構文解析に元となった式は「A＋B＊C／D」となります。

### 関連概念
