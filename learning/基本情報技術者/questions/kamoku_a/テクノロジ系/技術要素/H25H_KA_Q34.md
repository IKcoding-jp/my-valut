---
id: H25H_KA_Q34
year: H25春
kamoku: A
number: 34
type: 混合
field: テクノロジ系 » ネットワーク »ネットワーク方式
difficulty: 3
status: 未学習
source: "出典：平成25年春期 基本情報技術者試験 科目A 問34"
source_url: "https://www.fe-siken.com/kakomon/25_haru/q34.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
LANに接続されている複数のPCを，FTTHを使ってインターネットに接続するシステムがあり，装置AのWAN側インタフェースには1個のグローバルIPアドレスが割り当てられている。この1個のグローバルIPアドレスを使って複数のPCがインターネットを利用するのに必要となる装置Aの機能はどれか。![34.png/image-size:387×88](https://www.fe-siken.com/kakomon/25_haru/img/34.png)

## 選択肢
- ア: DHCP
- イ: NAPT(IPマスカレード)
- ウ: PPPoE
- エ: パケットフィルタリング

## 正解
イ

## 解説
NAPT
(IPマスカレード)は、プライベートIPアドレスとグローバルIPアドレスを相互変換するNATの考え方にポート番号を組み合わせた技術です。NAPTでは、インターネットに接続するノードに対して固有のポート番号を割り当て、IPアドレスだけでなくポート番号も一緒に変換します。これにより、1つのグローバルIPアドレスを使ってプライベートネットワーク内の複数のノードが同時にインターネットに接続することが可能となります。

### 各選択肢の解説
- ア: Dynamic Host Configuration Protocolの略。TCP/IPで、ネットワークに接続するノードへのIPアドレスの割り当てを自動的に行うプロトコルです。
- イ: 正しい。1つのグローバルIPアドレスで複数のPCが同時にインターネットを利用するためにはNAPT機能が必要です。
- ウ: Point-to-Point Protocol over Ethernetの略。PPPプロトコルをEthernet上で利用するためのプロトコルです。
- エ: パケットフィルタリング、通過するパケットのヘッダー情報を検査し、許可されたパケットのみをネットワークの内外へ通過させる機能です。主にファイアウォールやルータなどネットワークの境界に設置される機器に装備されています。

### 関連概念
- [[NAPT]]
- [[TCP/IP]]
- [[ネットワーク]]
- [[ファイアウォール]]
- [[プロトコル]]
