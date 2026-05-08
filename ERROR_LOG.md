# ERROR_LOG

## Critical error fixed (OUTPUT_1_BASELINE rebuild)

### Error description
- Prior engine applied an undocumented multiplication factor of 1000 in leak-rate to mass conversion.
- This inflated results by ~3 orders of magnitude and led to unrealistic single-valve losses.

### Root cause
- `src/calculations/engineering.py` used `CONTRACTUAL_ALIGNMENT_FACTOR = 1000`.
- The factor was presented as contractual alignment instead of a physics-based transformation.

### Corrective action
- Replaced engine with first-principles conversion in `src/calc_leak_rate.py`.
- Removed all alignment factors.
- Added dimensional proof and tests.

### Validation snapshot
- Single valve 1e-8 mbar·L/s @300K,1bar: 0.000051 g/year
- Baseline 410-valve scenario: 34.278 kg/year
- RTM-048 cap reference (1 Nm³/day): 65.20 kg/year

### Preventive controls
- Unit tests for dimensional consistency and expected ranges.
- Idempotent deterministic build (`python src/build_all.py`).
- Output hashes tracked in `OUTPUT_MANIFEST.json`.

### Legacy note
- Legacy path retained for audit: Previous baseline multiplied by CONTRACTUAL_ALIGNMENT_FACTOR=1000
