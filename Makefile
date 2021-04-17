SHELL := bash
.DEFAULT_GOAL := help
OS := $(shell uname)

.PHONY: help build run deploy stop test lint format gen-requirements

build: ## Build the docker image
	@docker build -t python-rpg-tools-app .

run: ## Run the docker container
	@docker run -d -p 5000:5000 python-rpg-tools-app

deploy: build run ## Build and run docker container

stop: ## Stop running container
	@docker stop $(docker ps | grep python-rpg-tools-app | cut -d" " -f1)

test: 
	@echo "Not set up yet"

lint: ## Get linter output from flake8
	@flake8

format: ## Format python code using black
	#@black
	@echo "Do nothing for now"

gen-requirements: ## Generate a new requirements.txt file
	@pip freeze | sed -e 's/==/>=/g' | grep -v pyspark > requirements.txt

help: ## Generate and display help info on make commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
