lint: ruff mypy

mypy:
	mypy .

ruff:
	ruff check .
