---
id: H24H_KA_Q31
year: H24春
kamoku: A
number: 31
type: 暗記
field: テクノロジ系 » データベース »データ操作
difficulty: 3
status: 未学習
source: "出典：平成24年春期 基本情報技術者試験 科目A 問31"
source_url: "https://www.fe-siken.com/kakomon/24_haru/q31.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
表Rに対する次のSQL文の操作はどの関係演算か。![31.png/image-size:243×40](https://www.fe-siken.com/kakomon/24_haru/img/31.png)〔SQL文〕SELECT A1, A3, A5, FROM R

## 選択肢
- ア: 結合
- イ: 差
- ウ: 射影
- エ: 直積

## 正解
ウ

## 解説
それぞれの演算は関係データベースの表に対する次のような操作を表してます。
射影表から選択した列を取り出す操作差基準となる表から別の表に属する行を取り除いたものを新しい表とする操作結合2つの表がもつ共通の属性で表を繋ぎ新しい表を作りだす操作直積関係データベースの2つの表の要素をすべて掛け合わせたものを新しい表とする操作
SELECT文は対象の表から指定されたデータを抽出するSQL文で、SELECT句につづき列名をカンマで区切って指定することでその列だけを抜き出すことが可能です。設問のSQL文は表RからA1，A3，A5列を抜き出すものなので、答えは「射影」になります。

### 関連概念
- [[FROM]]
- [[SELECT]]
- [[データベース]]
