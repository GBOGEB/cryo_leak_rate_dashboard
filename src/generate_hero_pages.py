#!/usr/bin/env python3
"""Generate audience-specific hero landing pages from SSoT config.yaml.

Produces three hero pages:
  - docs/heroes/executive.html   (ROI / cost focus)
  - docs/heroes/technical.html   (specs / engineering focus)
  - docs/heroes/compliance.html  (standards / traceability focus)

Usage:
    python src/generate_hero_pages.py
"""
import json
import yaml
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / 'docs'
HEROES = DOCS / 'heroes'
DATA = ROOT / 'data'
CONFIG = DATA / 'config.yaml'
ASSETS_REL = '../assets'

NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def _load_config() -> dict:
    with open(CONFIG) as f:
        return yaml.safe_load(f)


def _load_json(name: str) -> list | dict:
    with open(DATA / name) as f:
        return json.load(f)


def _page(title: str, body: str, active: str = '') -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — QPLANT Cryogenic Dashboard</title>
<link rel="stylesheet" href="{ASSETS_REL}/style.css">
<style>
  .hero-banner {{
    background: linear-gradient(135deg, #1a365d 0%, #2d5a87 100%);
    color: white; padding: 3rem 2rem; border-radius: 12px;
    margin-bottom: 2rem; text-align: center;
  }}
  .hero-banner h1 {{ color: white; font-size: 2.2rem; margin-bottom: 0.5rem; }}
  .hero-banner .subtitle {{ opacity: 0.85; font-size: 1.1rem; }}
  .kpi-row {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem; margin: 2rem 0; }}
  .kpi-card {{ background: #f0f4f8; border-left: 4px solid #2d5a87;
    padding: 1.5rem; border-radius: 8px; }}
  .kpi-card .value {{ font-size: 2rem; font-weight: 700; color: #1a365d; }}
  .kpi-card .label {{ color: #555; font-size: 0.9rem; margin-top: 0.3rem; }}
  .section {{ margin: 2rem 0; }}
  .section h2 {{ border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem; }}
  .nav-back {{ margin: 1rem 0; }}
  .nav-back a {{ color: #2d5a87; text-decoration: none; font-weight: 600; }}
  .nav-back a:hover {{ text-decoration: underline; }}
</style>
</head>
<body>
<main style="max-width:960px; margin:0 auto; padding:2rem;">
<div class="nav-back"><a href="../NAVIGATOR.html">← Back to Navigator</a></div>
{body}
<footer style="margin-top:3rem; padding-top:1rem; border-top:1px solid #e2e8f0;
  color:#888; font-size:0.85rem; text-align:center;">
  Generated {NOW} · QPLANT Cryogenic Dashboard v{_load_config().get('version','4.0.0')}
</footer>
</main>
</body>
</html>"""


def generate_executive():
    cfg = _load_config()
    scenarios = _load_json('scenarios.json')
    valves = _load_json('valve_candidates.json')

    version = cfg.get('version', '4.0.0')
    flow = cfg.get('flow_parameters', {}).get('wcs_hp', {})
    design_flow = flow.get('design_flow_gs', 350)

    # Derive cost facts from valve data
    cheapest = min(valves, key=lambda v: v.get('capex_eur', 99999))
    baseline_scn = next((s for s in scenarios if 'BASELINE' in s.get('id', '')), scenarios[0])
    n_valves = sum(seg.get('count', 0) for seg in baseline_scn.get('inventory', []))

    body = f"""
<div class="hero-banner">
  <h1>📊 Executive Summary</h1>
  <p class="subtitle">QPLANT Cryogenic Helium System — Cost & Risk Overview</p>
</div>

<div class="kpi-row">
  <div class="kpi-card"><div class="value">{version}</div><div class="label">System Version</div></div>
  <div class="kpi-card"><div class="value">{design_flow} g/s</div><div class="label">Design Flow (WCS.HP)</div></div>
  <div class="kpi-card"><div class="value">{n_valves}</div><div class="label">Total Valve Inventory</div></div>
  <div class="kpi-card"><div class="value">€{cheapest.get('capex_eur',0):,.0f}</div>
    <div class="label">Min Valve CAPEX ({cheapest.get('title','').split()[0]})</div></div>
</div>

<div class="section">
  <h2>Key Decisions</h2>
  <ul>
    <li><strong>Warm valve derogation:</strong> Meca Inox / Swagelok HDPE-sealed ball valves accepted —
        cheaper than VAT bellow-sealed, meet radiation spec. He leak rate to ambient ≤ 1×10⁻⁹ mbar·L/s
        considered unnecessarily stringent; higher rate acceptable for warm on/off service.</li>
    <li><strong>HP compressor redundancy:</strong> N+1 (3 active + 1 standby) via VFD speed control.</li>
    <li><strong>Helium recovery:</strong> Full MAC scope per CR1299.</li>
  </ul>
</div>

<div class="section">
  <h2>ROI Impact</h2>
  <p>Selecting economic warm valves over bellow-sealed alternatives saves an estimated
     <strong>30-50%</strong> on valve CAPEX while maintaining radiation compliance. The relaxed leak
     specification aligns with industry practice for warm-service helium circuits.</p>
</div>

<div class="section">
  <h2>Links</h2>
  <ul>
    <li><a href="../executive_summary.html">Full Executive Summary Dashboard</a></li>
    <li><a href="../STAKEHOLDER_PRESENTATION.html">Stakeholder Presentation</a></li>
    <li><a href="../index_v4_0.html">Technical Master Navigator (40 slides)</a></li>
  </ul>
</div>
"""
    return _page('Executive Summary', body, 'executive')


def generate_technical():
    cfg = _load_config()
    leak_classes = _load_json('leak_classes.json')
    version = cfg.get('version', '4.0.0')
    pressure = cfg.get('pressure_parameters', {}).get('wcs_hp_outlet', {})
    flow = cfg.get('flow_parameters', {}).get('wcs_hp', {})

    lc_rows = ''
    for lc in leak_classes:
        lc_rows += f"""<tr>
  <td>{lc.get('id','')}</td><td>{lc.get('title','')}</td>
  <td>{lc.get('leak_rate_mbar_l_s','')}</td>
  <td><span class="badge {lc.get('status','').lower()}">{lc.get('status','')}</span></td>
</tr>"""

    body = f"""
<div class="hero-banner" style="background:linear-gradient(135deg,#1a4731 0%,#2d7a54 100%);">
  <h1>⚙️ Technical Specifications</h1>
  <p class="subtitle">Engineering Parameters & Leak Rate Analysis</p>
</div>

<div class="kpi-row">
  <div class="kpi-card"><div class="value">{flow.get('design_flow_gs',350)} g/s</div>
    <div class="label">WCS.HP Design Flow</div></div>
  <div class="kpi-card"><div class="value">{pressure.get('nominal_barg',14)} barg</div>
    <div class="label">Nominal Outlet Pressure</div></div>
  <div class="kpi-card"><div class="value">{flow.get('redundancy_formula','N+1')}</div>
    <div class="label">Compressor Redundancy</div></div>
  <div class="kpi-card"><div class="value">{len(leak_classes)}</div>
    <div class="label">Leak Classes Defined</div></div>
</div>

<div class="section">
  <h2>Leak Rate Classifications</h2>
  <table>
    <thead><tr><th>ID</th><th>Title</th><th>Rate (mbar·L/s)</th><th>Status</th></tr></thead>
    <tbody>{lc_rows}</tbody>
  </table>
</div>

<div class="section">
  <h2>Calculation Engine</h2>
  <p>All conversions use first-principles ideal-gas calculations via
     <code>src/calc_leak_rate.py</code>. No empirical alignment factors.
     Dimensional proof chain: mbar·L/s → Pa·m³/s → mol/s → g/s → g/year.</p>
</div>

<div class="section">
  <h2>Links</h2>
  <ul>
    <li><a href="../dashboard.html">Interactive Dashboard (5 Plotly plots)</a></li>
    <li><a href="../calculations.html">Detailed Calculations</a></li>
    <li><a href="../rtm_traceability.html">RTM Traceability Matrix</a></li>
    <li><a href="../index_v4_0.html">40-Slide Master Navigator</a></li>
  </ul>
</div>
"""
    return _page('Technical Specifications', body, 'technical')


def generate_compliance():
    cfg = _load_config()
    anchors = _load_json('source_anchors.json')
    version = cfg.get('version', '4.0.0')

    anchor_rows = ''
    for a in anchors:
        anchor_rows += f"""<tr>
  <td>{a.get('id','')}</td><td>{a.get('title','')}</td>
  <td>{a.get('source_file','')}</td>
  <td><span class="badge {a.get('status','').lower()}">{a.get('status','')}</span></td>
</tr>"""

    body = f"""
<div class="hero-banner" style="background:linear-gradient(135deg,#4a1a6b 0%,#7a3d9e 100%);">
  <h1>📋 Compliance & Traceability</h1>
  <p class="subtitle">Standards, RTM Evidence, and Regulatory Alignment</p>
</div>

<div class="kpi-row">
  <div class="kpi-card"><div class="value">{len(anchors)}</div>
    <div class="label">Source Anchors Traced</div></div>
  <div class="kpi-card"><div class="value">EN 13185</div>
    <div class="label">Leak Detection Standard</div></div>
  <div class="kpi-card"><div class="value">RTM-048</div>
    <div class="label">System He Loss Cap</div></div>
  <div class="kpi-card"><div class="value">PED 2014/68/EU</div>
    <div class="label">Pressure Equipment</div></div>
</div>

<div class="section">
  <h2>Source Evidence</h2>
  <table>
    <thead><tr><th>ID</th><th>Title</th><th>Source File</th><th>Status</th></tr></thead>
    <tbody>{anchor_rows}</tbody>
  </table>
</div>

<div class="section">
  <h2>Compliance Framework</h2>
  <ul>
    <li><strong>EN 13185:</strong> Leak detection methodology for helium systems</li>
    <li><strong>RTM-048:</strong> System-level helium loss cap (≤ 1 Nm³/day ≈ 64 kg/year)</li>
    <li><strong>PED 2014/68/EU:</strong> Pressure equipment directive compliance</li>
    <li><strong>ITER QA:</strong> Quality assurance framework for cryogenic components</li>
  </ul>
</div>

<div class="section">
  <h2>Links</h2>
  <ul>
    <li><a href="../rtm_traceability.html">Full RTM Traceability Matrix</a></li>
    <li><a href="../handover.html">Handover Document</a></li>
    <li><a href="../NAVIGATOR.html">All Deliverables Navigator</a></li>
  </ul>
</div>
"""
    return _page('Compliance & Traceability', body, 'compliance')


def main():
    HEROES.mkdir(parents=True, exist_ok=True)

    pages = {
        'executive.html': generate_executive(),
        'technical.html': generate_technical(),
        'compliance.html': generate_compliance(),
    }

    for name, html in pages.items():
        path = HEROES / name
        path.write_text(html)
        print(f'  ✅  {path}')

    print(f'\n  Generated {len(pages)} hero pages in {HEROES}/')


if __name__ == '__main__':
    main()
