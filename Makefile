VENV = poetry run

# Linters
lint: ruff mypy

mypy:
	$(VENV) mypy ./

ruff:
	$(VENV) ruff check ./
