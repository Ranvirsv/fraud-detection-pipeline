.PHONY: help install venv clean format lint test run

VENV = .venv
PYTHON = $(VENV)/bin/python

install: venv
	uv sync

lint:
	uv run ruff check .

test:
	uv run pytest tests/

test-cov:
	uv run pytest --cov=src tests/

etl: 
	echo "Running ETL..."

api: 
	echo "Running API..."

streamlit: 
	echo "Running Streamlit..."