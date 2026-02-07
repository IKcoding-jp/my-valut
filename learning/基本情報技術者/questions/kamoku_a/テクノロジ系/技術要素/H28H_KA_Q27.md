---
id: H28H_KA_Q27
year: H28春
kamoku: A
number: 27
type: 暗記
field: テクノロジ系 » データベース »データ操作
difficulty: 3
status: 未学習
source: "出典：平成28年春期 基本情報技術者試験 科目A 問27"
source_url: "https://www.fe-siken.com/kakomon/28_haru/q27.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
関係XとYを結合した後，関係Zを得る関係代数演算はどれか。![27.png/image-size:488×159](https://www.fe-siken.com/kakomon/28_haru/img/27.png)

## 選択肢
- ア: 射影と選択
- イ: 射影と和
- ウ: 選択
- エ: 選択と和

## 正解
ア

## 解説
まず関係Xと関係Yを、共通の属性"学部コード"で自然結合すると以下のようになります。
関係Zは結合後の関係から"学部コード"がBである2行を抽出し、さらに｛学生番号，氏名，学部名｝の3つの列を取り出した結果です。
関係から条件に合う行（レコード／タプル）を取り出す操作を
選択
といい、"学部コード"がBである2行を抽出する操作がこれに該当します。また、関係から指定した列（属性）を取り出す操作を
射影
といい、｛学生番号，氏名，学部名｝の3つの列を取り出す操作がこれに該当します。
関係Zを得るために行われた関係演算はこの2つなので、正解は「ア」となります。

### 関連概念
