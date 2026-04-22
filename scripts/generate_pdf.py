#!/usr/bin/env python3
"""Resume PDF generator: JSON data + HTML template -> PDF via weasyprint.

Auto-pagination: ensures last page is at least 50% filled by
progressively compressing CSS spacing when needed.
"""

import argparse
import json
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

COMPACT_CSS_LEVELS = [
    # Level 1: mild compression
    """
    <style>
    @page { margin: 13mm 16mm; }
    body { font-size: 10pt; line-height: 1.5; }
    .section-title { margin-top: 14px; margin-bottom: 8px; padding-bottom: 3px; }
    .item-block { margin-bottom: 11px; }
    ul.details li { margin-bottom: 2px; line-height: 1.45; }
    .summary-text { line-height: 1.6; }
    </style>
    """,
    # Level 2: medium compression
    """
    <style>
    @page { margin: 12mm 15mm; }
    body { font-size: 9.5pt; line-height: 1.4; }
    .section-title { font-size: 12pt; margin-top: 12px; margin-bottom: 6px; padding-bottom: 3px; }
    .item-block { margin-bottom: 9px; }
    .item-title { font-size: 10.5pt; }
    .item-subtitle { font-size: 9.5pt; }
    ul.details { margin-top: 3px; }
    ul.details li { margin-bottom: 1px; line-height: 1.35; }
    .summary-text { font-size: 9.5pt; line-height: 1.5; }
    </style>
    """,
    # Level 3: heavy compression
    """
    <style>
    @page { margin: 10mm 14mm; }
    body { font-size: 9pt; line-height: 1.35; }
    .header h1 { font-size: 20pt; }
    .header .target { font-size: 11pt; }
    .section-title { font-size: 11.5pt; margin-top: 10px; margin-bottom: 5px; padding-bottom: 2px; }
    .item-block { margin-bottom: 7px; }
    .item-title { font-size: 10pt; }
    .item-subtitle { font-size: 9pt; }
    .item-date { font-size: 9pt; }
    ul.details { padding-left: 16px; margin-top: 2px; }
    ul.details li { margin-bottom: 0; line-height: 1.3; }
    .summary-text { font-size: 9pt; line-height: 1.45; }
    </style>
    """,
]

MIN_LAST_PAGE_FILL = 0.50


def load_template(template_name: str, templates_dir: Path):
    env = Environment(
        loader=FileSystemLoader(str(templates_dir)),
        autoescape=True,
    )
    candidates = [f"{template_name}.html", template_name]
    for c in candidates:
        try:
            return env.get_template(c)
        except Exception:
            continue
    available = [p.name for p in templates_dir.glob("*.html")]
    sys.exit(f"Template '{template_name}' not found. Available: {available}")


def check_last_page_fill(pdf_path: str):
    """Return (page_count, last_page_fill_ratio)."""
    try:
        import fitz
    except ImportError:
        return -1, 1.0  # can't check, assume ok
    doc = fitz.open(pdf_path)
    if len(doc) == 0:
        doc.close()
        return 0, 1.0
    last = doc[-1]
    rect = last.rect
    blocks = last.get_text("blocks")
    if blocks:
        max_y = max(b[3] for b in blocks)
        fill = max_y / rect.height
    else:
        fill = 0
    pages = len(doc)
    doc.close()
    return pages, fill


def inject_compact_css(html_content: str, level: int) -> str:
    """Inject compact CSS before </head>."""
    if level < 1 or level > len(COMPACT_CSS_LEVELS):
        return html_content
    css = COMPACT_CSS_LEVELS[level - 1]
    return html_content.replace("</head>", css + "\n</head>")


def generate_pdf(data_path: str, template_name: str, output_path: str):
    skill_dir = Path(__file__).resolve().parent.parent
    templates_dir = skill_dir / "templates"

    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    template = load_template(template_name, templates_dir)

    try:
        from weasyprint import HTML
    except ImportError:
        html_content = template.render(**data)
        html_fallback = Path(output_path).with_suffix(".html")
        html_fallback.write_text(html_content, encoding="utf-8")
        print(f"weasyprint not installed. HTML saved to {html_fallback}", file=sys.stderr)
        sys.exit(1)

    # Pass 0: render with original styles
    html_content = template.render(**data)
    HTML(string=html_content, base_url=str(templates_dir)).write_pdf(output_path)
    pages, fill = check_last_page_fill(output_path)
    if pages <= 1 or fill >= MIN_LAST_PAGE_FILL:
        print(f"PDF generated: {output_path} ({pages}页, 末页填充{fill:.0%})")
        return

    print(f"末页填充仅{fill:.0%}，尝试压缩排版...")
    best_path = output_path
    best_pages = pages
    best_fill = fill

    for level in range(1, len(COMPACT_CSS_LEVELS) + 1):
        compact_html = inject_compact_css(html_content, level)
        tmp_path = output_path.replace(".pdf", f"_compact{level}.pdf")
        HTML(string=compact_html, base_url=str(templates_dir)).write_pdf(tmp_path)
        p, f = check_last_page_fill(tmp_path)

        # Prefer fewer pages; if same pages, prefer higher fill
        improved = (p < best_pages) or (p == best_pages and f > best_fill)
        if improved:
            best_pages, best_fill = p, f
            import shutil
            shutil.move(tmp_path, output_path)
            print(f"  压缩级别{level}: {p}页, 末页填充{f:.0%} ✓")
            if p <= 1 or f >= MIN_LAST_PAGE_FILL:
                break
        else:
            Path(tmp_path).unlink(missing_ok=True)
            print(f"  压缩级别{level}: {p}页, 末页填充{f:.0%} (未改善)")
            break  # further compression won't help

    # Clean up any remaining temp files
    for level in range(1, len(COMPACT_CSS_LEVELS) + 1):
        Path(output_path.replace(".pdf", f"_compact{level}.pdf")).unlink(missing_ok=True)

    print(f"PDF generated: {output_path} ({best_pages}页, 末页填充{best_fill:.0%})")


def main():
    parser = argparse.ArgumentParser(description="Generate resume PDF from JSON data")
    parser.add_argument("--data", required=True, help="Path to JSON data file")
    parser.add_argument("--template", required=True, help="Template name (e.g. tech_zh, classic_en)")
    parser.add_argument("--output", required=True, help="Output PDF path")
    args = parser.parse_args()
    generate_pdf(args.data, args.template, args.output)


if __name__ == "__main__":
    main()
