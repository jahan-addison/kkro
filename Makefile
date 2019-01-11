
project = kkro

type:
	poetry run python -m mypy **/*.py

lint: type
	poetry run python -m flake8 $(project)/

test: type
	PYTHONPATH=./$(project) poetry run pytest $(project)/tests

start: lint
	poetry run python $(shell pwd)/$(project)/__main__.py


