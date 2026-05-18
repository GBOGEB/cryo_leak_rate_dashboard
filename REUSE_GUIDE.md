# Project Reuse Guide — Future Chat Sessions

> How to pick the `cryo_leak_rate_dashboard` project back up in a brand-new chat session,
> without losing context or re-doing setup.

---

## 🎯 Scenario: Starting a new chat session

You closed the previous chat (or the VM timed out). The project files in `/home/ubuntu/`
from that chat are no longer guaranteed to exist. Here's how to restart cleanly.

### Option 1 — Clone from GitHub (RECOMMENDED)

**When to use:** After you've pushed the repo to GitHub (see `GITHUB_REPO_CREATION_STEPS.md`).

```bash
# In the new Abacus AI Agent chat:
git clone https://github.com/GBOGEB/cryo_leak_rate_dashboard.git
cd cryo_leak_rate_dashboard

# 1) Recreate the Python venv and install deps
./setup.sh

# 2) Rebuild all derived artifacts (HTML, plots, manifest, handover)
./build.sh

# 3) Verify everything is healthy
./validate.sh
```

**Benefits**
- ✅ Latest version from GitHub
- ✅ Full git history
- ✅ Collaborator changes included
- ✅ Fast setup (~2 minutes)

### Option 2 — Upload a local ZIP backup

**When to use:** No GitHub repo yet, or you're offline.

```bash
# 1) Upload the ZIP through the chat UI
# 2) Then in the chat shell:

unzip cryo_leak_rate_dashboard.zip -d /home/ubuntu/
cd /home/ubuntu/cryo_leak_rate_dashboard

# 3) Sanity check git state
git status

# 4) Set up env and rebuild
./setup.sh
./build.sh
```

**Benefits**
- ✅ Works without GitHub access
- ✅ Captures any local-only uncommitted changes
- ⚠️ May be outdated relative to GitHub if others pushed updates

---

## 📦 What to bring into the new chat

### Essential (only if NOT using GitHub)
1. Full project ZIP
2. Any uncommitted changes you care about
3. Environment notes (Python version, OS quirks if any)

### Reference docs to point the new agent at
1. `HANDOVER.md` — project overview
2. `BUILD_LOG.md` — build history
3. `CONTINUATION_GUIDE.md` — agent continuation instructions
4. `BACKUP_STRATEGY.md` — persistence rules
5. `PROGRESS_TRACKER.md` — where we left off in the deployment process

### Nice to have
1. `ARTIFACTS.yaml` — deliverables catalog
2. `QUICK_ACCESS.md` — frequently used URLs and commands
3. `CHANGELOG.md` — version history

---

## 🔄 Handover message template

Paste this at the start of the new chat to give the agent full context:

```markdown
Continue work on MYRRHA QPLANT Cryogenic Dashboard

**Project:** cryo_leak_rate_dashboard
**GitHub:** https://github.com/GBOGEB/cryo_leak_rate_dashboard
**Version:** v4.0.0
**Status:** Deployed to GitHub Pages

**Context**
- Single Source of Truth in `data/config.yaml`
- 3 HP compressors (Kaeser FSD 575 SFC)
- 22/22 tests passing
- All documentation complete
- GitHub Pages live at https://gbogeb.github.io/cryo_leak_rate_dashboard/

**Task**
<your next task here>

**Reference**
- HANDOVER.md for project overview
- BUILD_LOG.md for history
- CONTINUATION_GUIDE.md for agent instructions
```

---

## 🎯 Quick commands reference

### Start working
```bash
git clone https://github.com/GBOGEB/cryo_leak_rate_dashboard.git
cd cryo_leak_rate_dashboard
./setup.sh
```

### Make changes
```bash
# Edit files...
./build.sh           # Rebuild HTML/plots/manifest
./validate.sh        # Run tests + link/manifest checks
git add .
git commit -m "feat: <message>"
git push
```

### Deploy updates to GitHub Pages
GitHub Pages auto-deploys from `main` after each push to `/docs/`.
For an explicit redeploy or smoke test:
```bash
./scripts/deploy.sh
```

### Create a new release
```bash
./scripts/release.sh v4.0.1
git push --tags origin
```

### Pre-push safety net
Always run before a push that touches deployment:
```bash
./scripts/pre_push_checklist.sh
```

---

## 🧠 Things to remember between sessions

| Detail | Value |
|---|---|
| GitHub owner | `GBOGEB` |
| Repo name | `cryo_leak_rate_dashboard` |
| Default branch | `main` |
| Pages source | `main` branch, `/docs` folder |
| Live URL | `https://gbogeb.github.io/cryo_leak_rate_dashboard/` |
| Local path | `/home/ubuntu/cryo_leak_rate_dashboard` |
| Current version | `v4.0.0` |
| Python venv | `./venv/` (recreate with `./setup.sh`) |
| Test runner | `pytest tests/` |
| Build entrypoint | `./build.sh` (calls `src/build_all.py`) |
