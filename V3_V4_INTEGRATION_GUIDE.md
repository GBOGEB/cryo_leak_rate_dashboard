# v3 / v4 Integration Guide

> **Generated:** 2026-05-18  
> **Scope:** How to connect the Material Properties Dashboard (v3) and Leak Rate Dashboard (v4)

---

## 1 — Repository Summary

| Property | v3 — Material Properties | v4 — Leak Rate Analysis |
|----------|--------------------------|------------------------|
| **Repo** | `document-organization-system` | `cryo_leak_rate_dashboard` |
| **Version** | v0.4.9 | v4.0.0 |
| **GitHub** | [GBOGEB/document-organization-system](https://github.com/GBOGEB/document-organization-system) | ⚠️ Not yet created |
| **Pages URL** | `gbogeb.github.io/document-organization-system/cryo_dashboard_v0_3_0/cryo_dashboard_v0_3_0/` | `gbogeb.github.io/cryo_leak_rate_dashboard/` (planned) |
| **Engine** | JavaScript (browser-side) | Python (build-time) |
| **Focus** | k(T), cp(T), Y(T) for 10 materials | He leak → mass flow → cost |
| **PRs** | 23 merged | Local only |
| **Tests** | 823 NIST parity assertions | 18 pytest tests |
| **HTML files** | 7 interactive + 8 analysis | 84 static |

---

## 2 — Integration Strategy

### Approach: Cross-Link (NOT Submodule)

**Rationale:**
- v3 and v4 are **different engineering domains** (material properties vs. leak rates)
- v3 is **actively developed** (23 PRs, NIST parity tests, v0.4.9)
- v3 updates independently and frequently
- Submodule complexity is not justified

**Integration method: Hyperlinks in both directions**

```
v4 (cryo_leak_rate_dashboard)          v3 (document-organization-system)
┌─────────────────────────┐            ┌─────────────────────────┐
│ VERSION_SELECTOR.html   │───────────→│ dashboard_modular.html  │
│ NAVIGATOR.html          │───────────→│ index_slides.html       │
│ index_v4_0.html         │            │                         │
│                         │            │ index.html              │
│                         │◄───────────│ (link back to v4)       │
└─────────────────────────┘            └─────────────────────────┘
```

---

## 3 — Step-by-Step Integration

### Step 1: Verify v3 is clean and deployed

```bash
cd /home/ubuntu/github_repos/document-organization-system
git status          # Should be clean
git log --oneline -3
# Latest: 6f08258 — Merge PR #23

# Verify GitHub Pages is live:
# https://gbogeb.github.io/document-organization-system/cryo_dashboard_v0_3_0/cryo_dashboard_v0_3_0/
```

**Status:** ✅ v3 is clean, pushed, and GitHub Pages is active.

### Step 2: Create `cryo_leak_rate_dashboard` GitHub repo

The user must create this repo on GitHub:
1. Go to [github.com/new](https://github.com/new)
2. Name: `cryo_leak_rate_dashboard`
3. Description: "MYRRHA QPLANT Cryogenic Leak Rate Analysis Dashboard v4.0.0"
4. Visibility: Private (or Public for GitHub Pages free tier)
5. Do NOT initialize with README (we have one)

### Step 3: Push v4 to GitHub

```bash
cd /home/ubuntu/cryo_leak_rate_dashboard
git remote add origin https://github.com/GBOGEB/cryo_leak_rate_dashboard.git
git push -u origin main
```

### Step 4: Deploy VERSION_SELECTOR.html

The `docs/VERSION_SELECTOR.html` is already created. To make it the root landing page:

**Option A: Keep current structure (simpler)**
```
docs/index.html → existing landing page (keep as-is)
docs/VERSION_SELECTOR.html → accessible at /VERSION_SELECTOR.html
```

**Option B: Replace root index (requires build system update)**
```bash
# Only do this after updating build scripts
cp docs/VERSION_SELECTOR.html docs/index.html
```

### Step 5: Enable GitHub Pages for v4

```
Repository Settings → Pages
Source: Deploy from branch
Branch: main
Folder: /docs
```

### Step 6: Add cross-link in v3

Optionally add a link from v3 back to v4. In `document-organization-system`, add to the v3 `index.html`:

```html
<a href="https://gbogeb.github.io/cryo_leak_rate_dashboard/">
  → QPLANT Leak Rate Dashboard (v4.0.0)
</a>
```

---

## 4 — URL Map After Deployment

### v4 URLs (cryo_leak_rate_dashboard)

| URL | Content |
|-----|---------|
| `gbogeb.github.io/cryo_leak_rate_dashboard/` | Landing (index.html) |
| `.../VERSION_SELECTOR.html` | Version selector with v3/v4 cards |
| `.../NAVIGATOR.html` | Card-based entry point |
| `.../index_v4_0.html` | 42-slide technical navigator |
| `.../STAKEHOLDER_PRESENTATION.html` | 10-slide executive deck |
| `.../dashboard.html` | Triage dashboard |
| `.../calculations.html` | Detailed calculations |
| `.../rtm_traceability.html` | RTM traceability |
| `.../visualizations/*.html` | 27 Plotly charts |
| `.../visualizations_v3/*.html` | 22 advanced analytics |
| `.../plots/*.html` | 5 core plots |
| `.../heroes/*.html` | 10 audience pages |
| `.../compressors/*.html` | HP redundancy + WCS protection |
| `.../liquid_he/*.html` | Liquid operations guide |
| `.../archive/*.html` | 3 archived presentations |

### v3 URLs (document-organization-system) — unchanged

| URL | Content |
|-----|---------|
| `gbogeb.github.io/document-organization-system/cryo_dashboard_v0_3_0/cryo_dashboard_v0_3_0/` | v3 Landing |
| `.../dashboard_modular.html` | Interactive material properties |
| `.../material_properties_dashboard_v1_10.html` | Legacy fallback |
| `.../files.html` | File browser |
| `.../index_slides.html` | Presentation |
| `.../ssot_launcher.html` | SSOT launcher |

---

## 5 — Testing Checklist

After deployment, verify all links work:

- [ ] `gbogeb.github.io/cryo_leak_rate_dashboard/` loads
- [ ] VERSION_SELECTOR.html displays both cards
- [ ] v4 NAVIGATOR.html card links work
- [ ] v4 index_v4_0.html loads with 42 slides
- [ ] v4 STAKEHOLDER_PRESENTATION.html loads with 10 slides
- [ ] v4 visualizations load (at least spot-check 3)
- [ ] v4 hero pages load (at least spot-check 2)
- [ ] v3 link from VERSION_SELECTOR opens material properties dashboard
- [ ] v3 dashboard_modular.html is fully interactive
- [ ] v3 → v4 cross-link works (if added)
- [ ] All relative paths in v4 HTML resolve correctly

---

## 6 — Future Considerations

### Material Properties Integration into v4
If v4 ever needs to reference v3 material property data directly:
1. v3 exports CSV/JSON from its interactive dashboard
2. v4 can import those as `data/material_properties_export.json`
3. No need for submodule — just data file exchange

### Shared SSoT Patterns
Both v3 and v4 follow the SSoT pattern:
- v3: `ssot.json` (material catalog, architecture, methods)
- v4: `data/config.yaml` + `data/*.json` (leak classes, scenarios, valves)

### Version Evolution
- v3 may evolve to v0.5.x, v0.6.x (new materials, methods)
- v4 may evolve to v4.1.x (new analysis, updated specs)
- Both maintain independent version lineages
