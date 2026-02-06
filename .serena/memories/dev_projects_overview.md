# 開発プロジェクト全体構造（D:\Dev）

## 概要
けんさくの開発プロジェクトは `D:\Dev` で一元管理されており、2026年2月1日に Vault の `projects/` 配下にシンボリックリンク化。Obsidian から直接アクセス可能。

---

## 主要実績プロジェクト

### 1. Roast Plus（業務アプリ）
- **所在**: D:\Dev\roastplus → projects/roastplus (symlink)
- **技術**: Next.js 16, React 19.2.0, TypeScript, Tailwind CSS v4
- **バックエンド**: Firebase, OpenAI API, EmailJS
- **UI/UX**: Framer Motion, Lottie, Phosphor Icons
- **テスト**: Vitest + React Testing Library
- **品質**: ESLint, Husky git hooks, 複雑性分析（Lizard）, デッドコード検出（Knip）
- **特徴**: 
  - 業務用アプリ（同僚8名が実運用中）
  - SRS（間隔反復システム）学習機能搭載（ts-fsrs）
  - 555+ commits（本格開発規模）
  - セキュリティ監査機能搭載
- **バージョン**: 0.10.2

### 2. maiKago（買い物管理アプリ）
- **所在**: D:\Dev\maikago → projects/maikago (symlink)
- **技術**: Flutter, Dart 3.0+, Firebase ecosystem
- **バックエンド**: Firebase Core, Auth, Firestore, Cloud Functions
- **認証**: Google Sign-In
- **マネタイズ**: In-App Purchase (iOS/Android), Google Mobile Ads
- **UI**: Material Design, Google Fonts
- **プラットフォーム**: iOS, Android, Web, Windows, macOS
- **特徴**:
  - Google Play で公開済み
  - 買いすぎ防止をテーマにした機能設計
  - マルチプラットフォーム対応（Flutter の強み）
  - カメラ・画像ピッカー統合、地理情報取得
- **バージョン**: 1.3.1+54

---

## その他開発プロジェクト（D:\Dev 配下、全19個）

### AI・学習支援系
- **aichatbot** → AI チャットボット
- **nofap-ai** → メンタルサポート系AI

### アプリ開発
- **4OCR / 4OCRtauri** → 光学文字認識 (OCR) アプリ（Rust/Tauri）
- **pomodorotimer** → ポモドーロテクニック タイマー
- **taskmanager** → タスク管理アプリ
- **medilog** → メディア/ログ管理

### 習慣・健康系
- **atomic-habits** → 習慣管理（Atomic Habits に基づく）
- **habitquest** → ゲーム感覚の習慣トラッカー
- **okusurism** → 服薬管理アプリ

### Claude Code 学習
- **claude-code-demo** → Claude Code デモ
- **claude-code-study** → Claude Code 学習プロジェクト
- **claude-code-study-nextjs** → Next.js 版

### その他
- **earthone** → 未確認（プロジェクト名から地球・環境関連？）
- **portfolio** → ポートフォリオサイト
- **reboot!** → リブートプロジェクト
- **learning** → 学習リソース

---

## シンボリックリンク設定（2026年2月1日実施）

すべてのプロジェクトは `D:\My vault\projects/` 配下に symlink 化済み：

```
projects/
├── roastplus → D:\Dev\roastplus
├── maikago → D:\Dev\maikago
├── aichatbot → D:\Dev\aichatbot
├── atomic-habits → D:\Dev\atomic-habits
├── 4ocr → D:\Dev\4OCR
├── 4ocr-tauri → D:\Dev\4OCRtauri
├── claude-code-demo → D:\Dev\claude-code-demo
├── claude-code-study → D:\Dev\claude-code-study
├── claude-code-study-nextjs → D:\Dev\claude-code-study-next.js
├── earthone → D:\Dev\earthone
├── habitquest → D:\Dev\habitquest
├── medilog → D:\Dev\medilog
├── nofap-ai → D:\Dev\nofap-ai
├── okusurism → D:\Dev\okusurism
├── pomodorotimer → D:\Dev\pomodorotimer
├── portfolio → D:\Dev\portfolio
├── reboot → D:\Dev\reboot!
├── taskmanager → D:\Dev\taskmanager
└── learning → D:\Dev\learning
```

---

## 技術スタック分析

### フロントエンド
- **モダン Web**: Next.js 16, React 19, TypeScript, Tailwind CSS
- **モバイル**: Flutter/Dart（クロスプラットフォーム）
- **デスクトップ**: Tauri（Rust ベース）

### バックエンド
- **Firebase** (Roast Plus, maiKago の核)
  - Authentication
  - Cloud Firestore（NoSQL DB）
  - Cloud Functions（サーバーレス）
  - Hosting

### 外部API連携
- OpenAI API（Roast Plus）
- EmailJS（メール送信）
- Google Sign-In
- Google Mobile Ads

### 品質管理
- **Linting**: ESLint 9
- **Testing**: Vitest (Unit/Integration)
- **型チェック**: TypeScript 5
- **セキュリティ**: npm audit
- **複雑性分析**: Lizard
- **デッドコード検出**: Knip
- **Git Hooks**: Husky, lint-staged

---

## 今後の参照ガイド

### セッション中のプロジェクト参照
- README.md、ドキュメント、ソースコードは `projects/[プロジェクト名]/` 配下で直接アクセス可能
- 開発相談時はこのメモを参照して背景情報を提供

### 新規プロジェクト追加時
1. D:\Dev に作成
2. PowerShell (admin) で symlink 追加:
   ```powershell
   New-Item -ItemType SymbolicLink -Name "[name]" -Target "D:\Dev\[name]" -Force
   ```
3. このメモ更新

### 開発レベル評価
- **本格開発規模**: Roast Plus（555+ commits、フルスタック、本番運用）、maiKago（マルチプラットフォーム、マネタイズ）
- **学習プロジェクト**: Claude Code 学習、習慣管理等
- **実験的**: 新しい技術スタック試験、AI連携実験
