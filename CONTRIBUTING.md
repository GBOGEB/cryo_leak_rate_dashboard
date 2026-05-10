# Contributing Guide

## Development Workflow

1. Create/update source logic in `src/`.
2. Rebuild with `./build.sh`.
3. Run `./validate.sh` (must pass).
4. Package with `./package.sh` before release/handover.

## Adding New Analysis Modules

- Add new module under `src/`.
- Keep calculations deterministic (fixed seeds, explicit constants).
- Export outputs to `docs/` and/or `outputs/` consistently.
- Register artifacts in manifest generation logic (`build.sh` Python manifest block).

## Updating Standards Database

- Edit `data/standards_compliance.json`.
- Preserve existing key schema (`standards`, `rtm_to_standards_mapping`, `lifecycle_phases`).
- Re-run `./setup.sh` or `./build.sh`.

## Adding New Visualizations

- Generate chart HTML under `docs/visualizations_v3/`.
- Add chart data CSV under `docs/visualizations_v3/data/` when possible.
- Link new artifacts from `docs/index.html` (via `src/build_dashboard.py`) if user-facing.

## Testing Requirements

All contributions must:
- pass `./validate.sh`,
- keep manifest checksums consistent,
- avoid non-deterministic output changes unless intentional and documented.

## Commit Message Format

Use conventional-style prefixes:
- `feat:` new feature
- `fix:` bug fix
- `docs:` documentation
- `test:` test updates
- `build:` build/CI changes
- `refactor:` internal improvements

Examples:
- `feat: add WCS scenario transient simulation`
- `fix: correct helium density fallback at 4.2K`
- `build: refresh manifest checksum tracking`
