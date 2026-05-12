# QPLANT Configuration — v4.0.0

*Auto-generated from `data/config.yaml` — do not edit manually.*

## System

| Parameter | Value |
|-----------|-------|
| name | MYRRHA QPLANT Helium Refrigeration |
| design_basis | ALaT + LKT Pre-Study Baseline |
| facility | SCK CEN — MYRRHA |

## Flow Parameters

### Wcs Hp

| Parameter | Value |
|-----------|-------|
| design_flow_gs | 350 |
| expected_flow_gs | 304 |
| max_flow_gs | 336 |
| redundancy_formula | 3/112 × (N+1), N=3 |

### Pvps

| Parameter | Value |
|-----------|-------|
| total_flow_gs | 50 |
| units_total | 10 |
| units_active | 9 |
| flow_per_unit_gs | 5 |
| n_minus_1_capable | True |

## Pressure Parameters

### Wcs Hp Outlet

| Parameter | Value |
|-----------|-------|
| nominal_barg | 14 |
| max_barg | 15 |
| min_barg | 10 |

### Helium Inventory

| Parameter | Value |
|-----------|-------|
| storage_bar | 15 |
| vessel_count | 3 |
| vessel_volume_m3 | 120 |

### Hcc Inlet

| Parameter | Value |
|-----------|-------|
| nominal_mbar | 1050 |

### Wcs Lcc Suction

| Parameter | Value |
|-----------|-------|
| nominal_mbar | 400 |
| min_mbar | 250 |
| max_mbar | 550 |
| control | VFD |

### Pressure Drops

| Parameter | Value |
|-----------|-------|
| qrb_to_wcs_mbar | 50 |
| cold_b_return_mbar | 26 |

### Heat Loads

| Parameter | Value |
|-----------|-------|
| non_isothermal_transport_W | 80 |
| equivalent_delta_T_K | 2 |

## Monte Carlo Distributions

### Vlp Pressure

| Parameter | Value |
|-----------|-------|
| min_mbar | 250 |
| expected_mbar | 400 |
| max_mbar | 500 |
| distribution | PERT |

### Lp Outlet

| Parameter | Value |
|-----------|-------|
| min_mbar | 900 |
| expected_mbar | 1050 |
| max_mbar | 1200 |
| distribution | PERT |

## Compressor Specifications

### Hp Compressors

| Parameter | Value |
|-----------|-------|
| count | 3 |
| model | Kaeser FSD 575 SFC |
| power_supply | 400V 3-phase |
| redundancy | N+1 where N=3 |
| configuration | 3 active compressors |

### Fsd575

| Parameter | Value |
|-----------|-------|
| capacity_nm3h | 575 |
| motor_power_kW | 315 |
| package_power_kW | 348.54 |
| per_unit_flow_gs | 112.54 |
| frequency_hz | 72 |
| vfd_range_pct | [30, 100] |
| efficiency_percent | [70, 75] |
| cooling_water_m3h | 18.2 |
| heat_rejection_kW | 323.9 |
| noise_dba | 75 |
| dimensions_mm | 3240 × 2145 × 2360 |
| weight_kg | 6770 |
| oil_charge_L | 173 |
| mtbf_hours | 8760 |
| mttr_hours | 8 |
| capital_cost_eur | 200000 |
| annual_maint_eur | 15000 |

### Three Skid Totals

| Parameter | Value |
|-----------|-------|
| max_total_flow_gs | 337.62 |
| package_power_kW | 1045.62 |
| cooling_water_m3h | 54.6 |
| heat_rejection_kW | 971.7 |

## Financial

### Compressor Capex

| Parameter | Value |
|-----------|-------|
| per_unit_eur | 200000 |
| total_3_units_eur | 600000 |
| total_system_eur | 1420000 |

### Annual Energy

| Parameter | Value |
|-----------|-------|
| per_unit_kwh | 1120000 |
| total_3_units_kwh | 3360000 |
| cost_3_units_eur | 504000 |

## Modeling Standards

| Parameter | Value |
|-----------|-------|
| fluid_properties | Real Gas (NIST REFPROP) |
| pressure_reference | Absolute (unless marked barg) |
| temperature_reference | Kelvin |

## Compliance

| Parameter | Value |
|-----------|-------|
| standards | ['PED 2014/68/EU', 'ASME B31.3', 'EN 13185', 'ISO 5208'] |
