# Pull Request Checklist — v4.0.0 Integration

## 🎯 PR Overview
- **Branch:** `main` (local) → feature branch for PR
- **Target:** `main`
- **Version:** v4.0.0
- **Commit:** `4aed987`
- **Author:** Abacus AI Agent
- **Date:** 2026-05-14
- **GitHub User:** GBOGEB

## ✅ Pre-Merge Verification Checklist

### 1. GitHub Actions Status
- [ ] **CI Workflow** (`ci.yml`) — tests, validation, link checker
- [ ] **Build Workflow** (`build.yml`) — full build pipeline
- [ ] **Deploy Workflow** (`deploy.yml`) — GitHub Pages deployment
- [ ] All checks passing (green ✅)

### 2. Files Included in PR (39 files changed, +2431 / −210)
- [ ] Source code changes (`src/`)
- [ ] Configuration updates (`data/config.yaml`)
- [ ] CI/CD workflows (`.github/workflows/ci.yml`, `deploy.yml`)
- [ ] Build scripts (`scripts/compute_hashes.py`, `validate_links.py`, `release.sh`, `deploy.sh`, `export_pdfs.sh`)
- [ ] Documentation (`BUILD_LOG.md`, `QUICK_ACCESS.md`)
- [ ] Hero pages (`docs/heroes/executive.html`, `technical.html`, `compliance.html`)
- [ ] Tests (`tests/` — 22 tests across 7 files)
- [ ] Manifest updates (`docs/manifest.json`)
- [ ] Deployment configs (`netlify.toml`, `vercel.json`)

### 3. Technical Validation
- [ ] All tests passing (22/22) — `pytest tests/ -v`
- [ ] No broken links (84 HTML files) — `python scripts/validate_links.py`
- [ ] SHA-256 hashes verified — `python scripts/compute_hashes.py`
- [ ] Build reproducible — `./build.sh`
- [ ] No merge conflicts
- [ ] `VERSION` file reads `4.0.0`

### 4. Documentation Completeness
- [ ] `CHANGELOG.md` updated with v4.0.0 entry
- [ ] `BUILD_LOG.md` complete with recursive build sequence
- [ ] `VERSION` file correct (`4.0.0`)
- [ ] `README.md` current
- [ ] `QUICK_ACCESS.md` with URL table
- [ ] `NAVIGATOR.html` updated with hero/CI sections

### 5. Configuration Integrity (SSoT)
- [ ] `data/config.yaml` — Single Source of Truth
- [ ] HP compressor count: **3** (corrected from 4)
- [ ] HP discharge pressure: **14 barg** (updated)
- [ ] LP suction pressure: **1.05 bara** (updated)
- [ ] All downstream files derive from config.yaml

### 6. Deployment Readiness
- [ ] GitHub Pages configured via `deploy.yml`
- [ ] Netlify config present (`netlify.toml`)
- [ ] Vercel config present (`vercel.json`)
- [ ] `QUICK_ACCESS.md` URL table ready
- [ ] `NAVIGATOR.html` working as entry point

## 📋 Post-Merge Actions
1. ⏳ Monitor GitHub Actions completion (~2–3 min)
2. ✅ Verify GitHub Pages deployment
3. 🌐 Test live URLs (see table below)
4. 🏷️ Create git tag `v4.0.0`
5. 📦 Create GitHub Release with notes
6. 📊 Update project board / close related issues

## 🚀 Deployment URLs to Verify

| Page | URL |
|------|-----|
| **Navigator** | `https://gbogeb.github.io/cryo_leak_rate_dashboard/NAVIGATOR.html` |
| **Landing Page** | `https://gbogeb.github.io/cryo_leak_rate_dashboard/index.html` |
| **40-Slide Master** | `https://gbogeb.github.io/cryo_leak_rate_dashboard/index_v4_0.html` |
| **Executive Summary** | `https://gbogeb.github.io/cryo_leak_rate_dashboard/executive_summary.html` |
| **Dashboard** | `https://gbogeb.github.io/cryo_leak_rate_dashboard/dashboard.html` |
| **Stakeholder Pres.** | `https://gbogeb.github.io/cryo_leak_rate_dashboard/STAKEHOLDER_PRESENTATION.html` |
| **RTM Traceability** | `https://gbogeb.github.io/cryo_leak_rate_dashboard/rtm_traceability.html` |
| **Hero: Executive** | `https://gbogeb.github.io/cryo_leak_rate_dashboard/heroes/executive.html` |
| **Hero: Technical** | `https://gbogeb.github.io/cryo_leak_rate_dashboard/heroes/technical.html` |
| **Hero: Compliance** | `https://gbogeb.github.io/cryo_leak_rate_dashboard/heroes/compliance.html` |

## 🔄 Rollback Plan
If issues detected post-merge:
```bash
git revert HEAD --no-edit
git push origin main
```
Or revert to previous commit:
```bash
git reset --hard fc31710
git push --force-with-lease origin main
```

---
*Generated: 2026-05-18 | Project: QPLANT Cryo Leak Rate Dashboard v4.0.0*
