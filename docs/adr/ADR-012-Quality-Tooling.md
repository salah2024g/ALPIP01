# ADR-012: Quality Tooling

## Status
Accepted

## Context

As ALPIP grows, maintaining code quality, consistency, and reliability becomes increasingly important. Automated quality checks reduce defects and ensure contributors follow the same standards.

## Decision

The project adopts the following quality tools:

- Ruff
- Black
- MyPy
- Pytest

These tools are mandatory before merging code into the main branch.

## Quality Policy

### Formatting

Black is the single source of formatting.

### Linting

Ruff performs static analysis and style checks.

### Type Checking

MyPy performs gradual static type checking.

### Testing

Pytest is the standard testing framework.

Every new feature must include appropriate tests.

## Consequences

Benefits:

- Consistent code style.
- Early error detection.
- Better maintainability.
- Easier code reviews.
- Safer future refactoring.

Trade-offs:

- Slightly longer development cycle.
- Additional CI execution time.
