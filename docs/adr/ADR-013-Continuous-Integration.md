# ADR-013: Continuous Integration

## Status

Accepted

## Context

ALPIP requires automated validation of every change to maintain code quality and prevent regressions.

## Decision

GitHub Actions is adopted as the project's Continuous Integration platform.

Every push and pull request to the main branch automatically executes:

- Ruff
- Black
- MyPy
- Pytest

A change is considered mergeable only if all quality checks pass.

## Consequences

### Benefits

- Automated quality verification.
- Consistent development workflow.
- Early detection of regressions.
- Reduced review effort.
- Reliable build history.

### Trade-offs

- Longer execution time for each pull request.
- Additional maintenance for CI workflows.
