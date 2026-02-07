---
id: H26A_KA_Q12
year: H26秋
kamoku: A
number: 12
type: 暗記
field: テクノロジ系 » コンピュータ構成要素 »メモリ
difficulty: 3
status: 未学習
source: "出典：平成26年秋期 基本情報技術者試験 科目A 問12"
source_url: "https://www.fe-siken.com/kakomon/26_aki/q12.html"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
コンピュータの電源投入時に最初に実行されるプログラムの格納に適しているものはどれか。ここで，主記憶のバッテリバックアップはしないものとする。

## 選択肢
- ア: DRAM
- イ: HDD
- ウ: ROM
- エ: SRAM

## 正解
ウ

## 解説
ROM
(Read Only Memory)は、読み出し専用で、電源の供給が切れても内容を保持しておくことのできる不揮発性のメモリです。
内容の書き換えができないという特徴を利用して、変更する必要のないシステムプログラムなどを格納しておく用途に使用されることが多いです。
一般的にはコンピュータに電源を投入すると、マザーボード上の
ROM
に格納されている「IPL」(Initial Program Loader)というプログラムが起動し、その後ハードディスク内のブートプログラム、続いてOSという順で起動して操作可能な状態になります。
DRAMとSRAMは電源供給がなくなると記憶内容が消去されてしまう揮発性メモリという点で不適切、HDDは書換えが可能な点で不適切です。

### 関連概念
- [[ROM]]
