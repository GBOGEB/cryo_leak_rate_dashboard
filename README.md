# MYRRHA QPLANT Cryogenic Helium Leak Rate Analysis Dashboard

![Version](https://img.shields.io/badge/version-4.0.0-blue)
![Tests](https://img.shields.io/badge/tests-22%2F22%20passing-success)
![Deployment](https://img.shields.io/badge/deployment-live-brightgreen)
![Pages](https://img.shields.io/badge/GitHub%20Pages-live-brightgreen)

> Single Source of Truth (SSoT) Implementation for MYRRHA QPLANT Cryogenic Engineering

**Version**: v4.0.0  
**Last Updated**: 2026-05-31  
**Status**: ✅ Deployed & Live on GitHub Pages

## 🌐 Live Site

**→ https://gbogeb.github.io/cryo_leak_rate_dashboard/**

## 🔗 Quick Links

| Link | Description |
|------|-------------|
| 🌐 [Live Dashboard](https://gbogeb.github.io/cryo_leak_rate_dashboard/) | GitHub Pages site — **LIVE** |
| 🧭 [Navigator](https://gbogeb.github.io/cryo_leak_rate_dashboard/NAVIGATOR.html) | Central navigation hub |
| 📐 [Technical (42 slides)](https://gbogeb.github.io/cryo_leak_rate_dashboard/index_v4_0.html) | Full technical deep-dive |
| 🎤 [Executive (10 slides)](https://gbogeb.github.io/cryo_leak_rate_dashboard/STAKEHOLDER_PRESENTATION.html) | Stakeholder summary |
| 📊 [Dashboard](https://gbogeb.github.io/cryo_leak_rate_dashboard/dashboard.html) | Interactive dashboard |
| 🏷️ [Release v4.0.0](https://github.com/GBOGEB/cryo_leak_rate_dashboard/releases/tag/v4.0.0) | Official release |

## Project Overview

This repository packages the cryogenic helium leak-rate engineering analysis into an idempotent, self-documenting handover system.

It combines:
- **Single Source of Truth** (`data/config.yaml`) for all engineering parameters,
- requirements traceability and standards evidence,
- deterministic build/regeneration workflows,
- machine-readable project state for agents,
- human-readable navigation for engineers and reviewers.

### Key v4.0.0 Changes
- Corrected HP compressor count: 4 → 3 (Kaeser FSD 575 SFC)
- Updated pressure parameters: 14 barg HP discharge, 1050 mbar HCC inlet
- Implemented SSoT configuration system
- Added recursive build tracking

## Quick Start

### For Users
1. Open `docs/VERSION_SELECTOR.html` in a browser (or visit the [live site](https://gbogeb.github.io/cryo_leak_rate_dashboard/)).
2. Explore slides via `docs/NAVIGATOR.html`.
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

Current release: **v4.0.0**

## 📁 Deployment Guides

| Document | Purpose |
|----------|---------|
| [GITHUB_PAGES_VISUAL_GUIDE.md](GITHUB_PAGES_VISUAL_GUIDE.md) | Step-by-step Pages setup with ASCII art |
| [POST_DEPLOYMENT_CHECKLIST.md](POST_DEPLOYMENT_CHECKLIST.md) | Remaining tasks after deployment |
| [FINAL_DEPLOYMENT_SUMMARY.md](FINAL_DEPLOYMENT_SUMMARY.md) | Complete project status |
| [scripts/site_verification.sh](scripts/site_verification.sh) | Automated URL verification |
