---
id: H30H_KA_Q16
year: H30春
kamoku: A
number: 16
type: 暗記
field: テクノロジ系 » ソフトウェア »オペレーティングシステム
difficulty: 3
status: 未学習
source: "出典：平成30年春期 基本情報技術者試験 科目A 問16"
source_url: "https://www.fe-siken.com/kakomon/30_haru/q16.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
三つのタスクA～Cの優先度と，各タスクを単独で実行した場合のCPUと入出力装置(I/O)の動作順序と処理時間は，表のとおりである。A～Cが同時に実行可能状態になって3ミリ秒経過後から7ミリ秒間のスケジューリング状況を表したものはどれか。ここで，I/Oは競合せず，OSのオーバーヘッドは考慮しないものとする。また，表の()の数字は処理時間を表すものとし，解答群の中の"待ち"はタスクが実行可能状態にあり，CPUの割当て待ちであることを意味する。![16.png/image-size:383×98](https://www.fe-siken.com/kakomon/30_haru/img/16.png)

## 選択肢
- ア: ![16a.png/image-size:446×84](https://www.fe-siken.com/kakomon/30_haru/img/16a.png)
- イ: ![16i.png/image-size:447×84](https://www.fe-siken.com/kakomon/30_haru/img/16i.png)
- ウ: ![16u.png/image-size:447×84](https://www.fe-siken.com/kakomon/30_haru/img/16u.png)
- エ: ![16e.png/image-size:447×85](https://www.fe-siken.com/kakomon/30_haru/img/16e.png)

## 正解
ウ

## 解説
3タスクが実行可能状態になってから全タスクが完了するまでの、CPUとI/Oの使用状態は次のようになります。
上記の表と動作順序と処理時間が一致しているのは「ウ」です。

### 各選択肢の解説
まずCPUは、最も優先度の高いタスクAの処理を開始する
開始から2ミリ秒後、タスクAがI/Oに移る。タスクAがI/Oを行っている間、CPUは次に優先度の高いタスクBを処理する
開始から4ミリ秒後、タスクAのI/Oが完了する。優先度はタスクA＞タスクBなので、CPUはタスクBを実行可能状態に戻し、タスクAの処理を再開する
開始から6ミリ秒後、タスクAが完了する。CPUは優先度の高いタスクBの処理を開始する
開始から7ミリ秒後、タスクBがI/Oに移る。タスクBがI/Oを行っている間、CPUは残ったタスクCを処理する
開始から9ミリ秒後、タスクCの前半のCPU処理が完了する。I/Oは競合しないのでタスクCはI/O処理を開始する。以降11ミリ秒後までCPUは処理待ち状態になる
開始から11ミリ秒後、タスクCのI/Oが完了する。タスクBはI/O中なのでCPUはタスクCの処理を再開する
開始から12ミリ秒後、タスクBのI/Oが完了する。優先度はタスクB＞タスクCなので、CPUはタスクCを実行可能状態に戻し、タスクBの処理を再開する
開始から14ミリ秒後、タスクBが完了する。CPUは残ったタスクCの処理を再開する
開始から16ミリ秒後、タスクCが完了する

### 関連概念
