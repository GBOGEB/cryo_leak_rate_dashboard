#!/bin/bash
# ─────────────────────────────────────────────────────────────────────────────
# Automated release script with SHA-256 tracking
# Usage: ./scripts/release.sh v4.1.0
# ─────────────────────────────────────────────────────────────────────────────
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

VERSION="${1:-}"
if [ -z "$VERSION" ]; then
    echo "Usage: ./scripts/release.sh v4.0.0"
    exit 1
fi

# Strip leading 'v' for VERSION file
SEMVER="${VERSION#v}"

echo "[$(date -Iseconds)] Starting release $VERSION"

# ── 1. Update VERSION file ──────────────────────────────────────────────────
echo "$SEMVER" > VERSION
echo "  ✅ VERSION → $SEMVER"

# ── 2. Compute hashes of source files ───────────────────────────────────────
mkdir -p dist
python3 scripts/compute_hashes.py src/ data/ > dist/source_hashes.json
echo "  ✅ Source hashes → dist/source_hashes.json"

# ── 3. Build everything ─────────────────────────────────────────────────────
if [ -x "./build.sh" ]; then
    echo "  🔨 Running build.sh ..."
    ./build.sh
fi

# ── 4. Compute hashes of generated files ────────────────────────────────────
python3 scripts/compute_hashes.py docs/ outputs/ > dist/output_hashes.json
echo "  ✅ Output hashes → dist/output_hashes.json"

# ── 5. Generate release notes ───────────────────────────────────────────────
cat > RELEASE_NOTES.md <<REOF
# Release $VERSION

**Date:** $(date -Iseconds)

## Changes

See [CHANGELOG.md](CHANGELOG.md) for full details.

## Artifact Hashes

Source hashes: \`dist/source_hashes.json\`
Output hashes: \`dist/output_hashes.json\`

## Validation

\`\`\`bash
./validate.sh --quick
python3 scripts/validate_links.py --report
\`\`\`
REOF
echo "  ✅ RELEASE_NOTES.md generated"

# ── 6. Git operations ───────────────────────────────────────────────────────
git add -A
git commit -m "release: $VERSION" || echo "  ℹ️  Nothing to commit"
git tag -a "$VERSION" -m "Release $VERSION" 2>/dev/null || echo "  ℹ️  Tag $VERSION already exists"

echo ""
echo "[$(date -Iseconds)] Release $VERSION complete"
echo "Push with: git push origin main --tags"
