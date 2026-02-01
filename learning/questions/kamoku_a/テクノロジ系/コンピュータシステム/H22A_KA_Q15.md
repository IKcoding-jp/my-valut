---
id: H22A_KA_Q15
year: H22秋
kamoku: A
number: 15
type: 暗記
field: テクノロジ系 » システム構成要素 »システムの構成
difficulty: 3
status: 未学習
source: "出典：平成22年秋期 基本情報技術者試験 科目A 問15"
source_url: "https://www.fe-siken.com/kakomon/22_aki/q15.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
NAS(Network Attached Storage)の構成図として適切なものはどれか。ここで，図の![15.png/image-size:23×17](https://www.fe-siken.com/kakomon/22_aki/img/15.png)はストレージの管理専用のファイルシステムを，二重線はストレージアクセス用のプロトコルを使用する専用ネットワークを意味するものとする。

## 選択肢
- ア: ![15a.png/image-size:145×136](https://www.fe-siken.com/kakomon/22_aki/img/15a.png)
- イ: ![15i.png/image-size:146×130](https://www.fe-siken.com/kakomon/22_aki/img/15i.png)
- ウ: ![15u.png/image-size:145×135](https://www.fe-siken.com/kakomon/22_aki/img/15u.png)
- エ: ![15e.png/image-size:140×103](https://www.fe-siken.com/kakomon/22_aki/img/15e.png)

## 正解
エ

## 解説
NAS
(Network Attached Storage)は、TCP/IPのコンピュータネットワークに直接接続して使用するファイルサーバでコントローラーとハードディスクから構成されています。
ファイルサービス専用のコンピュータであり、専用化や用途に合うようにチューニングされたOSなどにより、高速なファイルサービスと容易な管理機能が実現されています。
問題の構成図ですが、「NASの特徴であるネットワークに直接接続されている」ことを満たしているのは、「ウ」と「エ」、「NAS自身が管理システムをもっている」のは、「イ」と「エ」です。
したがって両方の特徴を示す「エ」がNASが正しく接続されている構成図ということになります。
ちなみに「ア」や「イ」のように、ネットワークを経由せずに直接PCに接続して使用する形態のストレージを、NASに対して
DAS
(Direct Attached Storage)といいます。

### 関連概念
- [[DAS]]
- [[NAS]]
- [[TCP/IP]]
- [[ネットワーク]]
- [[プロトコル]]
