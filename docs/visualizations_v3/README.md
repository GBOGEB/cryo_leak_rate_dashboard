# Visualizations v3 — Advanced Analytics Charts

**Version generated:** v3.1.0 → updated with v4.0.0 compressor data (2026-05-10)  
**Generator:** `src/generate_visuals_v3.py`

These 21 interactive Plotly charts provide deep-dive analytics for the QPLANT cryogenic system.
Charts with compressor data (availability, VFD, redundancy, cost-benefit) were regenerated on 2026-05-10
to reflect the v4.0.0 correction (3× FSD575 SFC compressors, 14 barg HP).

## Categories

### Leak Rate & Loss Analysis
- `boiloff_vs_leakrate.html` — Boil-off vs leak rate correlation
- `chart_leak_vs_loss_extended.html` — Extended leak vs loss analysis
- `chart_temp_effect_pressure.html` — Temperature effect with pressure isolines
- `chart_choked_flow.html` — Choked flow regime analysis
- `chart_compressibility.html` — Compressibility factor analysis

### Statistical / Monte Carlo
- `chart_mc_histogram.html` — Monte Carlo histogram
- `chart_mc_scatter.html` — Monte Carlo scatter plot
- `chart_sensitivity_bar.html` — Sensitivity indices
- `chart_scree.html` — PCA scree plot
- `chart_biplot.html` — PCA biplot

### System & Fleet
- `chart_valve_fleet_sensitivity.html` — Valve fleet sensitivity
- `chart_purity_dilution.html` — Purity/dilution analysis
- `chart_internal_vs_external.html` — Internal vs external leakage
- `chart_helium_properties.html` — Helium properties database

### Compressor & Reliability (v4.0.0 updated)
- `compressor_availability_comparison.html` — Availability comparison (3× FSD575)
- `vfd_energy_savings.html` — VFD energy savings model
- `redundancy_cost_benefit.html` — N+1 redundancy cost-benefit
- `wcs_hp_architecture.html` — WCS.HP protection architecture

### Financial
- `chart_cost_breakdown_box.html` — Cost breakdown box plot
- `chart_correlation_heatmap.html` — Correlation heatmap
- `chart_lifecycle_standards.html` — Lifecycle standards compliance

### Liquid Helium
- `liquid_inventory_depletion.html` — Liquid inventory depletion model
