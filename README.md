# Resume Guide - 引导式简历生成器

一个专业的简历生成助手，通过友好、耐心的多轮对话，逐步收集用户的个人信息和职业经历，然后生成精美的 PDF 简历。

## 特点

- 🗣️ **对话式收集** - 自然语言交互，不使用表单
- 🎯 **多级优化** - 5个优化级别，从真实还原到极致包装
- 🌐 **多语言支持** - 中文/英文简历
- 🎨 **多种模板** - 技术岗、经典通用、现代简约
- 💾 **数据保存** - 支持保存和修改已有简历

## 可用模板

| 模板名 | 说明 |
|--------|------|
| tech_zh | 技术岗 · 中文 |
| tech_en | 技术岗 · English |
| classic_zh | 经典通用 · 中文 |
| classic_en | 经典通用 · English |
| modern_zh | 现代简约 · 中文（侧边栏布局） |
| modern_en | 现代简约 · English（侧边栏布局） |

## 安装

1. 复制此目录到你的 Claude Code skills 目录：

```bash
cp -r resume-guide ~/.claude/skills/
```

2. 安装 Python 依赖：

```bash
pip3 install -r ~/.claude/skills/resume-guide/scripts/requirements.txt
```

## 使用

在 Claude Code 中输入：

```
/resume-guide
```

然后按照提示逐步填写你的信息即可。

## 项目结构

```
resume-guide/
├── SKILL.md           # 技能定义文件
├── scripts/           # PDF 生成脚本
│   ├── generate_pdf.py
│   └── requirements.txt
├── templates/         # 简历模板（HTML）
│   ├── tech_zh.html
│   ├── tech_en.html
│   ├── classic_zh.html
│   ├── classic_en.html
│   ├── modern_zh.html
│   └── modern_en.html
├── styles/           # 样式文件
│   └── base.css
└── fonts/            # 中文字体
    ├── NotoSansCJKsc-Regular.otf
    └── NotoSansCJKsc-Bold.otf
```

## 依赖

- Python 3.6+
- reportlab (PDF 生成)
- weasyprint (HTML 转 PDF)

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！
