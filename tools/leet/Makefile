BINARY := leet
BIN_DIR := $(CURDIR)/bin
PKG := ./cmd/leet

.PHONY: all build install test lint tidy run clean

all: build

build:
	@mkdir -p $(BIN_DIR)
	go build -o $(BIN_DIR)/$(BINARY) $(PKG)
	@echo "built $(BIN_DIR)/$(BINARY)"

install:
	go install $(PKG)

test:
	go test ./...

lint:
	@command -v golangci-lint >/dev/null && golangci-lint run || (echo "golangci-lint not installed, falling back to go vet" && go vet ./...)

tidy:
	go mod tidy

run: build
	$(BIN_DIR)/$(BINARY)

clean:
	rm -rf $(BIN_DIR) dist
