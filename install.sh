#!/bin/bash

# Resume Guide - Claude Code Skill 安装脚本

set -e

echo "📄 正在安装 Resume Guide Skill..."

# 检查 Claude Code skills 目录
SKILLS_DIR="$HOME/.claude/skills"
if [ ! -d "$SKILLS_DIR" ]; then
    echo "❌ 错误: 未找到 Claude Code skills 目录 ($SKILLS_DIR)"
    echo "请确保已安装 Claude Code"
    exit 1
fi

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 复制技能文件
echo "📋 复制技能文件到 $SKILLS_DIR/resume-guide..."
cp -r "$SCRIPT_DIR" "$SKILLS_DIR/resume-guide"

# 安装 Python 依赖
echo "📦 安装 Python 依赖..."
pip3 install -q reportlab weasyprint || {
    echo "⚠️  警告: Python 依赖安装失败，请手动运行:"
    echo "   pip3 install reportlab weasyprint"
}

echo ""
echo "✅ Resume Guide 安装完成！"
echo ""
echo "🚀 使用方法:"
echo "   在 Claude Code 中输入: /resume-guide"
echo ""
echo "📁 安装位置: $SKILLS_DIR/resume-guide"
