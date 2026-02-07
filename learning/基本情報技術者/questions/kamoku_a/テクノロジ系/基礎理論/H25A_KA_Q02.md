---
id: H25A_KA_Q02
year: H25秋
kamoku: A
number: 2
type: 混合
field: テクノロジ系 » 基礎理論 »離散数学
difficulty: 3
status: 未学習
source: "出典：平成25年秋期 基本情報技術者試験 科目A 問2"
source_url: "https://www.fe-siken.com/kakomon/25_aki/q2.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
32ビットのレジスタに16進数ABCDが入っているとき，2ビットだけ右に論理シフトしたときの値はどれか。

## 選択肢
- ア: 2AF3
- イ: 6AF3
- ウ: AF34
- エ: EAF3

## 正解
ア

## 解説
16進数ABCDを2進数に変換すると次のようなビット列になります。
1010 1011 1100 1101
論理シフトでは空いたビットを0で埋めるので2ビット分だけ右に論理シフトすると、結果は、
0010 1010 1111 0011
というビット列です。最後にこれを4ビットずつまとめて16進数に戻すと「2AF3」になります。

### 関連概念
