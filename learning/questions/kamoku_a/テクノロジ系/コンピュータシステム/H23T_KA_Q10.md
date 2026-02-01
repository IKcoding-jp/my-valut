---
id: H23T_KA_Q10
year: H23特
kamoku: A
number: 10
type: 混合
field: テクノロジ系 » コンピュータ構成要素 »メモリ
difficulty: 3
status: 未学習
source: "出典：平成23年特別 基本情報技術者試験 科目A 問10"
source_url: "https://www.fe-siken.com/kakomon/23_toku/q10.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
"LOAD　GR, B, AD"は，ADが示す番地にベースレジスタBの内容を加えた値を有効アドレスとして，その有効アドレスが示す主記憶に格納されているデータを汎用レジスタGRにロードする命令である。
図の状態で，次の命令を実行したとき，汎用レジスタGRにロードされるデータはどれか。
LOAD GR，1，200![10.png/image-size:317×295](https://www.fe-siken.com/kakomon/23_toku/img/10.png)

## 選択肢
- ア: 1201
- イ: 1300
- ウ: 2200
- エ: 2300

## 正解
イ

## 解説
命令語"LOAD　GR, B, AD"において引数であるADは「200」，Bは「1」なので、有効アドレスは200にベースレジスタ1が保持する値「100」を加算した
300
になります。
GRには主記憶上の300番地に格納されている値「1300」がロードされることになります。

### 関連概念
- [[LOAD]]
