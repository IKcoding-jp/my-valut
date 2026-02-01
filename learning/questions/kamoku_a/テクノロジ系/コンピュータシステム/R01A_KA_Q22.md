---
id: R01A_KA_Q22
year: R01秋
kamoku: A
number: 22
type: 混合
field: テクノロジ系 » ハードウェア »ハードウェア
difficulty: 3
status: 未学習
source: "出典：令和元年秋期 基本情報技術者試験 科目A 問22"
source_url: "https://www.fe-siken.com/kakomon/01_aki/q22.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
次の回路の入力と出力の関係として，正しいものはどれか。![22.png/image-size:260×112](https://www.fe-siken.com/kakomon/01_aki/img/22.png)

## 選択肢
- ア: ![22a.png/image-size:128×113](https://www.fe-siken.com/kakomon/01_aki/img/22a.png)
- イ: ![22i.png/image-size:126×113](https://www.fe-siken.com/kakomon/01_aki/img/22i.png)
- ウ: ![22u.png/image-size:128×114](https://www.fe-siken.com/kakomon/01_aki/img/22u.png)
- エ: ![22e.png/image-size:126×113](https://www.fe-siken.com/kakomon/01_aki/img/22e.png)

## 正解
イ

## 解説
設問中の各回路とその意味は次の通りです。
回路に適当なA・Bの組みを与えてみて出力を確認します。正しい出力である真理値表を残し、さらに別のA・Bを与えて正解を導くという方法で解いていきます。
まずは A=0、B=0 を試します。
出力Xは0となります。この検証で「ウ」と「エ」が誤りであることがわかり、正解の候補は「ア」「イ」に絞られます。
残った「ア」「イ」に対して、次は A=1、B=0 を試します。出力Xが0であれば「ア」が、出力Xが1であれば「イ」が正解です。
出力Xは1となります。よって、正解は「イ」になります。
また、本問の回路図はそれほど複雑ではないので、回路を論理式で表してベン図を用いて正解を導くこともできます。
回路図を論理式で表すと「
A
・B＋A・
B
」です。この集合をベン図上に表すと次にようになります。
この集合はXOR演算の集合と等しいため「イ」が正解と判断できます。

### 関連概念
