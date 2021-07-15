SHELL := bash
.DEFAULT_GOAL := help
OS := $(shell uname)

.PHONY: help build run deploy stop test format gen-requirements

build: ## Build the docker images
	@docker-compose build

run: ## Run the docker container
	@docker-compose up --build --detach

stop: ## Stop running container
	@docker stop rpg-tools-nginx rpg-tools-flask-app

test: 
	@echo "Not set up yet"

format: ## Format python code using black
	@black ./python/

lint: ## Run flake8 linter
	@flake8 ./python

gen-requirements: ## Generate a new requirements.txt file
	@pip-compile python/requirements.in > python/requirements.txt

help: ## Generate and display help info on make commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
