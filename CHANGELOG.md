# Changelog

All notable changes to the QPLANT Cryogenic Leak Rate Dashboard.

## [4.0.0] - 2026-05-10

### ⚠️ BREAKING CHANGES

**HP Compressor Configuration**
- **Count reduced from 4 to 3 units** (Kaeser FSD 575 SFC)
- Rationale: Design flow (350 g/s) achievable with 3 units
- Expected operational flow: 304 g/s
- WCS.HCC|WCS.HP maximum: 336 g/s (3-skid limit: 337.62 g/s)
- Redundancy maintained: N+1 where N=3 (2-of-3 active)

**Financial Impact of Correction**
- CAPEX reduction: €200k (3 vs 4 compressors)
- Compressor cost: €600k (was €800k)
- Total CAPEX: €1.42M (was €1.62M)
- Annual energy savings: Additional €224k/year
- **New ROI: 1.2-year payback** (was 1.7 years)
- **New NPV: €15.1M @ 5%** (was €13.9M)
- **New IRR: 83%** (was 58%)

### Changed

**Single Source of Truth Implementation**
- Created `data/config.yaml`: Human-editable configuration baseline
- Created `data/config.json`: Machine-readable export (auto-generated)
- Created `data/config.md`: Documentation tables (auto-generated)
- Created `src/config_loader.py`: Python configuration loader
- ALL calculations now reference SSoT (no hardcoded values)

**Pressure Parameters** (corrected from vendor/contractor data)
- WCS.HP outlet: 14 barg nominal (was 12 barg), max 15 barg, min 10 barg
- HCC inlet: 1050 mbar (was 1000 mbar) — prevents air ingress
- VLP suction: 400 mbar nominal (was fixed 300 mbar)
- VLP range: 250–550 mbar (VFD controlled)
- Helium inventory: 15 bar in 3× 120 m³ vessels

**Flow Parameters** (from ALaT + LKT pre-study)
- Design flow: 350 g/s (max user demand)
- Expected flow: 304 g/s (operational)
- WCS maximum: 336 g/s
- Per-unit flow: 112.54 g/s @ 72 Hz (ALaT vendor data)

**FSD575 Specifications** (corrected from ALaT annex pp. 67–69/73)
- Motor power: 315 kW (was 400 kW generic)
- Package power: 348.54 kW (water-cooled)
- Cooling water: 18.2 m³/h per skid
- Heat rejection: 323.9 kW per skid
- Weight: 6,770 kg, Oil charge: 173 L

**Monte Carlo Distributions** (PERT)
- VLP: 250|400|500 mbar (min|expected|max) — was 200|300|400
- LP outlet: 900|1050|1200 mbar — was 800|1000|1200

### Added

**PVPS Internal Redundancy** (new detail)
- Configuration: N+1 with 9 active + 1 standby = 10 total units
- Flow per unit: 5 g/s (total 50 g/s)
- N-1 resilience: 9 units can handle 50 g/s via VFD ramp-up

**Modeling Standards**
- Real Gas properties (NIST REFPROP) replacing Ideal Gas screening
- Absolute pressure reference standard (unless explicitly marked barg)
- Non-isothermal transport model: 80 W (2K equivalent) heat load

**New Files**
- `data/config.yaml`: Human-readable SSoT
- `data/config.json`: Machine-readable SSoT
- `data/config.md`: Human-readable parameter tables
- `src/config_loader.py`: Python module with dot-notation access
- `docs/index_v4_0.html`: Updated 40-slide master navigator
- `tests/test_config_loader.py`: SSoT validation tests

### Fixed

**Calculation Corrections**
- Fixed compressor count assumption (4 → 3)
- Corrected FSD575 power specs (315 kW motor, 348.54 kW package)
- Corrected pressure parameters across all modules
- Fixed Monte Carlo VLP/LP ranges
- Updated energy consumption formulas for 3 units
- Corrected cost models (CAPEX, OPEX, ROI)

**Data Integrity**
- Validated FSD575 specifications against ALaT vendor data
- Cross-referenced pressure parameters with contractor baseline
- Verified flow requirements against design documents

### Validation

- ✅ All unit tests passing
- ✅ Pressure parameter consistency across modules
- ✅ Energy calculations validated (3 units)
- ✅ Cost models verified (€600k compressors)
- ✅ SSoT configuration schema validated

## [3.1.0] - 2026-05-09

### Added
- Liquid helium properties database (saturation curve, subcooled)
- `src/liquid_he_loss.py` — leak rate to liquid inventory loss conversion
- `src/compressor_reliability.py` — k-of-M availability, VFD energy savings
- `src/wcs_scenarios.py` — WCS.HP protection, interlocks, leak budget
- `data/compressor_specs.json` — FSD575 and HSD Twin Combi specifications
- 6 new Plotly visualizations in docs/visualizations_v3/
- 3 new documentation pages (Liquid He Guide, HP Redundancy, WCS.HP Protection)
- 40-slide master navigator: docs/index_v3_1.html
- Idempotent setup/build/validate/package scripts
- Machine-readable manifest/backlog handover files

### Changed
- Corrected liquid He mass-flow conversion chain
- Updated master slide navigator to 40 slides

### Fixed
- Removed legacy conversion inflation issue from leak-rate handling

## [3.0.0] - 2026-05-08

### Added
- Standards compliance framework (8 international codes)
- RTM traceability matrix (9 items)
- FAT/SAT procedures
- PED compliance workflow
- Monte Carlo, PCA, and sensitivity statistical outputs
- 18 material/supplier-specific Plotly visualizations
