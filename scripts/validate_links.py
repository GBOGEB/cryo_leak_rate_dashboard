#!/usr/bin/env python3
"""Validate internal and external links across all HTML files.

Usage:
    python scripts/validate_links.py              # scan docs/
    python scripts/validate_links.py docs/ .      # scan specific dirs
    python scripts/validate_links.py --report      # write report to dist/
"""
import re
import sys
import json
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import urlparse, unquote

DOCS_ROOT = Path('docs')
REPORT_PATH = Path('dist/broken_links_report.json')


def extract_links(html_path: Path) -> list[dict]:
    """Extract href and src attributes from an HTML file."""
    text = html_path.read_text(errors='replace')
    links = []
    for attr in ('href', 'src'):
        for m in re.finditer(rf'{attr}\s*=\s*["\']([^"\']+)["\']', text):
            links.append({
                'file': str(html_path),
                'attr': attr,
                'url': m.group(1),
                'line': text[:m.start()].count('\n') + 1,
            })
    return links


def classify_link(url: str) -> str:
    """Classify a URL as internal, external, anchor, data, or mailto."""
    if url.startswith('#'):
        return 'anchor'
    if url.startswith('data:'):
        return 'data'
    if url.startswith('mailto:'):
        return 'mailto'
    if url.startswith('javascript:'):
        return 'javascript'
    parsed = urlparse(url)
    if parsed.scheme in ('http', 'https'):
        return 'external'
    return 'internal'


def validate_internal_link(html_path: Path, url: str, scan_roots: list[Path]) -> bool:
    """Check that an internal link target file exists."""
    # Strip fragment
    clean = url.split('#')[0].split('?')[0]
    if not clean:
        return True  # fragment-only or empty
    clean = unquote(clean)
    # Resolve relative to the HTML file's directory
    target = (html_path.parent / clean).resolve()
    if target.exists():
        return True
    # Also try from each scan root
    for root in scan_roots:
        if (root / clean).resolve().exists():
            return True
    return False


def main():
    write_report = '--report' in sys.argv
    roots_args = [a for a in sys.argv[1:] if a != '--report']
    scan_roots = [Path(r) for r in roots_args] if roots_args else [DOCS_ROOT]

    html_files = []
    for root in scan_roots:
        html_files.extend(sorted(root.rglob('*.html')))

    if not html_files:
        print(f'No HTML files found in {scan_roots}')
        sys.exit(0)

    all_links = []
    for f in html_files:
        all_links.extend(extract_links(f))

    broken = []
    stats = {'total': 0, 'internal': 0, 'external': 0, 'anchor': 0,
             'broken_internal': 0, 'skipped_external': 0}

    for link in all_links:
        stats['total'] += 1
        kind = classify_link(link['url'])
        link['kind'] = kind

        if kind == 'internal':
            stats['internal'] += 1
            ok = validate_internal_link(Path(link['file']), link['url'], scan_roots)
            if not ok:
                stats['broken_internal'] += 1
                link['status'] = 'BROKEN'
                broken.append(link)
            else:
                link['status'] = 'OK'
        elif kind == 'external':
            stats['external'] += 1
            stats['skipped_external'] += 1
            link['status'] = 'SKIPPED'
        elif kind == 'anchor':
            stats['anchor'] += 1
            link['status'] = 'OK'
        else:
            link['status'] = 'SKIPPED'

    # Print summary
    print(f"\n{'='*60}")
    print(f"  Link Validation Report")
    print(f"{'='*60}")
    print(f"  HTML files scanned:  {len(html_files)}")
    print(f"  Total links found:   {stats['total']}")
    print(f"  Internal links:      {stats['internal']}")
    print(f"  External links:      {stats['external']} (skipped)")
    print(f"  Anchor links:        {stats['anchor']}")
    print(f"  Broken internal:     {stats['broken_internal']}")
    print(f"{'='*60}")

    if broken:
        print("\n⚠️  Broken internal links:")
        for b in broken:
            print(f"  {b['file']}:{b['line']}  →  {b['url']}")
    else:
        print("\n✅  All internal links valid!")

    if write_report:
        REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
        report = {
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'stats': stats,
            'broken': broken,
            'files_scanned': [str(f) for f in html_files],
        }
        REPORT_PATH.write_text(json.dumps(report, indent=2) + '\n')
        print(f"\n📝  Report written to {REPORT_PATH}")

    sys.exit(1 if broken else 0)


if __name__ == '__main__':
    main()
