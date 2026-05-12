# MYRRHA QPLANT Cryogenic Leak Rate Dashboard — Handover Package

> **Version:** 4.0.0 &nbsp;|&nbsp; **Codename:** Critical Correction — 3× FSD575, SSoT Configuration  
> **Date:** 2026-05-10 &nbsp;|&nbsp; **Branch:** `main` &nbsp;|&nbsp; **Commit:** `ff01ec8`

---

## 1 — Project Overview

This repository packages the **MYRRHA QPLANT cryogenic helium leak-rate engineering analysis** into an idempotent, self-documenting handover system. It combines:

- **Requirements traceability** (RTM-047/048/067, EN 13185, PED 2014/68/EU)
- **Deterministic build workflows** (`setup.sh → build.sh → validate.sh → package.sh`)
- **Machine-readable state** (`docs/manifest.json`, `VERSION.json`, `OUTPUT_MANIFEST.json`)
- **Human-readable navigation** (40-slide master navigator, stakeholder presentation, Plotly dashboards)

### v4.0.0 Key Changes

| Area | Change | Impact |
|------|--------|--------|
| HP Compressors | Count corrected 4 → **3** (Kaeser FSD 575 SFC) | CAPEX −€200k |
| Motor power | 400 kW generic → **315 kW** (ALaT vendor data) | Energy models corrected |
| HP outlet pressure | 12 barg → **14 barg nominal** | Pressure maps updated |
| HCC inlet | 1000 mbar → **1050 mbar** | Air-ingress prevention |
| VLP suction | Fixed 300 → **400 mbar nominal** (VFD 250–550) | Monte Carlo ranges updated |
| SSoT | New `data/config.yaml` + `config_loader.py` | No hardcoded values |
| Financial model | CAPEX €1.42M, ROI 1.2 yr, NPV €15.1M, IRR 83% | All slides updated |

---

## 2 — Directory Structure

```
cryo_leak_rate_dashboard/
├── assets/                  # Shared CSS & JS for HTML pages
│   ├── style.css            # Dashboard styling (responsive + print)
│   └── triage.js            # Interactive controls (mode switch, expand/collapse)
├── data/                    # SSoT configuration and engineering data
│   ├── config.yaml          # ★ Single Source of Truth (human-editable)
│   ├── config.json          # Auto-generated machine-readable SSoT
│   ├── config.md            # Auto-generated parameter tables
│   ├── compressor_specs.json
│   ├── helium_properties.json
│   ├── leak_classes.json
│   ├── scenarios.json
│   ├── valve_candidates.json
│   ├── source_anchors.json
│   ├── standards_compliance.json
│   ├── material_costs.json
│   ├── meca_inox_specs.json
│   ├── operating_conditions.json
│   └── swagelok_specs.json
├── docs/                    # Generated documentation & visualizations
│   ├── index.html           # Landing page (phase cards, status pills)
│   ├── index_v4_0.html      # 40-slide master navigator (v4.0.0)
│   ├── STAKEHOLDER_PRESENTATION.html  # 40-slide stakeholder deck
│   ├── manifest.json        # Build state, file hashes, dependencies
│   ├── backlog.json         # Tracked backlog items
│   ├── changelog.md         # Human-readable changelog
│   ├── dashboard.html       # Interactive Plotly dashboard
│   ├── calculations.html    # Calculation detail pages
│   ├── executive_summary.html
│   ├── rtm_traceability.html
│   ├── handover.html / .pdf # Formal handover document
│   ├── plots/               # 5 core Plotly plots (HTML)
│   ├── visualizations/      # 18 v3.0 charts + backing CSV data
│   ├── visualizations_v3/   # 22 v3.1 charts (Plotly interactive)
│   ├── compressors/         # HP redundancy & WCS.HP protection pages
│   ├── liquid_he/           # Liquid operations guide
│   ├── standards/           # Compliance matrix, FAT/SAT, PED
│   ├── statistical/         # Monte Carlo, PCA, sensitivity results
│   ├── tables/              # HTML data tables
│   ├── tables_v3/           # Extended CSV data tables
│   └── data_exports/        # Full conversion grids (CSV/JSON)
├── src/                     # Python source modules
│   ├── calc_leak_rate.py    # ★ Core physics engine (first-principles)
│   ├── config_loader.py     # SSoT config loader (dot-notation access)
│   ├── generate_dashboard.py # Main dashboard/plot generator
│   ├── build_all.py         # Orchestrator: dashboard + handover + manifest
│   ├── build_dashboard.py   # Landing page (index.html) generator
│   ├── build_handover.py    # Handover document generator
│   ├── manifest.py          # SHA256 hashing & idempotent writes
│   ├── compressor_reliability.py  # k-of-M availability, VFD savings
│   ├── liquid_he_loss.py    # Leak rate → liquid inventory loss
│   ├── wcs_scenarios.py     # WCS.HP protection logic
│   ├── generate_visuals_v3.py     # v3.1 visualization generator
│   ├── generate_standards_stats.py # Standards & statistics
│   ├── materials_db.py      # Material properties database
│   ├── monte_carlo.py       # Monte Carlo simulation engine
│   ├── risk_model.py        # Risk assessment model
│   └── verify_triage.py     # Triage compliance checker
├── tests/                   # pytest test suite (22 tests)
│   ├── test_engineering.py  # Core physics validation
│   ├── test_calculations.py # Calculation integration tests
│   ├── test_config_loader.py # SSoT validation tests
│   ├── test_data_integrity.py # Data file consistency
│   ├── test_build_outputs.py  # Build output checks
│   ├── test_outputs.py      # Output file validation
│   └── conftest.py          # Shared fixtures
├── outputs/                 # Generated calculation outputs
│   ├── tables/              # CSV/JSON calculation results
│   ├── plots/               # Generated plot files
│   └── ...                  # Other versioned outputs
├── tables/                  # Static reference tables (CSV + MD)
├── traceability/            # RTM traceability matrix CSV
├── source/                  # Markdown source for handover docs
├── dist/                    # Packaged distribution
│   ├── handover.zip         # Complete handover bundle (~2.7 MB)
│   ├── test-report.html     # HTML test report
│   ├── test-results.json    # Machine-readable test results
│   └── junit.xml            # JUnit XML test results
├── setup.sh                 # Environment setup (venv + deps)
├── build.sh                 # Full build pipeline
├── validate.sh              # Test + verify pipeline
├── package.sh               # Create dist/handover.zip
├── Makefile                 # Make targets for above scripts
├── VERSION                  # Plain text version: 4.0.0
├── VERSION.json             # Structured version metadata
├── CHANGELOG.md             # Full changelog (all versions)
├── README.md                # Project README
├── requirements.txt         # Python dependencies (pinned)
└── .github/workflows/       # CI/CD pipeline
    └── build.yml
```

---

## 3 — Core Artifacts by Topic

### 3.1 Configuration (SSoT)

| File | Purpose |
|------|---------|
| `data/config.yaml` | Human-editable master configuration |
| `data/config.json` | Machine-readable export (auto-generated) |
| `data/config.md` | Documentation tables (auto-generated) |
| `src/config_loader.py` | Python loader with dot-notation access |

### 3.2 Engineering Modules

| File | Purpose |
|------|---------|
| `src/calc_leak_rate.py` | Core physics: mbar·L/s → mass flow (first-principles) |
| `src/compressor_reliability.py` | k-of-M availability, VFD energy savings |
| `src/liquid_he_loss.py` | Leak rate → liquid He inventory loss |
| `src/wcs_scenarios.py` | WCS.HP supply protection & interlocks |
| `src/monte_carlo.py` | Monte Carlo simulation engine |
| `src/risk_model.py` | Risk assessment model |
| `src/materials_db.py` | Material properties database |

### 3.3 Visualizations

| Location | Count | Description |
|----------|-------|-------------|
| `docs/plots/` | 5 | Core Plotly plots (leak vs loss, temp, cost, fleet, reliability) |
| `docs/visualizations/` | 18 | v3.0 material/supplier charts with CSV data |
| `docs/visualizations_v3/` | 22 | v3.1 extended charts (Monte Carlo, PCA, compressor, liquid He) |

### 3.4 Documentation

| File | Description |
|------|-------------|
| `docs/STAKEHOLDER_PRESENTATION.html` | 40-slide stakeholder deck |
| `docs/index_v4_0.html` | 40-slide master navigator (v4.0.0) |
| `docs/handover.html` / `.pdf` | Formal handover document |
| `docs/HANDOVER_AGENT.md` / `.docx` / `.pdf` | Agent-specific handover |
| `docs/compressors/*.html` | HP redundancy & WCS.HP protection |
| `docs/liquid_he/*.html` | Liquid He operations guide |
| `docs/standards/*.md` / `.csv` / `.json` | Compliance matrix, FAT/SAT, PED |

### 3.5 Testing

| File | Tests | Status |
|------|-------|--------|
| `tests/test_engineering.py` | 5 | ✅ Pass |
| `tests/test_calculations.py` | varies | ✅ Pass |
| `tests/test_config_loader.py` | varies | ✅ Pass |
| `tests/test_data_integrity.py` | varies | ✅ Pass |
| `tests/test_build_outputs.py` | varies | ✅ Pass |
| `tests/test_outputs.py` | varies | ✅ Pass |
| **Total** | **22** | **✅ All pass** |

### 3.6 Build & CI

| File | Purpose |
|------|---------|
| `setup.sh` | Create venv, install deps, initial build |
| `build.sh` | Full rebuild (dashboard + handover + manifest) |
| `validate.sh` | Run tests + verify outputs |
| `package.sh` | Create `dist/handover.zip` |
| `Makefile` | Make targets for all scripts |
| `.github/workflows/build.yml` | GitHub Actions CI pipeline |

---

## 4 — Version Control Status

| Property | Value |
|----------|-------|
| **Branch** | `main` |
| **Commit** | `ff01ec8` |
| **Tag** | v4.0.0 |
| **Build status** | verified |
| **Build timestamp** | 2026-05-12T09:23:12 UTC |
| **Python** | 3.11.6 |
| **Key deps** | numpy 1.26.4, pandas 2.2.3, plotly 5.24.1, scipy 1.14.1 |

### Changelog Summary (v4.0.0)

- **BREAKING:** HP compressor count corrected 4 → 3 (Kaeser FSD575 SFC)
- **BREAKING:** Financial model updated (CAPEX €1.42M, ROI 1.2 yr)
- **Added:** Single Source of Truth (`data/config.yaml` + `config_loader.py`)
- **Changed:** All pressure parameters corrected from vendor/contractor data
- **Changed:** Monte Carlo distributions updated (VLP, LP ranges)
- **Fixed:** FSD575 power specs, energy consumption, cost models
- **Validated:** 22/22 tests passing, all outputs verified

---

## 5 — Quick Start for New Agents

### Step 1: Read state files
```bash
cat VERSION                    # → 4.0.0
cat docs/manifest.json         # Build state, file hashes
cat docs/backlog.json          # Open items
cat CHANGELOG.md               # Version history
```

### Step 2: Setup environment
```bash
./setup.sh                     # Creates venv, installs deps, runs initial build
```

### Step 3: Validate
```bash
./validate.sh                  # Runs 22 tests, checks outputs
```

### Step 4: Build (if needed)
```bash
./build.sh                     # Full rebuild of all artifacts
```

### Step 5: Package (for distribution)
```bash
./package.sh                   # Creates dist/handover.zip
```

### Key files to read first
1. `data/config.yaml` — All engineering parameters (SSoT)
2. `src/calc_leak_rate.py` — Core physics engine
3. `docs/manifest.json` — Current build state
4. `CHANGELOG.md` — What changed and why

---

## 6 — Idempotent Rebuild Instructions

The entire project can be rebuilt from source files:

```bash
# 1. Fresh setup
./setup.sh

# 2. Full build (generates all HTML, plots, tables, manifests)
./build.sh

# 3. Run tests and verify outputs
./validate.sh

# 4. Package for distribution
./package.sh
```

**Idempotency guarantee:** Running `build.sh` multiple times produces identical outputs. File writes only occur when content has changed (SHA256-based).

### Source files (inputs to build)
- `data/*.json`, `data/*.yaml` — Engineering data
- `src/*.py` — Calculation and generation modules
- `assets/style.css`, `assets/triage.js` — Web assets
- `VERSION`, `VERSION.json` — Version metadata

### Generated files (outputs of build)
- `docs/*.html` — All HTML pages
- `docs/plots/`, `docs/visualizations*/` — All charts
- `docs/manifest.json` — Build manifest
- `outputs/` — Calculation results
- `dist/` — Distribution package

---

## 7 — Companion Files

| File | Purpose |
|------|---------|
| `ARTIFACTS.yaml` | Machine-readable catalog of all deliverables |
| `DOWNLOAD_CHECKLIST.md` | What to download for full handover |
| `REBUILD_GUIDE.md` | Detailed rebuild instructions with troubleshooting |

---

*Generated: 2026-05-12 | Project: MYRRHA QPLANT Cryogenic Leak Rate Dashboard v4.0.0*
