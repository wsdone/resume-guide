# Resume Guide - 引导式简历生成器

> **Claude Code Skill** — 这是一个为 [Claude Code](https://claude.ai/code) 设计的技能插件

**[English](../README.md)** | **[日本語](README.ja.md)** | **[Español](README.es.md)**

一个专业的简历生成助手，通过友好、耐心的多轮对话，逐步收集用户的个人信息和职业经历，然后生成精美的 PDF 简历。

## 特点

- **对话式收集** — 自然语言交互，不使用表单
- **5 级优化** — 从真实还原到极致包装
- **多语言支持** — 中文/英文简历
- **多种模板** — 技术岗、经典通用、现代简约
- **数据保存** — 支持保存和修改已有简历

## 可用模板

| 模板名 | 说明 |
|--------|------|
| `tech_zh` | 技术岗 · 中文 |
| `tech_en` | 技术岗 · English |
| `classic_zh` | 经典通用 · 中文 |
| `classic_en` | 经典通用 · English |
| `modern_zh` | 现代简约 · 中文（侧边栏布局） |
| `modern_en` | 现代简约 · English（侧边栏布局） |

## 前置要求

- [Claude Code](https://claude.ai/code) — Anthropic 官方 AI 编程助手
- Python 3.6+
- pip3

## 安装

### 方式一：一键安装（推荐）

在 Claude Code 中运行：

```
/install https://github.com/wsdone/resume-guide
```

### 方式二：安装脚本

```bash
git clone https://github.com/wsdone/resume-guide.git
cd resume-guide
chmod +x install.sh
./install.sh
```

或者使用 curl：

```bash
curl -fsSL https://raw.githubusercontent.com/wsdone/resume-guide/main/install.sh | bash
```

### 方式三：手动安装

```bash
git clone https://github.com/wsdone/resume-guide.git
cp -r resume-guide ~/.claude/skills/
pip3 install -r ~/.claude/skills/resume-guide/scripts/requirements.txt
```

## 使用方法

安装完成后，在 **Claude Code** 中输入：

```
/resume-guide
```

技能会首先让你选择语言，然后引导你逐步完成简历创建。

## 项目结构

```
resume-guide/
├── install.sh           # 一键安装脚本
├── SKILL.md             # 技能定义文件
├── scripts/             # PDF 生成脚本
│   ├── generate_pdf.py
│   └── requirements.txt
├── templates/           # 简历模板（HTML）
│   ├── tech_zh.html
│   ├── tech_en.html
│   ├── classic_zh.html
│   ├── classic_en.html
│   ├── modern_zh.html
│   └── modern_en.html
├── styles/              # 样式文件
│   └── base.css
└── fonts/               # 中文字体
    ├── NotoSansCJKsc-Regular.otf
    └── NotoSansCJKsc-Bold.otf
```

## 依赖

- Python 3.6+
- weasyprint（HTML 转 PDF）
- Jinja2（模板渲染）

## 许可证

MIT License

## 相关项目

- [interview-coach](https://github.com/wsdone/interview-coach) — AI 面试教练

## 贡献

欢迎提交 Issue 和 Pull Request！
