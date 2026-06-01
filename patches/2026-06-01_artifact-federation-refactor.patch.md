# Patch Package: Artifact Federation Refactor

> Single self-contained patch / architecture-decision / migration-manifest /
> handover document. This Markdown file is the **canonical source of truth**;
> all supporting files (`Makefile` targets, `manifest/`, `handover/`,
> `scripts/`) are generated from or validated against it.

## Metadata
- Repository: GBOGEB/cryo_leak_rate_dashboard
- Governance Custodian: GBOGEB/anthropic (repo id 1255640890)
- Patch Version: v0.1.0
- Patch Date: 2026-06-01
- Patch Type: architecture / artifact-governance / handover
- Baseline Ref: main
- Artifact Lineage: cryo_leak_rate_dashboard v4.0.0 → federation output contract v0.1.0
- Output Mode: single-file self-contained patch manifest

## Summary
This patch introduces a **repository output contract**: every architectural or
artifact-governance change is delivered as a single, fully self-contained
`*.patch.md` file under `patches/`. The file simultaneously serves as patch
description, architecture decision note, migration manifest, handover artifact,
packaging recipe, and local integration guide. Optional `Makefile`/`scripts`
support converts the Markdown into a zip / handover bundle locally, but the
Markdown remains the primary deliverable.

## Architectural Position
Within the federation (`anthropic` governance, `ABACUS` analysis, `CODEX`
libraries, `DOCX_RTM_Automation` requirements), `anthropic` acts as the
**governance / custodian layer**, not as a runtime or primitive-library repo.
Accordingly, patch packages emphasize policy, taxonomy, artifact-routing, review
checkpoints, and constraints on movement — rather than implementation-heavy
runtime code.

## Intent
- **Scope:** Define and seed the `*.patch.md` output contract plus its optional
  local packaging workflow inside this repository.
- **Reason:** Architecture / artifact-governance changes need one human-reviewable,
  versionable, diffable, archivable artifact that can be converted into a handover
  bundle.
- **Non-goals:**
  - No automatic semantic cross-repo moves.
  - No conceptual reassignment of artifacts without human review.
  - No rewriting or splicing of repo-level history files (`README`, `ADR`,
    `CHANGELOG`).
  - No changes to runtime engineering code (`src/`, `data/`, `tests/`).

## Repository Context
- Repo name: `GBOGEB/cryo_leak_rate_dashboard`
- Governance custodian: `GBOGEB/anthropic` (repo id `1255640890`)
- Branch / baseline: `main`
- Artifact lineage / version: dashboard v4.0.0; this contract v0.1.0

## Problem Statement
- **Architectural concern:** Federation artifacts (schemas, parsers, runtime,
  policy, taxonomy, federation contracts, governance docs) currently lack a single
  canonical hand-off format, so changes are described inconsistently across repos.
- **Current ambiguity:** It is unclear which repository owns a given artifact, what
  may be moved automatically, and what requires review.
- **Ownership assumptions:** `anthropic` owns governance/policy/taxonomy;
  consuming repos own their own runtime artifacts and emit patch packages for any
  cross-cutting change.

## Artifact Classification
| Class | Description | Typical owner |
|-------|-------------|---------------|
| schema | Data contracts / JSON-YAML shapes | producing repo |
| parser | Format readers / loaders | producing repo |
| runtime | Executable engineering code | producing repo |
| policy | Governance rules / constraints | `anthropic` |
| taxonomy | Classification vocabulary | `anthropic` |
| federation contract | Cross-repo interfaces | `anthropic` (custodian) |
| governance | Review checkpoints / handover docs | `anthropic` |

## Move Rules
- Move **artifacts, not concepts**.
- The only automatic refactoring permitted is **depth movement** (relocating an
  artifact deeper in the same repo's tree).
- **No** automatic cross-repo semantic moves.
- **Freeze** repo-level `README`, `ADR`, and `CHANGELOG` (never auto-spliced).

## Artifact Ownership Rules
- A patch package may move artifacts **within** the repository it lives in.
- Cross-repo moves are described as *proposals* only and require custodian review
  in `anthropic`.
- Each moved artifact records: source path, target path, move type, rationale, and
  owning concern.
- Manifest additions (`manifest/`) and packaging support (`Makefile`, `scripts/`)
  are always allowed.

## Refactor Constraints
- Allowed:
  - move artifacts deeper in the tree
  - add manifests
  - add setup / make packaging
- Not allowed:
  - automatic semantic cross-repo moves
  - conceptual reassignment without review
  - splicing repo-level history files

## Patch Plan
### Move 001
- From: _(none — additive)_
- To: `patches/2026-06-01_artifact-federation-refactor.patch.md`
- Reason: Establish the canonical patch-package artifact.
- Artifact Type: governance
- Owning Concern: federation output contract

### Move 002
- From: _(none — additive)_
- To: `patches/TEMPLATE.patch.md`
- Reason: Provide a reusable skeleton enforcing the contract structure.
- Artifact Type: governance
- Owning Concern: documentation / reuse

### Move 003
- From: _(none — additive)_
- To: `manifest/artifact-topology.yaml`
- Reason: Machine-readable federation topology + patch index.
- Artifact Type: federation contract
- Owning Concern: artifact-routing

## Proposed File Operations
```diff
+ patches/2026-06-01_artifact-federation-refactor.patch.md
+ patches/TEMPLATE.patch.md
+ patches/README.md
+ manifest/artifact-topology.yaml
+ handover/README.md
+ scripts/package_patch.sh
~ Makefile        # add: patch-bundle, handover-zip, patch-validate
```

## Files to Create
- `patches/TEMPLATE.patch.md`
- `patches/README.md`
- `manifest/artifact-topology.yaml`
- `handover/README.md`
- `scripts/package_patch.sh`
- `Makefile` additions (no new build tools introduced)

## Build / Package
```bash
make patch-validate    # check every patches/*.patch.md has required sections
make patch-bundle      # assemble handover bundle under dist/
make handover-zip      # zip the bundle + emit sha256 + manifest
```

## Integration Instructions
1. **Apply locally:** the files in *Proposed File Operations* are committed by this
   patch; no manual application is required when consuming this branch.
2. **Author a new patch:** copy `patches/TEMPLATE.patch.md` to
   `patches/YYYY-MM-DD_topic_vX.Y.patch.md` and fill in every section.
3. **Register it:** add an entry under `patches:` in
   `manifest/artifact-topology.yaml`.

## Validation
```bash
make patch-validate
```
Confirms each `patches/*.patch.md` contains the required headings
(`## Metadata`, `## Summary`, `## Patch Plan`, `## Validation`, `## Rollback`).

## Rollback
- Remove the added files (`patches/`, `manifest/`, `handover/`,
  `scripts/package_patch.sh`) and revert the `Makefile` additions.
- No runtime code, data, or repo-level history files are touched, so rollback is a
  clean reverse of this additive patch.

## Handover Notes
- **Risks:** low — additive, documentation/governance only; no runtime impact.
- **Open questions:** confirm whether `anthropic` wants patch packages mirrored
  into its governance repo or only referenced by id.
- **Required human review:** custodian sign-off in `anthropic` before any
  cross-repo artifact move described by a future patch is executed.

## Embedded Manifest
```yaml
version: 1
repository: GBOGEB/cryo_leak_rate_dashboard
governance_custodian: GBOGEB/anthropic
governance_custodian_id: 1255640890
patch:
  id: 2026-06-01_artifact-federation-refactor
  version: v0.1.0
  date: 2026-06-01
  type: [architecture, artifact-governance, handover]
  baseline_ref: main
  output_mode: single-file-self-contained
affected_artifacts:
  - path: patches/2026-06-01_artifact-federation-refactor.patch.md
    class: governance
  - path: patches/TEMPLATE.patch.md
    class: governance
  - path: manifest/artifact-topology.yaml
    class: federation-contract
move_rules:
  automatic: [depth-move]
  forbidden: [cross-repo-semantic-move, conceptual-reassignment, history-splice]
  frozen: [README, ADR, CHANGELOG]
review:
  required: true
  custodian: GBOGEB/anthropic
```
