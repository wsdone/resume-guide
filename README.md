# Resume Guide - Interactive Resume Generator

> **Claude Code Skill** — A skill plugin for [Claude Code](https://claude.ai/code)

**[中文](docs/README.zh-CN.md)** | **[日本語](docs/README.ja.md)** | **[Español](docs/README.es.md)**

A professional resume assistant that collects your information through friendly, patient multi-turn conversation, then generates a polished PDF resume.

## Features

- **Conversational** — Natural language interaction, no forms
- **5 Optimization Levels** — From faithful reproduction to maximum polish
- **Multi-language** — Chinese / English resumes
- **Multiple Templates** — Tech, Classic, Modern
- **Data Persistence** — Save and revise resumes anytime

## Available Templates

| Template | Description |
|----------|-------------|
| `tech_zh` | Tech · Chinese |
| `tech_en` | Tech · English |
| `classic_zh` | Classic · Chinese |
| `classic_en` | Classic · English |
| `modern_zh` | Modern · Chinese (sidebar layout) |
| `modern_en` | Modern · English (sidebar layout) |

## Prerequisites

- [Claude Code](https://claude.ai/code) — Anthropic's official AI coding assistant
- Python 3.6+
- pip3

## Installation

### Option 1: One-click install (Recommended)

Run this command in Claude Code:

```
/install https://github.com/wsdone/resume-guide
```

### Option 2: Install script

```bash
git clone https://github.com/wsdone/resume-guide.git
cd resume-guide
chmod +x install.sh
./install.sh
```

Or use curl:

```bash
curl -fsSL https://raw.githubusercontent.com/wsdone/resume-guide/main/install.sh | bash
```

### Option 3: Manual install

```bash
git clone https://github.com/wsdone/resume-guide.git
cp -r resume-guide ~/.claude/skills/
pip3 install -r ~/.claude/skills/resume-guide/scripts/requirements.txt
```

## Usage

After installation, type in **Claude Code**:

```
/resume-guide
```

Follow the prompts to fill in your information step by step. The skill will first ask you to choose your preferred language, then guide you through the resume creation process.

## Project Structure

```
resume-guide/
├── install.sh           # One-click install script
├── SKILL.md             # Skill definition
├── scripts/             # PDF generation
│   ├── generate_pdf.py
│   └── requirements.txt
├── templates/           # Resume HTML templates
│   ├── tech_zh.html
│   ├── tech_en.html
│   ├── classic_zh.html
│   ├── classic_en.html
│   ├── modern_zh.html
│   └── modern_en.html
├── styles/              # CSS styles
│   └── base.css
└── fonts/               # CJK fonts
    ├── NotoSansCJKsc-Regular.otf
    └── NotoSansCJKsc-Bold.otf
```

## Dependencies

- Python 3.6+
- weasyprint (HTML to PDF)
- Jinja2 (template rendering)

## License

MIT License

## Related Projects

- [interview-coach](https://github.com/wsdone/interview-coach) — AI Interview Coach

## Contributing

Issues and Pull Requests are welcome!
