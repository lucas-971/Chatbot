init-venv:
	@echo "***** $@"
	python -m venv ./.venv

update-venv:
	@echo "***** $@"
	cd app
	.venv\Scripts\activate &&\
	pip install --upgrade pip &&\
	pip install -r app\requirements.txt

init-project: init-venv, update-venv