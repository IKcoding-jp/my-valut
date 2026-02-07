---
id: H23A_KA_Q26
year: H23秋
kamoku: A
number: 26
type: 混合
field: テクノロジ系 » ハードウェア »ハードウェア
difficulty: 3
status: 未学習
source: "出典：平成23年秋期 基本情報技術者試験 科目A 問26"
source_url: "https://www.fe-siken.com/kakomon/23_aki/q26.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
論理式X＝A・B＋A・B＋A・Bと同じ結果が得られる論理回路はどれか。
ここで，論理式中の・は論理積，＋は論理和，XはXの否定を表す。

## 選択肢
- ア: ![26a.png/image-size:97×26](https://www.fe-siken.com/kakomon/23_aki/img/26a.png)
- イ: ![26i.png/image-size:98×27](https://www.fe-siken.com/kakomon/23_aki/img/26i.png)
- ウ: ![26u.png/image-size:98×26](https://www.fe-siken.com/kakomon/23_aki/img/26u.png)
- エ: ![26e.png/image-size:98×26](https://www.fe-siken.com/kakomon/23_aki/img/26e.png)

## 正解
イ

## 解説
集合演算則を用いて解く方法と、ベン図を用いて解く方法の2通りを解説します。
[集合演算則を用いた解法]
A
・B＋A・
B
＋
A
・
B
＝
A
・(B＋
B
)＋A・
B
//第1項と第3項をAでくくる
＝
A
＋A・
B
//B＋Bは1，1・X＝X
＝
A・(A＋B)
//ド・モルガン則を逆に適用する
＝
A・A＋A・B
//分配の法則
＝
A・B
//A・Aは0，0＋X＝X
A・B
は、NAND(not AND)回路の出力と同じなので正解は「イ」になります。
[ベン図を用いた解法]
第1項～第3項の論理式をベン図で表すと次のようになります。
これら３つの集合の論理和をベン図で表すと以下のようになり、NANDを示しているため、正解は「イ」ということになります。

### 関連概念
