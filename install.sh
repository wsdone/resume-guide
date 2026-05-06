#!/bin/bash

# Resume Guide - Claude Code Skill Install Script

set -e

echo "Installing Resume Guide Skill..."

# Check Claude Code skills directory
SKILLS_DIR="$HOME/.claude/skills"
if [ ! -d "$SKILLS_DIR" ]; then
    echo "Error: Claude Code skills directory not found ($SKILLS_DIR)"
    echo "Please make sure Claude Code is installed."
    exit 1
fi

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Copy skill files
echo "Copying skill files to $SKILLS_DIR/resume-guide..."
cp -r "$SCRIPT_DIR" "$SKILLS_DIR/resume-guide"

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install -q weasyprint Jinja2 || {
    echo "Warning: Python dependency installation failed. Please run manually:"
    echo "   pip3 install weasyprint Jinja2"
}

echo ""
echo "Resume Guide installed successfully!"
echo ""
echo "Usage:"
echo "   In Claude Code, type: /resume-guide"
echo ""
echo "Installed to: $SKILLS_DIR/resume-guide"
