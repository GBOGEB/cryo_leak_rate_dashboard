#!/bin/bash
# ─────────────────────────────────────────────────────────────────────────────
# One-command deployment to GitHub Pages
# Usage: ./scripts/deploy.sh
# ─────────────────────────────────────────────────────────────────────────────
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

BRANCH="$(git rev-parse --abbrev-ref HEAD)"

echo "┌──────────────────────────────────────────┐"
echo "│  QPLANT Cryogenic Dashboard — Deploy     │"
echo "└──────────────────────────────────────────┘"

# ── 1. Build ────────────────────────────────────────────────────────────────
echo "🔨  Building ..."
./build.sh

# ── 2. Validate ─────────────────────────────────────────────────────────────
echo "🔍  Validating ..."
./validate.sh --quick

# ── 3. Link check ───────────────────────────────────────────────────────────
echo "🔗  Checking links ..."
python3 scripts/validate_links.py --report || true

# ── 4. Package ──────────────────────────────────────────────────────────────
echo "📦  Packaging ..."
./package.sh

# ── 5. Compute final hashes ─────────────────────────────────────────────────
echo "🔐  Computing hashes ..."
python3 scripts/compute_hashes.py docs/ > dist/deploy_hashes.json

# ── 6. Summary ──────────────────────────────────────────────────────────────
VERSION="$(cat VERSION)"
COMMIT="$(git rev-parse --short HEAD)"

echo ""
echo "┌──────────────────────────────────────────┐"
echo "│  ✅  Deployment Ready                    │"
echo "│                                          │"
echo "│  Version: $VERSION                       │"
echo "│  Commit:  $COMMIT                        │"
echo "│  Branch:  $BRANCH                        │"
echo "│                                          │"
echo "│  Push with:                              │"
echo "│    git push origin $BRANCH               │"
echo "│                                          │"
echo "│  GitHub Pages deploys automatically      │"
echo "│  from the CI/CD pipeline.                │"
echo "└──────────────────────────────────────────┘"
