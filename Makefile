SHELL := bash
.DEFAULT_GOAL := help
OS := $(shell uname)

.PHONY: help build run deploy stop test format gen-requirements

test: 
	@echo "Not set up yet"

format: ## Format python code using black
	@black .

lint: ## Run flake8 linter
	@flake8

gen-requirements: ## Generate a new requirements.txt file
	@pip-compile requirements.in > requirements.txt

help: ## Generate and display help info on make commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
