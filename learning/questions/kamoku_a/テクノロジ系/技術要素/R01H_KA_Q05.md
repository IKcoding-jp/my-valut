---
id: R01H_KA_Q05
year: R01春
kamoku: A
number: 5
type: 混合
field: テクノロジ系 » アルゴリズムとプログラミング »データ構造
difficulty: 3
status: 未学習
source: "出典：令和元年春期 基本情報技術者試験 科目A 問5"
source_url: "https://www.fe-siken.com/kakomon/31_haru/q5.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
2分探索木として適切なものはどれか。ここで，1～9の数字は，各ノード(節)の値を表す。

## 選択肢
- ア: ![05a.png/image-size:148×124](https://www.fe-siken.com/kakomon/31_haru/img/05a.png)
- イ: ![05i.png/image-size:148×125](https://www.fe-siken.com/kakomon/31_haru/img/05i.png)
- ウ: ![05u.png/image-size:148×125](https://www.fe-siken.com/kakomon/31_haru/img/05u.png)
- エ: ![05e.png/image-size:148×124](https://www.fe-siken.com/kakomon/31_haru/img/05e.png)

## 正解
イ

## 解説
2分探索木
は、2分木の各節にデータをもたせることで探索を行えるようにした木構造です。各節がもつデータは「
その節から出る左部分木にあるどのデータよりも大きく、右部分木のどのデータよりも小さい
」という条件があり、これを利用して効率的にデータを探索することができるようになっています。
「左部分木の値＜ノードの値＜右部分木の値」という2分探索木の条件に照らして選択肢の木構造を検証すると、2分探索木として適切な木は「イ」とわかります。

### 関連概念
