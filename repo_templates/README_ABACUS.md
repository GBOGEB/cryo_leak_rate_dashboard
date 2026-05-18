# 🔬 ABACUS

> **CodeLLM & Deep Agent — Analysis, Notebooks, and Computational Studies**

---

## 📊 Analysis Catalog

### Compressor Studies
| Analysis | Format | Status |
|----------|--------|--------|
| MYRRHA warm-compressor comparison (ALaT FSD 575 vs LKT FSD 475) | Markdown + interactive HTML | ✅ Complete |
| HP compressor frequency-flow mapping | Notebook | 🔄 In progress |

### Vendor Reviews
| Review | Format | Status |
|--------|--------|--------|
| Cryoworld offer analysis (warm valves) | PowerPoint + notes | ✅ Complete |
| Meca Inox ball valve assessment | Markdown | ✅ Complete |
| Swagelok SS-42GSE assessment | Markdown | ✅ Complete |

### Leak Rate Analysis
| Analysis | Format | Status |
|----------|--------|--------|
| Helium leak rate dimensional proof | Python + HTML | ✅ Complete |
| Fleet sensitivity (410 valves @ mixed envelope) | Python + Plotly | ✅ Complete |
| RTM-048 system cap validation (1 Nm³/day → 60-70 kg/year) | Python test | ✅ Complete |

### Material Properties
| Analysis | Format | Status |
|----------|--------|--------|
| Helium properties (gas + liquid phases) | JSON database | ✅ Complete |
| AISI316 thermal conductivity (4K–300K) | Romberg integration | ✅ Complete |
| CuRRR100 thermal conductivity | Romberg integration | ✅ Complete |

---

## 📁 Structure

```
ABACUS/
├── analyses/
│   ├── compressors/
│   │   └── warm_compressor_comparison_ALaT_LKT.md
│   ├── valves/
│   │   └── warm_valve_leak_tightness_derogation.md
│   └── materials/
│       └── helium_properties_study.md
├── notebooks/
│   ├── 01_leak_rate_sensitivity.ipynb
│   ├── 02_monte_carlo_fleet.ipynb
│   └── 03_compressor_frequency_mapping.ipynb
├── vendor_reviews/
│   ├── cryoworld_offer_1.md
│   └── valve_vendor_comparison.md
├── data/
│   ├── materials/
│   └── compressor_specs/
├── README.md
└── requirements.txt
```

---

## 🏗️ Related Repositories

| Repo | Relationship |
|------|-------------|
| [cryo_leak_rate_dashboard](https://github.com/GBOGEB/cryo_leak_rate_dashboard) | Consumes analysis results |
| [CODEX](https://github.com/GBOGEB/CODEX) | Provides calculation libraries |
| [DOCX_RTM_Automation](https://github.com/GBOGEB/DOCX_RTM_Automation) | Requirements source |
