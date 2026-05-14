#!/bin/bash
# ─────────────────────────────────────────────────────────────────────────────
# Export key HTML pages to PDF using Python weasyprint
# Usage: ./scripts/export_pdfs.sh
# ─────────────────────────────────────────────────────────────────────────────
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
fi

EXPORTS_DIR="docs/exports"
mkdir -p "$EXPORTS_DIR"

VERSION="$(cat VERSION)"

echo "📄  Exporting PDFs (v${VERSION}) ..."

# Use Python for PDF generation (weasyprint fallback to print-css)
python3 -c "
import sys
from pathlib import Path

try:
    from weasyprint import HTML
    HAS_WEASY = True
except ImportError:
    HAS_WEASY = False
    print('  ⚠️  weasyprint not installed — skipping PDF export')
    print('  Install: pip install weasyprint')
    sys.exit(0)

exports = [
    ('docs/index.html',               'docs/exports/landing_page_v${VERSION}.pdf'),
    ('docs/executive_summary.html',    'docs/exports/executive_summary_v${VERSION}.pdf'),
    ('docs/dashboard.html',           'docs/exports/technical_dashboard_v${VERSION}.pdf'),
    ('docs/rtm_traceability.html',    'docs/exports/rtm_traceability_v${VERSION}.pdf'),
]

for src, dst in exports:
    src_path = Path(src)
    if not src_path.exists():
        print(f'  ⚠️  {src} not found — skipping')
        continue
    try:
        HTML(filename=str(src_path)).write_pdf(dst)
        print(f'  ✅  {dst}')
    except Exception as e:
        print(f'  ⚠️  {src} → {e}')
"

echo ""
echo "📁  PDFs exported to ${EXPORTS_DIR}/"
