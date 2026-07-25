#!/usr/bin/env bash

set -e

echo "=================================="
echo "ALPIP Quality Check"
echo "=================================="

echo
echo "[1/4] Ruff"
ruff check .

echo
echo "[2/4] Black"
black --check .

echo
echo "[3/4] MyPy"
mypy backend

echo
echo "[4/4] Pytest"
pytest

echo
echo "=================================="
echo "Quality checks completed successfully."
echo "=================================="
