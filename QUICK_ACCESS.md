# Quick Access URLs

## Production (GitHub Pages)

> Replace `<owner>` with your GitHub username/org.

| Page | URL |
|------|-----|
| **Navigator** | `https://<owner>.github.io/cryo_leak_rate_dashboard/NAVIGATOR.html` |
| **Landing Page** | `https://<owner>.github.io/cryo_leak_rate_dashboard/index.html` |
| **40-Slide Master** | `https://<owner>.github.io/cryo_leak_rate_dashboard/index_v4_0.html` |
| **Executive Summary** | `https://<owner>.github.io/cryo_leak_rate_dashboard/executive_summary.html` |
| **Interactive Dashboard** | `https://<owner>.github.io/cryo_leak_rate_dashboard/dashboard.html` |
| **Stakeholder Pres.** | `https://<owner>.github.io/cryo_leak_rate_dashboard/STAKEHOLDER_PRESENTATION.html` |
| **RTM Traceability** | `https://<owner>.github.io/cryo_leak_rate_dashboard/rtm_traceability.html` |

### Hero Pages
| Audience | URL |
|----------|-----|
| Executive (ROI) | `.../heroes/executive.html` |
| Technical (Specs) | `.../heroes/technical.html` |
| Compliance (Standards) | `.../heroes/compliance.html` |

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
| Actions | `https://github.com/<owner>/cryo_leak_rate_dashboard/actions` |
| Latest Release | `https://github.com/<owner>/cryo_leak_rate_dashboard/releases/latest` |
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
