VENV = poetry run

# Linters
lint: ruff mypy

mypy:
	$(VENV) mypy aiostdlib/

ruff:
	$(VENV) ruff check aiostdlib/
