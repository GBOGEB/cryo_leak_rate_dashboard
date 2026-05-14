#!/usr/bin/env python3
"""Compute SHA-256 hashes for all project files.

Usage:
    python scripts/compute_hashes.py                # scan current directory
    python scripts/compute_hashes.py docs/ outputs/  # scan specific dirs
    python scripts/compute_hashes.py --manifest      # update manifest.json
"""
import hashlib
import sys
import json
from pathlib import Path
from datetime import datetime, timezone

SKIP_DIRS = {'.git', '__pycache__', '.pytest_cache', 'venv', 'htmlcov', 'node_modules'}
SKIP_EXTENSIONS = {'.pyc', '.pyo', '.coverage'}


def sha256_file(path: str | Path) -> str:
    """Compute SHA-256 hex digest of a file."""
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def scan_directory(root: str | Path) -> dict:
    """Recursively scan a directory, returning {relative_path: metadata}."""
    root = Path(root)
    results = {}
    for path in sorted(root.rglob('*')):
        if path.is_dir():
            continue
        # Skip hidden / build dirs
        parts = path.relative_to(root).parts
        if any(p in SKIP_DIRS or p.startswith('.') for p in parts):
            continue
        if path.suffix in SKIP_EXTENSIONS:
            continue

        rel = str(path.relative_to(root))
        stat = path.stat()
        results[rel] = {
            'sha256': sha256_file(path),
            'size': stat.st_size,
            'modified': datetime.fromtimestamp(
                stat.st_mtime, tz=timezone.utc
            ).isoformat(),
        }
    return results


def main():
    update_manifest = '--manifest' in sys.argv
    roots = [a for a in sys.argv[1:] if a != '--manifest']
    if not roots:
        roots = ['.']

    all_hashes = {}
    for root in roots:
        all_hashes.update(scan_directory(root))

    payload = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'file_count': len(all_hashes),
        'files': all_hashes,
    }
    output = json.dumps(payload, indent=2)
    print(output)

    if update_manifest:
        manifest_path = Path('docs/manifest_hashes.json')
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(output + '\n')
        print(f'\n✅  Wrote {manifest_path} ({len(all_hashes)} files)', file=sys.stderr)


if __name__ == '__main__':
    main()
