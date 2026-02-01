---
id: H30A_KA_Q16
year: H30秋
kamoku: A
number: 16
type: 暗記
field: テクノロジ系 » ソフトウェア »オペレーティングシステム
difficulty: 3
status: 未学習
source: "出典：平成30年秋期 基本情報技術者試験 科目A 問16"
source_url: "https://www.fe-siken.com/kakomon/30_aki/q16.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
三つのタスクの優先度と，各タスクを単独で実行した場合のCPUと入出力装置(I/O)の動作順序と処理時間は，表のとおりである。優先度方式のタスクスケジューリングを行うOSの下で，三つのタスクが同時に実行可能状態になってから，全てのタスクの実行が終了するまでの，CPUの遊休時間は何ミリ秒か。ここで，CPUは1個であり，1CPUは1コアで構成され，I/Oは競合せず，OSのオーバーヘッドは考慮しないものとする。また，表の（ ）内の数字は処理時間を示すものとする。![16.png/image-size:348×99](https://www.fe-siken.com/kakomon/30_aki/img/16.png)

## 選択肢
- ア: 2
- イ: 3
- ウ: 4
- エ: 5

## 正解
イ

## 解説
CPUとI/Oが三つのタスクを処理する流れを図にまとめると次のようになります。
CPUが空き状態になるのは6～8ミリ秒の間と10～11ミリ秒の間で、全てのタスクが完了するまでのCPUの遊休時間は合計で「3ミリ秒」です。

### 関連概念
