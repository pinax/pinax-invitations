all: init test

init:
	python setup.py develop
	pip install tox "coverage<5"

test:
	coverage erase
	tox 
	coverage html
