# GitHub Pages Setup Guide

> **Project:** QPLANT Cryo Leak Rate Dashboard v4.0.0  
> **Deployment method:** GitHub Actions (`deploy.yml`)

---

## Prerequisites

- [x] Repository contains `docs/` directory with 84 HTML files
- [x] `deploy.yml` workflow present in `.github/workflows/`
- [x] All tests passing (22/22)
- [x] `NAVIGATOR.html` as entry point
- [ ] Repository pushed to GitHub
- [ ] PR merged to `main`

---

## Configuration Steps

### Step 1: Create GitHub Repository

1. Go to: https://github.com/new
2. **Repository name:** `cryo_leak_rate_dashboard`
3. **Description:** QPLANT Cryogenic Leak Rate Analysis Dashboard v4.0.0
4. **Visibility:** Public (required for free GitHub Pages) or Private (requires Pro/Team)
5. **Do NOT** initialize with README, .gitignore, or license
6. Click **Create repository**

### Step 2: Push Local Repository

```bash
cd /path/to/cryo_leak_rate_dashboard

# Add remote
git remote add origin https://github.com/GBOGEB/cryo_leak_rate_dashboard.git

# Push all branches and tags
git push -u origin main
git push --tags
```

### Step 3: Enable GitHub Pages

1. Navigate to: **Settings** → **Pages**
   - URL: `https://github.com/GBOGEB/cryo_leak_rate_dashboard/settings/pages`
2. **Build and deployment:**
   - Source: **GitHub Actions** ← Important! Not "Deploy from branch"
3. The `deploy.yml` workflow will handle everything automatically

> **Why GitHub Actions?** Our `deploy.yml` runs `setup.sh` + `build.sh` before deploying, ensuring all generated content is fresh and validated.

### Step 4: Trigger Initial Deploy

The deploy happens automatically on push to `main`. To manually trigger:

```bash
# Force a new deployment
git commit --allow-empty -m "chore: trigger deploy"
git push origin main
```

Or from the GitHub Actions tab:
1. Go to **Actions** → **Deploy to GitHub Pages**
2. Click **Run workflow** (if manual trigger is enabled)

### Step 5: Verify Deployment

Wait 60–90 seconds after the action completes, then visit:

| Page | URL |
|------|-----|
| **Main site** | https://gbogeb.github.io/cryo_leak_rate_dashboard/ |
| **Navigator** | https://gbogeb.github.io/cryo_leak_rate_dashboard/NAVIGATOR.html |
| **Dashboard** | https://gbogeb.github.io/cryo_leak_rate_dashboard/dashboard.html |
| **Executive** | https://gbogeb.github.io/cryo_leak_rate_dashboard/executive_summary.html |

---

## Architecture

```
Push to main
    │
    ├── ci.yml (tests + validation)
    │     ├── pytest 22 tests
    │     ├── validate_links.py
    │     └── Upload test-report artifact
    │
    └── deploy.yml (build + deploy)
          ├── setup.sh → build.sh
          ├── Upload docs/ as Pages artifact
          └── Deploy to GitHub Pages
                │
                └── https://gbogeb.github.io/cryo_leak_rate_dashboard/
```

---

## Custom Domain (Optional)

### Step 1: Add CNAME Record
In your DNS provider, create:
```
Type: CNAME
Name: cryo (or your subdomain)
Value: gbogeb.github.io
```

### Step 2: Configure in GitHub
1. Go to **Settings** → **Pages**
2. Under **Custom domain**, enter: `cryo.yourdomain.com`
3. Click **Save**
4. Wait for DNS check (can take up to 24 hours)
5. Enable **Enforce HTTPS** once DNS is verified

### Step 3: Add CNAME File
```bash
echo "cryo.yourdomain.com" > docs/CNAME
git add docs/CNAME
git commit -m "docs: add custom domain CNAME"
git push origin main
```

---

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| **404 error** | Pages not enabled or wrong source | Check Settings > Pages, ensure source = GitHub Actions |
| **Old content** | Browser cache or deploy pending | Hard refresh (Ctrl+Shift+R), check Actions tab |
| **Broken CSS/JS** | Wrong base URL | Ensure HTML uses relative paths (not absolute) |
| **Deploy failed** | Build error | Check Actions tab → Deploy workflow → view logs |
| **Tests fail in CI** | Missing dependency | Verify `requirements.txt` is complete |
| **Pages not updating** | Concurrent deploy cancelled | Wait and push again |

### Debug Commands

```bash
# Check if deploy.yml is valid
cat .github/workflows/deploy.yml | python3 -c "import yaml,sys; yaml.safe_load(sys.stdin); print('✅ Valid YAML')"

# Verify docs/ has correct content
ls docs/*.html | head -20
find docs/ -name "*.html" | wc -l  # Should be ~84

# Test locally
python -m http.server 8000 -d docs
# Then open http://localhost:8000
```

---

## Alternative Deployment Options

### Netlify
A `netlify.toml` is included. To deploy:
1. Connect repo at https://app.netlify.com
2. Build command: `./setup.sh && ./build.sh`
3. Publish directory: `docs`

### Vercel
A `vercel.json` is included. To deploy:
1. Connect repo at https://vercel.com
2. Framework: Other
3. Output directory: `docs`

### Local Server
```bash
cd cryo_leak_rate_dashboard
python -m http.server 8000 -d docs
# Open http://localhost:8000
```

---

*Guide created: 2026-05-18 | QPLANT Cryo Leak Rate Dashboard v4.0.0*
