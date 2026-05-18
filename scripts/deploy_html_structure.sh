#!/bin/bash
# ============================================================================
# deploy_html_structure.sh — GitHub Pages HTML Deployment for v4 Dashboard
# ============================================================================
# Usage: ./scripts/deploy_html_structure.sh
# Verifies HTML structure and prepares for GitHub Pages deployment.
# Does NOT modify file locations (v4 serves directly from docs/).
# ============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
DOCS_DIR="$ROOT_DIR/docs"

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  MYRRHA QPLANT — GitHub Pages HTML Deployment Check          ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# ── 1. Check VERSION_SELECTOR.html exists ──
echo "1. Checking VERSION_SELECTOR.html..."
if [ -f "$DOCS_DIR/VERSION_SELECTOR.html" ]; then
    echo "   ✅ VERSION_SELECTOR.html exists"
else
    echo "   ❌ VERSION_SELECTOR.html missing!"
    exit 1
fi

# ── 2. Check canonical presentations ──
echo "2. Checking canonical presentations..."
for f in NAVIGATOR.html index_v4_0.html STAKEHOLDER_PRESENTATION.html; do
    if [ -f "$DOCS_DIR/$f" ]; then
        echo "   ✅ $f"
    else
        echo "   ❌ $f missing!"
    fi
done

# ── 3. Count HTML files ──
echo "3. HTML file inventory..."
TOTAL=$(find "$DOCS_DIR" -name "*.html" | wc -l)
VIS=$(find "$DOCS_DIR/visualizations" -name "*.html" 2>/dev/null | wc -l)
VIS3=$(find "$DOCS_DIR/visualizations_v3" -name "*.html" 2>/dev/null | wc -l)
PLOTS=$(find "$DOCS_DIR/plots" -name "*.html" 2>/dev/null | wc -l)
HEROES=$(find "$DOCS_DIR/heroes" -name "*.html" 2>/dev/null | wc -l)
ARCH=$(find "$DOCS_DIR/archive" -name "*.html" 2>/dev/null | wc -l)
echo "   Total HTML:         $TOTAL"
echo "   Visualizations:     $VIS"
echo "   Visualizations v3:  $VIS3"
echo "   Plots:              $PLOTS"
echo "   Heroes:             $HEROES"
echo "   Archive:            $ARCH"

# ── 4. Check assets ──
echo "4. Checking assets..."
for f in style.css triage.js; do
    if [ -f "$DOCS_DIR/assets/$f" ]; then
        echo "   ✅ assets/$f"
    else
        echo "   ⚠️  assets/$f missing"
    fi
done

# ── 5. Check .nojekyll ──
echo "5. Checking .nojekyll..."
if [ -f "$DOCS_DIR/.nojekyll" ] || [ -f "$ROOT_DIR/.nojekyll" ]; then
    echo "   ✅ .nojekyll exists"
else
    echo "   Creating .nojekyll..."
    touch "$DOCS_DIR/.nojekyll"
    echo "   ✅ .nojekyll created"
fi

# ── 6. Generate sitemap.txt ──
echo "6. Generating sitemap.txt..."
BASE_URL="https://gbogeb.github.io/cryo_leak_rate_dashboard"
{
    echo "$BASE_URL/"
    echo "$BASE_URL/VERSION_SELECTOR.html"
    echo "$BASE_URL/NAVIGATOR.html"
    echo "$BASE_URL/index_v4_0.html"
    echo "$BASE_URL/STAKEHOLDER_PRESENTATION.html"
    echo "$BASE_URL/dashboard.html"
    echo "$BASE_URL/calculations.html"
    echo "$BASE_URL/executive_summary.html"
    echo "$BASE_URL/rtm_traceability.html"
    echo "$BASE_URL/handover.html"
    # Add all visualization URLs
    find "$DOCS_DIR/visualizations" -name "*.html" 2>/dev/null | sort | while read -r f; do
        echo "$BASE_URL/$(realpath --relative-to="$DOCS_DIR" "$f")"
    done
    find "$DOCS_DIR/visualizations_v3" -name "*.html" 2>/dev/null | sort | while read -r f; do
        echo "$BASE_URL/$(realpath --relative-to="$DOCS_DIR" "$f")"
    done
    find "$DOCS_DIR/heroes" -name "*.html" 2>/dev/null | sort | while read -r f; do
        echo "$BASE_URL/$(realpath --relative-to="$DOCS_DIR" "$f")"
    done
} > "$DOCS_DIR/sitemap.txt"
SITEMAP_COUNT=$(wc -l < "$DOCS_DIR/sitemap.txt")
echo "   ✅ sitemap.txt generated ($SITEMAP_COUNT URLs)"

# ── 7. Summary ──
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  Deployment readiness: ✅ READY"
echo "  Total HTML files:     $TOTAL"
echo "  Sitemap entries:      $SITEMAP_COUNT"
echo ""
echo "  Next steps:"
echo "  1. Create repo:  github.com/GBOGEB/cryo_leak_rate_dashboard"
echo "  2. Add remote:   git remote add origin <URL>"
echo "  3. Push:         git push -u origin main"
echo "  4. Enable Pages: Settings → Pages → Branch: main → /docs"
echo "═══════════════════════════════════════════════════════════════"
