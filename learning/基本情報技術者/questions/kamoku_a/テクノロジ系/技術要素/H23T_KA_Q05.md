---
id: H23T_KA_Q05
year: H23特
kamoku: A
number: 5
type: 混合
field: テクノロジ系 » アルゴリズムとプログラミング »データ構造
difficulty: 3
status: 未学習
source: "出典：平成23年特別 基本情報技術者試験 科目A 問5"
source_url: "https://www.fe-siken.com/kakomon/23_toku/q5.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
空の2分探索木に，8，12，5，3，10，7，6の順にデータを与えたときにできる2分探索木はどれか。

## 選択肢
- ア: ![05a.png/image-size:101×64](https://www.fe-siken.com/kakomon/23_toku/img/05a.png)
- イ: ![05i.png/image-size:101×91](https://www.fe-siken.com/kakomon/23_toku/img/05i.png)
- ウ: ![05u.png/image-size:87×90](https://www.fe-siken.com/kakomon/23_toku/img/05u.png)
- エ: ![05e.png/image-size:88×91](https://www.fe-siken.com/kakomon/23_toku/img/05e.png)

## 正解
エ

## 解説
2分探索木
は、2分木の各節にデータをもたせることで探索を行えるようにした木です。各節がもつデータは「その節から出る左部分木にあるどのデータよりも大きく、右部分木のどのデータよりも小さい」という条件があり、これを利用して効率的にデータを探索することが可能になっています。
まず8をルートノード（根）とします。
12＞8なのでそのまま右の部分木に追加します。
5＜8なのでそのまま左の部分木に追加します。
3＜8なので左の部分木なります。さらに3＜5のため節点5の左の部分木に追加します。
10＞8なので右の部分木なります。さらに10＜12なので節点12の左の部分木に追加します。
7＜8なので左の部分木なります。さらに7＞5なので節点5の右の部分木に追加します。
6＜8なので左の部分木なります。続いて6＞5なので節点5の右の部分木になり、さらに6＜7なので節点7の左部分木に追加します。
この過程を経て完成した2分探索木は「エ」と同じ構造になります。

### 関連概念
