
// MAPPING_HEROES Navigation & Interactivity
function setTier(tier) {
  document.querySelectorAll('.tier-content').forEach(el => el.style.display = 'none');
  document.querySelectorAll('.tier-nav a').forEach(el => el.classList.remove('active'));
  const target = document.getElementById('tier-' + tier);
  if (target) target.style.display = 'block';
  const btn = document.querySelector('.tier-nav a[data-tier="' + tier + '"]');
  if (btn) btn.classList.add('active');
}
function expandAll() { document.querySelectorAll('details').forEach(d => d.open = true); }
function collapseAll() { document.querySelectorAll('details').forEach(d => d.open = false); }
function exportPdf() { window.print(); }
document.addEventListener('DOMContentLoaded', () => { setTier && setTier('1'); });
