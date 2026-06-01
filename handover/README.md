# `handover/` — Handover Bundle Index

This directory is the staging/landing area for **handover bundles** assembled from
the repository output contract (see [`../patches/README.md`](../patches/README.md)).

A handover bundle packages the canonical `*.patch.md` source of truth together
with the federation manifest and an integrity checksum, so it can be archived or
transferred as a single artifact.

## How bundles are produced

```bash
make patch-validate   # verify every patches/*.patch.md has the required sections
make patch-bundle     # stage patches/ + manifest/ into dist/handover-patch/
make handover-zip     # zip the staged bundle and emit a sha256 checksum
```

Outputs (under `dist/`, which is git-ignored):

```
dist/handover-patch/                 # staged bundle contents
dist/handover-patch.zip              # the bundle
dist/handover-patch.zip.sha256       # integrity checksum
dist/handover-patch/MANIFEST.json    # generated file list with hashes
```

## Contents of a bundle

- All `patches/*.patch.md` files (the canonical source of truth)
- `manifest/artifact-topology.yaml` (federation topology + patch index)
- `MANIFEST.json` (generated: per-file SHA-256, size, count)

## Roles served by the bundle

- patch description · architecture decision note · migration manifest
- handover artifact · packaging recipe · local integration guide

The Markdown patch files remain the source of truth; everything here is generated
from them.
