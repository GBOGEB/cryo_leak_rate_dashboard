# V3 Discovery Report

> **Generated:** 2026-05-18  
> **Inspector:** Abacus AI Agent  
> **Scope:** Locate and analyze the "v3" cryogenic dashboard repository

---

## 1 — Repository Location

| Property | Value |
|----------|-------|
| **GitHub URL** | [GBOGEB/document-organization-system](https://github.com/GBOGEB/document-organization-system) |
| **Branch** | `main` |
| **v3 Subfolder** | `cryo_dashboard_v0_3_0/cryo_dashboard_v0_3_0/` |
| **GitHub Pages** | [Live Dashboard](https://gbogeb.github.io/document-organization-system/cryo_dashboard_v0_3_0/cryo_dashboard_v0_3_0/) |
| **Status** | ✅ **ACTIVE** — not archived, actively developed |
| **Size** | 594 KB (GitHub-reported) |
| **Latest Commit** | `6f08258` — Merge PR #23 (NIST parity tests + deployment checklist) |
| **Latest PR** | PR #23 — `feature/nist-parity-tests-and-deployment-checklist` |

---

## 2 — What Is v3?

**Official Name:** Cryogenic Material Property Dashboard  
**Version:** v0.4.9  
**Organization:** SCK CEN  
**Purpose:** Engineering tool for evaluating cryogenic material-property behaviour (1–300 K)

### v3 is NOT the same as v4

| Aspect | v3 (document-organization-system) | v4 (cryo_leak_rate_dashboard) |
|--------|-----------------------------------|-------------------------------|
| **Focus** | Material properties (k, cp, thermal contraction) | Helium leak rate analysis |
| **Materials** | 10 materials (AISI316, Al6061, G-10, Cu RRR variants, Ti-6Al-4V) | Helium gas (ideal gas law) |
| **Engine** | JavaScript (browser-side computation) | Python (build-time computation) |
| **Runtime** | Live interactive dashboard (Plotly.js) | Static HTML + embedded Plotly |
| **Data Source** | NIST Monograph 177 coefficients | Contract specs, valve catalogs |
| **Integration** | Trapezoid, Simpson, Romberg, Gauss-Legendre | Ideal gas conversions |
| **Panels** | 12 interactive panels | 5 triage pages + 84 HTML files |
| **Version** | v0.4.9 | v4.0.0 |

### They are **complementary** — v3 provides material property data that v4's cryogenic system design depends on.

---

## 3 — v3 File Structure

```
document-organization-system/
├── .github/workflows/          # CI/CD
├── .nojekyll                   # GitHub Pages config
├── Automation/
│   ├── Scripts/
│   └── Metadata_diffs_log_reviewable.html
├── cryo_dashboard_v0_3_0/
│   └── cryo_dashboard_v0_3_0/          ◄── THE v3 DASHBOARD
│       ├── index.html                   # Landing page
│       ├── dashboard_modular.html       # Primary runtime (modular)
│       ├── material_properties_dashboard_v1_10.html  # Legacy fallback
│       ├── files.html                   # File navigator
│       ├── html_preview_hub.html        # Preview hub
│       ├── ssot_launcher.html           # SSOT launcher
│       ├── index_slides.html            # Presentation slides
│       ├── style.css                    # Styling
│       ├── js/
│       │   ├── app.js                   # Legacy app
│       │   ├── app_modular.js           # Main orchestration (84 KB)
│       │   ├── materials.js             # Material database + evaluators
│       │   ├── numerics.js              # Integration methods
│       │   ├── plots.js                 # Plotly rendering
│       │   ├── export.js                # CSV/JSON/PNG export
│       │   ├── state.js                 # State management
│       │   ├── logger.js                # Logging
│       │   └── debug.js                 # Debug panel
│       ├── data/
│       │   └── materials.json           # Material property database
│       ├── schemas/
│       │   └── materials.schema.json    # JSON Schema
│       ├── tests/
│       │   ├── numerics.test.js
│       │   ├── export.test.js
│       │   ├── materials.validate.js
│       │   ├── file_index_integrity.test.js
│       │   ├── static_entrypoints.test.js
│       │   └── nist_parity.test.js      # 823 assertions
│       ├── docs/
│       │   ├── CHANGELOG.md
│       │   ├── ENGINEERING_HANDOVER.md
│       │   ├── GITHUB_PAGES_DEPLOYMENT_CHECKLIST.md
│       │   ├── NIST_PARITY_TEST_REPORT_v0.4.9.md
│       │   └── rtm/FEATURE_TEST_FILE_RTM_v0.4.9.md
│       ├── ssot.json                    # Single Source of Truth
│       ├── file_index.json              # File index
│       ├── file_index.yaml              # File index (YAML)
│       ├── visual_key.yaml              # Visual key
│       ├── VERSION                      # "v0.4.9"
│       └── package.json                 # npm config
├── docs/analysis/charts/                # Performance analysis charts (7 HTML)
├── performance_optimizations/           # Cache/async/zip optimizations
├── tests/                               # Top-level tests
├── README.md
└── setup_organization.py                # Organization automation
```

---

## 4 — v3 HTML Entry Points

| Entry Point | File | GitHub Pages URL |
|-------------|------|------------------|
| **Landing** | `index.html` | [Open](https://gbogeb.github.io/document-organization-system/cryo_dashboard_v0_3_0/cryo_dashboard_v0_3_0/index.html) |
| **Modular Dashboard** | `dashboard_modular.html` | [Open](https://gbogeb.github.io/document-organization-system/cryo_dashboard_v0_3_0/cryo_dashboard_v0_3_0/dashboard_modular.html) |
| **Legacy Dashboard** | `material_properties_dashboard_v1_10.html` | [Open](https://gbogeb.github.io/document-organization-system/cryo_dashboard_v0_3_0/cryo_dashboard_v0_3_0/material_properties_dashboard_v1_10.html) |
| **File Browser** | `files.html` | [Open](https://gbogeb.github.io/document-organization-system/cryo_dashboard_v0_3_0/cryo_dashboard_v0_3_0/files.html) |
| **Preview Hub** | `html_preview_hub.html` | [Open](https://gbogeb.github.io/document-organization-system/cryo_dashboard_v0_3_0/cryo_dashboard_v0_3_0/html_preview_hub.html) |
| **SSOT Launcher** | `ssot_launcher.html` | [Open](https://gbogeb.github.io/document-organization-system/cryo_dashboard_v0_3_0/cryo_dashboard_v0_3_0/ssot_launcher.html) |
| **Slides** | `index_slides.html` | [Open](https://gbogeb.github.io/document-organization-system/cryo_dashboard_v0_3_0/cryo_dashboard_v0_3_0/index_slides.html) |

---

## 5 — v3 Version Lineage

| Version | Date | Milestone |
|---------|------|-----------|
| v0.1.0 | 2026-03 | Tabbed dashboard prototype |
| v0.2.0 | 2026-03 | 14 engineering improvements in single file |
| v0.3.0 | 2026-04 | Modular production-style rebuild |
| v0.4.1 | 2026-05 | Integration method comparison panel |
| v0.4.2 | 2026-05 | Gauss-Legendre 4-point method |
| v0.4.3 | 2026-05 | Plot PNG export |
| v0.4.4 | 2026-05 | Result mode toggle |
| v0.4.5 | 2026-05 | Delta Summary panel + regression tests |
| v0.4.6 | 2026-05-04 | Thermal contraction, KPI strip, dual-axis, dark/light theme |
| v0.4.7 | 2026-05-05 | Comparison view modes, adaptive legend, cursor pins |
| v0.4.8 | 2026-05-05 | Maintenance release |
| **v0.4.9** | **2026-05-14** | **SSOT integration, slideshow presentation, launcher hub** |

---

## 6 — v3 Technical Capabilities

### Materials Database (10 materials)
- **Steels:** AISI 316
- **Aluminum:** Al 6061-T6
- **Composites:** G-10 CR Normal, G-10 CR Warp
- **Copper:** OFHC Cu RRR 50/100/150/300/500
- **Titanium:** Ti-6Al-4V

### Properties
- **k(T):** Thermal conductivity (W/m·K)
- **cp(T):** Specific heat (J/kg·K)  
- **Y(T):** Thermal contraction (×10⁻⁵)

### Integration Methods
- Composite Trapezoid (O(h²))
- Simpson's 1/3 Rule (O(h⁴))
- Romberg Integration (adaptive)
- Gauss-Legendre 4-point (O(h⁸))

### Engineering Formulas
- Conduction heat load: Qdot = (A/L) × ∫k(T)dT
- Cooldown energy: E = m × ∫cp(T)dT
- Thermal strain: ΔL = L_ref × [Y(T₂) − Y(T₁)] × 10⁻⁵
- Layered wall screening: R_total = Σᵢ (Lᵢ / (kᵢ × Aᵢ))

### Test Suite
- **823 NIST parity assertions** (nist_parity.test.js)
- Numerics regression tests
- Export consistency checks
- Material schema validation
- File index integrity
- Static entry point existence

---

## 7 — Key Finding

> **The v3 dashboard (document-organization-system) is a fully independent, actively maintained project.**  
> It is NOT a "previous version" of v4 — it is a **complementary tool** focusing on material properties rather than leak rates.  
> Both projects serve the MYRRHA QPLANT cryogenic engineering ecosystem and should remain as separate, cross-linked repositories.
