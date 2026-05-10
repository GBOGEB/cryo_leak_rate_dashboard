# QPLANT Cryogenic Leak Rate Dashboard

**Version**: v3.1.0  
**Last Updated**: 2026-05-09  
**Status**: ✅ Verified

## Project Overview

This repository packages the cryogenic helium leak-rate engineering analysis into an idempotent, self-documenting handover system.

It combines:
- requirements traceability and standards evidence,
- deterministic build/regeneration workflows,
- machine-readable project state for agents,
- human-readable navigation for engineers and reviewers.

## Quick Start

### For Users
1. Open `docs/index.html` in a browser.
2. Explore slides via `docs/index_v3_1.html`.
3. Download packaged bundle from `dist/handover.zip`.

### For Developers
1. `./setup.sh` (idempotent setup + conditional rebuild)
2. `./build.sh` (regenerate outputs + manifest)
3. `./validate.sh` (tests + integrity checks)
4. `./package.sh` (build + validate + zip bundle)

## Agent Handover Instructions

For incoming coding agents:
1. Read `docs/manifest.json` for current machine state.
2. Read `docs/backlog.json` for pending tasks.
3. Read `docs/changelog.md` for version history.
4. Run `./setup.sh` to sync environment and outputs.

## Project Structure

- `src/`: source modules and generators
- `data/`: input datasets and engineering assumptions
- `docs/`: dashboard pages, compliance artifacts, manifest/backlog
- `dist/`: packaging outputs (`handover.zip`, logs, test report)
- `tests/`: unit + integration tests

## Key Files

- `setup.sh`: idempotent entry point
- `build.sh`: deterministic rebuild pipeline
- `validate.sh`: full validation + checksum integrity
- `package.sh`: release bundle generation
- `src/build_dashboard.py`: generates `docs/index.html`
- `docs/manifest.json`: machine-readable current state
- `docs/backlog.json`: handover task queue

## CI/CD

GitHub Actions workflow: `.github/workflows/build.yml`
- triggers on push/PR to `main`
- runs setup, validation, packaging
- uploads `dist/handover.zip`
- deploys `docs/` to GitHub Pages on `main`

## Versioning Scheme

Semantic versioning (`MAJOR.MINOR.PATCH`):
- **MAJOR**: breaking structure or API changes
- **MINOR**: new analysis/features
- **PATCH**: fixes and non-breaking improvements

Current target release: **v3.1.0**
