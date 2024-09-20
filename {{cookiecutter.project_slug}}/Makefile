.PHONY: clean clean-build clean-pyc clean-test coverage dist docs help install lint lint/flake8

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style
	ruff check app tests

test: ## run tests quickly with the default Python
	pytest . 

coverage: ## check code coverage quickly with the default Python
	coverage run --source . -m pytest
	coverage report -m
	coverage html

release: dist ## package and upload a release
	twine upload dist/*

dist: clean install-build ## builds source and wheel package
	python -m build --sdist --wheel 

install-build: clean ## install the package to the active Python's site-packages for development
	pip install '.[build]'

install-dev: clean ## install the package to the active Python's site-packages for development
	pip install -e '.[dev]'

install: clean ## install the package to the active Python's site-packages
	pip install .
