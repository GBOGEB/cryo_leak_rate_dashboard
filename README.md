# Cryogenic Leak Rate Analysis Dashboard

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
