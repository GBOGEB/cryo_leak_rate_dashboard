# Pull Request Strategy — Multi-Repo Organization

> **Generated:** 2026-05-18
> **Scope:** PR workflow for all QPLANT engineering repos

---

## 🔴 Priority 1 — cryo_leak_rate_dashboard (CRITICAL)

### Current Status
- **Local branch:** `main` (only branch)
- **Remote:** ⚠️ **NO REMOTE CONFIGURED** — repo exists only locally
- **Content:** Full v4.0.0 dashboard (SSoT, 42-slide navigator, 18 tests passing, CI/CD configured)
- **Commits:** 10 commits, latest `b5b1586`

### Action Plan

#### Step 1: Push to GitHub (create remote repo)

```bash
cd /home/ubuntu/cryo_leak_rate_dashboard

# Option A: If repo already exists on GitHub
git remote add origin https://github.com/GBOGEB/cryo_leak_rate_dashboard.git
git push -u origin main

# Option B: If repo needs creation (user must create on GitHub first)
# 1. Go to https://github.com/new
# 2. Name: cryo_leak_rate_dashboard
# 3. Public, no README (we have one)
# 4. Then:
git remote add origin https://github.com/GBOGEB/cryo_leak_rate_dashboard.git
git branch -M main
git push -u origin main
```

#### Step 2: Create feature branch for organization work

```bash
git checkout -b feature/repo-organization-plan
# Add organization docs (this PR_STRATEGY.md, etc.)
git add GITHUB_REPO_ORGANIZATION.md PR_STRATEGY.md MIGRATION_CHECKLIST.md IMMEDIATE_ACTIONS.md
git add repo_templates/
git commit -m "docs: add multi-repo organization plan and PR strategy"
git push -u origin feature/repo-organization-plan
```

#### Step 3: Create PR

```
Title: docs: Multi-repo organization plan for QPLANT engineering ecosystem
Base: main
Head: feature/repo-organization-plan

Body:
## Summary
Adds comprehensive repository organization plan for the GBOGEB QPLANT engineering ecosystem.

## Files Added
- GITHUB_REPO_ORGANIZATION.md — Master repo architecture plan
- PR_STRATEGY.md — Per-repo PR workflow
- MIGRATION_CHECKLIST.md — Cross-repo migration tracking
- IMMEDIATE_ACTIONS.md — Next steps
- repo_templates/ — README templates for new/reorganized repos

## Context
The QPLANT project spans 5 active repos (CODEX, ABACUS, document-organization-system,
DOCX_RTM_Automation, and this dashboard). This PR establishes the organizational framework.

## Checklist
- [x] Organization plan reviewed
- [x] Content distribution matrix defined
- [x] PR strategy per repo documented
- [x] Migration checklist created
- [ ] User review and approval
```

#### Step 4: Enable GitHub Pages

```bash
# After merge to main, configure Pages:
# Settings → Pages → Source: Deploy from branch → main → /docs
```

### PR Checklist for v4.0.0 Release

- [x] All 18 tests passing
- [x] CI/CD workflows configured (build.yml, ci.yml, deploy.yml)
- [x] VERSION = 4.0.0
- [x] CHANGELOG.md updated
- [x] 42-slide master navigator (docs/index_v4_0.html)
- [x] Stakeholder presentation (10 slides)
- [x] All 5 Plotly plots generated
- [x] Handover documents generated (MD, HTML, PDF)
- [x] RTM traceability matrix complete
- [x] Standards compliance grid generated
- [x] OUTPUT_MANIFEST.json with SHA256 hashes
- [ ] Remote repo created on GitHub
- [ ] PR created and reviewed
- [ ] Merged to main
- [ ] GitHub Pages live
- [ ] Tagged v4.0.0

---

## 🟡 Priority 2 — CODEX

### Current Status
- **Remote:** ✅ https://github.com/GBOGEB/CODEX (6 MB)
- **Description:** "CODEX space for MCB (Blocks via MCP)"
- **Language:** Python
- **Last push:** 2026-05-18

### Proposed PR: Extract reusable calc modules

```
Title: feat: extract calc_leak_rate as reusable CODEX module
Branch: feature/calc-leak-rate-module

Content:
- Copy src/calc_leak_rate.py → codex/cryogenics/leak_rate.py
- Copy src/materials_db.py → codex/materials/properties.py
- Add unit tests
- Add __init__.py with public API
- Update README with module documentation
```

### Modules to Consider Extracting

| Source (cryo_leak_rate_dashboard) | Target (CODEX) | Type |
|---|---|---|
| `src/calc_leak_rate.py` | `codex/cryogenics/leak_rate.py` | Core physics |
| `src/materials_db.py` | `codex/materials/properties.py` | Material DB |
| `src/compressor_reliability.py` | `codex/reliability/compressor.py` | Reliability |
| `src/liquid_he_loss.py` | `codex/cryogenics/liquid_he.py` | Liquid He |
| `src/monte_carlo.py` | `codex/statistics/monte_carlo.py` | Statistical |
| `src/risk_model.py` | `codex/reliability/risk.py` | Risk assessment |
| `src/wcs_scenarios.py` | `codex/scenarios/wcs.py` | WCS logic |

---

## 🟡 Priority 3 — ABACUS

### Current Status
- **Remote:** ✅ https://github.com/GBOGEB/ABACUS (82 MB)
- **Description:** "CodeLLM and Deep Agent place to view and drop all files"
- **Language:** Python
- **Last push:** 2026-05-18

### Proposed PR: Organize analysis content

```
Title: docs: organize MYRRHA analysis notebooks and warm compressor studies
Branch: feature/organize-analyses

Content:
- Add analyses/warm_compressor_comparison_ALaT_LKT.md
- Organize Jupyter notebooks into topic folders
- Add data/ folder with analysis inputs
- Update README with analysis catalog
```

### Content to Add/Organize

| Content | Source | Target Path in ABACUS |
|---------|--------|-----------------------|
| Warm compressor comparison A.md | Uploads/ | `analyses/compressors/` |
| Cryoworld offer review | Uploads/ | `vendor_reviews/` |
| Valve leak rate analysis | Generated from dashboard | `analyses/valves/` |
| Material properties study | data/helium_properties.json | `data/materials/` |

---

## 🟡 Priority 4 — document-organization-system

### Current Status
- **Remote:** ✅ https://github.com/GBOGEB/document-organization-system (594 KB)
- **Description:** "Document Organization System"
- **Language:** HTML
- **Last push:** 2026-05-18
- **Contains:** v3 cryo dashboard folder (per image (4).png — material properties dashboard)

### Proposed PR: Update to reference v4.0.0

```
Title: docs: update references from v3 to v4.0.0 cryo dashboard
Branch: feature/v4-references

Content:
- Update cryo_dashboard_v0_3_0/ references to point to new repo
- Add redirect/link to cryo_leak_rate_dashboard GitHub Pages
- Archive v3 content with deprecation notice
- Update README with cross-repo links
```

---

## 🟢 Priority 5 — DOCX_RTM_Automation

### Current Status
- **Remote:** ✅ https://github.com/GBOGEB/DOCX_RTM_Automation (25 MB)
- **Description:** "Documents, CODE, pipeline, markdown for SoR, RTM"
- **Language:** Python
- **Last push:** 2026-05-15

### Proposed PR: Add uploaded contract & specification documents

```
Title: docs: add QPLANT contract specs, addenda, and SoR matrix
Branch: feature/add-qplant-specs

Content:
- contracts/QPS_Contract_pdf.pdf
- contracts/QPS_Contract_mirror_DOCX.pdf
- addenda/QPS_Addendum_II_Master.docx
- addenda/Addendum_II_Cryoplant_Technical_Requirements.docx
- addenda/Addendum_II_Cryoplant_Technical_Requirements_1212_1521.docx
- addenda/Technical_Addendum_Reliability_centred.docx
- specifications/QPLANT_HV02_exhaust_for_KAEZER.docx
- specifications/QPLANT_Helium_Recovery_and_Supply_MAC_CR1299.docx
- specifications/QPLANT_Interface_and_Terminal_Points_ACC_NF.docx
- requirements/SoR_Requirements_Matrix.csv
```

---

## 📋 PR Execution Order

```
Step 1 ─── cryo_leak_rate_dashboard: Create remote → Push main → Create org docs PR
                │
Step 2 ─── DOCX_RTM_Automation: PR to add uploaded contract/spec documents
                │
Step 3 ─── ABACUS: PR to organize analysis content
                │
Step 4 ─── CODEX: PR to extract reusable modules
                │
Step 5 ─── document-organization-system: PR to update v3→v4 references
                │
Step 6 ─── cryo_leak_rate_dashboard: Tag v4.0.0, enable GitHub Pages
```

---

## ⚙️ PR Review Workflow

### For All Repos
1. **Create feature branch** from `main`
2. **Make changes** locally
3. **Run tests** (if applicable)
4. **Push** to remote
5. **Create PR** with descriptive title and body
6. **User reviews** in GitHub UI
7. **Merge** only after user approval (never auto-merge)
8. **Tag** release if applicable
9. **Delete** feature branch after merge

### Git Commands Template

```bash
# Clone (if not already local)
git clone --depth=50 https://github.com/GBOGEB/<REPO>.git
cd <REPO>

# Create feature branch
git checkout -b feature/<description>

# Make changes...

# Stage and commit
git add -A
git commit -m "<prefix>: <description>"

# Push
git push -u origin feature/<description>

# Create PR (via GitHub Tool or gh CLI)
```
