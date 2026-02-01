---
id: H24H_KA_Q30
year: H24春
kamoku: A
number: 30
type: 暗記
field: テクノロジ系 » データベース »データ操作
difficulty: 3
status: 未学習
source: "出典：平成24年春期 基本情報技術者試験 科目A 問30"
source_url: "https://www.fe-siken.com/kakomon/24_haru/q30.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
"注文"表と"製品"表に対して，次のSQL文を実行したときに得られる結果はどれか。

SELECT 製品名, 数量 FROM 注文, 製品
WHERE 注文.製品コード = 製品.製品コード![30.png/image-size:317×180](https://www.fe-siken.com/kakomon/24_haru/img/30.png)

## 選択肢
- ア: ![30a.png/image-size:86×101](https://www.fe-siken.com/kakomon/24_haru/img/30a.png)
- イ: ![30i.png/image-size:86×101](https://www.fe-siken.com/kakomon/24_haru/img/30i.png)
- ウ: ![30u.png/image-size:86×120](https://www.fe-siken.com/kakomon/24_haru/img/30u.png)
- エ: ![30e.png/image-size:86×138](https://www.fe-siken.com/kakomon/24_haru/img/30e.png)

## 正解
ウ

## 解説
"注文"表と"製品"表を、2つの表の共通属性である製品コード列で結合すると次のようになります。
この結合表から、
SELECT 製品名, 数量
によって製品名と数量の列を抜き出すので、得られる結果表は以下のようになります。したがって「ウ」が正解です。

### 関連概念
- [[FROM]]
- [[SELECT]]
- [[WHERE]]
