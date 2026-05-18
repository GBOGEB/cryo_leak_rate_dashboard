# HTML Deliverables Organization Plan

> **Generated:** 2026-05-18  
> **Project:** MYRRHA QPLANT Cryogenic Engineering Ecosystem  
> **Scope:** All HTML deliverables across v3 (material properties) and v4 (leak rate analysis)

---

## 1 — Current HTML Inventory

### 1.1 v4.0.0 — Leak Rate Analysis Dashboard (`cryo_leak_rate_dashboard`)

**Location:** `/home/ubuntu/cryo_leak_rate_dashboard/docs/`  
**Remote:** ⚠️ No GitHub remote yet — needs `cryo_leak_rate_dashboard` repo creation  
**Total HTML files:** 84

#### Canonical Presentations (3)
| File | Slides | Audience | Status |
|------|--------|----------|--------|
| `index_v4_0.html` | 42 | Technical master navigator | ✅ v4.0.0 canonical |
| `STAKEHOLDER_PRESENTATION.html` | 10 | Executive / decision-makers | ✅ v4.0.0 aligned |
| `NAVIGATOR.html` | — | Main entry point (card-based) | ✅ v4.0.0 aligned |

#### Triage Dashboard Pages (7)
| File | Purpose | Status |
|------|---------|--------|
| `index.html` | Landing / handover hub | 🔄 Auto-generated |
| `dashboard.html` | Engineer triage view | 🔄 Auto-generated |
| `executive_summary.html` | Executive triage view | 🔄 Auto-generated |
| `calculations.html` | Detailed calculations | 🔄 Auto-generated |
| `rtm_traceability.html` | RTM traceability matrix | 🔄 Auto-generated |
| `handover.html` | Formal handover document | 🔄 Auto-generated |
| `triage_compliance.html` | Standards compliance grid | 🔄 Auto-generated |

#### Visualizations — `docs/visualizations/` (27 files)
- 18 × chartNN series (leak vs loss, temp sensitivity, pressure, valve size, seal materials, suppliers, cost, radiation, welding, warm/cold service, guard systems, Monte Carlo, sensitivity, lifecycle TCO, valve replacement)
- 9 × legacy charts (cost waterfall, enhanced leak rate, helium sankey, maintenance gantt, Monte Carlo cost, risk heatmap, scenario comparison, sensitivity tornado, supplier comparison)

#### Visualizations — `docs/visualizations_v3/` (22 files)
- 16 × v3.0 advanced analytics (extended leak vs loss, temp effect, choked flow, purity dilution, internal/external, helium properties, compressibility, lifecycle standards, fleet sensitivity, MC histogram/scatter, cost breakdown box, scree, biplot, correlation heatmap)
- 6 × v3.1 additions (liquid inventory depletion, compressor availability, boiloff vs leakrate, WCS HP architecture, redundancy cost benefit, VFD energy savings)

#### Plots — `docs/plots/` (5 files)
- Core triage plots: leak vs loss, temp/pressure effects, cost vs leaktightness, fleet sensitivity, reliability

#### Hero Pages — `docs/heroes/` (10 files)
- executive, technical, compliance, design, risk, materials, operations, control, cost, interface

#### Topic-Specific Pages (3)
- `compressors/HP_Redundancy_Analysis.html`
- `compressors/WCS_HP_Protection.html`
- `liquid_he/Liquid_Operations_Guide.html`

#### Tables — `docs/tables/` (4 files)
- supplier comparison, helium loss by valve count, material costs, operating conditions

#### Archive — `docs/archive/` (3 files)
- `index_v3_0_0_ARCHIVE.html` — v3.0 navigator (archived)
- `index_v3_1_0_ARCHIVE.html` — v3.1 navigator (archived)
- `presentation_v2_5_0_ARCHIVE.html` — v2.5 presentation (archived)

---

### 1.2 v3 (v0.4.9) — Material Properties Dashboard (`document-organization-system`)

**Location:** `cryo_dashboard_v0_3_0/cryo_dashboard_v0_3_0/` within `document-organization-system`  
**Remote:** [github.com/GBOGEB/document-organization-system](https://github.com/GBOGEB/document-organization-system)  
**GitHub Pages:** [Live](https://gbogeb.github.io/document-organization-system/cryo_dashboard_v0_3_0/cryo_dashboard_v0_3_0/)  
**Total HTML files:** 7

| File | Purpose | Status |
|------|---------|--------|
| `index.html` | Landing page | ✅ Active |
| `dashboard_modular.html` | Primary interactive dashboard | ✅ Active (v0.4.9) |
| `material_properties_dashboard_v1_10.html` | Legacy self-contained fallback | ✅ Active |
| `files.html` | File navigator | ✅ Active |
| `html_preview_hub.html` | Preview hub | ✅ Active |
| `ssot_launcher.html` | SSOT launcher | ✅ Active |
| `index_slides.html` | Presentation slides | ✅ Active |

#### Additional HTML in doc-org-system
- `docs/analysis/charts/` — 7 performance analysis charts (cache hit rates, complexity, errors, performance, pipeline, processing time, resource utilization)
- `Automation/Metadata_diffs_log_reviewable.html` — Metadata diff viewer

---

## 2 — Repository Assignment Strategy

### ✅ Recommended: Option C — Separate Repos with Cross-Links + GitHub Pages

```
┌─────────────────────────────────────────────────────────────────────┐
│                  GitHub Pages Deployment Map                        │
│                                                                     │
│  gbogeb.github.io/cryo_leak_rate_dashboard/                        │
│  ├── index.html ──────────→ VERSION_SELECTOR.html                  │
│  ├── v4/ ─────────────────→ v4.0.0 Leak Rate Dashboard             │
│  │   ├── NAVIGATOR.html                                            │
│  │   ├── index_v4_0.html (42 slides)                               │
│  │   ├── STAKEHOLDER_PRESENTATION.html (10 slides)                 │
│  │   ├── visualizations/ (27 charts)                               │
│  │   ├── visualizations_v3/ (22 charts)                            │
│  │   ├── plots/ (5 core plots)                                     │
│  │   ├── heroes/ (10 audience pages)                               │
│  │   ├── compressors/ (2 analysis pages)                           │
│  │   ├── liquid_he/ (1 operations guide)                           │
│  │   ├── tables/ (4 data tables)                                   │
│  │   └── archive/ (3 prior versions)                               │
│  └── material-properties/ ──→ Link to v3 dashboard                 │
│                                                                     │
│  gbogeb.github.io/document-organization-system/                     │
│  └── cryo_dashboard_v0_3_0/cryo_dashboard_v0_3_0/                  │
│      ├── index.html (landing)                                       │
│      ├── dashboard_modular.html (interactive)                       │
│      ├── index_slides.html (presentation)                           │
│      └── ... (7 HTML total)                                        │
└─────────────────────────────────────────────────────────────────────┘
```

#### Why Option C?

| Factor | Evaluation |
|--------|------------|
| **Independence** | ✅ v3 evolves independently (already at v0.4.9 with 23 PRs) |
| **Scope clarity** | ✅ v3 = material properties, v4 = leak rates — different domains |
| **GitHub Pages** | ✅ Each repo gets its own Pages site |
| **Cross-references** | ✅ VERSION_SELECTOR.html links both |
| **No breakage** | ✅ v3 URLs remain stable, v4 gets new clean URLs |
| **Team workflow** | ✅ Engineers can work on either without conflicts |

#### Why NOT submodules?

- v3 is NOT a dependency of v4 — it's a separate engineering tool
- Submodule complexity is not justified for a cross-link relationship
- Both repos update independently at different cadences

---

## 3 — Deployment Plan

### Step 1: Create `cryo_leak_rate_dashboard` repo on GitHub
```bash
# User must create the repo on github.com/GBOGEB
# Then add remote and push
cd /home/ubuntu/cryo_leak_rate_dashboard
git remote add origin https://github.com/GBOGEB/cryo_leak_rate_dashboard.git
git push -u origin main
```

### Step 2: Restructure docs/ for GitHub Pages
```
docs/
├── index.html                     # VERSION_SELECTOR (new root landing)
├── v4/                            # All v4 content (moved from docs/)
│   ├── NAVIGATOR.html
│   ├── index_v4_0.html
│   ├── STAKEHOLDER_PRESENTATION.html
│   ├── dashboard.html
│   ├── calculations.html
│   ├── executive_summary.html
│   ├── rtm_traceability.html
│   ├── handover.html
│   ├── triage_compliance.html
│   ├── visualizations/
│   ├── visualizations_v3/
│   ├── plots/
│   ├── heroes/
│   ├── compressors/
│   ├── liquid_he/
│   ├── tables/
│   ├── archive/
│   └── assets/
└── material-properties/           # Redirect page → v3 GitHub Pages
```

### Step 3: Enable GitHub Pages
```
Repository Settings → Pages
Source: Deploy from branch
Branch: main
Folder: /docs
```

### Step 4: Cross-Link v3 ↔ v4
- v4 VERSION_SELECTOR.html links to v3 GitHub Pages
- v3 index.html or ssot_launcher.html can link back to v4

---

## 4 — URL Structure After Deployment

### v4 Leak Rate Dashboard
| URL | Content |
|-----|---------|
| `gbogeb.github.io/cryo_leak_rate_dashboard/` | Version selector (landing) |
| `gbogeb.github.io/cryo_leak_rate_dashboard/v4/NAVIGATOR.html` | Main entry point |
| `gbogeb.github.io/cryo_leak_rate_dashboard/v4/index_v4_0.html` | 42-slide navigator |
| `gbogeb.github.io/cryo_leak_rate_dashboard/v4/STAKEHOLDER_PRESENTATION.html` | Executive 10-slide deck |

### v3 Material Properties Dashboard (existing — no changes)
| URL | Content |
|-----|---------|
| `gbogeb.github.io/document-organization-system/.../index.html` | v3 Landing |
| `gbogeb.github.io/document-organization-system/.../dashboard_modular.html` | Interactive dashboard |
| `gbogeb.github.io/document-organization-system/.../index_slides.html` | Presentation |

---

## 5 — Migration Considerations

### Files NOT to move
- `docs/presentation.html` — legacy v2.5 (stays in archive)
- `docs/presentation.pdf` — static PDF (stays as-is)
- `outputs/html/` — build artifacts (not for GitHub Pages)
- `htmlcov/` — test coverage (dev-only)

### Build system updates needed
- `src/build_dashboard.py` → update output paths to `docs/v4/`
- `src/generate_dashboard.py` → update `DOCS_DIR` to `docs/v4/`
- `src/build_all.py` → update asset copy paths
- `setup.sh`, `build.sh`, `validate.sh` → update references

### Risk: Breaking relative paths
- All `../assets/style.css` references in HTML need audit
- Plot iframe `src` paths need update
- Hero page cross-links need update
- **Mitigation:** Run link checker after migration

---

## 6 — Summary

| Item | Count | Location |
|------|-------|----------|
| **v4 HTML files** | 84 | `cryo_leak_rate_dashboard/docs/` |
| **v3 HTML files** | 7 + 8 | `document-organization-system/cryo_dashboard_v0_3_0/` |
| **Total HTML deliverables** | 99 | Across 2 repos |
| **Repos involved** | 2 | Separate, cross-linked |
| **GitHub Pages sites** | 2 | Independent deployment |
