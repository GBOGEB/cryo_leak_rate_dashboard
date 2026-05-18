# GitHub Repository Organization — GBOGEB

> **Generated:** 2026-05-18
> **Scope:** Multi-repo strategy for MYRRHA QPLANT Cryogenic Engineering
> **Account:** [github.com/GBOGEB](https://github.com/GBOGEB)

---

## 🏗️ Repository Landscape — Current State

### Tier 1 — Active Engineering Repos (daily use)

| # | Repo | Language | Size | Description | Last Push | Status |
|---|------|----------|------|-------------|-----------|--------|
| 1 | **cryo_leak_rate_dashboard** | Python/HTML | ~local only | v4.0.0 QPLANT Cryo Dashboard (SSoT) | local | ⚠️ **No remote — needs push** |
| 2 | [CODEX](https://github.com/GBOGEB/CODEX) | Python | 6 MB | MCB Blocks via MCP | 2026-05-18 | ✅ Active |
| 3 | [ABACUS](https://github.com/GBOGEB/ABACUS) | Python | 82 MB | CodeLLM + Deep Agent file drop | 2026-05-18 | ✅ Active |
| 4 | [document-organization-system](https://github.com/GBOGEB/document-organization-system) | HTML | 594 KB | Doc org system (v3 cryo dashboard folder) | 2026-05-18 | ✅ Active |
| 5 | [DOCX_RTM_Automation](https://github.com/GBOGEB/DOCX_RTM_Automation) | Python | 25 MB | SoR, RTM, pipeline, markdown | 2026-05-15 | ✅ Active |

### Tier 2 — Supporting Engineering Repos

| # | Repo | Size | Description | Status |
|---|------|------|-------------|--------|
| 6 | [Q_engineering_tools](https://github.com/GBOGEB/Q_engineering_tools) | 41 KB | Engineering tools | ✅ Active |
| 7 | [cryoplant-project](https://github.com/GBOGEB/cryoplant-project) | 6 KB | CodeLLM start | 🔄 Seed only |
| 8 | [cryogenic-compliance](https://github.com/GBOGEB/cryogenic-compliance) | 1 KB | Codes & standards | 🔄 Seed only |
| 9 | [CODESPACES_jyperter](https://github.com/GBOGEB/CODESPACES_jyperter) | 708 KB | Jupyter codespace | 🔄 Active |

### Tier 3 — Utility / Legacy / Forked Repos (60+ repos)

Includes forks of major projects (plotly.py, vscode, CoolProp, prettier, etc.) and utility repos. Not part of the core engineering workflow.

---

## 📐 Proposed Multi-Repo Architecture

### 🎯 Core Repos — The "QPLANT Quartet"

```
┌─────────────────────────────────────────────────────────────────┐
│                     QPLANT Engineering Ecosystem                │
│                                                                 │
│  ┌─────────────────┐     ┌─────────────────┐                   │
│  │   DOCX_RTM_     │     │   document-      │                  │
│  │   Automation     │     │   organization-  │                  │
│  │  (requirements,  │     │   system         │                  │
│  │   RTM, SoR)     │     │  (v3 dashboard,  │                  │
│  └────────┬────────┘     │   docs hub)      │                  │
│           │              └────────┬─────────┘                   │
│           ▼                       │                             │
│  ┌─────────────────┐              │                             │
│  │    CODEX         │◄────────────┘                             │
│  │  (MCB, blocks,   │                                          │
│  │   reusable libs) │                                          │
│  └────────┬────────┘                                           │
│           │                                                     │
│           ▼                                                     │
│  ┌─────────────────┐     ┌─────────────────┐                   │
│  │ cryo_leak_rate_ │◄────│    ABACUS        │                  │
│  │ dashboard        │     │  (CodeLLM,       │                  │
│  │ (v4.0.0 SSoT    │     │   notebooks,     │                  │
│  │  production app) │     │   analysis)      │                  │
│  └─────────────────┘     └─────────────────┘                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📁 Content Distribution Matrix

| Content Type | cryo_leak_rate_dashboard | CODEX | ABACUS | document-organization-system | DOCX_RTM_Automation |
|---|---|---|---|---|---|
| **Dashboard HTML/JS/CSS** | ✅ Master (v4.0.0) | ❌ | ❌ | 📄 v3 legacy copy | ❌ |
| **Calc engine (calc_leak_rate.py)** | ✅ Application copy | ✅ Library source | ❌ | ❌ | ❌ |
| **Plotly visualizations** | ✅ All 5 plots | ❌ | ✅ Exploratory | ❌ | ❌ |
| **RTM DOCX / SoR CSV** | 📄 Trace reference | ❌ | ❌ | 📄 Rendered | ✅ Master |
| **Contract PDFs** | 📄 Reference link | ❌ | ❌ | 📄 Rendered | ✅ Master |
| **Jupyter notebooks** | ❌ | ❌ | ✅ All | ❌ | ❌ |
| **Config YAML/JSON** | ✅ Master | ✅ Schema defs | ❌ | ❌ | ❌ |
| **CI/CD workflows** | ✅ GH Pages deploy | ✅ Tests + lint | ✅ nbval | ✅ Pages deploy | ✅ Lint |
| **Test suites** | ✅ pytest (18 tests) | ✅ Unit tests | ✅ Validation | ❌ | ✅ Schema |
| **Build scripts** | ✅ setup/build/validate/package | ✅ Makefile | ❌ | ❌ | ✅ Pipeline |
| **Material properties DB** | ✅ helium_properties.json | ✅ Materials library | ✅ Analysis input | ❌ | ❌ |
| **Compressor specs** | ✅ compressor_specs.json | ❌ | ✅ Comparison studies | ❌ | ❌ |
| **Warm compressor comparisons** | ❌ | ❌ | ✅ ALaT/LKT analysis | ❌ | ❌ |
| **Slide packages** | ✅ 42-slide navigator | ❌ | ❌ | ✅ Presentation hub | ❌ |
| **Handover docs** | ✅ Generated | ❌ | ❌ | ❌ | ✅ RTM handover |

---

## 🔗 Repository Dependencies

```
DOCX_RTM_Automation (SoR, RTM, contract specs)
    │
    ├──→ CODEX (reusable engineering libraries, MCB blocks)
    │       │
    │       └──→ cryo_leak_rate_dashboard (v4.0.0 production application)
    │                    ▲
    │                    │
    └──→ ABACUS (CodeLLM analysis, Jupyter notebooks, warm compressor studies)
    │
    └──→ document-organization-system (presentation hub, v3 legacy, GitHub Pages)
```

### Cross-Repo References

| From | To | Reference Type |
|------|----|----------------|
| cryo_leak_rate_dashboard | DOCX_RTM_Automation | RTM-047..067 traceability IDs |
| cryo_leak_rate_dashboard | CODEX | calc_leak_rate module origin |
| ABACUS | cryo_leak_rate_dashboard | Data inputs, config schemas |
| document-organization-system | cryo_leak_rate_dashboard | GitHub Pages v3→v4 migration |
| cryo_leak_rate_dashboard | Cryoworld offer docs | Valve spec source (image references) |
| cryo_leak_rate_dashboard | QPS Contract | Contract requirement source |

---

## 🏷️ Naming & Tagging Convention

### Branch Names
- `main` — production/stable
- `feature/<ticket>-<short-desc>` — feature work
- `fix/<ticket>-<short-desc>` — bug fixes
- `release/v<major>.<minor>.<patch>` — release branches

### Tag Format
- `v4.0.0` — semantic version
- `v4.0.0-rc1` — release candidate

### Commit Prefix Convention
```
feat:    New feature
fix:     Bug fix
docs:    Documentation only
chore:   Build, CI, tooling
refactor: Code restructure
test:    Adding/fixing tests
release: Version bump + tag
```

---

## 🗂️ Files Currently in Uploads (Not Yet Organized)

These uploaded files should be distributed across repos:

| File | Target Repo | Folder |
|------|-------------|--------|
| `SoR_Requirements_Matrix.csv` | DOCX_RTM_Automation | `requirements/` |
| `QPLANT_HV02 exhaust for KAEZER (1).docx` | DOCX_RTM_Automation | `specifications/` |
| `QPLANT_Helium Recovery and Supply MAC - CR1299.docx` | DOCX_RTM_Automation | `specifications/` |
| `QPLANT_Interface and Terminal Points_ACC NF.docx` | DOCX_RTM_Automation | `specifications/` |
| `Technical Addendum_Reliability centred...docx` | DOCX_RTM_Automation | `addenda/` |
| `Addendum II - Cryoplant Technical Requirements.docx` | DOCX_RTM_Automation | `addenda/` |
| `Addendum II - Cryoplant Technical Requirements1212_1521.docx` | DOCX_RTM_Automation | `addenda/` |
| `QPS_Contract_pdf.pdf` | DOCX_RTM_Automation | `contracts/` |
| `QPS_Contract_mirror_DOCX.pdf` | DOCX_RTM_Automation | `contracts/` |
| `QPS (Addendum II)_Master.docx` | DOCX_RTM_Automation | `addenda/` |
| `Cryoworld offer 1.pptx` | ABACUS or DOCX_RTM_Automation | `vendor_offers/` |
| `MYRRHA warm-compressor comparison A.md` | ABACUS | `analyses/` |
| `HUMAN.index.html` | document-organization-system | `legacy/` |
| `SLIDE_PACKAGES_STATUS.md` | cryo_leak_rate_dashboard | root (already there) |
| `cryo_leak_rate_dashboard.zip` | N/A (archive of this repo) | — |

---

## 📊 Repository Health Metrics

| Metric | cryo_dashboard | CODEX | ABACUS | doc-org-system | DOCX_RTM |
|--------|---------------|-------|--------|----------------|----------|
| Has remote? | ❌ **NO** | ✅ | ✅ | ✅ | ✅ |
| CI/CD? | ✅ (3 workflows) | TBD | TBD | ✅ (Pages) | TBD |
| Tests? | ✅ (18 pass) | TBD | TBD | ❌ | TBD |
| README? | ✅ | TBD | TBD | TBD | TBD |
| GH Pages? | ✅ (configured) | N/A | N/A | ✅ Active | N/A |
| Latest version | v4.0.0 | — | — | — | — |
| Open PRs | N/A (no remote) | ? | ? | ? | ? |

---

## 🔒 Access & Permissions

- All repos under personal account `GBOGEB`
- Abacus AI Agent has push access via [GitHub App](https://github.com/apps/abacusai/installations/select_target)
- Repos are **public** (CODEX, ABACUS, document-organization-system confirmed public)
- Consider making contract docs repo **private** (QPS contract sensitivity)

---

## 📝 Decision Log

| Decision | Rationale | Date |
|----------|-----------|------|
| Multi-repo over monorepo | Clear separation: app vs libs vs docs vs analysis | 2026-05-18 |
| cryo_leak_rate_dashboard as standalone | Self-contained deployable with GitHub Pages | 2026-05-18 |
| DOCX_RTM_Automation for all contract docs | Already contains SoR/RTM pipeline; natural home | 2026-05-18 |
| ABACUS for analysis notebooks | Already 82 MB with CodeLLM artifacts; right fit | 2026-05-18 |
| CODEX for reusable libraries | MCB blocks architecture already established | 2026-05-18 |
