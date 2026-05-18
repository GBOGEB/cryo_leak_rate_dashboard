# Multi-Repo Migration Checklist

> **Generated:** 2026-05-18
> **Tracking:** Cross-repo organization progress

---

## Phase 1: cryo_leak_rate_dashboard → GitHub

### 1.1 Repository Setup
- [ ] Create repo on GitHub (https://github.com/new → `cryo_leak_rate_dashboard`)
- [ ] Add remote: `git remote add origin https://github.com/GBOGEB/cryo_leak_rate_dashboard.git`
- [ ] Push main: `git push -u origin main`
- [ ] Verify push successful (10 commits, v4.0.0)

### 1.2 GitHub Pages
- [ ] Settings → Pages → Source: branch `main`, folder `/docs`
- [ ] Verify `index.html` loads at `https://gbogeb.github.io/cryo_leak_rate_dashboard/`
- [ ] Verify `index_v4_0.html` (42-slide navigator) accessible
- [ ] Verify `STAKEHOLDER_PRESENTATION.html` accessible
- [ ] Verify all 5 Plotly plots render correctly

### 1.3 Organization Docs PR
- [ ] Create branch `feature/repo-organization-plan`
- [ ] Add `GITHUB_REPO_ORGANIZATION.md`
- [ ] Add `PR_STRATEGY.md`
- [ ] Add `MIGRATION_CHECKLIST.md`
- [ ] Add `IMMEDIATE_ACTIONS.md`
- [ ] Add `repo_templates/` folder
- [ ] Create PR
- [ ] User review
- [ ] Merge

### 1.4 Release Tag
- [ ] Tag `v4.0.0` on main
- [ ] Write GitHub release notes
- [ ] Attach `dist/handover.zip` to release

---

## Phase 2: DOCX_RTM_Automation — Document Consolidation

### 2.1 Clone & Audit
- [ ] Clone repo locally: `git clone --depth=50 https://github.com/GBOGEB/DOCX_RTM_Automation.git`
- [ ] Audit existing folder structure
- [ ] Identify what's already there vs what needs adding

### 2.2 Add Contract Documents
- [ ] Create `contracts/` folder
- [ ] Add `QPS_Contract_pdf.pdf`
- [ ] Add `QPS_Contract_mirror_DOCX.pdf`

### 2.3 Add Addenda
- [ ] Create `addenda/` folder
- [ ] Add `QPS (Addendum II)_Master.docx`
- [ ] Add `Addendum II - Cryoplant Technical Requirements.docx`
- [ ] Add `Addendum II - Cryoplant Technical Requirements1212_1521.docx`
- [ ] Add `Technical Addendum_Reliability centred...docx`

### 2.4 Add Specifications
- [ ] Create `specifications/` folder (or use existing)
- [ ] Add `QPLANT_HV02 exhaust for KAEZER (1).docx`
- [ ] Add `QPLANT_Helium Recovery and Supply MAC - CR1299.docx`
- [ ] Add `QPLANT_Interface and Terminal Points_ACC NF.docx`

### 2.5 Add Requirements
- [ ] Add `SoR_Requirements_Matrix.csv` to `requirements/`

### 2.6 PR
- [ ] Create branch `feature/add-qplant-specs`
- [ ] Commit with descriptive message
- [ ] Push and create PR
- [ ] User review
- [ ] Merge

---

## Phase 3: ABACUS — Analysis Content Organization

### 3.1 Clone & Audit
- [ ] Clone repo locally: `git clone --depth=50 https://github.com/GBOGEB/ABACUS.git`
- [ ] Audit existing structure (82 MB — may need sparse checkout)
- [ ] Identify existing notebooks and analysis files

### 3.2 Add Analysis Content
- [ ] Create `analyses/compressors/` if not exists
- [ ] Add `MYRRHA warm-compressor comparison A.md`
- [ ] Create `vendor_reviews/` if not exists
- [ ] Document Cryoworld offer analysis

### 3.3 Organize Notebooks
- [ ] Inventory all `.ipynb` files
- [ ] Group by topic (cryogenics, materials, compliance)
- [ ] Add index/README for notebooks

### 3.4 PR
- [ ] Create branch `feature/organize-analyses`
- [ ] Commit with descriptive message
- [ ] Push and create PR
- [ ] User review
- [ ] Merge

---

## Phase 4: CODEX — Library Extraction

### 4.1 Clone & Audit
- [ ] Clone repo locally: `git clone --depth=50 https://github.com/GBOGEB/CODEX.git`
- [ ] Audit existing module structure
- [ ] Identify overlap with cryo_leak_rate_dashboard modules

### 4.2 Extract Reusable Modules
- [ ] Evaluate: `calc_leak_rate.py` → reusable library?
- [ ] Evaluate: `materials_db.py` → reusable library?
- [ ] Evaluate: `monte_carlo.py` → reusable library?
- [ ] Evaluate: `risk_model.py` → reusable library?
- [ ] Create proper package structure with `__init__.py`
- [ ] Add unit tests for extracted modules

### 4.3 PR
- [ ] Create branch `feature/extract-cryogenic-modules`
- [ ] Commit extracted modules
- [ ] Push and create PR
- [ ] User review
- [ ] Merge

---

## Phase 5: document-organization-system — v3 → v4 Update

### 5.1 Clone & Audit
- [ ] Clone repo locally: `git clone --depth=50 https://github.com/GBOGEB/document-organization-system.git`
- [ ] Audit `cryo_dashboard_v0_3_0/` folder
- [ ] Check what GitHub Pages currently serves

### 5.2 Update References
- [ ] Add deprecation notice to v3 dashboard
- [ ] Add link/redirect to new cryo_leak_rate_dashboard Pages
- [ ] Update README with cross-repo links
- [ ] Archive v3 content

### 5.3 PR
- [ ] Create branch `feature/v4-references`
- [ ] Commit updates
- [ ] Push and create PR
- [ ] User review
- [ ] Merge

---

## Phase 6: Cross-Repo Integration

### 6.1 Cross-References
- [ ] cryo_leak_rate_dashboard README → links to CODEX, ABACUS, DOCX_RTM_Automation
- [ ] CODEX README → links to cryo_leak_rate_dashboard (consumer)
- [ ] ABACUS README → links to cryo_leak_rate_dashboard (data input target)
- [ ] DOCX_RTM_Automation README → links to cryo_leak_rate_dashboard (implementation)
- [ ] document-organization-system → redirect to new dashboard

### 6.2 CI/CD Alignment
- [ ] Verify all CI workflows passing across repos
- [ ] Add cross-repo test triggers if needed
- [ ] Ensure GitHub Pages deployments working

### 6.3 Documentation
- [ ] Update GBOGEB profile README with repo ecosystem overview
- [ ] Create pinned repo list on GitHub profile

### 6.4 Final Validation
- [ ] All repos have README with cross-links
- [ ] All uploaded documents placed in correct repos
- [ ] All PRs merged or tracked
- [ ] GitHub Pages live for dashboard
- [ ] v4.0.0 tagged and released

---

## 📊 Progress Summary

| Phase | Repo | Status | PRs |
|-------|------|--------|-----|
| 1 | cryo_leak_rate_dashboard | 🔴 Not started | 0/2 |
| 2 | DOCX_RTM_Automation | 🔴 Not started | 0/1 |
| 3 | ABACUS | 🔴 Not started | 0/1 |
| 4 | CODEX | 🔴 Not started | 0/1 |
| 5 | document-organization-system | 🔴 Not started | 0/1 |
| 6 | Cross-repo integration | 🔴 Not started | 0/1 |

**Total PRs planned:** 7
**Total PRs created:** 0
**Total PRs merged:** 0
