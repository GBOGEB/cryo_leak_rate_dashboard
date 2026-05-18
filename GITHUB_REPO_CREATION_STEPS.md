# GitHub Repository Creation — Step-by-Step with Progress

## 🎯 Goal
Create `https://github.com/GBOGEB/cryo_leak_rate_dashboard`, push v4.0.0,
and enable GitHub Pages at `https://gbogeb.github.io/cryo_leak_rate_dashboard/`.

## ⏱️ Total time: ~10 minutes

---

## 📋 Checklist (follow in order)

### Step 1 — Create repository on GitHub
⏱️ ~2 minutes

1. [ ] Open browser: <https://github.com/new>
2. [ ] **Owner:** `GBOGEB` (your account)
3. [ ] **Repository name:** `cryo_leak_rate_dashboard`
4. [ ] **Description:**
   ```
   MYRRHA QPLANT Cryogenic Helium Leak Rate Analysis Dashboard v4.0.0
   Single Source of Truth (SSoT) implementation with 3 HP compressors
   ```
5. [ ] **Visibility:**
   - ✅ Public (recommended — free GitHub Pages)
   - OR Private (needs GitHub Pro for Pages)
6. [ ] **Initialize:**
   - ❌ Do NOT add README
   - ❌ Do NOT add .gitignore
   - ❌ Do NOT add license
   (We already have these locally — adding them on GitHub will cause a merge conflict)
7. [ ] Click **Create repository**
8. [ ] ✅ Mark complete

**Expected result:** Empty repo at `https://github.com/GBOGEB/cryo_leak_rate_dashboard`.

---

### Step 2 — Copy the push commands GitHub shows you
⏱️ ~1 minute

GitHub will display a block like:

```bash
git remote add origin https://github.com/GBOGEB/cryo_leak_rate_dashboard.git
git branch -M main
git push -u origin main
```

1. [ ] ✅ Copy/note these commands (we'll adapt slightly below)
2. [ ] Keep the GitHub tab open

---

### Step 3 — Execute the push from this chat
⏱️ ~2 minutes

Tell the agent **"push to GitHub now"** and it will run, or you can run yourself:

```bash
cd /home/ubuntu/cryo_leak_rate_dashboard

# 1) Add the remote (only needed once)
git remote add origin https://github.com/GBOGEB/cryo_leak_rate_dashboard.git

# 2) Sanity check
git remote -v

# 3) Push the main branch (sets upstream)
git push -u origin main

# 4) Push all tags (v4.0.0 etc.)
git push --tags origin
```

**Watch for:**
- Authentication prompt → use a **Personal Access Token (PAT)** with `repo` scope as the password
- Upload progress bar
- A success message ending in `* [new branch]      main -> main`

1. [ ] ✅ Mark complete after a clean push

> 💡 If the push fails with `Authentication failed`, generate a PAT here:
> <https://github.com/settings/tokens/new?scopes=repo&description=cryo_leak_rate_dashboard>

---

### Step 4 — Verify on GitHub
⏱️ ~1 minute

1. [ ] Refresh the repo page on GitHub
2. [ ] Confirm these top-level entries are visible:
   - [ ] `src/`
   - [ ] `docs/`
   - [ ] `data/`
   - [ ] `tests/`
   - [ ] `scripts/`
   - [ ] `README.md`
   - [ ] `CHANGELOG.md`
   - [ ] `VERSION`, `VERSION.json`
   - [ ] `BACKUP_STRATEGY.md`, `PROGRESS_TRACKER.md`
3. [ ] Check **commits** tab — most recent commit should match local `git log`
4. [ ] Check **tags** — `v4.0.0` should be present (if previously tagged)
5. [ ] ✅ Mark complete when verified

---

### Step 5 — Enable GitHub Pages
⏱️ ~3 minutes

1. [ ] Go to: `https://github.com/GBOGEB/cryo_leak_rate_dashboard/settings/pages`
2. [ ] Under **Build and deployment**:
   - **Source:** *Deploy from a branch*
   - **Branch:** `main`
   - **Folder:** `/docs`
3. [ ] Click **Save**
4. [ ] Wait 2–3 minutes for the first deployment (watch the **Actions** tab if curious)
5. [ ] Refresh the Pages settings page — you should see:
   ```
   ✓ Your site is live at https://gbogeb.github.io/cryo_leak_rate_dashboard/
   ```
6. [ ] Click that URL — it should load your dashboard
7. [ ] ✅ Mark complete

---

### Step 6 — Test the live deployment
⏱️ ~2 minutes

Open each URL in the browser and confirm it loads (no 404, no broken layout):

1. [ ] `https://gbogeb.github.io/cryo_leak_rate_dashboard/`
2. [ ] `https://gbogeb.github.io/cryo_leak_rate_dashboard/VERSION_SELECTOR.html`
3. [ ] `https://gbogeb.github.io/cryo_leak_rate_dashboard/NAVIGATOR.html`
4. [ ] `https://gbogeb.github.io/cryo_leak_rate_dashboard/index_v4_0.html`
5. [ ] `https://gbogeb.github.io/cryo_leak_rate_dashboard/STAKEHOLDER_PRESENTATION.html`
6. [ ] One Plotly plot, e.g. `…/plots/plot1_leak_vs_loss.html`
7. [ ] ✅ Mark complete

> 💡 If any HTML loads but Plotly figures are blank, hard-refresh (Ctrl+Shift+R) —
> GitHub Pages aggressively caches the first deployment.

---

## ✅ Success criteria

- [x] Repository created on GitHub
- [x] All files pushed and visible
- [x] Tags pushed (`v4.0.0`)
- [x] GitHub Pages enabled
- [x] Site accessible at `gbogeb.github.io/cryo_leak_rate_dashboard/`
- [x] All landing HTML pages load correctly
- [x] No 404 errors on the smoke-test URLs above

When all the above are ticked, update `PROGRESS_TRACKER.md` and you're done. 🎉
