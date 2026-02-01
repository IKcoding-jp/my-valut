---
id: H26H_KA_Q03
year: H26春
kamoku: A
number: 3
type: 混合
field: テクノロジ系 » 基礎理論 »離散数学
difficulty: 3
status: 未学習
source: "出典：平成26年春期 基本情報技術者試験 科目A 問3"
source_url: "https://www.fe-siken.com/kakomon/26_haru/q3.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
論理式A・B・C＋A・B・C＋A・B・C＋A・B・C と恒等的に等しいものはどれか。ここで，・は論理積，＋は論理和，AはAの否定を表す。

## 選択肢
- ア: A・B・C
- イ: A・B・C＋A・B・C
- ウ: A・B＋B・C
- エ: C

## 正解
エ

## 解説
ベン図を使用して解く方法と論理式の変形で解く方法の2通りを紹介します。
[ベン図]
[論理式の変形]
A
・
B
・C＋A・
B
・C＋
A
・B・C＋A・B・C
＝C・(
A
・
B
＋A・
B
＋
A
・B＋A・B)
//分配の法則
＝C・(
B
・(
A
＋A)＋B・(
A
＋A))
//分配の法則
＝C・(
B
＋B)
//A＋A＝1
＝
C
//B＋B＝1
したがって設問の論理式と等しいのは「C」になります。

### 関連概念
