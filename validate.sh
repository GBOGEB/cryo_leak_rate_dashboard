#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

if [ -f "venv/bin/activate" ]; then
  # shellcheck disable=SC1091
  source "venv/bin/activate"
fi

export PYTHONPATH="$ROOT_DIR:${PYTHONPATH:-}"

mkdir -p dist

QUICK_MODE="false"
if [ "${1:-}" = "--quick" ]; then
  QUICK_MODE="true"
fi

if [ "$QUICK_MODE" = "true" ]; then
  PYTEST_ARGS=(tests/test_calculations.py tests/test_data_integrity.py -v --maxfail=1)
else
  PYTEST_ARGS=(tests/ -v --cov=src --cov-report=html --cov-report=term --junitxml=dist/junit.xml)
fi

echo "[validate] Running pytest ${PYTEST_ARGS[*]}"
pytest "${PYTEST_ARGS[@]}"

echo "[validate] Validating manifest JSON syntax"
python -m json.tool docs/manifest.json > /dev/null

echo "[validate] Checking file integrity against manifest"
python - <<'PY'
import hashlib
import json
from pathlib import Path

root = Path('.')
manifest = json.loads((root / 'docs' / 'manifest.json').read_text(encoding='utf-8'))
files = manifest.get('files', {})

checked = 0
skip_dynamic = {'docs/index.html', 'docs/manifest.json'}
for rel, meta in files.items():
    if rel in skip_dynamic:
        continue
    path = root / rel
    if not path.exists():
        raise SystemExit(f"Missing file listed in manifest: {rel}")
    expected = meta.get('sha256')
    if not expected:
        continue
    h = hashlib.sha256(path.read_bytes()).hexdigest()
    if h != expected:
        raise SystemExit(f"Checksum mismatch for {rel}")
    checked += 1
print(f"Integrity check passed ({checked} files)")
PY

if [ "$QUICK_MODE" = "false" ]; then
  echo "[validate] Publishing HTML test report"
  if [ -f htmlcov/index.html ]; then
    cp htmlcov/index.html dist/test-report.html
  else
    cat > dist/test-report.html <<'HTML'
<!doctype html><html><body><h1>Coverage report not found</h1></body></html>
HTML
  fi

  echo "[validate] Writing machine-readable test summary"
  python - <<'PY'
import json
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

root = Path('.')
junit = root / 'dist' / 'junit.xml'
coverage_pct = '0.0%'

cov_index = root / 'htmlcov' / 'index.html'
if cov_index.exists():
    text = cov_index.read_text(encoding='utf-8', errors='ignore')
    marker = 'pc_cov'
    if marker in text:
        i = text.find(marker)
        snippet = text[i:i+300]
        import re
        m = re.search(r'(\d+(?:\.\d+)?%)', snippet)
        if m:
            coverage_pct = m.group(1)

if not junit.exists():
    raise SystemExit('Missing dist/junit.xml after pytest run')

root_xml = ET.parse(junit).getroot()

def as_int(value: str | None) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0

if root_xml.tag == 'testsuites':
    suites = root_xml.findall('testsuite')
    if suites:
        total = sum(as_int(s.attrib.get('tests')) for s in suites)
        failed = sum(as_int(s.attrib.get('failures')) + as_int(s.attrib.get('errors')) for s in suites)
        skipped = sum(as_int(s.attrib.get('skipped')) for s in suites)
    else:
        total = as_int(root_xml.attrib.get('tests'))
        failed = as_int(root_xml.attrib.get('failures')) + as_int(root_xml.attrib.get('errors'))
        skipped = as_int(root_xml.attrib.get('skipped'))
else:
    total = as_int(root_xml.attrib.get('tests'))
    failed = as_int(root_xml.attrib.get('failures')) + as_int(root_xml.attrib.get('errors'))
    skipped = as_int(root_xml.attrib.get('skipped'))

passed = max(total - failed - skipped, 0)

summary = {
    'total': total,
    'passed': passed,
    'failed': failed,
    'skipped': skipped,
    'coverage': coverage_pct,
    'last_run': datetime.now(timezone.utc).isoformat(),
}

(root / 'dist' / 'test-results.json').write_text(json.dumps(summary, indent=2, sort_keys=True), encoding='utf-8')

manifest_path = root / 'docs' / 'manifest.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
manifest['tests'] = {
    'total': total,
    'passed': passed,
    'failed': failed,
    'coverage': coverage_pct,
    'last_run': summary['last_run'],
}
manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding='utf-8')
print('Updated docs/manifest.json tests section')
PY

  python src/build_dashboard.py
fi

echo "[validate] Validation successful"
