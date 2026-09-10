# MIP Rollout Tracker - cryo_leak_rate_dashboard

Date: 2026-09-10
Scope: public GBOGEB repo follow-up for Modernize, Innovate, Perpetuate.

## Repo Role

Cryogenic leak-rate dashboard and reporting surface. This repo is a natural metric-history and visualisation endpoint for MIP, but it needs source/generated/deployment clarity first.

## MIP Position

| Layer | Status | First Gate |
| --- | --- | --- |
| Modernize | OPEN | Classify large artifact/report surface and validate build/deploy scripts. |
| Innovate | OPEN | Use dashboard as MIP metric-history surface after data contracts stabilise. |
| Perpetuate | OPEN | CI/deploy receipts with exact commit SHA and generated output hashes. |

## TODO

1. Run repo census: dashboards, source, tables, traces, generated reports, deployment config, CI workflows.
2. Execute or repair `validate.sh` and `build.sh` as the first observed contract.
3. Split runtime inputs, generated outputs, and human report artifacts.
4. Add metric-history rows for MIP pulse tracking once validation is green.
5. Connect dashboard inputs to cryogenic-accelerator-workspace SSOT outputs.

## DoD

- Validation/build status is observed and tied to an exact SHA.
- Generated artifacts are labelled separately from maintained source.
- Dashboard input contract is named.
- Metric-history view is ready for repo-level and cross-repo MIP progress.

## DoV

WITHHELD until validation/build proof is observed. Current PR is triage/control only.
