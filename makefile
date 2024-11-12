SHELL := /bin/bash

init-venv:
	@echo "***** $@"
	python3.12 -m venv ./.venv

update-venv:
	@echo "***** $@"
	cd app
	@source .venv/bin/activate &&\
	pip install --upgrade pip &&\
	pip install -r app/requirements.txt

init-project: init-venv, update-venv 