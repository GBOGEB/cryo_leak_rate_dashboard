# 📋 DOCX_RTM_Automation

> **MYRRHA QPLANT — Statement of Requirements, Requirements Traceability Matrix, Contract Documents**

---

## 📂 Document Library

### Contracts
| Document | Format | Reference |
|----------|--------|-----------|
| QPS Contract | PDF | `contracts/QPS_Contract_pdf.pdf` |
| QPS Contract (mirror DOCX) | PDF | `contracts/QPS_Contract_mirror_DOCX.pdf` |

### Addenda
| Document | Format | Reference |
|----------|--------|-----------|
| QPS (Addendum II) Master | DOCX | `addenda/QPS_Addendum_II_Master.docx` |
| Addendum II — Cryoplant Technical Requirements | DOCX | `addenda/` |
| Addendum II — Cryoplant Technical Requirements (1212_1521) | DOCX | `addenda/` |
| Technical Addendum — Reliability Centred | DOCX | `addenda/` |

### Specifications
| Document | Format | Reference |
|----------|--------|-----------|
| QPLANT HV02 Exhaust for KAESER | DOCX | `specifications/` |
| QPLANT Helium Recovery and Supply MAC — CR1299 | DOCX | `specifications/` |
| QPLANT Interface and Terminal Points ACC NF | DOCX | `specifications/` |

### Requirements
| Document | Format | Reference |
|----------|--------|-----------|
| SoR Requirements Matrix | CSV | `requirements/SoR_Requirements_Matrix.csv` |
| RTM-047..067 Traceability | CSV | `traceability/` |

---

## 📁 Structure

```
DOCX_RTM_Automation/
├── contracts/
│   ├── QPS_Contract_pdf.pdf
│   └── QPS_Contract_mirror_DOCX.pdf
├── addenda/
│   ├── QPS_Addendum_II_Master.docx
│   ├── Addendum_II_Cryoplant_Technical_Requirements.docx
│   ├── Addendum_II_Cryoplant_Technical_Requirements_1212_1521.docx
│   └── Technical_Addendum_Reliability_centred.docx
├── specifications/
│   ├── QPLANT_HV02_exhaust_for_KAEZER.docx
│   ├── QPLANT_Helium_Recovery_and_Supply_MAC_CR1299.docx
│   └── QPLANT_Interface_and_Terminal_Points_ACC_NF.docx
├── requirements/
│   └── SoR_Requirements_Matrix.csv
├── traceability/
│   └── RTM_047_067.csv
├── pipeline/                # Automation scripts
├── README.md
└── requirements.txt
```

---

## 🏗️ Related Repositories

| Repo | Relationship |
|------|-------------|
| [cryo_leak_rate_dashboard](https://github.com/GBOGEB/cryo_leak_rate_dashboard) | Implements requirements as dashboard |
| [CODEX](https://github.com/GBOGEB/CODEX) | Engineering libraries derived from requirements |
| [ABACUS](https://github.com/GBOGEB/ABACUS) | Analysis work validating requirements |
