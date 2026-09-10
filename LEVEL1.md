# GBOGEB Level 1 — Cryo Leak Rate Dashboard

Status: `PC3_LEVEL1_CANDIDATE`
Target: `LEVEL_1_0`
Role: `INDEPENDENT_LEAK_PHYSICS_EVIDENCE_WORKER`

## Index

Human Level-1 navigator. Machine state: `level1/ssot.json`; gate manifest: `level1/manifest.json`; reusable skill: `skill/`; executable Level-1 kernel: `level1/runtime.py`.

Existing capability is reused: `data/config.yaml` is the engineering SSOT; `src/build_dashboard.py` is a build runtime; `setup.sh`, `build.sh`, and `validate.sh` provide deterministic setup/build/verification; `docs/manifest.json` already carries machine-readable project state. Level-1 binds those assets into the common worker contract instead of duplicating them.

MIP cycles: PC1 census/control, PC2 executable skill/runtime/agents, PC3 DMAIC + measured-only PCA/BT + CI orchestration proof. Structural target on this branch is 12/12 = 1.0000; observed Level-1.0 requires executed green PC3 proof.

## AOD

AOD = **Architecture–Orchestration–Decision**.

### Architecture

Owns cryogenic helium leak-rate calculations, deterministic dashboard generation, validation and independent physics/evidence outputs.

### Orchestration

Local: `engineering SSOT -> leak-rate calculation/build -> validation -> dashboard/evidence receipt`. Federated receipts may flow through the routing hub to KEB/DOW and child disposition.

### Decision authority

May validate leak-rate physics and its own deterministic artifacts. Must not self-promote independent calculations into bidder evidence, contractual compliance or QPS child authority; source class and acceptance remain explicit.

## DMAIC

- **Define:** bind worker role, SSOT/native runtime, authority and the fixed 12-gate denominator.
- **Measure:** execute the Level-1 census at exact head and record missing gates, native-runtime visibility and deterministic receipts.
- **Analyze:** prioritize MIP gaps first; use PCA/BT only on measured observations or explicit comparisons.
- **Improve:** repair the smallest executable gap while retaining the existing leak calculator/build/validation path.
- **Control:** exact-head CI compiles and executes census/MIP/orchestration, proves no-input analytics DEFER, runs self-test and uploads receipts; first red recurses on that invariant.

MIP = **Modernize (repair/reuse), Innovate (new useful nodes/edges/functions), Perpetuate (repeat exact-SHA execution and receipts).**

## PCA

PCA is a measured multivariate priority diagnostic. `python level1/runtime.py pca --input rows.json` requires real numeric observations; inadequate or zero-variance inputs DEFER. Synthetic self-test data only proves the engine. PCA can prioritize tests/features/workers but cannot override leak physics, source class or engineering/compliance authority.

## BT

Bradley–Terry is an observed pairwise priority diagnostic using explicit `[winner, loser]` comparisons. No comparisons DEFER. BT may rank repairs/alternatives, never replace independent physics evidence, bidder evidence or child disposition.

## Level-1.0 DoV

`LEVEL_1_0` requires all 12 gates true and a green exact-head `Level 1 MIP` workflow. A complete branch without executed CI remains candidate. Level-1 bootstrap creates no QPS engineering/compliance/negotiation credit.
