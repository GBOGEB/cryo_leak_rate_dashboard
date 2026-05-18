# 🧊 Cryo Leak Rate Dashboard

> **MYRRHA QPLANT — Cryogenic Helium Leak-Rate Analysis Dashboard v4.0.0**

[![Build](https://i.ytimg.com/vi/GlqQGLz6hfs/hqdefault.jpg)
[![Tests](https://placehold.co/1200x600/e2e8f0/1e293b?text=continuous_integration__CI__build_status_badge_fro)
[![Pages](https://i.ytimg.com/vi/jfL6I0VDgGw/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCDIgyqNGN9bFR2zNmXseZOxGqRGw)

---

## 🔗 Live Dashboard

| View | URL | Audience |
|------|-----|----------|
| **Master Navigator** (42 slides) | [index_v4_0.html](https://gbogeb.github.io/cryo_leak_rate_dashboard/index_v4_0.html) | All |
| **Stakeholder Presentation** (10 slides) | [STAKEHOLDER_PRESENTATION.html](https://gbogeb.github.io/cryo_leak_rate_dashboard/STAKEHOLDER_PRESENTATION.html) | Management |
| **Triage Dashboard** | [dashboard.html](https://gbogeb.github.io/cryo_leak_rate_dashboard/dashboard.html) | Engineers |
| **Executive Summary** | [executive_summary.html](https://gbogeb.github.io/cryo_leak_rate_dashboard/executive_summary.html) | Decision-makers |
| **Calculations Detail** | [calculations.html](https://gbogeb.github.io/cryo_leak_rate_dashboard/calculations.html) | Specialists |
| **RTM Traceability** | [rtm_traceability.html](https://gbogeb.github.io/cryo_leak_rate_dashboard/rtm_traceability.html) | QA |

---

## 🚀 Quick Start

### Users
Open the [Live Dashboard](https://gbogeb.github.io/cryo_leak_rate_dashboard/) — no install needed.

### Developers
```bash
git clone https://github.com/GBOGEB/cryo_leak_rate_dashboard.git
cd cryo_leak_rate_dashboard
./setup.sh        # Install dependencies
./build.sh        # Generate all outputs
./validate.sh     # Run tests (18 tests)
./package.sh      # Create handover.zip
```

---

## 📁 Project Structure

```
cryo_leak_rate_dashboard/
├── src/                    # Python source code
│   ├── calc_leak_rate.py   # Core physics engine (first-principles)
│   ├── generate_dashboard.py  # HTML/plot generator
│   ├── build_all.py        # Master build orchestrator
│   └── ...
├── data/                   # Configuration & input data (JSON/YAML)
│   ├── config.yaml         # SSoT configuration
│   ├── scenarios.json      # System-level scenarios
│   ├── leak_classes.json   # Leak rate classifications
│   └── valve_candidates.json  # Valve comparison data
├── docs/                   # Generated HTML pages (GitHub Pages root)
│   ├── index_v4_0.html     # 42-slide master navigator
│   ├── plots/              # Interactive Plotly charts
│   └── assets/             # CSS + JS
├── tests/                  # pytest test suite
├── outputs/                # Generated tables & plots
├── scripts/                # CI/CD and utility scripts
├── dist/                   # Packaged artifacts
└── traceability/           # RTM CSV files
```

---

## 🔬 Core Physics

The calculation engine (`src/calc_leak_rate.py`) uses **first-principles ideal gas law** to convert helium leak rates:

```
mbar·L/s → Pa·m³/s → mol/s → g/s → g/year → kg/year
```

No empirical alignment factors. Fully traceable dimensional chain.

---

## 🏗️ Related Repositories

| Repo | Purpose |
|------|---------|
| [CODEX](https://github.com/GBOGEB/CODEX) | Reusable engineering libraries (MCB blocks) |
| [ABACUS](https://github.com/GBOGEB/ABACUS) | Analysis notebooks, CodeLLM artifacts |
| [DOCX_RTM_Automation](https://github.com/GBOGEB/DOCX_RTM_Automation) | SoR, RTM, contract documents |
| [document-organization-system](https://github.com/GBOGEB/document-organization-system) | Document hub, v3 legacy dashboard |

---

## 📜 License

Internal — SCK CEN / MYRRHA Project
