# ADR-008: Frontend Architecture

## Status

Accepted


## Context

ALPIP requires a scalable user interface supporting multiple legal modules.


## Decision

Frontend will use:

- Next.js App Router
- Component based architecture
- API client abstraction
- Plugin UI extension points


## Benefits

- Modular UI
- Easier feature expansion
- Separation of concerns


## Consequences

All UI features must follow frontend module boundaries.
