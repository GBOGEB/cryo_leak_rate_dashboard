# Changelog

All notable changes to this project are documented in this file.

## [3.1.0] - 2026-05-09

### Added
- Liquid helium properties database (4K-300K, 1-12 bar)
- Leak rate to liquid inventory loss conversion
- HP compressor redundancy analysis (N=3, N+1 FSD575, N+1 HSD)
- VFD energy savings modeling using affinity laws
- WCS.HP supply protection logic (70/20/10 leak budget)
- Six new Plotly visualizations and associated data exports
- Idempotent setup/build/validate/package scripts
- Machine-readable manifest/backlog handover files

### Changed
- Corrected liquid He mass-flow conversion chain
- Updated master slide navigator to 40 slides

### Fixed
- Removed legacy conversion inflation issue from leak-rate handling

## [3.0.0] - 2026-05-08

### Added
- Standards compliance framework
- RTM traceability matrix
- FAT/SAT procedures
- PED workflow, Monte Carlo, PCA, and sensitivity outputs
