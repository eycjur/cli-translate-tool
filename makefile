all: build install

.PHONY: build
build:
	poetry run pyinstaller --onefile --collect-all charset_normalizer main.py

.PHONY: install
install:
	chmod +x dist/main
	sudo ln -sf $(shell pwd)/dist/main /usr/local/bin/T
