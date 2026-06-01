# `patches/` — Repository Output Contract

This directory defines the **output contract** for architectural and
artifact-governance changes in this repository (and, by convention, across the
`GBOGEB` federation custodied by [`GBOGEB/anthropic`](https://github.com/GBOGEB/anthropic),
repo id `1255640890`).

## The contract

Each architectural / governance change is delivered as **one self-contained
`*.patch.md` file**. That single Markdown file is the canonical source of truth
and serves multiple roles at once:

- patch description
- architecture decision note
- migration manifest
- handover artifact
- packaging recipe
- local integration guide

Supporting files (`Makefile` targets, `manifest/`, `handover/`, `scripts/`) are
**optional** and are generated from or validated against the patch file. A single
Markdown file is preferred because it is human-reviewable, versionable, diffable,
archivable, and convertible into bundle contents.

## Naming convention

```
patches/YYYY-MM-DD_topic_vX.Y.patch.md
```

Components: **date** · **topic** · **version** · type suffix `.patch.md`.

Examples:

```
patches/2026-06-01_artifact-federation-refactor.patch.md
patches/2026-06-01_federated-artifact-ownership_v0.1.patch.md
patches/2026-06-01_abacus-codex-artstyle-governance_handover.patch.md
```

## Required sections

Every `*.patch.md` must contain at least these headings (enforced by
`make patch-validate`):

- `## Metadata`
- `## Summary`
- `## Patch Plan`
- `## Validation`
- `## Rollback`

The full recommended structure is captured in [`TEMPLATE.patch.md`](TEMPLATE.patch.md):
Intent, Repository Context, Problem Statement, Artifact Classification, Move Rules,
Patch Plan, Proposed File Operations, Integration Instructions, Packaging,
Handover Notes, and an Embedded Manifest.

## Authoring a new patch

1. Copy the template:
   ```bash
   cp patches/TEMPLATE.patch.md patches/$(date +%F)_my-topic_v0.1.patch.md
   ```
2. Fill in every section.
3. Register the patch under `patches:` in `manifest/artifact-topology.yaml`.
4. Validate, then optionally bundle:
   ```bash
   make patch-validate
   make patch-bundle
   make handover-zip
   ```

## Move rules (governance)

- Move **artifacts, not concepts**.
- The only automatic refactoring is **depth movement** within a repo.
- **No** automatic cross-repo semantic moves — these are proposals requiring
  custodian review in `anthropic`.
- **Freeze** repo-level `README`, `ADR`, and `CHANGELOG`.
