#!/bin/bash
# =============================================================================
# Site Verification Script
# Run AFTER GitHub Pages is live to verify all critical URLs
# Usage: ./scripts/site_verification.sh
# =============================================================================

SITE_URL="https://gbogeb.github.io/cryo_leak_rate_dashboard"

echo "=== GitHub Pages Site Verification ==="
echo "Site: $SITE_URL"
echo "Timestamp: $(date -Iseconds)"
echo ""

PASS=0
FAIL=0
TOTAL=0

# Array of critical URLs to check
declare -a URLS=(
    "$SITE_URL/"
    "$SITE_URL/NAVIGATOR.html"
    "$SITE_URL/index_v4_0.html"
    "$SITE_URL/STAKEHOLDER_PRESENTATION.html"
    "$SITE_URL/VERSION_SELECTOR.html"
    "$SITE_URL/executive_summary.html"
    "$SITE_URL/dashboard.html"
    "$SITE_URL/calculations.html"
    "$SITE_URL/rtm_traceability.html"
    "$SITE_URL/handover.html"
)

# Friendly names for each URL
declare -a NAMES=(
    "Homepage (index.html)"
    "Navigator"
    "Technical Presentation (v4.0)"
    "Stakeholder Presentation"
    "Version Selector"
    "Executive Summary"
    "Dashboard"
    "Calculations"
    "RTM Traceability"
    "Handover"
)

echo "Testing ${#URLS[@]} critical URLs..."
echo "────────────────────────────────────────────────"
echo ""

for i in "${!URLS[@]}"; do
    url="${URLS[$i]}"
    name="${NAMES[$i]}"
    ((TOTAL++))

    # Test URL with timeout
    response=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "$url" 2>/dev/null)

    if [ "$response" == "200" ]; then
        echo "  ✅ $name"
        echo "     $url"
        ((PASS++))
    elif [ "$response" == "000" ]; then
        echo "  ⏳ $name (timeout – site may still be deploying)"
        echo "     $url"
        ((FAIL++))
    else
        echo "  ❌ $name (HTTP $response)"
        echo "     $url"
        ((FAIL++))
    fi
    echo ""
done

# --- Visualization spot-checks ---
echo "────────────────────────────────────────────────"
echo "Testing visualization files..."
echo ""

declare -a VIZ_URLS=(
    "$SITE_URL/plots/plot1_leak_vs_loss.html"
    "$SITE_URL/assets/style.css"
    "$SITE_URL/assets/triage.js"
)
declare -a VIZ_NAMES=(
    "Plot: Leak vs Loss"
    "Asset: style.css"
    "Asset: triage.js"
)

for i in "${!VIZ_URLS[@]}"; do
    url="${VIZ_URLS[$i]}"
    name="${VIZ_NAMES[$i]}"
    ((TOTAL++))

    response=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "$url" 2>/dev/null)

    if [ "$response" == "200" ]; then
        echo "  ✅ $name"
        ((PASS++))
    else
        echo "  ❌ $name (HTTP $response)"
        ((FAIL++))
    fi
done

echo ""

# --- Hero pages (optional) ---
echo "────────────────────────────────────────────────"
echo "Testing hero pages (optional)..."
echo ""

for hero in executive engineer specialist; do
    url="$SITE_URL/heroes/${hero}.html"
    ((TOTAL++))
    response=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "$url" 2>/dev/null)
    if [ "$response" == "200" ]; then
        echo "  ✅ Hero: $hero"
        ((PASS++))
    else
        echo "  ⚠️  Hero: $hero (HTTP $response – non-critical)"
        ((FAIL++))
    fi
done

echo ""

# --- Summary ---
echo "════════════════════════════════════════════════"
echo "  SUMMARY"
echo "════════════════════════════════════════════════"
echo ""
echo "  Passed: $PASS / $TOTAL"
echo "  Failed: $FAIL / $TOTAL"
echo ""

if [ $FAIL -eq 0 ]; then
    echo "  ✅ ALL PAGES ACCESSIBLE"
    echo ""
    echo "  Your site is live and working!"
    echo "  Main URL: $SITE_URL"
    echo ""
    echo "  Next steps:"
    echo "    1. Create GitHub Release (tag v4.0.0)"
    echo "    2. Update documentation with live URLs"
    echo "    3. Share with stakeholders"
    exit 0
else
    echo "  ⚠️  SOME PAGES NOT ACCESSIBLE ($FAIL failures)"
    echo ""
    echo "  Possible causes:"
    echo "    - Pages still deploying (wait 5 minutes, re-run)"
    echo "    - Incorrect Pages configuration"
    echo "    - Files missing from /docs folder"
    echo ""
    echo "  Re-run after waiting: ./scripts/site_verification.sh"
    exit 1
fi
