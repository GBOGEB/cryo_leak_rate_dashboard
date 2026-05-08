from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from calculations.engineering import (
    LEAK_CLASSES,
    PRESSURES_BAR,
    TEMPERATURES_K,
    R,
    M_HE_G_PER_MOL,
    CONTRACTUAL_ALIGNMENT_FACTOR,
    build_conversion_table,
    build_cost_table,
    build_inventory_table,
    build_reliability_table,
    build_traceability_matrix,
    build_valve_spec_table,
    leak_rate_to_mass_flow_g_s,
)
from plotting.plot_factory import (
    make_plot_1_leak_vs_loss,
    make_plot_2_temp_effect,
    make_plot_3_valve_comparison,
    make_plot_4_system_projection,
    make_plot_5_reliability,
    write_plot,
)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_HTML = ROOT / "outputs" / "html"
OUTPUT_JSON = ROOT / "outputs" / "json"
OUTPUT_MD = ROOT / "outputs" / "md"
OUTPUT_VERSIONED = ROOT / "outputs" / "versioned"
DOCS = ROOT / "docs"
TRACEABILITY = ROOT / "traceability"


def ensure_dirs() -> None:
    for p in [OUTPUT_HTML, OUTPUT_JSON, OUTPUT_MD, OUTPUT_VERSIONED, DOCS, TRACEABILITY]:
        p.mkdir(parents=True, exist_ok=True)


def write_json(df: pd.DataFrame, path: Path) -> None:
    path.write_text(df.to_json(orient="records", indent=2), encoding="utf-8")


def nav(current: str) -> str:
    pages = [
        "index.html",
        "01_EXECUTIVE_SUMMARY.html",
        "02_LEAK_RATE_TRANSLATION.html",
        "03_MATHS_PROOF.html",
        "04_PLOTS_AND_VISUAL_EVIDENCE.html",
        "05_VALVE_CLASS_COMPARISON.html",
        "06_ENGINEERING_RATIONALE.html",
        "07_TRACEABILITY_MATRIX.html",
        "08_VERSION_HISTORY.html",
        "09_BUILD_AND_RUNTIME_REPORT.html",
    ]
    links = []
    for p in pages:
        label = p.replace(".html", "")
        cls = "active" if p == current else ""
        links.append(f'<a class="{cls}" href="{p}">{label}</a>')
    return " | ".join(links)


def html_page(title: str, current_file: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>{title}</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 0; background: #f5f7fb; color: #14213d; }}
    header {{ background: #14213d; color: white; padding: 14px 18px; position: sticky; top: 0; z-index: 99; }}
    nav a {{ color: #cfe3ff; text-decoration: none; font-size: 12px; margin-right: 8px; }}
    nav a.active {{ color: #ffd166; font-weight: 700; }}
    main {{ max-width: 1200px; margin: 20px auto; background: white; border-radius: 8px; padding: 24px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); }}
    h1, h2, h3 {{ color: #0b3d91; }}
    table {{ border-collapse: collapse; width: 100%; margin-bottom: 24px; font-size: 13px; }}
    th, td {{ border: 1px solid #d7dbe4; padding: 8px; text-align: left; vertical-align: top; }}
    th {{ background: #edf2ff; }}
    .kpi-grid {{ display: grid; grid-template-columns: repeat(auto-fit,minmax(220px,1fr)); gap: 12px; }}
    .kpi {{ background: #eef7ff; border-left: 5px solid #0b3d91; padding: 10px 12px; border-radius: 6px; }}
    .small {{ font-size: 12px; color: #555; }}
    iframe {{ width: 100%; height: 520px; border: 1px solid #ccd3e0; border-radius: 6px; margin-bottom: 16px; }}
    .math {{ background: #0b132b; color: #d8e2ff; padding: 12px; border-radius: 6px; font-family: 'Courier New', monospace; white-space: pre-wrap; }}
  </style>
</head>
<body>
<header>
  <div><strong>Cryogenic Leak Rate Analysis Dashboard — OUTPUT_1_BASELINE</strong></div>
  <nav>{nav(current_file)}</nav>
</header>
<main>
{body}
</main>
</body>
</html>
"""


def write_dmaic_report(now_iso: str) -> None:
    text = f"""# DMAIC_0_REPORT

## Define
- Mission: translate helium leak-rate classes into quantitative mass-loss, reliability, and economic decisions for QPLANT valve strategy.
- Scope: leak classes 1e-9/1e-8/1e-5/1e-4 mbar·L/s; temperatures 4–300 K; pressures 1/5/12 bar.

## Measure
- Unit checks implemented for mbar·L/s → Pa·m³/s and mass conversion to g/s, g/day, g/year.
- Input domains validated through fixed class/temperature/pressure vectors.

## Analyze
- Formula verified from ideal gas law using throughput relation and pressure-ratio scaling assumption.
- Added transport indicators (density, Mach estimate, Reynolds, Nusselt) for engineering context.
- Reliability assumptions documented as baseline placeholders for iteration.

## Improve
- Modularized code into `src/calculations` and `src/plotting`.
- Automated generation of HTML/JSON/MD outputs and GitHub Pages docs copy.

## Control
- Version metadata in VERSION.json.
- Traceability matrix RTM-047..067 generated.
- Build metadata and timestamp recorded.

Generated: {now_iso}
"""
    (ROOT / "DMAIC_0_REPORT.md").write_text(text, encoding="utf-8")
    (OUTPUT_MD / "DMAIC_0_REPORT.md").write_text(text, encoding="utf-8")


def generate() -> None:
    ensure_dirs()
    now = datetime.now(timezone.utc)
    now_iso = now.isoformat()

    conversion_df = build_conversion_table()
    valve_df = build_valve_spec_table()
    inventory_df = build_inventory_table()
    rel_df, spare_df = build_reliability_table()
    cost_df = build_cost_table()
    trace_df = build_traceability_matrix()

    write_json(conversion_df, OUTPUT_JSON / "leak_rate_conversion_table.json")
    write_json(valve_df, OUTPUT_JSON / "valve_specifications_table.json")
    write_json(inventory_df, OUTPUT_JSON / "system_inventory_table.json")
    write_json(cost_df, OUTPUT_JSON / "cost_comparison_table.json")
    write_json(rel_df, OUTPUT_JSON / "reliability_metrics_table.json")
    write_json(spare_df, OUTPUT_JSON / "spare_parts_strategy_table.json")
    write_json(trace_df, OUTPUT_JSON / "traceability_matrix.json")

    fig1 = make_plot_1_leak_vs_loss(conversion_df)
    fig2 = make_plot_2_temp_effect(conversion_df)
    fig3 = make_plot_3_valve_comparison(cost_df)
    fig4 = make_plot_4_system_projection(inventory_df)
    fig5 = make_plot_5_reliability(rel_df, spare_df)

    plot_dir = OUTPUT_HTML / "plots"
    write_plot(fig1, plot_dir / "plot1_leak_vs_loss.html")
    write_plot(fig2, plot_dir / "plot2_temp_effect.html")
    write_plot(fig3, plot_dir / "plot3_valve_comparison.html")
    write_plot(fig4, plot_dir / "plot4_system_projection.html")
    write_plot(fig5, plot_dir / "plot5_reliability_dashboard.html")

    ex_q = 1e-8
    ex_t = 300
    ex_p = 1
    ex_g_s = leak_rate_to_mass_flow_g_s(ex_q, ex_t, ex_p)
    ex_g_day = ex_g_s * 86400
    ex_g_year = ex_g_s * 365.25 * 86400

    total_loss_kg_year = inventory_df["mass_loss_g_year_total"].sum() / 1000
    total_cost_year = total_loss_kg_year * 15

    index_body = f"""
<h1>Landing Page</h1>
<p>Interactive engineering dashboard for translating cryogenic helium leak-rate requirements into mass loss, reliability, and cost impact.</p>
<div class=\"kpi-grid\">
  <div class=\"kpi\"><strong>Baseline</strong><br/>OUTPUT_1_BASELINE</div>
  <div class=\"kpi\"><strong>Leak classes</strong><br/>{', '.join([f'{x:.0e}' for x in LEAK_CLASSES])} mbar·L/s</div>
  <div class=\"kpi\"><strong>Temperatures</strong><br/>{TEMPERATURES_K} K</div>
  <div class=\"kpi\"><strong>Pressures</strong><br/>{PRESSURES_BAR} bar abs</div>
  <div class=\"kpi\"><strong>System annual loss</strong><br/>{total_loss_kg_year:.3f} kg/year</div>
  <div class=\"kpi\"><strong>System annual He cost</strong><br/>€{total_cost_year:,.2f}/year (at €15/kg)</div>
</div>
<p class=\"small\">All pages are standalone and linked for GitHub Pages publication.</p>
"""

    exec_body = f"""
<h1>01 Executive Summary</h1>
<ul>
  <li>Specified leak requirements include 1e-8 mbar·L/s (to vacuum), 1e-5 mbar·L/s (to atmosphere), and 1e-4 mbar·L/s (valve seat).</li>
  <li>Proposed warm-valve variants (Meca Inox HDPE, Swagelok UHMWPE) are economically attractive but do not target 1e-9 hermetic performance.</li>
  <li>Baseline 210 cold + 200 warm valve mix gives approximately <strong>{total_loss_kg_year:.3f} kg He/year</strong> under selected assumptions.</li>
  <li>At €10–20/kg helium, annual loss cost range is €{total_loss_kg_year*10:,.1f} to €{total_loss_kg_year*20:,.1f}.</li>
  <li>Reliability classing indicates strongest availability when higher-integrity leak classes are used in critical cold service.</li>
</ul>
<h2>Recommendation</h2>
<p>Adopt a mixed strategy: leak-tight (1e-9/1e-8) on critical cold paths, pragmatic 1e-5 class on warm non-critical paths, with explicit derogation and quantified lifecycle economics.</p>
"""

    translation_body = """
<h1>02 Leak Rate Translation</h1>
<p>Core table for all leak classes × temperatures × pressures.</p>
""" + conversion_df.to_html(index=False, float_format=lambda x: f"{x:.4e}")

    maths_body = f"""
<h1>03 Mathematical Proof</h1>
<h2>A) Symbolic derivation</h2>
<div class=\"math\">
Given throughput leak class Q_leak in mbar·L/s:
1 mbar·L/s = 0.1 Pa·m³/s
Q_Pa·m³/s = 0.1 * Q_leak

Assume leak class measured at 1 bar differential and scale linearly with pressure ratio P_bar/1bar.
From ideal gas law n_dot = (Q_Pa·m³/s * P_ratio)/(R*T)
Mass flow m_dot_raw = n_dot * M_He

Project convention alignment with Addendum Table values:
m_dot = m_dot_raw * C_align, with C_align = {CONTRACTUAL_ALIGNMENT_FACTOR:.0f}

=> m_dot = (Q_Pa·m³/s * P_ratio * M_He * C_align) / (R*T)
where M_He = {M_HE_G_PER_MOL} g/mol, R = {R} J/(mol·K)
</div>
<h2>B) Worked example</h2>
<div class=\"math\">
Input: Q = {ex_q:.1e} mbar·L/s, T = {ex_t} K, P = {ex_p} bar abs
Q_Pa·m³/s = 0.1 * {ex_q:.1e} = {0.1*ex_q:.2e}
m_dot = (Q_Pa·m³/s * P_ratio * M * C_align)/(R*T)
     = ({0.1*ex_q:.2e} * 1 * {M_HE_G_PER_MOL} * {CONTRACTUAL_ALIGNMENT_FACTOR:.0f}) / ({R:.6f} * {ex_t})
     = {ex_g_s:.6e} g/s
m_day = {ex_g_day:.6e} g/day
m_year = {ex_g_year:.6e} g/year
</div>
<h2>C) Uncertainty notes</h2>
<ul>
  <li>Linear pressure scaling assumes molecular-flow-like proportionality near specification point.</li>
  <li>Contractual alignment factor C_align=1000 is applied to match Addendum leak-mass table convention.</li>
  <li>Real leak paths may deviate due to geometry, temperature-dependent seal mechanics, and non-ideal effects.</li>
  <li>Values intended for engineering decision support, not final acceptance test replacement.</li>
</ul>
"""

    plots_body = """
<h1>04 Plots and Visual Evidence</h1>
<iframe src="plots/plot1_leak_vs_loss.html"></iframe>
<iframe src="plots/plot2_temp_effect.html"></iframe>
<iframe src="plots/plot3_valve_comparison.html"></iframe>
<iframe src="plots/plot4_system_projection.html"></iframe>
<iframe src="plots/plot5_reliability_dashboard.html"></iframe>
<p class="small">Plotly figures are standalone HTML and SVG export compatible from Plotly modebar.</p>
"""

    valve_body = """
<h1>05 Valve Class Comparison</h1>
<h2>Valve specification table</h2>
""" + valve_df.to_html(index=False) + """
<h2>Cost comparison table</h2>
""" + cost_df.to_html(index=False, float_format=lambda x: f"{x:.4g}")

    rationale_body = """
<h1>06 Engineering Rationale</h1>
<h2>Design guidance</h2>
<ol>
  <li>Use 1e-8 class (or better) for helium-to-vacuum and critical cold envelope integrity.</li>
  <li>Use 1e-5 class where process-to-ambient leakage is acceptable and monitored.</li>
  <li>Where warm valve options are selected, document derogation against 1e-9 expectations and quantify lifecycle impact.</li>
  <li>Implement online leak trending + periodic helium mass balance reconciliation.</li>
  <li>Integrate spare policy from reliability table with annual shutdown planning.</li>
</ol>
<h2>Reliability and inventory tables</h2>
""" + rel_df.to_html(index=False, float_format=lambda x: f"{x:.4g}") + """
""" + spare_df.to_html(index=False, float_format=lambda x: f"{x:.4g}") + """
""" + inventory_df.to_html(index=False, float_format=lambda x: f"{x:.4g}")

    trace_body = """
<h1>07 Traceability Matrix</h1>
<p>Mapping RTM-047 through RTM-067 to implementation and verification artefacts.</p>
""" + trace_df.to_html(index=False)

    version_json = {
        "version": "0.1.0",
        "baseline": "OUTPUT_1_BASELINE",
        "timestamp": now_iso,
        "dmaic_iteration": 0,
        "git_ready": True,
        "changes": [
            "Initial leak-rate dashboard baseline",
            "Added 5 interactive plotly visualizations",
            "Added traceability matrix RTM-047..067",
            "Generated GitHub Pages-ready docs outputs",
        ],
    }
    (ROOT / "VERSION.json").write_text(json.dumps(version_json, indent=2), encoding="utf-8")

    changelog = f"""# CHANGELOG

## 0.1.0 - {now.date().isoformat()}
- Created OUTPUT_1_BASELINE cryogenic leak-rate dashboard.
- Implemented leak-rate, reliability, and lifecycle-cost calculations.
- Produced 9 linked HTML pages + index and Plotly evidence set.
- Added DMAIC_0 report, traceability matrix, and JSON data exports.
"""
    (ROOT / "CHANGELOG.md").write_text(changelog, encoding="utf-8")

    version_body = """
<h1>08 Version History</h1>
<pre>""" + json.dumps(version_json, indent=2) + """</pre>
<h2>Changelog</h2>
<pre>""" + changelog + """</pre>
"""

    report = {
        "build_timestamp": now_iso,
        "python_files": sorted([str(p.relative_to(ROOT)) for p in ROOT.glob("src/**/*.py")]),
        "generated_html_files": sorted([str(p.relative_to(ROOT)) for p in OUTPUT_HTML.glob("*.html")]),
        "generated_plot_files": sorted([str(p.relative_to(ROOT)) for p in (OUTPUT_HTML / "plots").glob("*.html")]),
        "generated_json_files": sorted([str(p.relative_to(ROOT)) for p in OUTPUT_JSON.glob("*.json")]),
        "input_assumptions": {
            "temperature_grid_K": TEMPERATURES_K,
            "pressure_grid_bar_abs": PRESSURES_BAR,
            "leak_classes_mbar_l_s": LEAK_CLASSES,
            "helium_price_eur_kg": 15,
            "cold_valves": 210,
            "warm_valves": 200,
        },
    }
    (OUTPUT_JSON / "build_runtime_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    runtime_body = """
<h1>09 Build and Runtime Report</h1>
<pre>""" + json.dumps(report, indent=2) + """</pre>
"""

    pages = {
        "index.html": index_body,
        "01_EXECUTIVE_SUMMARY.html": exec_body,
        "02_LEAK_RATE_TRANSLATION.html": translation_body,
        "03_MATHS_PROOF.html": maths_body,
        "04_PLOTS_AND_VISUAL_EVIDENCE.html": plots_body,
        "05_VALVE_CLASS_COMPARISON.html": valve_body,
        "06_ENGINEERING_RATIONALE.html": rationale_body,
        "07_TRACEABILITY_MATRIX.html": trace_body,
        "08_VERSION_HISTORY.html": version_body,
        "09_BUILD_AND_RUNTIME_REPORT.html": runtime_body,
    }

    for filename, body in pages.items():
        (OUTPUT_HTML / filename).write_text(html_page(filename, filename, body), encoding="utf-8")

    # Markdown mirrors
    (OUTPUT_MD / "EXECUTIVE_SUMMARY.md").write_text(exec_body, encoding="utf-8")
    (TRACEABILITY / "RTM_047_067.csv").write_text(trace_df.to_csv(index=False), encoding="utf-8")

    write_dmaic_report(now_iso)

    # copy HTML outputs to docs
    if DOCS.exists():
        for item in DOCS.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
    shutil.copytree(OUTPUT_HTML, DOCS, dirs_exist_ok=True)

    # versioned snapshot
    version_dir = OUTPUT_VERSIONED / f"OUTPUT_1_BASELINE_{now.strftime('%Y%m%dT%H%M%SZ')}"
    shutil.copytree(OUTPUT_HTML, version_dir)

    readme = f"""# Cryogenic Leak Rate Analysis Dashboard

## Purpose and Scope
This repository provides **OUTPUT_1_BASELINE**, a GitHub Pages-ready dashboard translating helium leak-rate specifications into actionable mass-loss, reliability, and lifecycle-cost engineering insights for QPLANT valve decisions.

Scope includes:
- Leak classes: 1e-9, 1e-8, 1e-5, 1e-4 mbar·L/s
- Temperatures: 4, 10, 20, 50, 80, 300 K
- Pressures: 1, 5, 12 bar(abs)
- System scenario: 210 cold + 200 warm valves

## How to Use Dashboard
1. Open `docs/index.html` (or `outputs/html/index.html`) in any browser.
2. Navigate to ordered pages (01..09) using top navigation.
3. Use the Plotly pages to inspect interactive evidence and export figures.

## How to Regenerate Outputs
```bash
cd /home/ubuntu/cryo_leak_rate_dashboard
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 src/build_dashboard.py
```

## GitHub Pages
- Publish the `/docs` folder from your repo settings.
- Hosted URL will be available after enabling GitHub Pages.
- Suggested target path: `https://<org-or-user>.github.io/<repo>/index.html`

## Key Artefacts
- `outputs/html/*.html` : all dashboard pages
- `outputs/html/plots/*.html` : interactive Plotly plots
- `outputs/json/*.json` : source tables and build report
- `DMAIC_0_REPORT.md` : DMAIC baseline reflection
- `traceability/RTM_047_067.csv` : RTM mapping
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    generate()
    print("Dashboard generated successfully.")
