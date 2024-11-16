lint: ruff mypy

mypy:
	mypy aiostdlib/

ruff:
	ruff check aiostdlib/
