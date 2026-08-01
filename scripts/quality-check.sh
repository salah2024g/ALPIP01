#!/usr/bin/env bash
set -e

echo "==> Ruff"
ruff check .

echo "==> Black"
black --check .

echo "==> MyPy (backend)"
(
    cd backend
    mypy app
)

echo "==> Pytest"
pytest
