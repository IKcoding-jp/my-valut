---
id: H29H_KA_Q08
year: H29春
kamoku: A
number: 8
type: 理解
field: テクノロジ系 » コンピュータ構成要素 »プロセッサ
difficulty: 3
status: 未学習
source: "出典：平成29年春期 基本情報技術者試験 科目A 問8"
source_url: "https://www.fe-siken.com/kakomon/29_haru/q8.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
動作クロック周波数が700MHzのCPUで，命令の実行に必要なクロック数とその命令の出現率が表に示す値である場合，このCPUの性能は約何MIPSか。![08.png/image-size:389×98](https://www.fe-siken.com/kakomon/29_haru/img/08.png)

## 選択肢
- ア: 10
- イ: 50
- ウ: 70
- エ: 100

## 正解
エ

## 解説
まず1命令を実行するのに必要な平均クロック数を求めます。
各命令を実行するのに必要なクロック数に、出現率を乗じたものを足し合わせて、
(4×0.3)＋(8×0.6)＋(10×0.1)
＝1.2＋4.8＋1.0＝7.0
上の計算結果から、1命令に必要な平均クロック数は7クロックであるとわかります。
CPUの動作クロック数が700MHzなので、1秒間の命令実行可能回数は、
700×10
6
÷7＝100×10
6
回
MIPSは1秒間に実行できる命令数を百万単位で表す指標なので、このCPUの性能は
100MIPS
になります。したがって「エ」が正解です。

### 関連概念
- [[MIPS]]
