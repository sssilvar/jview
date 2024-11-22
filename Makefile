UV = uv run

BLACK = $(UV) black .
RUFF =  $(UV) ruff check .
MYPY = $(UV) mypy
TESTS = $(UV) pytest

install:
	uv sync

lint: install
	$(BLACK)
	$(RUFF)
	$(RUFF) --fix  # If any fixable issues are found, apply them (for local development)
	$(MYPY)

test: install lint
	$(TESTS)

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +

.PHONY: install lint test clean