"""
HP Compressor Redundancy & Reliability Analysis — v3.1.0

Models N-of-M parallel compressor configurations for helium HP supply:
  - N=3 baseline (2-out-of-3)
  - N+1 FSD575 VFD (3-out-of-4 or 2-out-of-4)
  - N+1 HSD Twin Combi (1-out-of-2)

Includes:
  - Availability (Markov-based combinatorial)
  - Reliability R(t) curves
  - VFD energy savings analysis
  - Cost-benefit comparison

Reference: MIL-HDBK-217, IEEE 493, IEC 61078.
"""

from __future__ import annotations
import math
from dataclasses import dataclass
from typing import Optional

import pandas as pd


# ── Constants ───────────────────────────────────────────────────────
HOURS_PER_YEAR = 8760.0
OPERATING_HOURS_YEAR = 8000.0
ELECTRICITY_COST_EUR_KWH = 0.15


@dataclass
class CompressorConfig:
    """Definition of a compressor configuration."""
    name: str
    total_units: int           # M — total installed
    required_units: int        # k — minimum for full operation
    capacity_per_unit_pct: float  # % of total system capacity per unit
    mtbf_hours: float = 8760.0    # per-unit MTBF
    mttr_hours: float = 8.0       # per-unit MTTR
    power_kw: float = 400.0       # per-unit electrical power at full load
    has_vfd: bool = False
    vfd_turndown_min: float = 0.30  # minimum speed fraction
    capital_cost_eur: float = 175000.0  # per unit
    annual_maint_eur: float = 15000.0   # per unit
    compressor_type: str = "oil-flooded screw"
    efficiency_pct: float = 72.5


# ── Pre-defined configurations ──────────────────────────────────────

CONFIGS = {
    "N3_baseline": CompressorConfig(
        name="N=3 Baseline (2-of-3)",
        total_units=3,
        required_units=2,
        capacity_per_unit_pct=50.0,
        mtbf_hours=8760,
        mttr_hours=8,
        power_kw=400,
        has_vfd=False,
        capital_cost_eur=175000,
        annual_maint_eur=15000,
        compressor_type="oil-flooded screw",
        efficiency_pct=72.5,
    ),
    "N1_FSD575_A1": CompressorConfig(
        name="N+1 FSD575 VFD (3-of-4)",
        total_units=4,
        required_units=3,
        capacity_per_unit_pct=33.3,
        mtbf_hours=8760,
        mttr_hours=8,
        power_kw=400,
        has_vfd=True,
        vfd_turndown_min=0.30,
        capital_cost_eur=205000,
        annual_maint_eur=15000,
        compressor_type="oil-flooded screw + VFD",
        efficiency_pct=72.5,
    ),
    "N1_FSD575_A2": CompressorConfig(
        name="N+1 FSD575 VFD (2-of-4)",
        total_units=4,
        required_units=2,
        capacity_per_unit_pct=50.0,
        mtbf_hours=8760,
        mttr_hours=8,
        power_kw=400,
        has_vfd=True,
        vfd_turndown_min=0.30,
        capital_cost_eur=205000,
        annual_maint_eur=15000,
        compressor_type="oil-flooded screw + VFD",
        efficiency_pct=72.5,
    ),
    "N1_HSD_twin": CompressorConfig(
        name="N+1 HSD Twin Combi (1-of-2)",
        total_units=2,
        required_units=1,
        capacity_per_unit_pct=100.0,
        mtbf_hours=8760,
        mttr_hours=8,
        power_kw=575,
        has_vfd=False,
        capital_cost_eur=350000,
        annual_maint_eur=10000,
        compressor_type="oil-free centrifugal twin-head",
        efficiency_pct=82.5,
    ),
}


# ── Single-unit calculations ───────────────────────────────────────

def failure_rate(mtbf: float) -> float:
    """Failure rate λ = 1/MTBF [failures/hour]."""
    return 1.0 / mtbf


def single_availability(mtbf: float, mttr: float) -> float:
    """Steady-state availability A = MTBF / (MTBF + MTTR)."""
    return mtbf / (mtbf + mttr)


def single_reliability(t_hours: float, mtbf: float) -> float:
    """Reliability at time t: R(t) = e^(-λt)."""
    lam = failure_rate(mtbf)
    return math.exp(-lam * t_hours)


# ── k-out-of-M system calculations ────────────────────────────────

def _comb(n: int, k: int) -> int:
    """Binomial coefficient C(n, k)."""
    return math.comb(n, k)


def system_availability_k_of_m(A: float, M: int, k: int) -> float:
    """
    Availability of a k-out-of-M parallel system.
    System works if ≥ k of M units are operational.
    
    A_sys = Σ_{i=k}^{M} C(M,i) × A^i × (1-A)^(M-i)
    """
    q = 1.0 - A  # unavailability
    a_sys = 0.0
    for i in range(k, M + 1):
        a_sys += _comb(M, i) * (A ** i) * (q ** (M - i))
    return a_sys


def system_reliability_k_of_m(t_hours: float, mtbf: float,
                                M: int, k: int) -> float:
    """
    Reliability of a k-out-of-M system at time t.
    R_sys(t) = Σ_{i=k}^{M} C(M,i) × R(t)^i × (1-R(t))^(M-i)
    """
    R = single_reliability(t_hours, mtbf)
    F = 1.0 - R
    r_sys = 0.0
    for i in range(k, M + 1):
        r_sys += _comb(M, i) * (R ** i) * (F ** (M - i))
    return r_sys


def system_mtbf_approx(A_sys: float, mttr_sys: float = 8.0) -> float:
    """
    Approximate system MTBF from system availability.
    A_sys = MTBF_sys / (MTBF_sys + MTTR_sys)
    => MTBF_sys = A_sys × MTTR_sys / (1 - A_sys)
    """
    if A_sys >= 1.0:
        return float("inf")
    return A_sys * mttr_sys / (1.0 - A_sys)


def downtime_hours_year(A_sys: float) -> float:
    """Annual downtime in hours from system availability."""
    return HOURS_PER_YEAR * (1.0 - A_sys)


# ── VFD Energy Savings ─────────────────────────────────────────────

def vfd_power_at_load(full_load_kw: float, load_fraction: float,
                       vfd_efficiency: float = 0.97) -> float:
    """
    Power consumption with VFD at partial load.
    Affinity law for compressors: P ∝ Speed³
    With VFD: speed ∝ load → P = P_full × (load)³ / η_VFD
    """
    return full_load_kw * (load_fraction ** 3) / vfd_efficiency


def fixed_speed_power_at_load(full_load_kw: float,
                                load_fraction: float) -> float:
    """
    Fixed-speed compressor with unloading.
    Simplified: draws ~70% power at 50% load (typical screw with slide valve).
    Linear interpolation: P = P_full × (0.4 + 0.6 × load_fraction)
    """
    return full_load_kw * (0.4 + 0.6 * load_fraction)


def annual_energy_savings_vfd(
    full_load_kw: float,
    avg_load_fraction: float = 0.70,
    operating_hours: float = OPERATING_HOURS_YEAR,
    electricity_cost: float = ELECTRICITY_COST_EUR_KWH,
    vfd_efficiency: float = 0.97,
) -> dict:
    """Calculate annual energy savings from VFD vs fixed-speed."""
    P_fixed = fixed_speed_power_at_load(full_load_kw, avg_load_fraction)
    P_vfd = vfd_power_at_load(full_load_kw, avg_load_fraction, vfd_efficiency)

    E_fixed = P_fixed * operating_hours  # kWh/yr
    E_vfd = P_vfd * operating_hours
    delta_E = E_fixed - E_vfd
    savings_eur = delta_E * electricity_cost
    savings_pct = (delta_E / E_fixed) * 100 if E_fixed > 0 else 0

    return {
        "power_fixed_kw": round(P_fixed, 1),
        "power_vfd_kw": round(P_vfd, 1),
        "energy_fixed_kwh_yr": round(E_fixed, 0),
        "energy_vfd_kwh_yr": round(E_vfd, 0),
        "energy_savings_kwh_yr": round(delta_E, 0),
        "cost_savings_eur_yr": round(savings_eur, 0),
        "savings_pct": round(savings_pct, 1),
    }


# ── Comprehensive comparison ──────────────────────────────────────

def build_comparison_table() -> pd.DataFrame:
    """Build full comparison table for all predefined configurations."""
    rows = []
    for key, cfg in CONFIGS.items():
        A_single = single_availability(cfg.mtbf_hours, cfg.mttr_hours)
        A_sys = system_availability_k_of_m(A_single, cfg.total_units,
                                            cfg.required_units)
        dt = downtime_hours_year(A_sys)
        mtbf_sys = system_mtbf_approx(A_sys, cfg.mttr_hours)

        total_capex = cfg.capital_cost_eur * cfg.total_units
        total_maint = cfg.annual_maint_eur * cfg.total_units

        # Energy cost (running units × power × operating hours)
        running = cfg.required_units
        if cfg.has_vfd:
            avg_load = 0.70
            P_per = vfd_power_at_load(cfg.power_kw, avg_load)
        else:
            P_per = cfg.power_kw
        annual_energy_cost = running * P_per * OPERATING_HOURS_YEAR * ELECTRICITY_COST_EUR_KWH

        rows.append({
            "config_key": key,
            "name": cfg.name,
            "units": f"{cfg.total_units}×{cfg.capacity_per_unit_pct:.0f}%",
            "redundancy": f"{cfg.required_units}-of-{cfg.total_units}",
            "type": cfg.compressor_type,
            "A_single_pct": round(A_single * 100, 4),
            "A_system_pct": round(A_sys * 100, 6),
            "A_system_nines": -math.log10(1 - A_sys) if A_sys < 1 else float("inf"),
            "downtime_h_yr": round(dt, 4),
            "MTBF_system_hours": round(mtbf_sys, 0),
            "MTBF_system_years": round(mtbf_sys / HOURS_PER_YEAR, 1),
            "total_capex_eur": total_capex,
            "annual_maint_eur": total_maint,
            "annual_energy_eur": round(annual_energy_cost, 0),
            "total_annual_opex_eur": round(total_maint + annual_energy_cost, 0),
            "has_vfd": cfg.has_vfd,
            "efficiency_pct": cfg.efficiency_pct,
        })

    return pd.DataFrame(rows)


def build_reliability_curves(
    t_max_hours: float = 8760.0,
    n_points: int = 200,
) -> pd.DataFrame:
    """Build R(t) curves for all configurations."""
    import numpy as np
    times = np.linspace(0, t_max_hours, n_points)
    data = {"hours": times}

    for key, cfg in CONFIGS.items():
        R_vals = [
            system_reliability_k_of_m(t, cfg.mtbf_hours,
                                       cfg.total_units, cfg.required_units)
            for t in times
        ]
        data[cfg.name] = R_vals

    return pd.DataFrame(data)


def build_vfd_savings_table(
    full_load_kw: float = 400.0,
    loads: list[float] | None = None,
) -> pd.DataFrame:
    """Build table comparing fixed-speed vs VFD at various load points."""
    if loads is None:
        loads = [0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00]

    rows = []
    for load in loads:
        info = annual_energy_savings_vfd(full_load_kw, load)
        info["load_pct"] = round(load * 100, 0)
        rows.append(info)

    return pd.DataFrame(rows)


# ── Quick report ───────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== HP Compressor Redundancy Comparison ===\n")
    df = build_comparison_table()
    display_cols = ["name", "redundancy", "A_system_pct", "downtime_h_yr",
                    "MTBF_system_years", "total_capex_eur", "total_annual_opex_eur"]
    print(df[display_cols].to_string(index=False))

    print("\n=== VFD Energy Savings (400 kW unit) ===\n")
    vfd_df = build_vfd_savings_table()
    print(vfd_df[["load_pct", "power_fixed_kw", "power_vfd_kw",
                   "cost_savings_eur_yr", "savings_pct"]].to_string(index=False))
