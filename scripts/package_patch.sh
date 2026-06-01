#!/usr/bin/env bash
#
# package_patch.sh — assemble a handover bundle from the repository output
# contract (patches/*.patch.md + manifest/) into dist/, with a generated
# MANIFEST.json, a zip archive, and a SHA-256 checksum.
#
# Usage:
#   scripts/package_patch.sh validate    # check required sections only
#   scripts/package_patch.sh bundle      # stage bundle under dist/handover-patch/
#   scripts/package_patch.sh zip         # bundle + create zip + sha256
#   scripts/package_patch.sh             # same as 'zip'
#
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

PATCH_DIR="patches"
MANIFEST_FILE="manifest/artifact-topology.yaml"
STAGE_DIR="dist/handover-patch"
ZIP_FILE="dist/handover-patch.zip"

REQUIRED_SECTIONS=(
  "## Metadata"
  "## Summary"
  "## Patch Plan"
  "## Validation"
  "## Rollback"
)

log() { echo "[package_patch] $*"; }

list_patches() {
  # Canonical patch files only (exclude the TEMPLATE).
  find "$PATCH_DIR" -maxdepth 1 -type f -name '*.patch.md' ! -name 'TEMPLATE.patch.md' | sort
}

validate() {
  local found=0 failed=0
  while IFS= read -r patch; do
    [ -z "$patch" ] && continue
    found=$((found + 1))
    for section in "${REQUIRED_SECTIONS[@]}"; do
      if ! grep -qF "$section" "$patch"; then
        echo "  ✗ $patch is missing required section: '$section'" >&2
        failed=$((failed + 1))
      fi
    done
  done < <(list_patches)

  if [ "$found" -eq 0 ]; then
    echo "  ✗ No patch packages found under $PATCH_DIR/ (*.patch.md)" >&2
    return 1
  fi
  if [ "$failed" -ne 0 ]; then
    echo "  ✗ Validation failed: $failed missing section(s)" >&2
    return 1
  fi
  log "Validation passed ($found patch package(s))"
}

stage_bundle() {
  validate
  rm -rf "$STAGE_DIR"
  mkdir -p "$STAGE_DIR/patches" "$STAGE_DIR/manifest"

  while IFS= read -r patch; do
    [ -z "$patch" ] && continue
    cp "$patch" "$STAGE_DIR/patches/"
  done < <(list_patches)

  if [ -f "$MANIFEST_FILE" ]; then
    cp "$MANIFEST_FILE" "$STAGE_DIR/manifest/"
  fi

  generate_manifest_json "$STAGE_DIR"
  log "Staged bundle at $STAGE_DIR"
}

generate_manifest_json() {
  local stage="$1"
  STAGE_DIR_ENV="$stage" python3 - <<'PY'
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

stage = Path(os.environ["STAGE_DIR_ENV"])
out = stage / "MANIFEST.json"

files = {}
for path in sorted(stage.rglob("*")):
    if path.is_dir() or path.name == "MANIFEST.json":
        continue
    data = path.read_bytes()
    rel = str(path.relative_to(stage))
    files[rel] = {
        "sha256": hashlib.sha256(data).hexdigest(),
        "size": len(data),
    }

payload = {
    "bundle": "handover-patch",
    "generated": datetime.now(timezone.utc).isoformat(),
    "file_count": len(files),
    "files": files,
}
out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"[package_patch] Wrote {out} ({len(files)} files)")
PY
}

make_zip() {
  stage_bundle
  rm -f "$ZIP_FILE" "$ZIP_FILE.sha256"
  (cd "$(dirname "$STAGE_DIR")" && zip -r "$(basename "$ZIP_FILE")" "$(basename "$STAGE_DIR")" >/dev/null)
  sha256sum "$ZIP_FILE" | awk '{print $1}' > "$ZIP_FILE.sha256"
  log "Bundle ready: $ZIP_FILE"
  log "SHA256 stored at $ZIP_FILE.sha256"
}

mkdir -p dist

case "${1:-zip}" in
  validate) validate ;;
  bundle)   stage_bundle ;;
  zip)      make_zip ;;
  *)
    echo "Unknown command: ${1:-}" >&2
    echo "Usage: $0 [validate|bundle|zip]" >&2
    exit 2
    ;;
esac
