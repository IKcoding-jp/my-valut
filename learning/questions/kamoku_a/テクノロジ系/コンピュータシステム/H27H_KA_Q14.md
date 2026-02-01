---
id: H27H_KA_Q14
year: H27春
kamoku: A
number: 14
type: 混合
field: テクノロジ系 » システム構成要素 »システムの評価指標
difficulty: 3
status: 未学習
source: "出典：平成27年春期 基本情報技術者試験 科目A 問14"
source_url: "https://www.fe-siken.com/kakomon/27_haru/q14.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
オンラインリアルタイムシステムにおけるCPUの使用率と平均応答時間の関係を表したグラフとして，適切なものはどれか。ここで，トランザクションの発生はポアソン分布に従い，その処理時間は指数分布に従うものとする。

## 選択肢
- ア: ![14a.png/image-size:209×151](https://www.fe-siken.com/kakomon/27_haru/img/14a.png)
- イ: ![14i.png/image-size:199×152](https://www.fe-siken.com/kakomon/27_haru/img/14i.png)
- ウ: ![14u.png/image-size:206×151](https://www.fe-siken.com/kakomon/27_haru/img/14u.png)
- エ: ![14e.png/image-size:203×151](https://www.fe-siken.com/kakomon/27_haru/img/14e.png)

## 正解
ア

## 解説
M/M/1の待ち行列モデルに従うと利用率(CPU利用率)
※
がρ(ロー)の時の平均応答時間は次の式で計算することができます。
仮に平均サービス時間を1として利用率(ρ)の値を変化させていくと、
と、利用率が上がるにつれて加速度的に平均応答時間が増加していくことがわかります。この関係をグラフにしたものが「ア」です。
以下は管理人がExcelで作成した利用率の変化と平均応答時間の関係表したグラフです。「ア」のグラフとほぼ同じ変化を示していることが確認できると思います。
※
利用率…単位時間当たりに処理の窓口を利用している割合。この設問ではCPU使用率を利用率に置き換えて説明してます。

### 各選択肢の解説
0.2 のとき　1.25
0.4 のとき　1.66…
0.5 のとき　2.00
0.7 のとき　3.33…
0.9 のとき　10.00

### 関連概念
- [[トランザクション]]
