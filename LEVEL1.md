# GBOGEB Level 1 — Cryo Leak Rate Dashboard

Status: `PC1_CONTROL_PLANE`
Target: `LEVEL_1_0`
Role: `INDEPENDENT_LEAK_PHYSICS_EVIDENCE_WORKER`

## Index

Human Level-1 navigator. Machine state: `level1/ssot.json`; gate manifest: `level1/manifest.json`; reusable skill: `skill/`; executable Level-1 kernel arrives in PC2.

Existing capability is reused: `data/config.yaml` is the engineering SSOT; `src/build_dashboard.py` is a build runtime; `setup.sh`, `build.sh`, and `validate.sh` provide deterministic setup/build/verification; `docs/manifest.json` already carries machine-readable project state. Level-1 binds those assets into the common worker contract instead of duplicating them.

MIP cycles: PC1 census/control, PC2 executable skill/runtime/agents, PC3 DMAIC + measured-only PCA/BT + CI orchestration proof. Structural targets are 0.3333 -> 0.7500 -> 1.0000; observed Level-1.0 requires executed green PC3 proof.

## AOD

AOD = **Architecture–Orchestration–Decision**.

### Architecture

Owns cryogenic helium leak-rate calculations, deterministic dashboard generation, validation and independent physics/evidence outputs.

### Orchestration

Local: `engineering SSOT -> leak-rate calculation/build -> validation -> dashboard/evidence receipt`. Federated receipts may flow through the routing hub to KEB/DOW and child disposition.

### Decision authority

May validate leak-rate physics and its own deterministic artifacts. Must not self-promote independent calculations into bidder evidence, contractual compliance or QPS child authority; source class and acceptance remain explicit.
