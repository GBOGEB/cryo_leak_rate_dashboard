# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
