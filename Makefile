.PHONY: all setup build test package clean

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
