import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]



def test_required_outputs_exist():
    subprocess.run(["python3", "src/build_all.py"], cwd=ROOT, check=True)

    required = [
        ROOT / "docs" / "index.html",
        ROOT / "docs" / "dashboard.html",
        ROOT / "docs" / "calculations.html",
        ROOT / "docs" / "executive_summary.html",
        ROOT / "docs" / "rtm_traceability.html",
        ROOT / "docs" / "handover.html",
        ROOT / "docs" / "handover.pdf",
        ROOT / "source" / "handover.md",
        ROOT / "source" / "developer_notes.md",
        ROOT / "OUTPUT_MANIFEST.json",
        ROOT / "ERROR_LOG.md",
    ]
    for path in required:
        assert path.exists(), f"Missing expected output: {path}"



def test_manifest_has_hashes():
    manifest = json.loads((ROOT / "OUTPUT_MANIFEST.json").read_text(encoding="utf-8"))
    assert manifest["file_count"] > 0
    assert any(entry["path"] == "docs/dashboard.html" for entry in manifest["files"])
    for entry in manifest["files"][:10]:
        assert len(entry["sha256"]) == 64
