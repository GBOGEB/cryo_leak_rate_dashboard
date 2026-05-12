# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [4.0.0] - 2026-05-10

### ⚠ BREAKING CHANGES
- HP compressor count corrected from 4 to **3** (Kaeser FSD 575 SFC)
- HP outlet pressure corrected from 10 barg to **14 barg**
- HCC inlet pressure corrected from "~1 bar" to **1050 mbar**
- VLP nominal pressure set to **400 mbar** (was implicit)

### Added
- **Single Source of Truth (SSoT):** `data/config.yaml`, `data/config.json`, `data/config.md`
- Config loader module (`src/config_loader.py`) with dot-notation access
- `docs/index_v4_0.html` — Phase 4 dashboard landing page
- Comprehensive v4.0.0 entry in root `CHANGELOG.md` and `VERSION.json`

### Changed
- `src/compressor_reliability.py` — fully rewritten: 3-unit fleet, 348.54 kW package power (ALaT vendor sheet), new CONFIGS dict (N3_baseline, N1_FSD575_VFD 2-of-3, N1_HSD_twin)
- `src/wcs_scenarios.py` — fully rewritten: HP_OUTLET_BARG=14, HCC_INLET_MBAR=1050, VLP_NOMINAL_MBAR=400, interlock setpoints from SSoT
- `data/compressor_specs.json` — corrected: 315 kW motor, 112.54 g/s per unit, 3-skid max 337.62 g/s
- `src/build_v3_1.py` — updated version strings, chart titles, VFD power reference
- `src/build_dashboard.py` — default version 4.0.0, phase cards link to index_v4_0.html
- `docs/STAKEHOLDER_PRESENTATION.html` — all 10 slides corrected (€600k compressors, €1.42M CAPEX, €1,185k savings, 1.2yr payback, €15.1M NPV, 83% IRR)
- All 6 v3.1 Plotly visualizations regenerated with corrected data
- Financial model: 3 × €200k = €600k compressors (was 4 × €180k = €720k)

### Fixed
- Compressor count propagated consistently across all modules, charts, and documentation
- Pressure parameters now traceable to ALaT vendor datasheet
- Residual "4 ×" references removed from all HTML pages

## [3.1.0] - 2026-05-09

### Added
- Liquid helium properties database (4K-300K, 1-12 bar)
- Leak rate to liquid inventory loss conversion tooling
- HP compressor redundancy analysis (N=3, N+1 FSD575, N+1 HSD)
- VFD energy savings modeling based on affinity laws
- WCS.HP supply protection logic (70/20/10 leak budget)
- 6 new Plotly visualizations for operations/reliability/cost
- Compressor specification tables (FSD575 vs HSD Twin Combi)
- Idempotent setup/build/validate/package scripts for handover automation
- Machine-readable state files (`docs/manifest.json`, `docs/backlog.json`)

### Changed
- Corrected liquid He mass-flow conversion chain
- Updated master slide navigator to 40 slides
- Expanded helium properties with liquid-phase references

### Fixed
- Unit conversion error in `src/liquid_he_loss.py` (legacy 1000x issue removed)

## [3.0.0] - 2026-05-08

### Added
- Standards compliance framework (8 international codes)
- RTM traceability matrix and FAT/SAT procedures
- PED 2014/68/EU compliance workflow
- Monte Carlo simulation (10,000 runs, covariance)
- PCA analysis, sensitivity analysis, and correlation matrix outputs
- 15+ interactive Plotly charts for engineering/statistical review
- 32-slide (later extended) presentation navigator
