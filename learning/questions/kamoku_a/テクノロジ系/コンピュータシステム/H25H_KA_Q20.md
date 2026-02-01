---
id: H25H_KA_Q20
year: H25春
kamoku: A
number: 20
type: 混合
field: テクノロジ系 » ソフトウェア »オペレーティングシステム
difficulty: 3
status: 未学習
source: "出典：平成25年春期 基本情報技術者試験 科目A 問20"
source_url: "https://www.fe-siken.com/kakomon/25_haru/q20.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
仮想記憶管理におけるページ置換えの方式のうち，LRU制御方式はどれか。

## 選択肢
- ア: 各ページに参照フラグと変更フラグを付加して管理し，参照なしかつ変更なしのページを優先して置き換える。
- イ: 主記憶にある全てのページを同一の確率でランダムに選択し，置き換える。
- ウ: 最も長い間参照されていないページを置き換える。
- エ: 最も長い間主記憶にあったページを置き換える。

## 正解
ウ

## 解説
LRU
(Least Recently Used)は、置き換え対象の中で最も長い時間参照されていないものを置き換え対象とするアルゴリズムです。
このアルゴリズムは、最近使用されたページは再び近い将来に参照される可能性が高く、長い間参照されていないページは今後も参照される可能性が低いということを根拠としています。

### 各選択肢の解説
- ア: LFU(Least Frequently Used)方式の説明です。
- イ: ランダム置換アルゴリズムの説明です。
- ウ: 正しい。LRU方式の説明です。
- エ: FIFO(First In First Out)方式の説明です。

### 関連概念
- [[LRU]]
- [[アルゴリズム]]
