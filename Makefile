.ONESHELL:
SHELL := bash
.DEFAULT_GOAL := help
OS := $(shell uname)

.PHONY: help test format lint rebuild_venv gen_requirements run_test_uvicorn

PYTHON_VERSION=3.11.2
VENV=rpg-tools

test: 
	echo "Not set up yet"

format: ## Format python code using black
	black .

lint: ## Run flake8 linter
	flake8

rebuild_venv: ## rebuild the virtualenv for this project using pyenv
	pyenv install ${PYTHON_VERSION} --skip-existing
	pyenv rehash
	pyenv virtualenv-delete --force ${VENV}
	pyenv virtualenv ${PYTHON_VERSION} ${VENV}
	pyenv local ${VENV}
	python -m pip install -U pip setuptools wheel pip-tools
	python -m pip install -r requirements.txt
	python -m pip install -e .[all]
	pre-commit install
	pyenv rehash

gen_requirements: ## Generate new requirements.txt files
	pip-compile --upgrade --resolver=backtracking --output-file=requirements.txt pyproject.toml
	pip-compile --upgrade --resolver=backtracking --extra=dev --output-file=requirements_dev.txt pyproject.toml
	pip-compile --upgrade --resolver=backtracking --extra=test --output-file=requirements_test.txt pyproject.toml

sync_requirements: ## Use pip-sync to reinstall requirements
	pip-sync --verbose requirements.txt requirements_dev.txt requirements_test.txt

run_test_uvicorn: ## Run fastapi/uvicorn test server
	uvicorn main:app --reload

help: ## Generate and display help info on make commands
	grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
