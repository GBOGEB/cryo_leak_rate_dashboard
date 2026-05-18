#!/bin/bash
# ============================================================
# Post-Merge Validation Script — Cryo Leak Rate Dashboard v4.0.0
# Run this after merging PR to verify GitHub integration health
# ============================================================

set -euo pipefail

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

PASS=0
FAIL=0
WARN=0

pass() { echo -e "  ${GREEN}✅ $1${NC}"; PASS=$((PASS+1)); }
fail() { echo -e "  ${RED}❌ $1${NC}"; FAIL=$((FAIL+1)); }
warn() { echo -e "  ${YELLOW}⚠️  $1${NC}"; WARN=$((WARN+1)); }
info() { echo -e "  ${CYAN}ℹ️  $1${NC}"; }

echo "╔══════════════════════════════════════════════════════════╗"
echo "║   GitHub Integration Validation — v4.0.0                ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""
echo "Timestamp: $(date -Iseconds)"
echo ""

# ── 1. Git Status ────────────────────────────────────────────
echo "━━━ 1. Git Status ━━━"
if git status --porcelain | grep -q .; then
    warn "Working tree has uncommitted changes"
    git status --short | head -10
else
    pass "Working tree clean"
fi
echo ""

# ── 2. Branch Check ──────────────────────────────────────────
echo "━━━ 2. Branch Check ━━━"
BRANCH=$(git branch --show-current)
info "Current branch: $BRANCH"
if [ "$BRANCH" = "main" ]; then
    pass "On main branch (post-merge expected)"
else
    warn "Not on main branch — expected after merge"
fi
echo ""

# ── 3. Remote Configuration ──────────────────────────────────
echo "━━━ 3. Remote Configuration ━━━"
if git remote -v 2>/dev/null | grep -q origin; then
    REMOTE_URL=$(git config --get remote.origin.url)
    pass "Remote 'origin' configured: $REMOTE_URL"
else
    fail "No remote 'origin' configured"
    info "Run: git remote add origin https://github.com/GBOGEB/cryo_leak_rate_dashboard.git"
fi
echo ""

# ── 4. Recent Commits ────────────────────────────────────────
echo "━━━ 4. Recent Commits ━━━"
echo "  Last 5 commits:"
git log --oneline -5 | sed 's/^/    /'
echo ""

# ── 5. Version Check ─────────────────────────────────────────
echo "━━━ 5. Version Check ━━━"
if [ -f "VERSION" ]; then
    VER=$(cat VERSION | tr -d '[:space:]')
    if [ "$VER" = "4.0.0" ]; then
        pass "VERSION = $VER"
    else
        fail "VERSION = $VER (expected 4.0.0)"
    fi
else
    fail "VERSION file missing"
fi
echo ""

# ── 6. GitHub Actions Workflows ──────────────────────────────
echo "━━━ 6. GitHub Actions Workflows ━━━"
WORKFLOWS=("ci.yml" "deploy.yml" "build.yml")
for wf in "${WORKFLOWS[@]}"; do
    if [ -f ".github/workflows/$wf" ]; then
        pass ".github/workflows/$wf present"
    else
        fail ".github/workflows/$wf MISSING"
    fi
done
echo ""

# ── 7. Key Files Verification ────────────────────────────────
echo "━━━ 7. Key Files Verification ━━━"
KEY_FILES=(
    "docs/NAVIGATOR.html"
    "docs/index.html"
    "docs/manifest.json"
    "data/config.yaml"
    "BUILD_LOG.md"
    "QUICK_ACCESS.md"
    "CHANGELOG.md"
    "README.md"
    "requirements.txt"
    "PR_CHECKLIST.md"
    "PR_REVIEW_SUMMARY.md"
    "GITHUB_INTEGRATION_STATUS.md"
    "GITHUB_PAGES_SETUP.md"
)
for f in "${KEY_FILES[@]}"; do
    if [ -f "$f" ]; then
        pass "$f"
    else
        fail "$f MISSING"
    fi
done
echo ""

# ── 8. Test Suite ─────────────────────────────────────────────
echo "━━━ 8. Test Suite ━━━"
TEST_COUNT=$(find tests/ -name "test_*.py" -type f | wc -l)
info "Test files found: $TEST_COUNT"
if command -v pytest &> /dev/null || [ -f "venv/bin/pytest" ]; then
    if [ -f "venv/bin/pytest" ]; then
        PYTEST="venv/bin/pytest"
    else
        PYTEST="pytest"
    fi
    info "Running quick test check..."
    if PYTHONPATH="${PWD}:${PYTHONPATH:-}" $PYTEST tests/ --co -q 2>/dev/null | tail -1; then
        pass "Test collection successful"
    else
        warn "Could not collect tests (may need venv activation)"
    fi
else
    warn "pytest not found — install with: pip install pytest"
fi
echo ""

# ── 9. HTML File Count ────────────────────────────────────────
echo "━━━ 9. HTML Files ━━━"
HTML_COUNT=$(find docs/ -name "*.html" -type f 2>/dev/null | wc -l)
if [ "$HTML_COUNT" -ge 80 ]; then
    pass "$HTML_COUNT HTML files in docs/ (expected ~84)"
else
    warn "$HTML_COUNT HTML files in docs/ (expected ~84)"
fi
echo ""

# ── 10. SSoT Config Validation ────────────────────────────────
echo "━━━ 10. SSoT Configuration ━━━"
if [ -f "data/config.yaml" ]; then
    if command -v python3 &> /dev/null; then
        python3 -c "
import yaml
with open('data/config.yaml') as f:
    cfg = yaml.safe_load(f)
hp = cfg.get('compressor_specifications', {}).get('hp_compressors', {})
count = hp.get('count', 'N/A')
pp = cfg.get('pressure_parameters', {}).get('wcs_hp_outlet', {})
pressure = pp.get('nominal_barg', 'N/A')
print(f'  HP compressor count: {count}')
print(f'  HP discharge pressure: {pressure} barg')
if count == 3:
    print('  ✅ Compressor count correct (3)')
else:
    print(f'  ❌ Compressor count wrong (expected 3, got {count})')
if pressure == 14:
    print('  ✅ Pressure correct (14 barg)')
else:
    print(f'  ❌ Pressure wrong (expected 14, got {pressure})')
" 2>/dev/null || warn "Could not validate config.yaml (PyYAML not installed)"
    else
        warn "Python3 not available for config validation"
    fi
else
    fail "data/config.yaml missing — SSoT not configured"
fi
echo ""

# ── 11. GitHub URLs ──────────────────────────────────────────
echo "━━━ 11. GitHub URLs ━━━"
if git remote -v 2>/dev/null | grep -q origin; then
    REPO_URL=$(git config --get remote.origin.url | sed 's/\.git$//')
    if [[ $REPO_URL == git@github.com:* ]]; then
        REPO_URL=$(echo "$REPO_URL" | sed 's/git@github.com:/https:\/\/github.com\//')
    fi
    info "Repository:  $REPO_URL"
    info "Actions:     $REPO_URL/actions"
    info "Pull Reqs:   $REPO_URL/pulls"
    info "Settings:    $REPO_URL/settings"
    info "Pages:       $REPO_URL/settings/pages"
else
    info "No remote — URLs not available yet"
    info "Expected:    https://github.com/GBOGEB/cryo_leak_rate_dashboard"
fi
echo ""

# ── Summary ──────────────────────────────────────────────────
echo "╔══════════════════════════════════════════════════════════╗"
echo "║   VALIDATION SUMMARY                                    ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo -e "  ${GREEN}Passed:${NC}   $PASS"
echo -e "  ${RED}Failed:${NC}   $FAIL"
echo -e "  ${YELLOW}Warnings:${NC} $WARN"
echo ""

if [ $FAIL -eq 0 ]; then
    echo -e "${GREEN}══════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}  ✅ ALL CHECKS PASSED — Ready for deployment${NC}"
    echo -e "${GREEN}══════════════════════════════════════════════════════════${NC}"
else
    echo -e "${RED}══════════════════════════════════════════════════════════${NC}"
    echo -e "${RED}  ❌ $FAIL CHECK(S) FAILED — Review issues above${NC}"
    echo -e "${RED}══════════════════════════════════════════════════════════${NC}"
fi
