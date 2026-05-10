#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

if [ -f "venv/bin/activate" ]; then
  # shellcheck disable=SC1091
  source "venv/bin/activate"
fi

mkdir -p dist

echo "[package] Running build"
./build.sh

echo "[package] Running validation"
./validate.sh

echo "[package] Creating distribution bundle"
rm -f dist/handover.zip dist/handover.zip.sha256
zip -r dist/handover.zip \
  docs/ \
  src/ \
  data/ \
  tests/ \
  .github/ \
  .githooks/ \
  README.md \
  CONTRIBUTING.md \
  CHANGELOG.md \
  VERSION \
  requirements.txt \
  Makefile \
  .gitignore \
  setup.sh \
  build.sh \
  validate.sh \
  package.sh \
  docs/manifest.json >/dev/null

sha256sum dist/handover.zip | awk '{print $1}' > dist/handover.zip.sha256

echo "[package] Bundle ready: dist/handover.zip"
echo "[package] SHA256 stored at dist/handover.zip.sha256"
echo "[package] Download artifacts from the dist/ directory"
