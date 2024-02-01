init-venv:
	@echo "***** $@"
	${PYTHON} -m venv ./.venv

update-venv: init-venv
	@echo "***** $@"
	cd app
	.venv\Scripts\activate &&\
	pip install --upgrade pip &&\
	pip install -r app\requirements.txt

install-black: update-venv
	@echo "***** $@"
	cd app
	.venv\Scripts\activate &&\
	pip install black