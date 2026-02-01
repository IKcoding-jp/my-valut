---
id: H22H_KA_Q22
year: H22春
kamoku: A
number: 22
type: 混合
field: テクノロジ系 » ソフトウェア »開発ツール
difficulty: 3
status: 未学習
source: "出典：平成22年春期 基本情報技術者試験 科目A 問22"
source_url: "https://www.fe-siken.com/kakomon/22_haru/q22.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
次の一連の3アドレス命令で得られる結果xを表す式はどれか。ここで，3アドレス命令では，三つのオペランドを用いた命令"c = a op b"を" op(a，b，c)"として表記する。opは一つの演算子を表し，結果xを表す式においては優先順位の高い順に＊，／，＋，－ とする。

／(c，d，w1)
＋(b，w1，w2)
／(e，f，w3)
－(w3，g，w4)
＊(w2，w4，x)

## 選択肢
- ア: b＋c／d＊e／f－g
- イ: b＋c／d＊(e／f－g)
- ウ: (b＋c／d)＊e／f－g
- エ: (b＋c／d)＊(e／f－g)

## 正解
エ

## 解説
設問の指示である"c＝a op b"⇒"op(a，b，c)"に従って、各3アドレス命令を命令の形に戻していきます。
したがって結果xを表す式は「エ」となります。

### 各選択肢の解説
／(c，d，w1) ⇒ w1＝c／d
＋(b，w1，w2) ⇒ w2＝b＋w1w1＝c／dより、w2＝b＋c／d
／(e，f，w3) ⇒ w3＝e／f
－(w3，g，w4) ⇒ w4＝w3－gw3＝e／fより、w4＝e／f－g
＊(w2，w4，x) ⇒ x＝w2＊w4w2＝b＋c／d、w4＝e／f－gより、x＝(b＋c／d)＊(e／f－g)

### 関連概念
