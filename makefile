LOGPATH=./var/log/

setup:
	mkdir -p $(LOGPATH)

dev: setup
	poetry shell
	poetry install


clean:	
	find . -type d -name 'var' -exec rm -rf {} +
	find . -type d -name '__pycache__' -exec rm -rf {} +