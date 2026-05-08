function setMode(mode) {
  document.body.classList.remove('mode-preview', 'mode-code', 'mode-print');
  document.body.classList.add(`mode-${mode}`);
}

function expandAll() {
  document.querySelectorAll('details').forEach(d => d.open = true);
}

function collapseAll() {
  document.querySelectorAll('details').forEach(d => d.open = false);
}

function exportPdf() {
  window.print();
}
