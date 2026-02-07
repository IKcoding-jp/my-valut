---
id: H24H_KA_Q25
year: H24春
kamoku: A
number: 25
type: 混合
field: テクノロジ系 » ハードウェア »ハードウェア
difficulty: 3
status: 未学習
source: "出典：平成24年春期 基本情報技術者試験 科目A 問25"
source_url: "https://www.fe-siken.com/kakomon/24_haru/q25.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
7セグメントLED点灯回路で，出力ポートに16進数で6Dを出力したときの表示状態はどれか。ここで，P7を最上位ビット(MSB)，P0を最下位ビット(LSB)とし，ポート出力が1のとき，LEDは点灯する。![25.png/image-size:394×181](https://www.fe-siken.com/kakomon/24_haru/img/25.png)

## 選択肢
- ア: ![25a.png/image-size:53×72](https://www.fe-siken.com/kakomon/24_haru/img/25a.png)
- イ: ![25i.png/image-size:53×72](https://www.fe-siken.com/kakomon/24_haru/img/25i.png)
- ウ: ![25u.png/image-size:53×72](https://www.fe-siken.com/kakomon/24_haru/img/25u.png)
- エ: ![25e.png/image-size:54×72](https://www.fe-siken.com/kakomon/24_haru/img/25e.png)

## 正解
ウ

## 解説
まず入力値である16進数 6D を2進数に変換します。16進数を2進数に基数変換するときには、16進数を各桁ごとに2進数4桁に変えていくだけです。
P7が最上位ビット、P0が最下位ビットなので、ビット位置と出力ポートおよび点灯位置の関係は次のようになっています。
出力が"1"のポートに対応するLEDが点灯するため、点灯するLEDは最下位ビットから順番に「a, c, d, f，g」の5つです。点灯箇所を確認すると「ウ」の表示状態になることがわかります

### 関連概念
