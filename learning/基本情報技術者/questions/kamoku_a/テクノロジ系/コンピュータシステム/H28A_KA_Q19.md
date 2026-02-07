---
id: H28A_KA_Q19
year: H28秋
kamoku: A
number: 19
type: 混合
field: テクノロジ系 » ソフトウェア »オペレーティングシステム
difficulty: 3
status: 未学習
source: "出典：平成28年秋期 基本情報技術者試験 科目A 問19"
source_url: "https://www.fe-siken.com/kakomon/28_aki/q19.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
LRUアルゴリズムで，ページ置換えの判断基準に用いられる項目はどれか。

## 選択肢
- ア: 最後に参照した時刻
- イ: 最初に参照した時刻
- ウ: 単位時間当たりの参照頻度
- エ: 累積の参照回数

## 正解
ア

## 解説
LRU
(Least Recently Used)は、ページアウト要求があった場合に管理している中で「最後に参照された時刻が最も昔であるページ」を置換え対象とするアルゴリズムです。このアルゴリズムにより最近参照されたページが主記憶に残り、使用頻度の低いページは新しいページと入れ替わることになります。
ちなみに「単位時間当たりの参照頻度」はLFU(Least Frequently Used)アルゴリズムが用いる基準です。

### 関連概念
- [[LRU]]
- [[アルゴリズム]]
