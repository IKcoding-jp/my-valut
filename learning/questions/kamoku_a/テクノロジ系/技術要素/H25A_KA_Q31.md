---
id: H25A_KA_Q31
year: H25秋
kamoku: A
number: 31
type: 暗記
field: テクノロジ系 » データベース »トランザクション処理
difficulty: 3
status: 未学習
source: "出典：平成25年秋期 基本情報技術者試験 科目A 問31"
source_url: "https://www.fe-siken.com/kakomon/25_aki/q31.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
"商品"表に対して，更新SQL文を実行するトランザクションが，デッドロックの発生によって異常終了した。異常終了後の"商品"表はどれか。ここで，"商品"表に対する他のトランザクションは，参照は行うが更新はしないものとする。![31.png/image-size:216×108](https://www.fe-siken.com/kakomon/25_aki/img/31.png)〔更新SQL文〕DELETE FROM 商品 WHERE 商品コード＝'B020'

## 選択肢
- ア: ![31a.png/image-size:215×93](https://www.fe-siken.com/kakomon/25_aki/img/31a.png)
- イ: ![31i.png/image-size:214×92](https://www.fe-siken.com/kakomon/25_aki/img/31i.png)
- ウ: ![31u.png/image-size:214×70](https://www.fe-siken.com/kakomon/25_aki/img/31u.png)
- エ: ![31e.png/image-size:214×49](https://www.fe-siken.com/kakomon/25_aki/img/31e.png)

## 正解
イ

## 解説
トランザクションには「トランザクション内の処理がすべて実行されるか、または全く実行されないというどちらかの状態で終了しなければならない」という特性が要求されます。この特性をトランザクションの原子性(Atomicity)といいます。
障害やデッドロックによってトランザクションが正常終了しなかったときは、原子性を保証するために、DBMSはトランザクションの更新前ログを使用してデータベースをトランザクション開始直前の状態に戻す
ロールバック
を行います。これにより、データベースは何の処理も行わなかったのと同じ状態に戻ります。
したがって、異常終了後の表の状態はSQL文実行前と同じ状態の「イ」となります。

### 関連概念
- [[DELETE]]
- [[FROM]]
- [[WHERE]]
- [[データベース]]
- [[トランザクション]]
