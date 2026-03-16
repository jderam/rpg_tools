.ONESHELL:
SHELL := bash
.DEFAULT_GOAL := help

.PHONY: help install sync lock format lint check test test-cov run_test_uvicorn

install: ## Install all dependencies (including test and dev)
	uv sync --frozen --all-extras

sync: ## Sync dependencies from lockfile
	uv sync --frozen

lock: ## Update the lockfile
	uv lock

format: ## Format code with ruff
	uv run ruff format .

lint: ## Lint code with ruff
	uv run ruff check .

check: ## Run format check and lint
	uv run ruff format --check .
	uv run ruff check .

test: ## Run tests with pytest
	uv run pytest

test-cov: ## Run tests with coverage report
	uv run pytest --cov=rpg_tools --cov-report=term-missing

run_test_uvicorn: ## Run fastapi/uvicorn test server
	uv run uvicorn main:app --reload

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
