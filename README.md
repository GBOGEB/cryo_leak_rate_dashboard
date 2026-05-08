# Cryogenic Leak-Rate Dashboard (Fixed Baseline)

This repository rebuilds `OUTPUT_1_BASELINE` with corrected leak-rate physics and a full triage output system.

## Build
```bash
python src/build_all.py
```

## Output structure
- `docs/`: GitHub Pages-ready HTML views + `handover.pdf`
- `source/`: markdown source pack
- `data/`: classified input objects
- `outputs/tables`: generated CSV/JSON evidence tables
- `OUTPUT_MANIFEST.json`: deterministic output registry with hashes

## Audience views
- `docs/executive_summary.html` (manager)
- `docs/dashboard.html` (engineer)
- `docs/calculations.html` (specialist)
- `docs/rtm_traceability.html` (specialist / QA)
- `docs/handover.html` + `docs/handover.pdf` (formal handover)
