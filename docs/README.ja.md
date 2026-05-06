# Resume Guide - 対話型レジュメジェネレーター

> **Claude Code Skill** — [Claude Code](https://claude.ai/code) 向けスキルプラグイン

**[English](../README.md)** | **[中文](README.zh-CN.md)** | **[Español](README.es.md)**

フレンドリーで忍耐強いマルチターンの対話を通じて、ユーザーの情報を収集し、洗練された PDF レジュメを生成するプロフェッショナルなレジュメアシスタントです。

## 特徴

- **対話型収集** — フォームを使わず、自然言語でインタラクション
- **5段階の最適化** — 忠実な再現から最大限の磨き上げまで
- **多言語対応** — 中国語 / 英語のレジュメ
- **複数テンプレート** — Tech、Classic、Modern
- **データ保存** — レジュメの保存と修正がいつでも可能

## 利用可能なテンプレート

| テンプレート | 説明 |
|-------------|------|
| `tech_zh` | 技術職 · 中国語 |
| `tech_en` | 技術職 · 英語 |
| `classic_zh` | クラシック · 中国語 |
| `classic_en` | クラシック · 英語 |
| `modern_zh` | モダン · 中国語（サイドバーレイアウト） |
| `modern_en` | モダン · 英語（サイドバーレイアウト） |

## 前提条件

- [Claude Code](https://claude.ai/code) — Anthropic 公式 AI コーディングアシスタント
- Python 3.6+
- pip3

## インストール

### 方法1：ワンクリックインストール（推奨）

Claude Code で次のコマンドを実行：

```
/install https://github.com/wsdone/resume-guide
```

### 方法2：インストールスクリプト

```bash
git clone https://github.com/wsdone/resume-guide.git
cd resume-guide
chmod +x install.sh
./install.sh
```

または curl を使用：

```bash
curl -fsSL https://raw.githubusercontent.com/wsdone/resume-guide/main/install.sh | bash
```

### 方法3：手動インストール

```bash
git clone https://github.com/wsdone/resume-guide.git
cp -r resume-guide ~/.claude/skills/
pip3 install -r ~/.claude/skills/resume-guide/scripts/requirements.txt
```

## 使い方

インストール後、**Claude Code** で次のように入力：

```
/resume-guide
```

スキルがまず言語の選択を求め、その後レジュメ作成プロセスをガイドします。

## 依存関係

- Python 3.6+
- weasyprint（HTML → PDF）
- Jinja2（テンプレートレンダリング）

## ライセンス

MIT License

## 関連プロジェクト

- [interview-coach](https://github.com/wsdone/interview-coach) — AI 面接コーチ

## コントリビュート

Issue と Pull Request を歓迎します！
