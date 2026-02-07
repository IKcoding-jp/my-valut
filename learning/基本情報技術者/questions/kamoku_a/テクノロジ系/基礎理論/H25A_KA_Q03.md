---
id: H25A_KA_Q03
year: H25秋
kamoku: A
number: 3
type: 理解
field: テクノロジ系 » 基礎理論 »通信に関する理論
difficulty: 3
status: 未学習
source: "出典：平成25年秋期 基本情報技術者試験 科目A 問3"
source_url: "https://www.fe-siken.com/kakomon/25_aki/q3.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
4桁の整数N1N2N3N4から，次の方法によって検査数字(チェックディジット)Cを計算したところ，C＝4となった。N2＝7，N3＝6，N4＝2のとき，N1の値は幾らか。ここで，mod(x，y)は，xをyで割った余りとする。

検査数字：C＝mod((N1×1＋N2×2＋N3×3＋N4×4)，10)

## 選択肢
- ア: 0
- イ: 2
- ウ: 4
- エ: 6

## 正解
ウ

## 解説
設問で与えられている検査数字を計算する式に、N
2
～N
4
およびCを代入してN
1
を求めます。
4＝mod(N
1
×1 ＋ 7×2 ＋ 6×3 ＋ 2×4，10)
4＝mod(N
1
＋14＋18＋8，10)
4＝mod(N
1
＋40，10)
40＋Nを10で割ったとき、余りが4になるということです。N
1
は1桁の自然数であることを考慮すると、「(N
1
＋40)÷10＝● 余り 4」を満たすN
1
は「4」しかありません。
したがって「ウ」が正解です。

### 関連概念
