# ADR-002: Database Architecture

## Status

Accepted

## Context

ALPIP requires a structured persistence layer.

## Decision

The platform will use:

- SQLAlchemy ORM
- Repository Pattern
- Migration Management

## Benefits

- Separation between business logic and persistence
- Easier testing
- Future database migration support

## Consequences

All database access should pass through repositories.
