#!/usr/bin/env bash
# scripts/pre_push_checklist.sh — automated pre-push validation
#
# Verifies the repository is in a healthy, deterministic state before pushing
# to GitHub. Writes a human-readable report to dist/pre_push_report.txt and
# exits 0 only when every required check passes.

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

mkdir -p dist
REPORT="dist/pre_push_report.txt"
: > "$REPORT"

PASS=0
FAIL=0
WARN=0
TOTAL=6

log() { echo "$*" | tee -a "$REPORT"; }
section() { log ""; log "=========================================="; log "$*"; log "=========================================="; }

section "Pre-Push Checklist"
log "Timestamp:    $(date -Iseconds)"
log "Repo root:    $REPO_ROOT"
log "Git HEAD:     $(git rev-parse --short HEAD 2>/dev/null || echo 'no-git')"
log "Branch:       $(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo 'no-git')"
log "Total checks: $TOTAL"

# ---------------------------------------------------------------------------
# 1. Git status — working tree clean
# ---------------------------------------------------------------------------
section "1/6 Git status"
if git diff-index --quiet HEAD -- 2>/dev/null && [ -z "$(git ls-files --others --exclude-standard)" ]; then
    log "   ✅ Working tree clean (no uncommitted or untracked source changes)"
    ((PASS++))
else
    UNCOMMITTED="$(git status --short)"
    if [ -n "$UNCOMMITTED" ]; then
        log "   ⚠️  Uncommitted / untracked changes detected:"
        echo "$UNCOMMITTED" | sed 's/^/      /' | tee -a "$REPORT"
        ((WARN++))
    else
        log "   ✅ Tree clean"
        ((PASS++))
    fi
fi

# ---------------------------------------------------------------------------
# 2. Tests
# ---------------------------------------------------------------------------
section "2/6 Running tests"
if [ -d tests ]; then
    if [ -x venv/bin/pytest ]; then
        PYTEST=venv/bin/pytest
    elif command -v pytest >/dev/null 2>&1; then
        PYTEST=pytest
    else
        PYTEST=""
    fi

    if [ -z "$PYTEST" ]; then
        log "   ⚠️  pytest not installed — skipping (run ./setup.sh first)"
        ((WARN++))
    else
        if "$PYTEST" tests/ -q --tb=short >/tmp/_pp_tests.txt 2>&1; then
            SUMMARY=$(tail -2 /tmp/_pp_tests.txt | tr -d '\n')
            log "   ✅ All tests passing — $SUMMARY"
            ((PASS++))
        else
            log "   ❌ Tests failing — last 20 lines:"
            tail -20 /tmp/_pp_tests.txt | sed 's/^/      /' | tee -a "$REPORT"
            ((FAIL++))
        fi
    fi
else
    log "   ⚠️  No tests/ directory found"
    ((WARN++))
fi

# ---------------------------------------------------------------------------
# 3. Manifest integrity
# ---------------------------------------------------------------------------
section "3/6 Manifest integrity"
if [ -f docs/manifest.json ]; then
    FILE_COUNT=$(python3 - <<'PY' 2>/dev/null
import json
try:
    with open("docs/manifest.json") as fh:
        data = json.load(fh)
    files = data.get("files", {})
    print(len(files) if hasattr(files, "__len__") else 0)
except Exception:
    print(0)
PY
)
    FILE_COUNT=${FILE_COUNT:-0}
    if [ "$FILE_COUNT" -ge 100 ]; then
        log "   ✅ docs/manifest.json has $FILE_COUNT file entries"
        ((PASS++))
    else
        log "   ⚠️  docs/manifest.json appears thin ($FILE_COUNT entries)"
        ((WARN++))
    fi
else
    log "   ⚠️  docs/manifest.json missing — run ./build.sh"
    ((WARN++))
fi

# ---------------------------------------------------------------------------
# 4. Link validation
# ---------------------------------------------------------------------------
section "4/6 Link validation"
if [ -f scripts/validate_links.py ]; then
    if python3 scripts/validate_links.py >/tmp/_pp_links.txt 2>&1; then
        log "   ✅ Link validator finished without errors"
        ((PASS++))
    else
        EXIT=$?
        log "   ⚠️  Link validator returned non-zero ($EXIT) — last 15 lines:"
        tail -15 /tmp/_pp_links.txt | sed 's/^/      /' | tee -a "$REPORT"
        ((WARN++))
    fi
else
    log "   ⚠️  scripts/validate_links.py not present — skipped"
    ((WARN++))
fi

# ---------------------------------------------------------------------------
# 5. Critical landing pages present
# ---------------------------------------------------------------------------
section "5/6 Landing pages present"
MISSING=0
for f in \
    docs/index.html \
    docs/VERSION_SELECTOR.html \
    docs/NAVIGATOR.html \
    docs/index_v4_0.html \
    docs/STAKEHOLDER_PRESENTATION.html
do
    if [ -f "$f" ]; then
        log "   ✅ $f"
    else
        log "   ❌ MISSING: $f"
        MISSING=$((MISSING+1))
    fi
done
if [ "$MISSING" -eq 0 ]; then
    ((PASS++))
else
    log "   ❌ $MISSING required landing page(s) missing"
    ((FAIL++))
fi

# ---------------------------------------------------------------------------
# 6. Required documentation files
# ---------------------------------------------------------------------------
section "6/6 Documentation files"
DOC_MISSING=0
for f in README.md CHANGELOG.md VERSION VERSION.json \
         BACKUP_STRATEGY.md PROGRESS_TRACKER.md \
         GITHUB_REPO_CREATION_STEPS.md REUSE_GUIDE.md
do
    if [ -f "$f" ]; then
        log "   ✅ $f"
    else
        log "   ❌ MISSING: $f"
        DOC_MISSING=$((DOC_MISSING+1))
    fi
done
if [ "$DOC_MISSING" -eq 0 ]; then
    ((PASS++))
else
    log "   ❌ $DOC_MISSING documentation file(s) missing"
    ((FAIL++))
fi

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
section "Summary"
log "Passed:   $PASS / $TOTAL"
log "Warnings: $WARN"
log "Failed:   $FAIL"
log ""

if [ $FAIL -eq 0 ]; then
    log "✅ READY TO PUSH TO GITHUB"
    log ""
    log "Next steps:"
    log "  1. Create repo: https://github.com/new"
    log "  2. Add remote:  git remote add origin https://github.com/GBOGEB/cryo_leak_rate_dashboard.git"
    log "  3. Push:        git push -u origin main && git push --tags origin"
    log ""
    log "Report saved to: $REPORT"
    exit 0
else
    log "❌ FIX ISSUES BEFORE PUSHING"
    log "Report saved to: $REPORT"
    exit 1
fi
