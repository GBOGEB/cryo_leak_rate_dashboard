#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

VERSION="$(cat VERSION 2>/dev/null || echo "3.1.0")"
VENV_DIR="venv"
REQ_FILE="requirements.txt"
REQ_HASH_FILE=".setup.requirements.sha256"

log() { echo "[setup] $*"; }

log "Checking Python version >= 3.8"
python3 - <<'PY'
import sys
if sys.version_info < (3, 8):
    raise SystemExit("Python 3.8+ is required")
print(f"Python OK: {sys.version.split()[0]}")
PY

if [ ! -d "$VENV_DIR" ]; then
  log "Creating virtual environment: $VENV_DIR"
  python3 -m venv "$VENV_DIR"
else
  log "Virtual environment exists: $VENV_DIR"
fi

# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

CURRENT_REQ_HASH=""
if [ -f "$REQ_FILE" ]; then
  CURRENT_REQ_HASH="$(sha256sum "$REQ_FILE" | awk '{print $1}')"
fi
PREV_REQ_HASH="$(cat "$REQ_HASH_FILE" 2>/dev/null || true)"

if [ "$CURRENT_REQ_HASH" != "$PREV_REQ_HASH" ]; then
  log "Installing dependencies (requirements changed or first setup)"
  pip install --upgrade pip >/dev/null
  pip install -r "$REQ_FILE"
  echo "$CURRENT_REQ_HASH" > "$REQ_HASH_FILE"
else
  log "Dependencies unchanged, skipping pip install"
fi

log "Validating core data file schemas"
python - <<'PY'
import json
from pathlib import Path

root = Path('.')
checks = {
    root / 'data' / 'standards_compliance.json': ['standards', 'rtm_to_standards_mapping'],
    root / 'data' / 'helium_properties.json': ['description', 'critical_point'],
    root / 'data' / 'compressor_specs.json': ['compressors', 'configurations'],
}
for path, keys in checks.items():
    payload = json.loads(path.read_text(encoding='utf-8'))
    missing = [k for k in keys if k not in payload]
    if missing:
        raise SystemExit(f"Schema validation failed for {path}: missing keys {missing}")
print('Schema validation passed')
PY

mkdir -p docs
if [ ! -f docs/manifest.json ]; then
  log "No manifest found; creating bootstrap manifest"
  cat > docs/manifest.json <<'JSON'
{
  "version": "3.1.0",
  "build": {
    "timestamp": "",
    "git_commit": "unknown",
    "builder": "setup.sh v3.1.0",
    "status": "pending"
  },
  "dependencies": {},
  "files": {},
  "outputs": {
    "charts": 0,
    "tables": 0,
    "reports": 0,
    "slides": 0,
    "total_size_mb": 0
  },
  "tests": {
    "total": 0,
    "passed": 0,
    "failed": 0,
    "coverage": "0.0%",
    "last_run": ""
  }
}
JSON
fi

log "Evaluating source/data checksum drift from manifest"
SHOULD_BUILD="$(python - <<'PY'
import hashlib, json
from pathlib import Path

root = Path('.')
manifest = json.loads((root / 'docs' / 'manifest.json').read_text(encoding='utf-8'))
manifest_files = manifest.get('files', {})

def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()

changed = False
for base in ['src', 'data']:
    for p in sorted((root / base).rglob('*')):
        if not p.is_file():
            continue
        rel = str(p.relative_to(root)).replace('\\\\', '/')
        current = sha(p)
        previous = manifest_files.get(rel, {}).get('sha256')
        if current != previous:
            changed = True
            break
    if changed:
        break
print('yes' if changed else 'no')
PY
)"

if [ "$SHOULD_BUILD" = "yes" ]; then
  log "Source files changed, rebuilding..."
  ./build.sh
else
  log "No source/data changes detected; build is up to date"
  python src/build_dashboard.py
fi

mkdir -p .githooks
if [ -f .githooks/pre-commit ] && [ -d .git/hooks ]; then
  cp .githooks/pre-commit .git/hooks/pre-commit
  chmod +x .git/hooks/pre-commit
fi

BUILD_STATUS="$(python - <<'PY'
import json
from pathlib import Path
manifest = json.loads(Path('docs/manifest.json').read_text(encoding='utf-8'))
print(manifest.get('build', {}).get('status', 'pending'))
PY
)"

log "Setup completed"
echo "Version: v${VERSION}"
echo "Build status: ${BUILD_STATUS}"
echo "Next steps: ./validate.sh && ./package.sh"
