# 🚨 Immediate Actions — What to Do RIGHT NOW

> **Generated:** 2026-05-18
> **Priority:** Unblock cryo_leak_rate_dashboard deployment

---

## Action 1 — Push cryo_leak_rate_dashboard to GitHub ⏱️ 5 min

**Why:** This repo has NO remote. All v4.0.0 work exists only locally.

### Option A: Create new repo on GitHub

1. Go to https://github.com/new
2. Repository name: `cryo_leak_rate_dashboard`
3. Description: `MYRRHA QPLANT — Cryogenic Helium Leak-Rate Analysis Dashboard v4.0.0`
4. Public ✅
5. **Do NOT** initialize with README (we have one)
6. Click "Create repository"

Then run:
```bash
cd /home/ubuntu/cryo_leak_rate_dashboard
git remote add origin https://github.com/GBOGEB/cryo_leak_rate_dashboard.git
git branch -M main
git push -u origin main
```

### Option B: Use existing repo (if already created)

```bash
cd /home/ubuntu/cryo_leak_rate_dashboard
git remote add origin https://github.com/GBOGEB/cryo_leak_rate_dashboard.git
git push -u origin main
```

### Verify:
```bash
git remote -v
# Should show: origin https://github.com/GBOGEB/cryo_leak_rate_dashboard.git
```

---

## Action 2 — Enable GitHub Pages ⏱️ 2 min

1. Go to: `https://github.com/GBOGEB/cryo_leak_rate_dashboard/settings/pages`
2. Source: **Deploy from a branch**
3. Branch: `main`
4. Folder: `/docs`
5. Click **Save**

### Verify:
- Wait ~60 seconds
- Open: `https://gbogeb.github.io/cryo_leak_rate_dashboard/`
- Open: `https://gbogeb.github.io/cryo_leak_rate_dashboard/index_v4_0.html`

---

## Action 3 — Create organization docs PR ⏱️ 5 min

```bash
cd /home/ubuntu/cryo_leak_rate_dashboard
git checkout -b feature/repo-organization-plan
git add GITHUB_REPO_ORGANIZATION.md PR_STRATEGY.md MIGRATION_CHECKLIST.md IMMEDIATE_ACTIONS.md
git add repo_templates/
git commit -m "docs: add multi-repo organization plan for QPLANT engineering ecosystem"
git push -u origin feature/repo-organization-plan
```

Then create PR on GitHub.

---

## Action 4 — Tag v4.0.0 release ⏱️ 2 min

After merging the org docs PR:
```bash
git checkout main
git pull
git tag -a v4.0.0 -m "Release v4.0.0: SSoT Implementation, 42-slide navigator, corrected physics engine"
git push origin v4.0.0
```

Then create GitHub Release at `https://github.com/GBOGEB/cryo_leak_rate_dashboard/releases/new`

---

## Action 5 — Upload specs to DOCX_RTM_Automation ⏱️ 10 min

```bash
cd /home/ubuntu
git clone --depth=50 https://github.com/GBOGEB/DOCX_RTM_Automation.git /home/ubuntu/github_repos/DOCX_RTM_Automation
cd /home/ubuntu/github_repos/DOCX_RTM_Automation

git checkout -b feature/add-qplant-specs

# Create folders
mkdir -p contracts addenda specifications requirements

# Copy files
cp "/home/ubuntu/Uploads/QPS_Contract_pdf.pdf" contracts/
cp "/home/ubuntu/Shared/Uploads/QPS_Contract_mirror_DOCX.pdf" contracts/
cp "/home/ubuntu/Shared/Uploads/QPS (Addendum II)_Master.docx" addenda/
cp "/home/ubuntu/Uploads/Addendum II -  Cryoplant Technical Requirements.docx" addenda/
cp "/home/ubuntu/Uploads/Addendum II -  Cryoplant Technical Requirements1212_1521.docx" addenda/
cp "/home/ubuntu/Uploads/Technical Addendum_Reliability centred_linked to QPLANT Reliability Consideration.docx" addenda/
cp "/home/ubuntu/Uploads/QPLANT_HV02 exhaust for KAEZER (1).docx" specifications/
cp "/home/ubuntu/Uploads/QPLANT_Helium Recovery and Supply MAC - CR1299.docx" specifications/
cp "/home/ubuntu/Uploads/QPLANT_Interface and Terminal Points_ACC NF.docx" specifications/
cp "/home/ubuntu/Uploads/SoR_Requirements_Matrix.csv" requirements/

git add -A
git commit -m "docs: add QPLANT contract specs, addenda, and SoR matrix"
git push -u origin feature/add-qplant-specs
```

---

## Action 6 — Add warm compressor analysis to ABACUS ⏱️ 5 min

```bash
cd /home/ubuntu
# NOTE: ABACUS is 82 MB — use sparse checkout if needed
git clone --depth=50 https://github.com/GBOGEB/ABACUS.git /home/ubuntu/github_repos/ABACUS
cd /home/ubuntu/github_repos/ABACUS

git checkout -b feature/add-compressor-analysis
mkdir -p analyses/compressors
cp "/home/ubuntu/Uploads/MYRRHA warm-compressor comparison A.md" analyses/compressors/

git add -A
git commit -m "docs: add MYRRHA warm-compressor comparison (ALaT FSD 575 vs LKT FSD 475)"
git push -u origin feature/add-compressor-analysis
```

---

## ⏱️ Total Estimated Time: ~30 minutes

| # | Action | Time | Blocker? |
|---|--------|------|----------|
| 1 | Push dashboard to GitHub | 5 min | 🔴 **Critical — unlocks everything** |
| 2 | Enable GitHub Pages | 2 min | Depends on #1 |
| 3 | Create org docs PR | 5 min | Depends on #1 |
| 4 | Tag v4.0.0 | 2 min | Depends on #3 merge |
| 5 | Upload specs to DOCX_RTM | 10 min | Independent |
| 6 | Add analysis to ABACUS | 5 min | Independent |

---

## ✅ Success Criteria

After completing all actions:
- [ ] `cryo_leak_rate_dashboard` is on GitHub with remote configured
- [ ] GitHub Pages serves the v4.0.0 dashboard
- [ ] Organization docs PR is created (or merged)
- [ ] v4.0.0 is tagged
- [ ] Contract/spec documents are in DOCX_RTM_Automation
- [ ] Warm compressor analysis is in ABACUS
- [ ] All 5 core repos have cross-references in READMEs
