---
id: R01A_KA_Q47
year: R01秋
kamoku: A
number: 47
type: 暗記
field: テクノロジ系 » システム開発技術 »ソフトウェア構築
difficulty: 3
status: 未学習
source: "出典：令和元年秋期 基本情報技術者試験 科目A 問47"
source_url: "https://www.fe-siken.com/kakomon/01_aki/q47.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
エラー埋込法において，埋め込まれたエラー数をS，埋め込まれたエラーのうち発見されたエラー数をm，埋め込まれたエラーを含まないテスト開始前の潜在エラー数をT，発見された総エラー数をnとしたとき，S，T，m，nの関係を表す式はどれか。

## 選択肢
- ア: mS＝n－mT
- イ: mS＝Tn－m
- ウ: mS＝nT
- エ: mS＝Tn

## 正解
ア

## 解説
まず4つのエラー数の関係を図示します。
潜在エラーのうちテストで発見されたエラー数は、次の式で表すことができます（下のオレンジ色の部分）。
発見された総エラー数－埋め込まれたエラーのうち発見されたエラー数＝n－m
埋め込まれたエラーの発見率
mS
と潜在エラーの発見率
n－mT
は同程度と考えられるので、
mS
＝
n－mT
の関係式が成り立ちます。

### 関連概念
- [[テスト]]
