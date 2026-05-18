# 🧱 CODEX

> **MCB (Modular Code Blocks) via MCP — Reusable Engineering Libraries**

---

## 📦 Module Catalog

### Cryogenics
| Module | Description | Source |
|--------|-------------|--------|
| `codex.cryogenics.leak_rate` | Helium leak-rate → mass-flow conversions (ideal gas law) | Extracted from cryo_leak_rate_dashboard |
| `codex.cryogenics.liquid_he` | Liquid helium inventory loss calculations | Extracted from cryo_leak_rate_dashboard |

### Materials
| Module | Description | Source |
|--------|-------------|--------|
| `codex.materials.properties` | Material properties database (He, AISI316, CuRRR100) | cryo_leak_rate_dashboard + CoolProp |

### Reliability
| Module | Description | Source |
|--------|-------------|--------|
| `codex.reliability.compressor` | HP compressor N+1 redundancy analysis | cryo_leak_rate_dashboard |
| `codex.reliability.risk` | Risk model for cryogenic systems | cryo_leak_rate_dashboard |

### Statistics
| Module | Description | Source |
|--------|-------------|--------|
| `codex.statistics.monte_carlo` | Monte Carlo simulation framework | cryo_leak_rate_dashboard |

### Scenarios
| Module | Description | Source |
|--------|-------------|--------|
| `codex.scenarios.wcs` | WCS.HP supply protection logic | cryo_leak_rate_dashboard |

---

## 🚀 Usage

```python
from codex.cryogenics.leak_rate import leak_rate_to_mass_flow_g_year

# Convert 1e-9 mbar·L/s at 4K, 12 bar to g/year
result = leak_rate_to_mass_flow_g_year(1e-9, temperature_k=4.0, pressure_bar=12.0)
print(f"Mass loss: {result:.4f} g/year")
```

---

## 📁 Structure

```
CODEX/
├── codex/
│   ├── __init__.py
│   ├── cryogenics/
│   │   ├── __init__.py
│   │   ├── leak_rate.py
│   │   └── liquid_he.py
│   ├── materials/
│   │   ├── __init__.py
│   │   └── properties.py
│   ├── reliability/
│   │   ├── __init__.py
│   │   ├── compressor.py
│   │   └── risk.py
│   ├── statistics/
│   │   ├── __init__.py
│   │   └── monte_carlo.py
│   └── scenarios/
│       ├── __init__.py
│       └── wcs.py
├── tests/
├── README.md
├── setup.py
└── requirements.txt
```

---

## 🏗️ Related Repositories

| Repo | Relationship |
|------|-------------|
| [cryo_leak_rate_dashboard](https://github.com/GBOGEB/cryo_leak_rate_dashboard) | Primary consumer of CODEX modules |
| [ABACUS](https://github.com/GBOGEB/ABACUS) | Analysis notebooks using CODEX |
| [DOCX_RTM_Automation](https://github.com/GBOGEB/DOCX_RTM_Automation) | Requirements source |
