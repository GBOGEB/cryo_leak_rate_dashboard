# Post-Deployment Checklist

## ✅ Phase 1: GitHub Pages Configuration (User Action Required)

- [ ] Navigate to: https://github.com/GBOGEB/cryo_leak_rate_dashboard/settings/pages
- [ ] Set Source: **"Deploy from a branch"**
- [ ] Set Branch: **"main"**
- [ ] Set Folder: **"/docs"**
- [ ] Click **"Save"**
- [ ] Wait 3 minutes for deployment
- [ ] Verify URL live: https://gbogeb.github.io/cryo_leak_rate_dashboard/

**Status:** ⏳ PENDING USER ACTION

> 📖 See [GITHUB_PAGES_VISUAL_GUIDE.md](GITHUB_PAGES_VISUAL_GUIDE.md) for detailed step-by-step with ASCII art.

---

## ✅ Phase 2: Site Verification (After Phase 1)

### Automated Verification
```bash
./scripts/site_verification.sh
```

- [ ] All critical URLs return 200 OK
- [ ] No 404 errors

### Manual Verification
- [ ] Homepage loads (VERSION_SELECTOR)
- [ ] Can navigate to v4 dashboard
- [ ] Technical presentation displays (42 slides)
- [ ] Executive presentation displays (10 slides)
- [ ] Plotly visualizations render
- [ ] Hero pages load
- [ ] All links work

**Status:** ⏳ AFTER PHASE 1

---

## ✅ Phase 3: Create GitHub Release (Recommended)

### Steps
1. [ ] Go to: https://github.com/GBOGEB/cryo_leak_rate_dashboard/releases/new
2. [ ] Tag: `v4.0.0`
3. [ ] Target: `main`
4. [ ] Title: `Release v4.0.0: Single Source of Truth Implementation`
5. [ ] Description: Copy from release notes below
6. [ ] Click **"Publish release"**

### Release Notes Template

```markdown
# Release v4.0.0: Single Source of Truth Implementation

## 🎯 Major Changes
- Implemented Single Source of Truth (SSoT) in `data/config.yaml`
- Corrected HP compressor count: 4 → 3 (Kaeser FSD 575 SFC)
- Updated pressure parameters: 14 barg HP discharge, 1050 mbar HCC inlet
- Added recursive build tracking system

## 📊 Deliverables
- 42-slide technical presentation
- 10-slide stakeholder presentation
- 27 interactive visualizations
- Comprehensive navigation system (NAVIGATOR.html)
- Professional landing page (VERSION_SELECTOR.html)

## 🔧 Technical Details
- 22/22 tests passing
- 423 files tracked
- CI/CD pipeline configured
- GitHub Pages deployment

## 🔗 Links
- **Live Site:** https://gbogeb.github.io/cryo_leak_rate_dashboard/
- **Documentation:** See HANDOVER.md
- **Build Log:** See BUILD_LOG.md

## 🙏 Acknowledgments
MYRRHA QPLANT Team, SCK CEN
```

**Status:** ⏳ RECOMMENDED AFTER PHASE 2

---

## ✅ Phase 4: Update Documentation URLs (After Phase 2)

Replace all placeholder URLs with live URLs in:

- [ ] README.md (add live site badge)
- [ ] HANDOVER.md (update URLs section)
- [ ] QUICK_ACCESS.md (confirm all URLs)
- [ ] ARTIFACTS.yaml (add live URLs)

### Commit and push
```bash
git add README.md HANDOVER.md QUICK_ACCESS.md ARTIFACTS.yaml
git commit -m "docs: update with live GitHub Pages URLs"
git push origin main
```

**Status:** ⏳ AFTER PHASE 2

---

## ✅ Phase 5: Share with Stakeholders (After Phase 2)

### Email Template

```
Subject: MYRRHA QPLANT Cryogenic Dashboard v4.0.0 – Now Live

Dear Team,

The MYRRHA QPLANT Cryogenic Helium Leak Rate Analysis Dashboard v4.0.0
is now live and accessible at:

  https://gbogeb.github.io/cryo_leak_rate_dashboard/

Key Features:
  ✅ Single Source of Truth (SSoT) implementation
  ✅ Corrected 3 HP compressor configuration
  ✅ 42-slide technical deep-dive
  ✅ 10-slide executive summary
  ✅ 27 interactive visualizations
  ✅ Professional navigation system

Access Points:
  - Main Dashboard:   [URL]/NAVIGATOR.html
  - Technical Detail:  [URL]/index_v4_0.html
  - Executive Summary: [URL]/STAKEHOLDER_PRESENTATION.html

Repository:
  https://github.com/GBOGEB/cryo_leak_rate_dashboard

Best regards,
[Your Name]
```

**Status:** ⏳ AFTER PHASE 2

---

## ✅ Phase 6: Restore CI/CD Workflows (Optional)

### If GitHub App permissions updated

```bash
cd /home/ubuntu/cryo_leak_rate_dashboard

# Restore workflows
git checkout backup/pre-push-workflows -- .github/

# Commit and push
git add .github/workflows/
git commit -m "ci: restore GitHub Actions workflows"
git push origin main
```

### Verify workflows
- [ ] Check: https://github.com/GBOGEB/cryo_leak_rate_dashboard/actions
- [ ] CI workflow runs on push
- [ ] Tests execute automatically
- [ ] Deploy workflow works

**Status:** ⏳ OPTIONAL

---

## 📊 Completion Summary

```
Phase 1: Pages Config        [⏳] PENDING
Phase 2: Site Verification   [⏳] PENDING
Phase 3: GitHub Release      [⏳] PENDING
Phase 4: Update Docs         [⏳] PENDING
Phase 5: Share               [⏳] PENDING
Phase 6: CI/CD (Optional)    [⏳] PENDING

Overall: 80% → 100%
```

---

## 🎉 Final Success Criteria

Project is 100% complete when:

- [x] Code pushed to GitHub
- [x] All tests passing
- [ ] GitHub Pages live
- [ ] All URLs verified working
- [ ] GitHub Release created
- [ ] Documentation updated with live URLs
- [ ] Stakeholders notified
- [ ] (Optional) CI/CD active

**Current Status: 80% Complete**
**Next: Configure GitHub Pages**
