"""
WCS.HP Supply Protection Scenario Analysis — v3.1.0

Models Worst Case Supply scenarios for the HP helium compressor system:
  - Normal operation (all compressors available)
  - WCS (1 compressor failed, sidestreams isolated)
  - Emergency (2 compressors failed, beam reduced)

Includes:
  - Leak budget allocation (main supply, sidestreams, contingency)
  - Interlock logic table
  - Decision matrix for each scenario
"""

from __future__ import annotations
from dataclasses import dataclass
import pandas as pd


# ── Leak Budget Constants ──────────────────────────────────────────
TOTAL_LEAK_BUDGET = 1e-5  # mbar·L/s (RTM-048 system max)

LEAK_ALLOCATIONS = {
    "main_hp_supply": {
        "budget_mbar_l_s": 7e-6,
        "fraction_pct": 70,
        "description": "Critical path: compressors → QVB, largest valve count",
    },
    "sidestreams": {
        "budget_mbar_l_s": 2e-6,
        "fraction_pct": 20,
        "description": "Non-critical: recovery, purification, research taps (can be shut off)",
    },
    "contingency": {
        "budget_mbar_l_s": 1e-6,
        "fraction_pct": 10,
        "description": "Future expansions, measurement error margin",
    },
}


# ── Interlock Logic ────────────────────────────────────────────────

INTERLOCKS = [
    {
        "condition": "HP header pressure LOW",
        "setpoint": "< 13.5 barg",
        "action": "Close sidestream isolation valves",
        "purpose": "Protect main HP supply from sidestream leaks",
        "priority": "WARNING",
    },
    {
        "condition": "HP header pressure LOW-LOW",
        "setpoint": "< 13.0 barg",
        "action": "Alarm + start backup compressor",
        "purpose": "Prevent beam dump, restore redundancy",
        "priority": "ALARM",
    },
    {
        "condition": "Compressor failure (any)",
        "setpoint": "Trip signal from PLC",
        "action": "Start standby compressor (auto)",
        "purpose": "Maintain N redundancy",
        "priority": "AUTO",
    },
    {
        "condition": "2 compressors failed",
        "setpoint": "Second trip within MTTR window",
        "action": "Reduce beam to 50% intensity",
        "purpose": "Match available compressor capacity",
        "priority": "ALARM",
    },
    {
        "condition": "Sidestream leak detected",
        "setpoint": "Local He detector > 100 ppm",
        "action": "Isolate affected branch (NC valve closes)",
        "purpose": "Limit He loss, protect inventory",
        "priority": "AUTO",
    },
    {
        "condition": "All compressors failed",
        "setpoint": "No running units",
        "action": "Emergency beam shutdown, vent to recovery",
        "purpose": "Safe shutdown, minimize He loss",
        "priority": "TRIP",
    },
]


# ── Scenario Definitions ──────────────────────────────────────────

@dataclass
class WCSScenario:
    name: str
    compressors_available: int
    compressors_running: int
    capacity_pct: float
    hp_header_barg: float
    sidestreams_open: bool
    beam_operation_pct: float
    total_leak_mbar_l_s: float
    status: str
    description: str


SCENARIOS = [
    WCSScenario(
        name="Normal Operation",
        compressors_available=3,
        compressors_running=2,
        capacity_pct=100.0,
        hp_header_barg=14.0,
        sidestreams_open=True,
        beam_operation_pct=100.0,
        total_leak_mbar_l_s=9e-6,
        status="NOMINAL",
        description="All 3 compressors available (2 running, 1 standby). "
                    "Sidestreams open, full beam operation.",
    ),
    WCSScenario(
        name="WCS — 1 Compressor Failed",
        compressors_available=2,
        compressors_running=2,
        capacity_pct=100.0,
        hp_header_barg=13.8,
        sidestreams_open=False,
        beam_operation_pct=100.0,
        total_leak_mbar_l_s=7e-6,
        status="WARNING",
        description="2 compressors running at 100% capacity, no standby. "
                    "Sidestreams closed by interlock to protect main supply.",
    ),
    WCSScenario(
        name="Emergency — 2 Compressors Failed",
        compressors_available=1,
        compressors_running=1,
        capacity_pct=50.0,
        hp_header_barg=13.2,
        sidestreams_open=False,
        beam_operation_pct=50.0,
        total_leak_mbar_l_s=3.5e-6,
        status="ALARM",
        description="1 compressor running at 50% capacity. "
                    "Beam reduced to 50%. Sidestreams closed.",
    ),
    WCSScenario(
        name="Total Failure",
        compressors_available=0,
        compressors_running=0,
        capacity_pct=0.0,
        hp_header_barg=0.0,
        sidestreams_open=False,
        beam_operation_pct=0.0,
        total_leak_mbar_l_s=0.0,
        status="TRIP",
        description="All compressors failed. Emergency beam shutdown. "
                    "Vent to recovery system.",
    ),
]


# ── Table Builders ─────────────────────────────────────────────────

def build_leak_budget_table() -> pd.DataFrame:
    """Leak budget allocation table."""
    rows = []
    for circuit, info in LEAK_ALLOCATIONS.items():
        rows.append({
            "circuit": circuit.replace("_", " ").title(),
            "budget_mbar_l_s": info["budget_mbar_l_s"],
            "fraction_pct": info["fraction_pct"],
            "justification": info["description"],
        })
    rows.append({
        "circuit": "TOTAL",
        "budget_mbar_l_s": TOTAL_LEAK_BUDGET,
        "fraction_pct": 100,
        "justification": "RTM-048 system cap",
    })
    return pd.DataFrame(rows)


def build_interlock_table() -> pd.DataFrame:
    """Interlock logic table."""
    return pd.DataFrame(INTERLOCKS)


def build_scenario_table() -> pd.DataFrame:
    """WCS scenario comparison table."""
    rows = []
    for s in SCENARIOS:
        rows.append({
            "scenario": s.name,
            "compressors_available": s.compressors_available,
            "compressors_running": s.compressors_running,
            "capacity_pct": s.capacity_pct,
            "hp_header_barg": s.hp_header_barg,
            "sidestreams": "Open" if s.sidestreams_open else "Closed",
            "beam_pct": s.beam_operation_pct,
            "leak_budget_mbar_l_s": s.total_leak_mbar_l_s,
            "status": s.status,
            "description": s.description,
        })
    return pd.DataFrame(rows)


# ── Quick report ───────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Leak Budget Allocation ===\n")
    print(build_leak_budget_table().to_string(index=False))

    print("\n=== Interlock Logic ===\n")
    print(build_interlock_table()[["condition", "setpoint", "action", "priority"]].to_string(index=False))

    print("\n=== WCS Scenarios ===\n")
    df = build_scenario_table()
    print(df[["scenario", "capacity_pct", "hp_header_barg",
              "sidestreams", "beam_pct", "status"]].to_string(index=False))
