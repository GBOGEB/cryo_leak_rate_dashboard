# CHANGELOG

## 3.1.0 — Liquid Helium Operations & HP Compressor Redundancy (2026-05-08)
- Extended helium_properties.json with full liquid phase data (saturation curve, subcooled, critical point).
- New calculation module: src/liquid_he_loss.py — converts gas leak rates to liquid He inventory depletion.
- New calculation module: src/compressor_reliability.py — k-of-M parallel system availability, VFD energy savings.
- New calculation module: src/wcs_scenarios.py — WCS.HP supply protection, interlock logic, leak budget allocation.
- New data file: data/compressor_specs.json — FSD575 VFD and HSD Twin Combi specifications.
- 6 new interactive Plotly visualizations: liquid depletion, compressor availability, boil-off vs leak rate,
  WCS.HP architecture, redundancy cost-benefit, VFD energy savings.
- 3 new documentation pages: Liquid He Operations Guide, HP Redundancy Analysis, WCS.HP Protection.
- 40-slide master navigator (docs/index_v3_1.html) covering all v3.1 content.
- Build script: src/build_v3_1.py for deterministic v3.1 output generation.

## 3.0.0 — Standards & Statistical Framework (2026-05-08)
- Added standards compliance tables, PCA analysis, statistical framework.
- 16 new charts in visualizations_v3/ for advanced analysis.

## 2.5.0 — Visual Dashboard Enhanced (2026-05-08)
- 18 interactive Plotly charts with material-specific comparison.
- Monte Carlo cost simulation, sensitivity analysis, lifecycle TCO.
- Interactive calculator for real-time helium loss estimation.

## 2.0.0
- Fixed critical leak-rate conversion error (removed non-physical x1000 factor).
- Added first-principles dimensional proof and worked examples.
- Implemented multi-format triage package (HTML/MD/PDF/JSON).
- Added status badges, collapsible sections, mode switching, print CSS.
- Added deterministic build orchestration and output manifest hashing.
- Added unit and integration tests for math and output completeness.
