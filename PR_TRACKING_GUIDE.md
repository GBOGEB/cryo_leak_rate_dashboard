# Pull Request Tracking Guide

> QPLANT Cryogenic Engineering — Multi-Repository Ecosystem  
> Last verified: 2026-06-02

---

## 🎯 PR Summary

### PRs Created During This Session

```
Repository                    PR #    Status      Content
──────────────────────────────────────────────────────────────────────
DOCX_RTM_Automation          #14     ✅ Merged   Contract specs, addenda, SoR matrix
ABACUS                       #400    ✅ Merged   Warm-compressor comparison (ALaT vs LKT)
cryo_leak_rate_dashboard     N/A     Direct      Main dashboard v4.0.0 (direct push)
```

---

## 📋 PR #14: DOCX_RTM_Automation

### Repository

**GBOGEB/DOCX_RTM_Automation**

### PR Details

| Field | Value |
|---|---|
| **Number** | #14 |
| **Status** | ✅ Merged |
| **Title** | `docs: add QPLANT contract specs, addenda, and SoR matrix` |
| **Branch** | `feature/add-qplant-specs` → `main` |
| **Created** | 2026-05-18 06:48:02 UTC |
| **Merged** | 2026-05-18 06:50:40 UTC |
| **Merge Commit** | `01d9498` |
| **Changed Files** | 10 |

### Description

Added QPLANT contract documents, technical addenda, specifications, and SoR requirements matrix to an organized folder structure.

### Files Added

```
contracts/
├── QPS_Contract_pdf.pdf
└── QPS_Contract_mirror_DOCX.pdf

addenda/
├── QPS_Addendum_II_Master.docx
├── Addendum_II_Cryoplant_Technical_Requirements.docx
├── Addendum_II_Cryoplant_Technical_Requirements_1212_1521.docx
└── Technical_Addendum_Reliability_centred.docx

specifications/
├── QPLANT_HV02_exhaust_for_KAEZER.docx
├── QPLANT_Helium_Recovery_and_Supply_MAC_CR1299.docx
└── QPLANT_Interface_and_Terminal_Points_ACC_NF.docx

requirements/
└── SoR_Requirements_Matrix.csv
```

### URLs to Track

| Resource | URL |
|---|---|
| **PR Page** | https://github.com/GBOGEB/DOCX_RTM_Automation/pull/14 |
| **Diff** | https://github.com/GBOGEB/DOCX_RTM_Automation/pull/14/files |
| **Merge Commit** | https://github.com/GBOGEB/DOCX_RTM_Automation/commit/01d9498 |
| **Repository** | https://github.com/GBOGEB/DOCX_RTM_Automation |
| **Commit History** | https://github.com/GBOGEB/DOCX_RTM_Automation/commits/main |

### Verification Checklist

- [x] PR merged by user
- [x] 10 files now in repository
- [x] Folder structure organized (contracts/, addenda/, specifications/, requirements/)
- [x] Documents accessible via GitHub

---

## 📋 PR #400: ABACUS

### Repository

**GBOGEB/ABACUS**

### PR Details

| Field | Value |
|---|---|
| **Number** | #400 |
| **Status** | ✅ Merged |
| **Title** | `docs: add MYRRHA warm-compressor comparison (ALaT FSD 575 vs LKT FSD 475)` |
| **Branch** | `feature/add-compressor-analysis` → `main` |
| **Created** | 2026-05-18 06:48:41 UTC |
| **Merged** | 2026-05-18 06:50:08 UTC |
| **Merge Commit** | `a9dd4d2` |
| **Changed Files** | 1 |

### Description

Integrated the MYRRHA warm-compressor comparison study (ALaT FSD 575 SFC vs LKT FSD 475 SFC) into the analyses/compressors/ directory, including an interactive HTML mass-flow visualization.

### Files Added

```
analyses/compressors/
└── MYRRHA_warm_compressor_comparison_ALaT_LKT.md
```

### Key Findings in the Analysis

| Target (g/s) | 3× ALaT FSD 575 (72 Hz) | 3× LKT FSD 475 (62 Hz max) |
|---|---|---|
| 350 | ❌ Above capacity | ❌ Above capacity |
| 336 | ✅ At limit | ❌ Above capacity |
| 275 | ✅ Feasible | ✅ Feasible |
| 200 | ✅ Feasible | ✅ Feasible |

- **ALaT FSD 575 SFC** (72 Hz): 112.54 g/s per skid → 337.6 g/s for 3 units
- **LKT FSD 475 SFC** (62 Hz): 96.1 g/s per skid → 288.3 g/s for 3 units (max)
- **LKT FSD 475 SFC** nominal: 88 g/s per skid → 264 g/s for 3 units

### URLs to Track

| Resource | URL |
|---|---|
| **PR Page** | https://github.com/GBOGEB/ABACUS/pull/400 |
| **Diff** | https://github.com/GBOGEB/ABACUS/pull/400/files |
| **Merge Commit** | https://github.com/GBOGEB/ABACUS/commit/a9dd4d2 |
| **Repository** | https://github.com/GBOGEB/ABACUS |
| **Commit History** | https://github.com/GBOGEB/ABACUS/commits/main |
| **Analysis File** | https://github.com/GBOGEB/ABACUS/blob/main/analyses/compressors/MYRRHA_warm_compressor_comparison_ALaT_LKT.md |

### Verification Checklist

- [x] PR merged by user
- [x] Analysis integrated into `analyses/compressors/`
- [x] Interactive HTML visualization included (embedded in Markdown)
- [x] Detailed comparison tables with per-skid and 3-skid totals
- [x] Source references to ALaT and LKT pre-studies documented

---

## 📋 cryo_leak_rate_dashboard (Main Project)

### Repository

**GBOGEB/cryo_leak_rate_dashboard**

### Details

| Field | Value |
|---|---|
| **PR Number** | N/A (direct push to main) |
| **Status** | ✅ Deployed on GitHub Pages |
| **Version** | v4.0.0 |
| **Latest Commit** | `1e03811` |
| **GitHub Pages** | ✅ Live |

### Why No PR?

This was a new repository setup and single-developer workflow. All changes were pushed directly to `main`. This is standard practice for:
- New repository creation and initial deployment
- Single developer workflow
- Direct deployment to production (GitHub Pages)

### Key Commits

```
1e03811 - fix: update handover.zip and build.yml links to valid GitHub URLs
05bf986 - fix: remove handover.zip binary to unblock GitHub Pages build
b7e0d1b - chore: trigger GitHub Pages rebuild
f640e7f - fix: repair all broken links for GitHub Pages deployment
f7a571a - docs: add alignment verification report and sync status summary
50193fa - docs: deployment complete — all URLs verified live
```

### URLs to Track

| Resource | URL |
|---|---|
| **Repository** | https://github.com/GBOGEB/cryo_leak_rate_dashboard |
| **Live Dashboard** | https://gbogeb.github.io/cryo_leak_rate_dashboard/ |
| **Commit History** | https://github.com/GBOGEB/cryo_leak_rate_dashboard/commits/main |
| **Release v4.0.0** | https://github.com/GBOGEB/cryo_leak_rate_dashboard/releases/tag/v4.0.0 |
| **CI/CD Actions** | https://github.com/GBOGEB/cryo_leak_rate_dashboard/actions |

### Verification Checklist

- [x] 100+ HTML files deployed in `docs/`
- [x] v4.0.0 release tagged
- [x] GitHub Pages live and functional
- [x] All 84 links verified — zero 404s
- [x] 22/22 tests passing

---

## 🔄 Multi-Repo Ecosystem Overview

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  QPLANT Engineering Ecosystem                               │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1️⃣  cryo_leak_rate_dashboard (Main Dashboard)              │
│      ├─ Method: Direct push (no PR)                        │
│      ├─ Latest: 1e03811                                    │
│      └─ Status: ✅ Live on GitHub Pages                    │
│                                                             │
│  2️⃣  DOCX_RTM_Automation (Engineering Documents)            │
│      ├─ PR #14 ✅ Merged (2026-05-18)                      │
│      ├─ 10 contract/spec/addenda files                     │
│      └─ Status: ✅ Integrated                              │
│                                                             │
│  3️⃣  ABACUS (Analysis Studies)                              │
│      ├─ PR #400 ✅ Merged (2026-05-18)                     │
│      ├─ Warm-compressor comparison (ALaT vs LKT)           │
│      └─ Status: ✅ Integrated                              │
│                                                             │
│  4️⃣  document-organization-system (v3 Reference Tool)       │
│      ├─ No PRs this session                                │
│      └─ Status: ✅ Active (last push 2026-05-28)           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 Quick Reference Table

| Repository | Type | PR / Commit | Status | URL |
|---|---|---|---|---|
| cryo_leak_rate_dashboard | Main Dashboard | `1e03811` (direct) | ✅ Live | [repo](https://github.com/GBOGEB/cryo_leak_rate_dashboard) · [site](https://gbogeb.github.io/cryo_leak_rate_dashboard/) |
| DOCX_RTM_Automation | Documents | PR #14 → `01d9498` | ✅ Merged | [PR](https://github.com/GBOGEB/DOCX_RTM_Automation/pull/14) · [repo](https://github.com/GBOGEB/DOCX_RTM_Automation) |
| ABACUS | Analysis | PR #400 → `a9dd4d2` | ✅ Merged | [PR](https://github.com/GBOGEB/ABACUS/pull/400) · [repo](https://github.com/GBOGEB/ABACUS) |
| document-organization-system | v3 Tool | N/A | ✅ Active | [repo](https://github.com/GBOGEB/document-organization-system) |

---

## 🔍 How to Track PRs on GitHub

### For DOCX_RTM_Automation PR #14

**Option 1 — Direct URL:**
```
https://github.com/GBOGEB/DOCX_RTM_Automation/pull/14
```

**Option 2 — Through Repository:**
1. Go to https://github.com/GBOGEB/DOCX_RTM_Automation
2. Click the **Pull requests** tab
3. Click **Closed** to see merged PRs
4. Find PR #14

**Option 3 — Through Commits:**
1. Go to https://github.com/GBOGEB/DOCX_RTM_Automation/commits/main
2. Look for merge commit `01d9498`

---

### For ABACUS PR #400

**Option 1 — Direct URL:**
```
https://github.com/GBOGEB/ABACUS/pull/400
```

**Option 2 — Through Repository:**
1. Go to https://github.com/GBOGEB/ABACUS
2. Click the **Pull requests** tab
3. Click **Closed** to see merged PRs
4. Find PR #400

**Option 3 — Through Commits:**
1. Go to https://github.com/GBOGEB/ABACUS/commits/main
2. Look for merge commit `a9dd4d2`

---

### For cryo_leak_rate_dashboard (No PRs)

**Track via Commits:**
```
https://github.com/GBOGEB/cryo_leak_rate_dashboard/commits/main
```

**Track via Release:**
```
https://github.com/GBOGEB/cryo_leak_rate_dashboard/releases/tag/v4.0.0
```

**Track via CI/CD Actions:**
```
https://github.com/GBOGEB/cryo_leak_rate_dashboard/actions
```

---

## 📌 Bookmark These URLs

### Essential Daily Links

| Purpose | URL |
|---|---|
| All Repositories | https://github.com/GBOGEB?tab=repositories |
| Main Dashboard (repo) | https://github.com/GBOGEB/cryo_leak_rate_dashboard |
| Main Dashboard (live) | https://gbogeb.github.io/cryo_leak_rate_dashboard/ |
| PR #14 (Documents) | https://github.com/GBOGEB/DOCX_RTM_Automation/pull/14 |
| PR #400 (Analysis) | https://github.com/GBOGEB/ABACUS/pull/400 |

---

## 📧 Notification Settings

To track PR activity on any repository:

1. Go to the repository page
2. Click **Watch** (top right)
3. Select **All Activity**
4. Receive notifications for all PR updates, commits, and issues

### Recommended Watch Settings

| Repository | Watch Level | Reason |
|---|---|---|
| cryo_leak_rate_dashboard | All Activity | Primary project — track all commits and deployments |
| DOCX_RTM_Automation | Participating | Documents repo — track new PRs and discussions |
| ABACUS | Participating | Analysis repo — track new PRs |
| document-organization-system | Releases Only | Reference tool — track major updates |

---

## ✅ Current Status Summary

| Repository | Latest | Status | Action Needed |
|---|---|---|---|
| cryo_leak_rate_dashboard | `1e03811` | ✅ Live on GitHub Pages | None — all 84 links verified |
| DOCX_RTM_Automation | PR #14 merged | ✅ Integrated | None |
| ABACUS | PR #400 merged | ✅ Integrated | None |
| document-organization-system | Active | ✅ Active | None |

**All systems operational and tracked!** 🚀
