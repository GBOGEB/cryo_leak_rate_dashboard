# Backup & Persistence Strategy — CRITICAL INFORMATION

> **Question answered:** *"Do I need to copy the full zip and project files or all OK from here?"*
>
> **Short answer:** Files in `/home/ubuntu/` persist for the lifetime of THIS chat/VM only.
> If you start a NEW chat, the easiest way to get the project back is to **push to GitHub now**
> and clone it later. Downloading the ZIP is a fine secondary safety net.

---

## ⚠️ VM File Persistence Rules

### What Persists WITHIN This Conversation
- ✅ Files in `/home/ubuntu/` stay available while this chat/VM is active
- ✅ Git commits remain in the local repo
- ✅ All created files remain accessible across messages
- ✅ You can work across multiple messages without re-uploading

### What Does NOT Persist After Chat Ends
- ❌ Local files in `/home/ubuntu/` are **not guaranteed** to be available in a NEW conversation
- ❌ The VM shuts down after an inactivity period
- ❌ Uncommitted changes may be lost when the VM stops
- ❌ Local-only repos (not pushed to GitHub) may be lost

---

## 🎯 RECOMMENDATION: Push to GitHub ASAP

### Option A — GitHub as primary backup (BEST)
- ✅ Push `cryo_leak_rate_dashboard` to GitHub NOW
- ✅ All files backed up remotely
- ✅ Can clone in any new chat session
- ✅ Version controlled and shareable
- ✅ No manual download/upload cycles

```bash
cd /home/ubuntu/cryo_leak_rate_dashboard
git remote add origin https://github.com/GBOGEB/cryo_leak_rate_dashboard.git
git push -u origin main
git push --tags origin
```

**Result:** Everything safe on GitHub forever.

### Option B — Download ZIP (manual safety copy)
- ✅ Click the **Files** button in the chat UI (top right) and download the project directory
- ✅ Keep a local backup on your computer
- ⚠️ Must re-upload in new chat sessions to continue
- ⚠️ Manual version management — no history beyond what you ZIP

**Use case:** You can't or don't want to push to GitHub right now.

### Option C — Both (RECOMMENDED)
- ✅ Push to GitHub (primary backup)
- ✅ Download ZIP (local safety copy)
- ✅ Best of both worlds

---

## 📦 What to Back Up

### MUST back up (unique, hand-authored content)
1. **Source code** — `src/`
2. **Configuration / SSoT** — `data/config.yaml`, `data/*.json`
3. **Documentation** — all `.md` files at the repo root
4. **Tests** — `tests/`
5. **Scripts** — `scripts/`, `setup.sh`, `build.sh`, `validate.sh`, `package.sh`
6. **Templates** — `repo_templates/`
7. **Version metadata** — `VERSION`, `VERSION.json`, `CHANGELOG.md`

### Can be regenerated (do not need to back up)
- `docs/*.html` (rebuild via `./build.sh`)
- `outputs/` (rebuild via build scripts)
- `dist/` (rebuild via `./package.sh`)
- `__pycache__/`, `.pytest_cache/`, `htmlcov/`, `.coverage` (Python temp)
- `venv/` (recreate via `./setup.sh`)

### Already on GitHub (if pushed)
- All committed files
- Full git history
- Tags and branches

---

## 🔄 For Reuse in NEW Chat Sessions

### If pushed to GitHub
```bash
# In a fresh chat:
git clone https://github.com/GBOGEB/cryo_leak_rate_dashboard.git
cd cryo_leak_rate_dashboard
./setup.sh
./build.sh
```
**Result:** Full project restored in ~2 minutes.

### If only a local ZIP backup
1. Upload the ZIP in the new chat
2. Extract: `unzip cryo_leak_rate_dashboard.zip -d /home/ubuntu/`
3. Rebuild:
   ```bash
   cd /home/ubuntu/cryo_leak_rate_dashboard
   ./setup.sh && ./build.sh
   ```
**Result:** Project restored in ~5 minutes.

---

## ✅ CURRENT STATUS (as of this commit)

- 🟡 **Local state:** v4.0.0 fully committed locally — `git status` clean
- 🔴 **GitHub state:** No remote configured yet — **at risk** if the VM shuts down
- 🔢 **Local commits not yet on GitHub:** all of them (the repo has never been pushed)

### RECOMMENDED ACTION
**Push to GitHub in the next 5 minutes.** Follow `GITHUB_REPO_CREATION_STEPS.md`.

---

## 🧠 Mental model for future chats

Think of this VM as a **scratch workspace**, not durable storage.
GitHub is your **durable workspace**. Every meaningful change should end on GitHub.

| Storage | Durable? | Survives new chat? | Use it for |
|---|---|---|---|
| `/home/ubuntu/` in this chat | ⚠️ Short-term | ❌ No | Scratch / in-progress work |
| Local ZIP on your computer | ✅ Yes | ✅ Yes (after upload) | Offline safety copy |
| **GitHub repo** | ✅ Yes | ✅ Yes (just clone) | **Primary source of truth** |
