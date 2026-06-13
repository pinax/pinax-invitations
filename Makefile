all: init test

init:
	pip install -e .
	pip install tox "coverage<5"

test:
	coverage erase
	tox 
	coverage html
