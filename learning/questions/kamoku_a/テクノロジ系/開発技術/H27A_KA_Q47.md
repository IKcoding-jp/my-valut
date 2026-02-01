---
id: H27A_KA_Q47
year: H27秋
kamoku: A
number: 47
type: 暗記
field: テクノロジ系 » システム開発技術 »ソフトウェア構築
difficulty: 3
status: 未学習
source: "出典：平成27年秋期 基本情報技術者試験 科目A 問47"
source_url: "https://www.fe-siken.com/kakomon/27_aki/q47.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
プログラム中の図の部分を判定条件網羅(分岐網羅)でテストするときのテストケースとして，適切なものはどれか。![47.png/image-size:181×157](https://www.fe-siken.com/kakomon/27_aki/img/47.png)

## 選択肢
- ア: ![47a.png/image-size:88×40](https://www.fe-siken.com/kakomon/27_aki/img/47a.png)
- イ: ![47i.png/image-size:83×65](https://www.fe-siken.com/kakomon/27_aki/img/47i.png)
- ウ: ![47u.png/image-size:82×65](https://www.fe-siken.com/kakomon/27_aki/img/47u.png)
- エ: ![47e.png/image-size:82×91](https://www.fe-siken.com/kakomon/27_aki/img/47e.png)

## 正解
ウ

## 解説
ホワイトボックステスト
における網羅性のレベルである「分岐網羅」は、プログラム中の判定条件で結果が真となる場合、偽となる場合を少なくとも1回は実行するようにテストケースを設計する手法です。
問題の流れ図では、分岐の判定条件が「A OR B」となっているため、この判定条件で真偽の両方に分岐するテストケースとなっているかを検討します。

### 各選択肢の解説
- ア: テストケースが1つだけなので不適切です。
- イ: 2つのテストケースは「偽 OR 真＝真」「真 OR 偽＝真」となり、両方とも真である場合の処理にしか進まないので不適切です。
- ウ: 正しい。「偽 OR 偽＝偽」「真 OR 真＝真」となり、それぞれ真の場合の処理、偽の場合の処理に進むので分岐網羅のテストケースとして適切です。
- エ: 3つのテストケースは「偽 OR 真＝真」「真 OR 偽＝真」「真 OR 真＝真」となり、すべてが真である場合の処理にしか進まないので不適切です。

### 関連概念
- [[テスト]]
