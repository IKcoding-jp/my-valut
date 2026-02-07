#!/usr/bin/env python3
"""
過去問自動取得スクリプト
fe-siken.com から基本情報技術者試験の問題を取得し、
既存のフォーマットに変換して保存する。

対応年度: H21春〜R06（新制度・旧制度両対応）
- 新制度（R02〜R06）: 科目A 60問（all指定時）
- 旧制度（〜R01）: 科目A 80問（all指定時）
- MAX_QUESTIONS_PER_RUN: 80（1回の実行で最大80問まで取得可能）

画像URL: ページURLのディレクトリ部分（base_url）を使い、
相対パスの画像を絶対URLに自動変換する。

使い方:
    # 単一問題取得
    python scripts/fetch_question.py R05 15
    python scripts/fetch_question.py H30春 15

    # 範囲指定取得
    python scripts/fetch_question.py R05 1-20

    # 科目A全問取得（R02以降: 60問、R01以前: 80問）
    python scripts/fetch_question.py R05 all
"""

import sys
import os
import re
import time
import json
import io
import requests
from bs4 import BeautifulSoup
from pathlib import Path

# Windows環境でのUTF-8出力を強制（絵文字・日本語の文字化け防止）
if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
if sys.stderr.encoding != "utf-8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# ── 設定 ──────────────────────────────────────────

BASE_URL = "https://www.fe-siken.com/kakomon"
REPO_ROOT = Path(__file__).resolve().parent.parent
QUESTIONS_DIR = REPO_ROOT / "questions" / "kamoku_a"
PROGRESS_FILE = REPO_ROOT / "learning" / "進捗ログ.md"
REQUEST_INTERVAL = 2.5  # サーバー負荷対策（秒）
MAX_QUESTIONS_PER_RUN = 80  # 旧制度80問にも対応
USER_AGENT = "Mozilla/5.0 (compatible; FEvault-study-tool/1.0)"

# ── 年度コード → URLパス変換 ──────────────────────

# 新制度（令和5年〜）: XX_menjo
# 旧制度（〜令和4年）: XX_haru / XX_aki
# 令和2-4年: XX_menjo (免除試験形式)
YEAR_MAP = {
    # 新制度 CBT（令和5年〜）
    "R07": "07_menjo", "R06": "06_menjo", "R05": "05_menjo",
    # 旧制度 → 免除試験
    "R04": "04_menjo", "R03": "03_menjo", "R02": "02_menjo",
    # 旧制度（春秋あり）
    "R01秋": "01_aki", "R01春": "31_haru",
    "H31春": "31_haru",
    "H30秋": "30_aki", "H30春": "30_haru",
    "H29秋": "29_aki", "H29春": "29_haru",
    "H28秋": "28_aki", "H28春": "28_haru",
    "H27秋": "27_aki", "H27春": "27_haru",
    "H26秋": "26_aki", "H26春": "26_haru",
    "H25秋": "25_aki", "H25春": "25_haru",
    "H24秋": "24_aki", "H24春": "24_haru",
    "H23秋": "23_aki", "H23特": "23_toku",
    "H22秋": "22_aki", "H22春": "22_haru",
    "H21秋": "21_aki", "H21春": "21_haru",
}

# 年度コード → 西暦年（frontmatter用）
YEAR_TO_WESTERN = {
    "R07": 2025, "R06": 2024, "R05": 2023, "R04": 2022,
    "R03": 2021, "R02": 2020, "R01": 2019,
    "H31": 2019, "H30": 2018, "H29": 2017, "H28": 2016,
    "H27": 2015, "H26": 2014, "H25": 2013, "H24": 2012,
    "H23": 2011, "H22": 2010, "H21": 2009,
}

# 年度コード → 日本語表記
YEAR_TO_LABEL = {
    "R07": "令和7年度", "R06": "令和6年度", "R05": "令和5年度",
    "R04": "令和4年度", "R03": "令和3年度", "R02": "令和2年度",
    "R01秋": "令和元年秋期", "R01春": "令和元年春期",
    "H31春": "平成31年春期",
    "H30秋": "平成30年秋期", "H30春": "平成30年春期",
    "H29秋": "平成29年秋期", "H29春": "平成29年春期",
    "H28秋": "平成28年秋期", "H28春": "平成28年春期",
    "H27秋": "平成27年秋期", "H27春": "平成27年春期",
    "H26秋": "平成26年秋期", "H26春": "平成26年春期",
    "H25秋": "平成25年秋期", "H25春": "平成25年春期",
    "H24秋": "平成24年秋期", "H24春": "平成24年春期",
    "H23秋": "平成23年秋期", "H23特": "平成23年特別",
    "H22秋": "平成22年秋期", "H22春": "平成22年春期",
    "H21秋": "平成21年秋期", "H21春": "平成21年春期",
}

# ── 分野判定 ──────────────────────────────────────

# fe-siken.comの分類 → リポジトリのディレクトリパス
FIELD_TO_DIR = {
    "基礎理論": "テクノロジ系/基礎理論",
    "アルゴリズム": "テクノロジ系/基礎理論",
    "離散数学": "テクノロジ系/基礎理論",
    "応用数学": "テクノロジ系/基礎理論",
    "情報に関する理論": "テクノロジ系/基礎理論",
    "通信に関する理論": "テクノロジ系/基礎理論",
    "計測・制御に関する理論": "テクノロジ系/基礎理論",
    "コンピュータ構成要素": "テクノロジ系/コンピュータシステム",
    "システム構成要素": "テクノロジ系/コンピュータシステム",
    "ソフトウェア": "テクノロジ系/コンピュータシステム",
    "ハードウェア": "テクノロジ系/コンピュータシステム",
    "プロセッサ": "テクノロジ系/コンピュータシステム",
    "メモリ": "テクノロジ系/コンピュータシステム",
    "入出力デバイス": "テクノロジ系/コンピュータシステム",
    "バス": "テクノロジ系/コンピュータシステム",
    "オペレーティングシステム": "テクノロジ系/コンピュータシステム",
    "ミドルウェア": "テクノロジ系/コンピュータシステム",
    "ファイルシステム": "テクノロジ系/コンピュータシステム",
    "開発ツール": "テクノロジ系/コンピュータシステム",
    "システムの評価指標": "テクノロジ系/コンピュータシステム",
    "ヒューマンインタフェース": "テクノロジ系/技術要素",
    "マルチメディア": "テクノロジ系/技術要素",
    "データベース": "テクノロジ系/技術要素",
    "データベース設計": "テクノロジ系/技術要素",
    "データ操作": "テクノロジ系/技術要素",
    "トランザクション処理": "テクノロジ系/技術要素",
    "ネットワーク": "テクノロジ系/技術要素",
    "ネットワーク方式": "テクノロジ系/技術要素",
    "通信プロトコル": "テクノロジ系/技術要素",
    "ネットワーク応用": "テクノロジ系/技術要素",
    "セキュリティ": "テクノロジ系/技術要素",
    "情報セキュリティ": "テクノロジ系/技術要素",
    "情報セキュリティ管理": "テクノロジ系/技術要素",
    "情報セキュリティ対策": "テクノロジ系/技術要素",
    "セキュリティ実装技術": "テクノロジ系/技術要素",
    "システム開発技術": "テクノロジ系/開発技術",
    "ソフトウェア開発管理技術": "テクノロジ系/開発技術",
    "プロジェクトマネジメント": "マネジメント系",
    "サービスマネジメント": "マネジメント系",
    "システム監査": "マネジメント系",
    "システム戦略": "ストラテジ系",
    "システム企画": "ストラテジ系",
    "経営戦略マネジメント": "ストラテジ系",
    "技術戦略マネジメント": "ストラテジ系",
    "ビジネスインダストリ": "ストラテジ系",
    "企業活動": "ストラテジ系",
    "法務": "ストラテジ系",
    "会計・財務": "ストラテジ系",
}

# 分野のキーワード → 細分類（field フロントマター用）
FIELD_KEYWORDS = {
    "セキュリティ": ["暗号", "認証", "攻撃", "ファイアウォール", "マルウェア", "脆弱性",
                   "SSL", "TLS", "PKI", "VPN", "WAF", "IDS", "IPS", "ディジタル署名",
                   "公開鍵", "秘密鍵", "共通鍵", "ハッシュ", "HTTPS"],
    "ネットワーク": ["IP", "ルータ", "プロトコル", "TCP", "UDP", "DNS", "DHCP",
                   "サブネット", "MACアドレス", "LAN", "WAN", "OSI", "HTTP",
                   "SMTP", "POP", "IMAP", "FTP", "NTP", "ポート番号"],
    "データベース": ["SQL", "正規化", "トランザクション", "ACID", "ロック", "デッドロック",
                   "主キー", "外部キー", "SELECT", "INSERT", "関係データベース", "ER図",
                   "インデックス", "ビュー"],
    "システム構成": ["稼働率", "MTBF", "MTTR", "スループット", "レスポンスタイム",
                   "フォールトトレラント", "冗長化", "負荷分散", "クラスタ",
                   "スケールアウト", "スケールアップ"],
}

# ── 問題タイプ自動判定 ────────────────────────────

def classify_question_type(question_text, explanation_text, field_path):
    """問題タイプを自動判定する（暗記/理解/混合）"""
    text = question_text + explanation_text

    # 計算・ロジックが必要なキーワード
    understanding_keywords = [
        "計算", "求めよ", "いくつか", "何倍", "何ビット", "稼働率",
        "スループット", "アドレス", "変換", "論理式", "真理値",
        "進数", "基数", "補数", "浮動小数点", "ソート", "探索",
        "トレース", "アルゴリズム", "フローチャート",
    ]

    # 暗記中心のキーワード
    memorization_keywords = [
        "どれか", "適切なもの", "正しいもの", "記述として",
        "説明として", "特徴として", "目的として",
    ]

    has_understanding = any(kw in text for kw in understanding_keywords)
    has_memorization = any(kw in text for kw in memorization_keywords)

    if has_understanding and has_memorization:
        return "混合"
    elif has_understanding:
        return "理解"
    else:
        return "暗記"


# ── HTML パーサー ─────────────────────────────────

def fetch_question_page(url):
    """指定URLからHTMLを取得してパースする"""
    headers = {"User-Agent": USER_AGENT}
    response = requests.get(url, headers=headers, timeout=15)
    response.encoding = "utf-8"

    if response.status_code != 200:
        return None, f"HTTP {response.status_code}"

    return BeautifulSoup(response.text, "html.parser"), None


def parse_question(soup, url):
    """BeautifulSoupオブジェクトから問題データを抽出する"""
    data = {"source_url": url}

    # ページURLのディレクトリ部分を取得（相対パスの画像URL解決用）
    base_url = url.rsplit("/", 1)[0] + "/"  # 例: https://www.fe-siken.com/kakomon/05_menjo/

    # 問題文
    mondai_div = soup.find("div", id="mondai")
    if mondai_div:
        # テキストと画像の両方を取得
        data["question_text"] = get_content_with_images(mondai_div, base_url)
    else:
        return None, "問題文が見つかりません"

    # 選択肢
    choices = {}
    for label, sel_id in [("ア", "select_a"), ("イ", "select_i"),
                           ("ウ", "select_u"), ("エ", "select_e")]:
        span = soup.find("span", id=sel_id)
        if span:
            choices[label] = get_content_with_images(span, base_url)
    data["choices"] = choices

    # 正解
    answer_box = soup.find("div", class_="answerBox")
    if answer_box:
        answer_text = answer_box.get_text(strip=True)
        # 「正解を表示する」ボタンの後の文字を取得
        answer_text = answer_text.replace("正解を表示する", "").strip()
        if answer_text:
            data["answer"] = answer_text[0]  # ア/イ/ウ/エの1文字
        else:
            # ボタン内のテキストからは取れない場合、kaisetsu から推定
            data["answer"] = guess_answer_from_explanation(soup)
    else:
        data["answer"] = guess_answer_from_explanation(soup)

    # 解説
    kaisetsu_div = soup.find("div", id="kaisetsu")
    if kaisetsu_div:
        explanation_parts = []
        for li in kaisetsu_div.find_all("li"):
            cls = li.get("class", [])
            label = ""
            if "lia" in cls:
                label = "ア"
            elif "lii" in cls:
                label = "イ"
            elif "liu" in cls:
                label = "ウ"
            elif "lie" in cls:
                label = "エ"
            text = li.get_text(strip=True)
            if label:
                explanation_parts.append(f"- {label}: {text}")
            else:
                explanation_parts.append(text)

        # 解説のリスト以外のテキストも取得
        general_text_parts = []
        for child in kaisetsu_div.children:
            if hasattr(child, "name"):
                if child.name not in ["ul", "ol", "script", "ins"]:
                    t = child.get_text(strip=True)
                    if t:
                        general_text_parts.append(t)
            elif isinstance(child, str) and child.strip():
                general_text_parts.append(child.strip())

        data["explanation_general"] = "\n".join(general_text_parts)
        data["explanation_choices"] = "\n".join(explanation_parts)
    else:
        data["explanation_general"] = ""
        data["explanation_choices"] = ""

    # 分類
    field_raw = ""
    for h3 in soup.find_all("h3"):
        if "分類" in h3.get_text():
            next_div = h3.find_next_sibling("div")
            if next_div:
                field_raw = next_div.get_text(strip=True)
                break
    data["field_raw"] = field_raw

    # 出典情報
    source_list = soup.find_all("ul", class_="recentList")
    if source_list:
        data["source_info"] = source_list[0].get_text(strip=True)
    else:
        data["source_info"] = ""

    return data, None


def get_content_with_images(element, base_url=""):
    """テキストと画像を含むコンテンツを取得する

    base_url: ページURLのディレクトリ部分（例: https://www.fe-siken.com/kakomon/05_menjo/）
              相対パスの画像を正しく解決するために使用
    """
    parts = []
    for child in element.descendants:
        if isinstance(child, str):
            text = child.strip()
            if text:
                parts.append(text)
        elif hasattr(child, "name") and child.name == "img":
            src = child.get("src", "")
            alt = child.get("alt", "画像")
            if src and not src.startswith("http"):
                if src.startswith("/"):
                    # 絶対パス（/img/titlelogo.png等）
                    src = f"https://www.fe-siken.com{src}"
                elif base_url:
                    # 相対パス（img/55.png等）→ ページURLベースで解決
                    src = f"{base_url}{src}"
                else:
                    src = f"https://www.fe-siken.com/{src}"
            parts.append(f"![{alt}]({src})")
        elif hasattr(child, "name") and child.name == "br":
            parts.append("\n")
    return "".join(parts)


def guess_answer_from_explanation(soup):
    """解説から正解を推定する"""
    kaisetsu = soup.find("div", id="kaisetsu")
    if not kaisetsu:
        return "?"
    for li in kaisetsu.find_all("li"):
        text = li.get_text(strip=True)
        if "正しい" in text or "正解" in text or "○" in text:
            cls = li.get("class", [])
            if "lia" in cls:
                return "ア"
            elif "lii" in cls:
                return "イ"
            elif "liu" in cls:
                return "ウ"
            elif "lie" in cls:
                return "エ"
    return "?"


# ── 分野の解析 ────────────────────────────────────

def parse_field(field_raw):
    """fe-siken.comの分類文字列からリポジトリのフィールド情報を生成する"""
    # 例: "テクノロジ系 » ソフトウェア » 開発ツール"
    parts = [p.strip() for p in field_raw.split("»")]

    # 最も具体的な分野名でディレクトリを決定
    dir_path = None
    field_detail = field_raw

    for part in reversed(parts):
        part_clean = part.strip()
        if part_clean in FIELD_TO_DIR:
            dir_path = FIELD_TO_DIR[part_clean]
            break

    # 大分類でのフォールバック
    if not dir_path and len(parts) >= 1:
        top = parts[0].strip()
        if "テクノロジ" in top:
            dir_path = "テクノロジ系/技術要素"
        elif "マネジメント" in top:
            dir_path = "マネジメント系"
        elif "ストラテジ" in top:
            dir_path = "ストラテジ系"
        else:
            dir_path = "テクノロジ系/技術要素"

    return dir_path, field_detail


# ── ファイル生成 ──────────────────────────────────

def generate_question_id(year_code, q_number):
    """問題IDを生成する"""
    # R05 → R05, H30春 → H30H, H30秋 → H30A
    base = year_code.replace("春", "H").replace("秋", "A").replace("特", "T")
    return f"{base}_KA_Q{q_number:02d}"


def generate_markdown(data, year_code, q_number):
    """問題データからMarkdownファイルの内容を生成する"""
    q_id = generate_question_id(year_code, q_number)
    dir_path, field_detail = parse_field(data.get("field_raw", ""))

    # 西暦年
    year_base = re.match(r'[RH]\d+', year_code)
    western_year = YEAR_TO_WESTERN.get(year_base.group() if year_base else year_code, 0)

    # 問題タイプ自動判定
    q_type = classify_question_type(
        data.get("question_text", ""),
        data.get("explanation_general", "") + data.get("explanation_choices", ""),
        dir_path
    )

    # 日本語ラベル
    year_label = YEAR_TO_LABEL.get(year_code, year_code)

    # 選択肢
    choices_text = ""
    for label in ["ア", "イ", "ウ", "エ"]:
        if label in data.get("choices", {}):
            choices_text += f"- {label}: {data['choices'][label]}\n"

    # 解説組み立て
    explanation = ""
    if data.get("explanation_general"):
        explanation += data["explanation_general"] + "\n\n"
    if data.get("explanation_choices"):
        explanation += "### 各選択肢の解説\n" + data["explanation_choices"]

    # 関連概念の抽出
    related = extract_related_concepts(data)
    related_text = "\n".join(f"- [[{c}]]" for c in related)

    md = f"""---
id: {q_id}
year: {year_code}
kamoku: A
number: {q_number}
type: {q_type}
field: {field_detail}
difficulty: 3
status: 未学習
source: "出典：{year_label} 基本情報技術者試験 科目A 問{q_number}"
source_url: "{data.get('source_url', '')}"
last_attempt: null
confidence_history: []
result_history: []
time_spent_seconds: []
---

## 問題
{data.get('question_text', '（取得失敗）')}

## 選択肢
{choices_text.rstrip()}

## 正解
{data.get('answer', '?')}

## 解説
{explanation.rstrip()}

### 関連概念
{related_text}
"""
    return md.strip() + "\n", dir_path, q_id


def extract_related_concepts(data):
    """問題文と解説からキーワードを抽出する"""
    text = (data.get("question_text", "") + " " +
            data.get("explanation_general", "") + " " +
            data.get("explanation_choices", ""))

    # よく出る技術用語パターン
    concepts = set()
    patterns = [
        r'[A-Z]{2,}[/・][A-Z]+',  # SSL/TLS, TCP/IP
        r'[A-Z]{2,}(?:\s|$)',     # HTTP, SQL, etc.
    ]

    for pattern in patterns:
        for match in re.findall(pattern, text):
            m = match.strip()
            if len(m) >= 2 and m not in ("OR", "AND", "NOT", "ON", "IF", "IN", "AS", "BY"):
                concepts.add(m)

    # 日本語の技術用語
    jp_terms = [
        "暗号化", "復号", "認証", "署名", "ハッシュ", "公開鍵", "秘密鍵", "共通鍵",
        "ファイアウォール", "正規化", "トランザクション", "稼働率", "冗長",
        "プロトコル", "アルゴリズム", "データベース", "ネットワーク",
        "オブジェクト指向", "テスト", "レビュー", "監査",
    ]
    for term in jp_terms:
        if term in text:
            concepts.add(term)

    return sorted(list(concepts))[:5]  # 最大5個


# ── 保存 ──────────────────────────────────────────

def save_question(md_content, dir_path, q_id):
    """問題ファイルを保存する"""
    target_dir = QUESTIONS_DIR / dir_path
    target_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{q_id}.md"
    filepath = target_dir / filename

    if filepath.exists():
        return filepath, True  # 既に存在（スキップ）

    filepath.write_text(md_content, encoding="utf-8")
    return filepath, False


# ── learning_progress.md 更新 ─────────────────────

def count_total_questions():
    """questions/ 配下の総問題数をカウントする"""
    count = 0
    for md_file in QUESTIONS_DIR.rglob("*.md"):
        if md_file.name != "_テンプレート.md":
            count += 1
    return count


# ── メイン処理 ────────────────────────────────────

def resolve_year_url(year_code):
    """年度コードからURLパスを解決する"""
    if year_code in YEAR_MAP:
        return YEAR_MAP[year_code]

    # フォールバック: 自動推定
    # R05 → 05_menjo, H30春 → 30_haru
    match = re.match(r'([RH])(\d+)(春|秋|特)?', year_code)
    if not match:
        return None

    era, num, season = match.groups()
    num = int(num)

    if era == "R" and num >= 2:
        return f"{num:02d}_menjo"
    elif season == "春":
        return f"{num:02d}_haru"
    elif season == "秋":
        return f"{num:02d}_aki"
    elif season == "特":
        return f"{num:02d}_toku"
    else:
        # 平成で季節指定なし → 春をデフォルト
        return f"{num:02d}_haru"


def fetch_single_question(year_code, q_number, verbose=True):
    """1問を取得して保存する"""
    url_path = resolve_year_url(year_code)
    if not url_path:
        print(f"  ❌ 年度コード '{year_code}' を解決できません")
        return False

    url = f"{BASE_URL}/{url_path}/q{q_number}.html"

    if verbose:
        print(f"  📥 取得中: {url}")

    soup, err = fetch_question_page(url)
    if err:
        print(f"  ❌ 取得失敗: {err}")
        return False

    data, err = parse_question(soup, url)
    if err:
        print(f"  ❌ パース失敗: {err}")
        return False

    md_content, dir_path, q_id = generate_markdown(data, year_code, q_number)
    filepath, skipped = save_question(md_content, dir_path, q_id)

    if skipped:
        if verbose:
            print(f"  ⏭️  スキップ（既存）: {filepath.relative_to(REPO_ROOT)}")
        return True

    if verbose:
        print(f"  ✅ 保存: {filepath.relative_to(REPO_ROOT)}")
        print(f"     分野: {data.get('field_raw', '不明')}")
        print(f"     正解: {data.get('answer', '?')}")

    return True


def fetch_range(year_code, start, end, verbose=True):
    """範囲指定で問題を取得する"""
    total = min(end - start + 1, MAX_QUESTIONS_PER_RUN)
    success = 0
    fail = 0
    skip = 0

    print(f"\n🔄 {YEAR_TO_LABEL.get(year_code, year_code)} 問{start}〜問{start + total - 1} を取得します...\n")

    for i, q_num in enumerate(range(start, start + total)):
        if i > 0:
            time.sleep(REQUEST_INTERVAL)

        url_path = resolve_year_url(year_code)
        url = f"{BASE_URL}/{url_path}/q{q_num}.html"

        print(f"[{i+1}/{total}] 問{q_num}: ", end="", flush=True)

        soup, err = fetch_question_page(url)
        if err:
            print(f"❌ {err}")
            fail += 1
            continue

        data, err = parse_question(soup, url)
        if err:
            print(f"❌ {err}")
            fail += 1
            continue

        md_content, dir_path, q_id = generate_markdown(data, year_code, q_num)
        filepath, skipped = save_question(md_content, dir_path, q_id)

        if skipped:
            print(f"⏭️  スキップ（既存）")
            skip += 1
        else:
            field = data.get('field_raw', '不明')
            answer = data.get('answer', '?')
            print(f"✅ {q_id} [{field}] 正解:{answer}")
            success += 1

    # サマリー
    total_questions = count_total_questions()
    print(f"\n{'─' * 50}")
    print(f"📊 結果サマリー")
    print(f"   新規取得: {success}問")
    print(f"   スキップ: {skip}問")
    print(f"   失敗:     {fail}問")
    print(f"   問題バンク総数: {total_questions}問")
    print(f"{'─' * 50}")

    return success


def main():
    if len(sys.argv) < 3:
        print("使い方:")
        print("  python scripts/fetch_question.py <年度> <問番号|範囲|all>")
        print()
        print("MAX_QUESTIONS_PER_RUN: 80（1回で最大80問）")
        print("all指定: R02以降=60問、R01以前=80問")
        print()
        print("例:")
        print("  python scripts/fetch_question.py R05 15        # 1問取得")
        print("  python scripts/fetch_question.py R05 1-20      # 範囲取得")
        print("  python scripts/fetch_question.py R05 all       # 全問取得（R02以降:60問, R01以前:80問）")
        print("  python scripts/fetch_question.py H30春 32      # 旧制度")
        print()
        print("対応年度:")
        for code in sorted(YEAR_MAP.keys()):
            label = YEAR_TO_LABEL.get(code, code)
            print(f"  {code:8s} → {label}")
        sys.exit(1)

    year_code = sys.argv[1]
    target = sys.argv[2]

    # URLパス確認
    url_path = resolve_year_url(year_code)
    if not url_path:
        print(f"❌ 年度コード '{year_code}' が見つかりません。")
        print(f"   対応年度一覧は引数なしで実行してください。")
        sys.exit(1)

    if target == "all":
        # 新制度(R02〜): 60問、旧制度(〜R01): 80問
        year_base = re.match(r'([RH])(\d+)', year_code)
        if year_base:
            era, num = year_base.group(1), int(year_base.group(2))
            if era == "R" and num >= 2:
                max_q = 60
            else:
                max_q = 80
        else:
            max_q = 80
        fetch_range(year_code, 1, max_q)
    elif "-" in target:
        # 範囲指定
        parts = target.split("-")
        start = int(parts[0])
        end = int(parts[1])
        fetch_range(year_code, start, end)
    else:
        # 単一問題
        q_number = int(target)
        print(f"\n🔄 {YEAR_TO_LABEL.get(year_code, year_code)} 問{q_number} を取得します...\n")
        success = fetch_single_question(year_code, q_number)
        if success:
            total = count_total_questions()
            print(f"\n   問題バンク総数: {total}問")


if __name__ == "__main__":
    main()
