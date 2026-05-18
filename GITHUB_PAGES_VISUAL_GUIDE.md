# GitHub Pages Visual Setup Guide

## 🎯 Your Mission
Get this URL live: **https://gbogeb.github.io/cryo_leak_rate_dashboard/**

## ⏱️ Time: 5 minutes

---

## 📍 Step 1: Navigate to Pages Settings

### Option A: Via Repository Settings
```
1. Go to: https://github.com/GBOGEB/cryo_leak_rate_dashboard
2. Click "Settings" tab (top right)
3. Scroll to "Pages" in left sidebar
```

### Option B: Direct Link (Faster)
```
https://github.com/GBOGEB/cryo_leak_rate_dashboard/settings/pages
```

---

## 📍 Step 2: Configure Build and Deployment

You'll see a page titled **"GitHub Pages"**

### Find the "Build and deployment" section:

```
┌─────────────────────────────────────────┐
│ Build and deployment                    │
├─────────────────────────────────────────┤
│                                         │
│ Source                                  │
│ ┌─────────────────────────────────┐     │
│ │ Deploy from a branch        ▼   │     │
│ └─────────────────────────────────┘     │
│                                         │
│ Branch                                  │
│ ┌──────────┐  ┌──────────┐             │
│ │ main  ▼  │  │ /docs ▼  │  [Save]     │
│ └──────────┘  └──────────┘             │
└─────────────────────────────────────────┘
```

### Configure these 3 fields:

1. **Source dropdown:**
   - Click dropdown
   - Select: **"Deploy from a branch"**
   - (NOT "GitHub Actions")

2. **Branch dropdown 1:**
   - Click first dropdown
   - Select: **"main"**

3. **Branch dropdown 2:**
   - Click second dropdown
   - Select: **"/docs"**
   - (This tells GitHub to serve from the docs/ folder)

4. **Click "Save"** button

---

## 📍 Step 3: Wait for Deployment

After clicking Save, you'll see:

```
┌─────────────────────────────────────────┐
│ ✅ Your GitHub Pages site is currently  │
│    being built from the /docs folder    │
│    in the main branch.                  │
└─────────────────────────────────────────┘
```

**Wait 2–3 minutes** for deployment to complete.

**Refresh the page** after waiting.

---

## 📍 Step 4: Get Your Live URL

After deployment completes, you'll see:

```
┌─────────────────────────────────────────┐
│ ✅ Your site is live at                 │
│                                         │
│ https://gbogeb.github.io/               │
│        cryo_leak_rate_dashboard/        │
│                                         │
│ [Visit site →]                          │
└─────────────────────────────────────────┘
```

**Click the "Visit site" button** or copy the URL!

---

## 📍 Step 5: Verify Deployment

Your site should show the **VERSION SELECTOR** landing page:

```
┌─────────────────────────────────────────┐
│  MYRRHA QPLANT Cryogenic Tools          │
├─────────────────────────────────────────┤
│                                         │
│  ┌─────────────────────────────────┐    │
│  │ Leak Rate Analysis v4.0.0       │    │
│  │ Current Production              │    │
│  │ • System-level analysis         │    │
│  │ • HP compressor sizing          │    │
│  │ [Enter Dashboard →]             │    │
│  └─────────────────────────────────┘    │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │ Material Properties v3          │    │
│  │ Active Reference Tool           │    │
│  │ • NIST-validated properties     │    │
│  │ [View Properties Tool →]        │    │
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────┘
```

**If you see this, SUCCESS! 🎉**

---

## 🔧 Troubleshooting

### Issue: "404 – Page not found"
**Solutions:**
1. Wait 5 more minutes (deployment still in progress)
2. Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
3. Check URL is exactly: `gbogeb.github.io/cryo_leak_rate_dashboard/`
4. Verify `/docs` folder exists in your repo

### Issue: "Branch dropdown shows 'None'"
**Solution:** Wait 1 minute and refresh – GitHub is indexing

### Issue: "Cannot access Settings tab"
**Solution:**
1. Make sure you're logged into GitHub
2. Verify you have admin access to the repo
3. Check repo is public (or you have GitHub Pro for private Pages)

### Issue: Page loads but looks broken
**Solutions:**
1. Check browser console for errors (F12)
2. Wait for all resources to load
3. Try a different browser
4. Report errors in browser console

---

## ✅ Success Checklist

After setup, verify these:

- [ ] URL loads: https://gbogeb.github.io/cryo_leak_rate_dashboard/
- [ ] VERSION_SELECTOR page displays
- [ ] Can click "Enter Dashboard" button
- [ ] NAVIGATOR.html loads
- [ ] Technical presentation loads (42 slides)
- [ ] At least one visualization loads (Plotly chart)
- [ ] No 404 errors in navigation

---

## 🎯 What Happens Next

After Pages is configured:

1. **Automatic Updates:**
   - Every `git push` to main automatically updates the site
   - Changes appear in ~2 minutes

2. **All HTML Files Accessible:**
   - All HTML files in `docs/` are now live
   - Direct URLs work (e.g., `.../NAVIGATOR.html`)

3. **Professional URLs:**
   - Share with stakeholders
   - Add to documentation
   - Include in presentations

---

## 📞 After Setup

**Tell me:** "Pages configured" or "Site is live"

**I will:**
- Create verification report
- Test all URLs
- Create final deployment checklist
- Generate GitHub Release
- Update all documentation with live URLs
