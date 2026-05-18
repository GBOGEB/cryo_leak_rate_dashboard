# GitHub Pages Setup Guide — NEXT STEP

## 🎯 Goal
Deploy live website at: **https://gbogeb.github.io/cryo_leak_rate_dashboard/**

## ⏱️ Time Required: 5 minutes

---

## 📋 Step-by-Step Instructions

### Step 1: Navigate to Pages Settings
⏱️ 30 seconds

1. Go directly to:
   **https://github.com/GBOGEB/cryo_leak_rate_dashboard/settings/pages**

   Or: Repository → **Settings** tab → scroll to **Pages** in left sidebar (under "Code and automation")

### Step 2: Configure Source
⏱️ 1 minute

In the **"Build and deployment"** section:

1. **Source:** Select **"Deploy from a branch"** (not "GitHub Actions")
2. **Branch:**
   - Dropdown 1: Select **`main`**
   - Dropdown 2: Select **`/docs`**
3. Click **"Save"**

You should see:
> ✅ Your site is being published from the /docs folder in the main branch

### Step 3: Wait for Deployment
⏱️ 2-3 minutes

GitHub will build and deploy your site. **Refresh the page after 2 minutes.**

You should see:
> ✅ Your site is live at https://gbogeb.github.io/cryo_leak_rate_dashboard/

### Step 4: Verify Your Site
⏱️ 2 minutes

Visit: **https://gbogeb.github.io/cryo_leak_rate_dashboard/**

**Test these URLs:**
- [ ] Main: `.../` → VERSION_SELECTOR landing page
- [ ] Navigator: `.../NAVIGATOR.html`
- [ ] Technical: `.../index_v4_0.html`
- [ ] Executive: `.../STAKEHOLDER_PRESENTATION.html`
- [ ] Visualizations: `.../visualizations_v3/compressor_availability_comparison.html`
- [ ] Hero: `.../heroes/executive.html`

**All should load without 404 errors.**

---

## ✅ Success Criteria

Your deployment is successful when:
- [x] GitHub shows "Your site is live at..."
- [x] Main URL loads VERSION_SELECTOR
- [x] Navigation links work
- [x] Presentations display correctly
- [x] Visualizations render (Plotly charts)
- [x] No 404 errors

---

## 🔧 Troubleshooting

### Issue: "None" option in branch dropdown
**Solution:** Wait 1 minute and refresh. GitHub is indexing your repo.

### Issue: 404 on site URL
**Solutions:**
1. Wait 3-5 minutes (deployment in progress)
2. Check branch is "main" and folder is "/docs"
3. Verify `docs/` folder exists in repo
4. Clear browser cache

### Issue: Pages option not in Settings
**Solution:** Verify repository is **public** (Pages requires public repo or GitHub Pro)

---

## 📞 After GitHub Pages Setup

1. **Test thoroughly** — all links, visualizations
2. **Create GitHub Release** — `v4.0.0` tag
3. **Share URLs** with stakeholders
4. **Add workflow permissions** — to enable CI/CD
5. **Set up custom domain** (optional)
