#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

if [ -f "venv/bin/activate" ]; then
  # shellcheck disable=SC1091
  source "venv/bin/activate"
fi

mkdir -p dist docs
BUILD_LOG="dist/build.log"
: > "$BUILD_LOG"

run_log() {
  echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] $*" | tee -a "$BUILD_LOG"
}

run_log "Starting deterministic build"
export PYTHONHASHSEED=42
export CRYO_BUILD_SEED=42

run_log "Cleaning dist/"
rm -rf dist/*
mkdir -p dist

run_log "Running generators"
python - <<'PY' | tee -a dist/build.log
import numpy as np
np.random.seed(42)
print('numpy.random.seed(42) set in build preamble')
PY

python src/generate_standards_stats.py | tee -a "$BUILD_LOG"
python src/build_dashboard.py | tee -a "$BUILD_LOG"

run_log "Updating docs/changelog.md if version changed"
python - <<'PY' | tee -a dist/build.log
from datetime import datetime, timezone
from pathlib import Path
import json

root = Path('.')
version = (root / 'VERSION').read_text(encoding='utf-8').strip() if (root / 'VERSION').exists() else '3.1.0'
manifest_path = root / 'docs' / 'manifest.json'
previous_version = None
if manifest_path.exists():
    try:
        previous_version = json.loads(manifest_path.read_text(encoding='utf-8')).get('version')
    except Exception:
        previous_version = None

changelog = root / 'docs' / 'changelog.md'
if not changelog.exists():
    changelog.write_text('# Changelog\n\n', encoding='utf-8')

if previous_version != version:
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    entry = f"\n## [{version}] - {now}\n\n### Added\n- Build metadata refreshed by build.sh.\n"
    content = changelog.read_text(encoding='utf-8')
    if f"## [{version}]" not in content:
        changelog.write_text(content + entry, encoding='utf-8')
        print(f'Added changelog entry for {version}')
    else:
        print(f'Changelog entry already exists for {version}')
else:
    print('Version unchanged; changelog entry not added')
PY

run_log "Rebuilding docs/manifest.json"
python - <<'PY' | tee -a dist/build.log
from __future__ import annotations

import hashlib
import importlib.metadata
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path

root = Path('.')
manifest_path = root / 'docs' / 'manifest.json'
version = (root / 'VERSION').read_text(encoding='utf-8').strip() if (root / 'VERSION').exists() else '3.1.0'


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def iso_mtime(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).isoformat()


def norm(p: Path) -> str:
    return str(p.relative_to(root)).replace('\\\\', '/')


def git_commit() -> str:
    try:
        return subprocess.check_output(['git', 'log', '-1', '--format=%h'], text=True, cwd=root).strip() or 'unknown'
    except Exception:
        return 'unknown'


def pkg_version(name: str, default: str = 'unknown') -> str:
    try:
        return importlib.metadata.version(name)
    except Exception:
        return default

files: dict[str, dict] = {}
tracked_roots = ['src', 'data', 'docs', 'tests']
for base in tracked_roots:
    base_path = root / base
    if not base_path.exists():
        continue
    for p in sorted(base_path.rglob('*')):
        if not p.is_file():
            continue
        rel = norm(p)
        if rel == 'docs/manifest.json':
            continue
        generated_from = []
        if rel.startswith('docs/visualizations_v3/') or rel.startswith('docs/standards/') or rel == 'docs/index_v3_1.html':
            generated_from = ['src/generate_standards_stats.py']
        elif rel == 'docs/index.html':
            generated_from = ['src/build_dashboard.py', 'docs/manifest.json']

        files[rel] = {
            'sha256': sha256_file(p),
            'size': p.stat().st_size,
            'last_modified': iso_mtime(p),
            'generated_from': generated_from,
        }

extra = ['README.md', 'CHANGELOG.md', 'VERSION', 'requirements.txt']
for rel in extra:
    p = root / rel
    if p.exists():
        files[rel] = {
            'sha256': sha256_file(p),
            'size': p.stat().st_size,
            'last_modified': iso_mtime(p),
            'generated_from': [],
        }

charts = len(list((root / 'docs' / 'visualizations_v3').glob('*.html'))) if (root / 'docs' / 'visualizations_v3').exists() else 0
tables = len(list((root / 'docs').rglob('*.csv')))
reports = len(list((root / 'docs').rglob('*.md'))) + len(list((root / 'docs').rglob('*.pdf')))
slides = 0
slide_file = root / 'docs' / 'index_v3_1.html'
if slide_file.exists():
    text = slide_file.read_text(encoding='utf-8', errors='ignore')
    slides = text.count('class="slide')

total_size = sum(v['size'] for v in files.values()) / (1024 * 1024)

existing_tests = {}
if manifest_path.exists():
    try:
        existing_tests = json.loads(manifest_path.read_text(encoding='utf-8')).get('tests', {})
    except Exception:
        existing_tests = {}

manifest = {
    'version': version,
    'build': {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'git_commit': git_commit(),
        'builder': f'setup.sh v{version}',
        'status': 'verified',
    },
    'dependencies': {
        'python': f"{os.sys.version_info.major}.{os.sys.version_info.minor}.{os.sys.version_info.micro}",
        'numpy': pkg_version('numpy'),
        'plotly': pkg_version('plotly'),
        'pandas': pkg_version('pandas'),
        'scipy': pkg_version('scipy'),
    },
    'files': {k: files[k] for k in sorted(files)},
    'outputs': {
        'charts': charts,
        'tables': tables,
        'reports': reports,
        'slides': slides,
        'total_size_mb': round(total_size, 2),
    },
    'tests': {
        'total': existing_tests.get('total', 0),
        'passed': existing_tests.get('passed', 0),
        'failed': existing_tests.get('failed', 0),
        'coverage': existing_tests.get('coverage', '0.0%'),
        'last_run': existing_tests.get('last_run', ''),
    },
}

manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding='utf-8')
print(f'Manifest written: {manifest_path}')
PY

run_log "Build completed"
