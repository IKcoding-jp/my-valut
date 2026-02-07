---
id: H28A_KA_Q06
year: H28秋
kamoku: A
number: 6
type: 混合
field: テクノロジ系 » アルゴリズムとプログラミング »データ構造
difficulty: 3
status: 未学習
source: "出典：平成28年秋期 基本情報技術者試験 科目A 問6"
source_url: "https://www.fe-siken.com/kakomon/28_aki/q6.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
2分探索木になっている2分木はどれか。

## 選択肢
- ア: ![06a.png/image-size:137×107](https://www.fe-siken.com/kakomon/28_aki/img/06a.png)
- イ: ![06i.png/image-size:137×107](https://www.fe-siken.com/kakomon/28_aki/img/06i.png)
- ウ: ![06u.png/image-size:164×107](https://www.fe-siken.com/kakomon/28_aki/img/06u.png)
- エ: ![06e.png/image-size:165×107](https://www.fe-siken.com/kakomon/28_aki/img/06e.png)

## 正解
イ

## 解説
2分探索木
は、2分木（各節からでる枝の数が2本以下になっている木）の各節にデータをもたせることで探索を行えるようにした木です。各節がもつデータは「
その節から出る左部分木にあるどのデータよりも大きく、右部分木のどのデータよりも小さい
」という条件があります。
要するに、どの部分を見ても「左＜中＜右」の関係を満たしていれば2分探索木といえるということです。最も簡単に見分ける方法は、図示されている木構造の各節点を左から順にならべて昇順になっているか否かを確認することです。

### 各選択肢の解説
- ア: 左から順に 10、15、14、16、19 となり、2分探索木の条件を満たすためには15と14の位置が逆だとわかります。
- イ: 左から順に 10、14、16、17、18、19 となり、昇順に整列されているため2分探索木だとわかります。
- ウ: 左から順に 15、16、14、18、19、20 となり、15、16、14の順番が昇順になっていません。
- エ: 左から順に 10、18、14、20、15、19、16 となり、昇順ではありません。なお、この木構造は2分探索木ではありませんが、全ての葉が同じ「深さ」を持っているため完全2分木という形状になっています。

### 関連概念
