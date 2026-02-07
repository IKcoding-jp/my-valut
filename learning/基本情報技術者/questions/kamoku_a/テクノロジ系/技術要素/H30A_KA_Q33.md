---
id: H30A_KA_Q33
year: H30秋
kamoku: A
number: 33
type: 混合
field: テクノロジ系 » ネットワーク »通信プロトコル
difficulty: 3
status: 未学習
source: "出典：平成30年秋期 基本情報技術者試験 科目A 問33"
source_url: "https://www.fe-siken.com/kakomon/30_aki/q33.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
TCP/IPネットワークでDNSが果たす役割はどれか。

## 選択肢
- ア: PCやプリンターなどからのIPアドレス付与の要求に対して，サーバに登録してあるIPアドレスの中から使用されていないIPアドレスを割り当てる。
- イ: サーバにあるプログラムを，サーバのIPアドレスを意識することなく，プログラム名の指定だけで呼び出すようにする。
- ウ: 社内のプライベートIPアドレスをグローバルIPアドレスに変換し，インターネットへのアクセスを可能にする。
- エ: ドメイン名やホスト名などとIPアドレスとを対応付ける。

## 正解
エ

## 解説
TCP/IPを利用したネットワークでは、各ノードを識別するため一意のIPアドレスが割り当てられていますが、このIPアドレスは数字の羅列で人間にとって覚えにくいため、IPアドレスと対応する別名であるドメイン名が付けられています。
DNS
(Domain Name System)は、このドメイン名とIPアドレスを結びつけて相互変換する(名前解決する)仕組みです。

### 各選択肢の解説
- ア: DHCP(Dynamic Host Configuration Protocol)の説明です。
- イ: RPC(Remote Procedure Call)の役割です。
- ウ: NAT(Network Address Translation)の説明です。
- エ: 正しい。DNSの説明です。

### 関連概念
- [[DNS]]
- [[TCP/IP]]
- [[ネットワーク]]
