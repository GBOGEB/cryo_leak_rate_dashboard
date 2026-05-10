# Coding Agent Handover (Recursive / No-Drift Contract)

## Mission
Maintain and extend the Cryo Dashboard as an **idempotent, deterministic, self-documenting system**.

## Agent Type
- Role: Autonomous coding/maintenance agent
- Mode: Deterministic engineering build + verification
- Priority: Safety, reproducibility, traceability

## Responsibilities
1. Run `./setup.sh` before edits.
2. Implement changes in `src/` and `data/` only (unless infra/doc updates are required).
3. Rebuild using `./build.sh`.
4. Validate using `./validate.sh`.
5. Package using `./package.sh`.
6. Confirm `docs/manifest.json` matches filesystem state and test status.

## Focus Areas
- Physics correctness (`src/calc_leak_rate.py`, `src/liquid_he_loss.py`)
- Reliability logic (`src/compressor_reliability.py`, `src/wcs_scenarios.py`)
- Dashboard generation (`src/build_dashboard.py`, docs outputs)
- CI/CD and packaging reliability (`.github/workflows/build.yml`, shell scripts)

## Hard Rules (No Drift / No Dilution)
- Do not introduce non-deterministic outputs without fixed seeds and explicit rationale.
- Keep JSON writes stable (`sort_keys=True`, UTF-8, explicit schema checks).
- Preserve idempotency of setup/build/validate/package scripts.
- Ensure generated artifacts remain reproducible from repository state.
- Update tests with any behavior change.

## Output Contract
A valid handover state must include:
- Passing `./validate.sh`
- Updated `docs/manifest.json`
- Updated `docs/index.html` navigation state
- Fresh `dist/handover.zip` and `dist/handover.zip.sha256`

## Suggested Immediate Next Tasks
- Confirm compressor MTBF assumptions with vendor data
- Confirm HSD Twin Combi interpretation (M=N+1 semantics)
- Improve mobile chart responsiveness (docs CSS)
