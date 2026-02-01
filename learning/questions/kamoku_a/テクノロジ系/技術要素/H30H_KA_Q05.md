---
id: H30H_KA_Q05
year: H30春
kamoku: A
number: 5
type: 暗記
field: テクノロジ系 » アルゴリズムとプログラミング »データ構造
difficulty: 3
status: 未学習
source: "出典：平成30年春期 基本情報技術者試験 科目A 問5"
source_url: "https://www.fe-siken.com/kakomon/30_haru/q5.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
次の二つのスタック操作を定義する。
PUSH n：スタックにデータ(整数値n)をプッシュする。
POP：スタックからデータをポップする。
空のスタックに対して，次の順序でスタック操作を行った結果はどれか。

PUSH 1 → PUSH 5 → POP → PUSH 7 → PUSH 6 → PUSH 4 → POP → POP → PUSH 3

## 選択肢
- ア: ![05a.png/image-size:30×102](https://www.fe-siken.com/kakomon/30_haru/img/05a.png)
- イ: ![05i.png/image-size:30×102](https://www.fe-siken.com/kakomon/30_haru/img/05i.png)
- ウ: ![05u.png/image-size:29×101](https://www.fe-siken.com/kakomon/30_haru/img/05u.png)
- エ: ![05e.png/image-size:29×101](https://www.fe-siken.com/kakomon/30_haru/img/05e.png)

## 正解
ウ

## 解説
コンピュータの世界で使われるデータ構造のひとつに「スタック」があります。スタックは、最後に格納したデータから先に取り出す後入れ先出し（Last-in First-out：LIFO）の構造をもちます。
スタックでは、データを挿入するPUSH命令、データを取り出すPOP命令を使用してデータ操作を行います。
空のスタックを命令通りに操作していくと、
PUSH 11PUSH 51，5POP1PUSH 71，7PUSH 61，7，6PUSH 41，7，6，4POP1，7，6POP1，7PUSH 31，7，3
となり、操作結果は「ウ」の状態になることがわかります。

### 関連概念
- [[POP]]
- [[PUSH]]
