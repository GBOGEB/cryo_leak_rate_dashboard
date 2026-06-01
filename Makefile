.PHONY: all setup build test package clean patch-validate patch-bundle handover-zip

all: setup build test package

setup:
	./setup.sh

build:
	./build.sh

test:
	./validate.sh

package:
	./package.sh

clean:
	rm -rf dist/
	find . -type d -name "__pycache__" -exec rm -rf {} +

# ── Patch-package output contract (patches/*.patch.md) ────────────────
patch-validate:
	./scripts/package_patch.sh validate

patch-bundle:
	./scripts/package_patch.sh bundle

handover-zip:
	./scripts/package_patch.sh zip
