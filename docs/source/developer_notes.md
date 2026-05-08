# Developer Notes

## Rebuild command
```bash
python src/build_all.py
```

## Extension points
- Edit `data/*.json` to change leak classes, valve candidates, and scenarios.
- Update formulas in `src/calc_leak_rate.py` only if first-principles derivation is preserved.
- Add new figures in `src/generate_dashboard.py` and link from `docs/dashboard.html`.

## Determinism policy
- All writes are idempotent (`write_text_if_changed`).
- Manifest uses sorted paths and stable JSON serialization.

## DMAIC View Note
- DEFINE: Maintenance guide for future contributors.
- MEASURE: Documents commands and extension points.
- ANALYZE: Shows where changes can break traceability.
- IMPROVE: Reduces onboarding effort.
- CONTROL: Tests in `tests/` gate regressions.
