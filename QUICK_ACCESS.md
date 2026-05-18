# Quick Access URLs

> **GitHub User:** GBOGEB  
> **Repo:** cryo_leak_rate_dashboard  
> **Version:** v4.0.0  
> **Updated:** 2026-05-18

## Production (GitHub Pages)

| Page | URL |
|------|-----|
| **Navigator** | https://gbogeb.github.io/cryo_leak_rate_dashboard/NAVIGATOR.html |
| **Landing Page** | https://gbogeb.github.io/cryo_leak_rate_dashboard/index.html |
| **40-Slide Master** | https://gbogeb.github.io/cryo_leak_rate_dashboard/index_v4_0.html |
| **Executive Summary** | https://gbogeb.github.io/cryo_leak_rate_dashboard/executive_summary.html |
| **Interactive Dashboard** | https://gbogeb.github.io/cryo_leak_rate_dashboard/dashboard.html |
| **Stakeholder Pres.** | https://gbogeb.github.io/cryo_leak_rate_dashboard/STAKEHOLDER_PRESENTATION.html |
| **RTM Traceability** | https://gbogeb.github.io/cryo_leak_rate_dashboard/rtm_traceability.html |

### Hero Pages
| Audience | URL |
|----------|-----|
| Executive (ROI) | https://gbogeb.github.io/cryo_leak_rate_dashboard/heroes/executive.html |
| Technical (Specs) | https://gbogeb.github.io/cryo_leak_rate_dashboard/heroes/technical.html |
| Compliance (Standards) | https://gbogeb.github.io/cryo_leak_rate_dashboard/heroes/compliance.html |

## Development (Local)

```bash
# Start server
cd cryo_leak_rate_dashboard
python -m http.server 8000 -d docs

# Access
open http://localhost:8000/NAVIGATOR.html
```

## CI/CD Status

| Resource | URL |
|----------|-----|
| Actions | https://github.com/GBOGEB/cryo_leak_rate_dashboard/actions |
| Latest Release | https://github.com/GBOGEB/cryo_leak_rate_dashboard/releases/latest |
| Pages Deployment | Check Actions → "Deploy to GitHub Pages" |

## Quick Commands

```bash
# Full build
./build.sh

# Quick validation
./validate.sh --quick

# Run tests
pytest tests/ -v

# Check links
python scripts/validate_links.py --report

# Compute hashes
python scripts/compute_hashes.py docs/ > dist/hashes.json

# Create release
./scripts/release.sh v4.1.0

# One-command deploy
./scripts/deploy.sh
```
