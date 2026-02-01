# Vault 自動修正ロジック

自動修正可能な6項目の実装詳細。低リスク修正のみをここに記載。

---

## 1. Frontmatter追加（learning/questions/）

### 条件

- `learning/questions/` 配下のファイル
- frontmatterが存在しない OR frontmatterが不完全（必須フィールド不足）

### 処理フロー

1. **既存frontmatterの確認**
   - frontmatterが存在する場合 → マージ（既存フィールド保持）
   - frontmatterが存在しない場合 → 作成

2. **必須フィールドの抽出**
   ```yaml
   exam_id: "[ファイルパスから推測]" # 例: kamoku_a → FE-A
   question_id: "[ファイル名から抽出]" # 例: H21H_KA_Q61.md → H21H_KA_Q61
   topic: "[フォルダ構造から推測]" # 例: ストラテジ系 → ストラテジ
   tags: ["#learning/基本情報"]
   correct_answer: "[ファイル内から検出 or 未判定]"
   difficulty: "未評価"
   status: "not_attempted"
   created: "[ファイルのmtimeから推測]"
   ```

3. **本体コンテンツの保持**
   - frontmatter前のコンテンツをそのまま保持
   - ただし、frontmatter後に重複するメタデータ行があれば削除

4. **Git安全性**
   - frontmatter追加前に「git add」で修正ファイルを記録
   - 追加後に「git diff」で変更を確認

### 実装例

```markdown
---
exam_id: FE-A
question_id: H21H_KA_Q61
topic: ストラテジ系
tags: ["#learning/基本情報"]
correct_answer: C
difficulty: 中
status: not_attempted
created: 2025-01-15
last_attempt: null
confidence_history: []
result_history: []
---

# 問題: H21H_KA_Q61

[既存コンテンツをそのまま保持]
```

### リスク評価

**低リスク**。既存コンテンツを一切変更しないため。

---

## 2. タグ正規化（非標準 → 標準タグへのマッピング）

### 条件

- Vault全体のあらゆる `*.md` ファイル
- frontmatterの `tags` フィールドに非標準タグが含まれている

### マッピングテーブル

| 非標準タグ | 標準タグ | 理由 |
|-----------|--------|------|
| `#learning/FE` | `#learning/基本情報` | 略称→正式名 |
| `#learning/fe` | `#learning/基本情報` | 小文字→大文字 |
| `#learning/基本` | `#learning/基本情報` | 略称→正式名 |
| `#learning/coffee` | `#learning/コーヒーマイスター` | 英語→日本語 |
| `#project/roast` | `#project/roast-plus` | 略称→正式名 |
| `#reading/book` | `#reading/リスト` | 一般名→標準名 |
| `#status/doing` | `#status/進行中` | 英語→日本語 |
| `#status/done` | `#status/完了` | 英語→日本語 |
| `#priority/high` | `#priority/高` | 英語→日本語 |
| `#priority/medium` | `#priority/中` | 英語→日本語 |
| `#priority/low` | `#priority/低` | 英語→日本語 |

### 処理フロー

1. **ファイルごとに走査**
   ```
   各ファイルのfrontmatterのtagsフィールドを確認
   ```

2. **非標準タグの検出**
   ```
   既知の非標準タグとマッピングテーブルを照合
   マッピングなしの非標準タグの場合：
   - ユーザーに確認を取ってから修正
   - 修正しないで「提案」に含める
   ```

3. **置換実行**
   ```yaml
   # Before
   tags: ["#learning/FE", "#status/doing"]
   
   # After
   tags: ["#learning/基本情報", "#status/進行中"]
   ```

4. **Git記録**
   ```
   修正ファイルを「タグ正規化」として記録
   ```

### リスク評価

**低リスク**。タグの論理的意味は変わらず、置換ルールが明確。

---

## 3. 命名規則修正（ファイル移動 + wikilinkアップデート）

### 対象パターン

#### 3-1. デイリージャーナルパス修正

**違反例**: `journal/2026-02-01.md`

**修正先**: `journal/2026/02/2026-02-01.md`

### 処理フロー

1. **移動対象の特定**
   ```
   journal/配下のファイルで正規表現に非合致するもの
   パターン: ^journal/\d{4}/\d{2}/\d{4}-\d{2}-\d{2}\.md$
   に合わないファイル
   ```

2. **ディレクトリ作成**
   ```
   journal/YYYY/MM/ が存在しなければ作成
   ```

3. **ファイル移動**
   ```
   git mv journal/YYYY-MM-DD.md journal/YYYY/MM/YYYY-MM-DD.md
   ```

4. **wikilinkアップデート**
   ```
   Vault全体を走査
   [[journal/YYYY-MM-DD]] をすべて検出
   [[journal/YYYY/MM/YYYY-MM-DD]] に置換
   ```

5. **確認と記録**
   ```
   git status で移動が反映されているか確認
   git commit: "chore: journal命名規則修正 (XX件のファイル移動)"
   ```

### リスク評価

**中程度リスク**。wikilinkアップデートが必要。必ず git commit 前に確認を取る。

---

## 4. デフォルトfrontmatter追加（journal/）

### 条件

- `journal/YYYY/MM/YYYY-MM-DD.md` ファイル
- frontmatterが存在しない OR 最小限の情報のみ

### デフォルトfrontmatter

```yaml
---
date: YYYY-MM-DD
tags: ["#journal/日報"]
mood: "未記録"
energy_level: "未記録"
created: YYYY-MM-DDTHH:MM:SSZ
updated: YYYY-MM-DDTHH:MM:SSZ
---
```

### 処理フロー

1. **ファイル走査**
   ```
   journal/YYYY/MM/ 配下のすべてのファイル
   ```

2. **frontmatter確認**
   ```
   frontmatterがない場合 → テンプレートから作成
   frontmatterがある場合 → dateフィールド確認
   dateフィールドがない場合 → ファイル名から推測し追加
   ```

3. **タイムスタンプ推測**
   ```
   created: ファイルのmtime（ファイルシステムから取得）
   updated: 現在時刻
   ```

4. **本体コンテンツ保持**
   ```
   既存コンテンツはすべて保持
   ```

### リスク評価

**低リスク**。既存コンテンツを変更しない。

---

## 5. 過去問道場データの自動統合（CSVインポート）

### 条件

- `learning/過去問道場データ/` に新しいCSVファイルがある
- CSVがまだ `learning/questions/` に反映されていない

### 処理フロー

1. **CSV読み込み**
   ```python
   # cp932 エンコーディング必須
   df = pd.read_csv('file.csv', encoding='cp932')
   ```

2. **問題ファイルの作成 or 更新**
   ```
   各行について:
   - exam_id, question_id から ファイルパスを決定
   - 既存ファイルがあれば → frontmatterのみ更新（result_history追加）
   - 既存ファイルがなければ → 新規作成
   ```

3. **frontmatterへの記録**
   ```yaml
   result_history: [前回までの履歴] + [今回の成績]
   # 例:
   # result_history: 
   #   - date: 2026-01-20
   #     result: correct
   #     time_spent: 120
   #   - date: 2026-02-01
   #     result: incorrect
   #     time_spent: 90
   ```

4. **Git記録**
   ```
   git add learning/questions/
   git commit: "chore: 過去問道場データ統合 (YYYY-MM-DD実施分, XX問新規作成, YY問更新)"
   ```

### 注意事項

- **1回分（60問）ごとに実行**（過学習バイアス防止）
- CSV読み込み後はファイルを `learning/過去問道場データ/archive/` に移動（重複実行防止）

### リスク評価

**中程度リスク**。新規ファイル作成多数。ただしCSVスキーマが明確なため実装は堅牢。

---

## 6. memory_logs.md への要約追記

### 条件

- Vault健全性チェック実行後
- 緊急問題 OR 重要な修正があった場合

### 記録形式

```markdown
- **YYYY-MM-DD（Vault健全性チェック）**:
  - 健全性スコア: XX/100点（前回比 ±XX点）
  - 修正項目: [frontmatter追加XX件、タグ正規化XX箇所、命名規則修正XX件]
  - 緊急問題: [あれば記録]
  - 推奨改善: [TOP 3を記録]
```

### 処理フロー

1. **memory_logs.mdを開く**
   ```
   D:\My vault\memory_logs.md
   ```

2. **最新エントリの日付確認**
   ```
   最新エントリの日付を取得（スコアの前回比を計算）
   ```

3. **新規エントリの追加**
   ```
   ファイルの末尾に新規エントリを追加
   ```

4. **Git記録**
   ```
   git add memory_logs.md
   git commit に含める（別途commitmessageで記載）
   ```

### リスク評価

**低リスク**。既存エントリは変更しない。

---

## 自動修正の実行順序

必ずこの順序で実行（後の修正が前の結果に依存）:

1. **frontmatter追加** (learning/questions/)
2. **frontmatter追加** (journal/)
3. **タグ正規化**（全体）
4. **命名規則修正**（ファイル移動）
5. **wikilinkアップデート**（移動に伴う）
6. **過去問道場CSV統合**（フロー4の後）
7. **memory_logs.mdへの記録**

---

## Git安全性チェックリスト

修正実行前に確認:

- [ ] 現在のブランチが `main` である
- [ ] `git status` で未コミット変更がない
- [ ] バックアップcommitを作成: `git commit -m "chore: Vault健全性チェック実行前のバックアップ"`
- [ ] 修正後に `git diff --stat` で変更ファイル数が期待値と一致

修正実行後に確認:

- [ ] `git status` で変更が記録されている
- [ ] `git log --oneline` で新しいcommitが追加されている
- [ ] 修正内容が期待通り（サンプルファイル確認）

---

## 非自動化ケース（ユーザー確認必須）

以下は自動修正せず、**提案のみ**:

1. **重複情報の統合**
   - どのファイルが「情報源」か判定が必要
   - wikilinkへの参照変更が大規模

2. **ファイル削除**
   - 完全に不要なファイルの削除提案
   - ユーザーの明確な同意が必須

3. **セクション構造の修正**
   - テンプレート遵守の修正
   - セクション順序変更が大きな変更

4. **編集禁止エリアの修正**
   - `.obsidian/`, `LINE/` の不正な編集を検出
   - ユーザー確認後、git reset で戻す

---

*最終更新: 2026-02-01*
