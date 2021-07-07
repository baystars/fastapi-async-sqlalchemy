MAKEFLAGS += --warn-undefined-variables
SHELL := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help

# all targets are phony
.PHONY: $(shell egrep -o ^[a-zA-Z_-]+: $(MAKEFILE_LIST) | sed 's/://')

TEST_ENDPOINT="http://localhost:8000"
TEST_USER="foo"
TEST_PASSWORD="foo"

ifneq ("$(wildcard ./.env)","")
  include ./.env
endif

pip: ## Install package by pip
	@pip install -r requirements.txt

run: ## Run server
	uvicorn app.main:app --host=0.0.0.0 --port=8000 --reload

create: ## Create table
	python -m app.main

help: ## Print this help
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
