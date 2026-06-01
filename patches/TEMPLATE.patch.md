# Patch Package: <TITLE>

> Single self-contained patch / architecture-decision / migration-manifest /
> handover document. This Markdown file is the **canonical source of truth**.
> Copy this template to `patches/YYYY-MM-DD_topic_vX.Y.patch.md` and fill in
> every section. Required headings (checked by `make patch-validate`):
> `## Metadata`, `## Summary`, `## Patch Plan`, `## Validation`, `## Rollback`.

## Metadata
- Repository: GBOGEB/<repo>
- Governance Custodian: GBOGEB/anthropic (repo id 1255640890)
- Patch Version: v0.1.0
- Patch Date: YYYY-MM-DD
- Patch Type: architecture / artifact-governance / handover
- Baseline Ref: <branch-or-commit>
- Artifact Lineage: <upstream → this patch>
- Output Mode: single-file self-contained patch manifest

## Summary
<plain-English explanation of what this patch does and why>

## Architectural Position
<ABACUS / CODEX / ARTSTYLE / governance interpretation — where this artifact
sits in the federation and which concern owns it>

## Intent
- **Scope:** <what is in scope>
- **Reason:** <why this change is needed>
- **Non-goals:** <explicitly out of scope>

## Repository Context
- Repo name: `GBOGEB/<repo>`
- Governance custodian: `GBOGEB/anthropic` (repo id `1255640890`)
- Branch / baseline: <branch>
- Artifact lineage / version: <version>

## Problem Statement
- **Architectural concern:** <what is being addressed>
- **Current ambiguity:** <what is unclear today>
- **Ownership assumptions:** <who owns what>

## Artifact Classification
<which classes are touched: schema, parser, runtime, policy, taxonomy,
federation contract, governance>

## Move Rules
- Move artifacts, not concepts.
- Only automatic refactoring is depth movement.
- No automatic cross-repo semantic moves.
- Freeze repo-level `README`, `ADR`, `CHANGELOG`.

## Artifact Ownership Rules
<table or bullets describing ownership for the affected artifacts>

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
- From:
- To:
- Reason:
- Artifact Type:
- Owning Concern:

### Move 002
- From:
- To:
- Reason:
- Artifact Type:
- Owning Concern:

## Proposed File Operations
```diff
# representative patch-style entries here
+ path/to/new/file
~ path/to/modified/file
- path/to/removed/file
```

## Files to Create
- <list of files this patch creates>

## Build / Package
```bash
make patch-validate
make patch-bundle
make handover-zip
```

## Integration Instructions
1. <local application steps>
2. <follow-up steps>

## Validation
```bash
make patch-validate
```
<what success looks like>

## Rollback
<steps to cleanly reverse this patch>

## Handover Notes
- **Risks:** <risks>
- **Open questions:** <open questions>
- **Required human review:** <review checkpoints>

## Embedded Manifest
```yaml
version: 1
repository: GBOGEB/<repo>
governance_custodian: GBOGEB/anthropic
governance_custodian_id: 1255640890
patch:
  id: <YYYY-MM-DD_topic>
  version: v0.1.0
  date: YYYY-MM-DD
  type: [architecture, artifact-governance, handover]
  baseline_ref: <branch>
  output_mode: single-file-self-contained
affected_artifacts: []
move_rules:
  automatic: [depth-move]
  forbidden: [cross-repo-semantic-move, conceptual-reassignment, history-splice]
  frozen: [README, ADR, CHANGELOG]
review:
  required: true
  custodian: GBOGEB/anthropic
```
