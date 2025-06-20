LOGPATH=./var/log/
PYTHON_BIN=/usr/bin/python3.12
VENV=.venv


setup:
	${PYTHON_BIN} -m venv ${VENV}
	${VENV}/bin/python -m pip install --upgrade pip setuptools wheel
	mkdir -p $(LOGPATH)

dev: setup
	source ${VENV}/bin/activate; poetry install -v

clean:	
	rm -rf ${VENV}
	find . -type d -name 'var' -exec rm -rf {} +
	find . -type d -name '__pycache__' -exec rm -rf {} +
