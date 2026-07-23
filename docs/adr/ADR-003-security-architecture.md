# ADR-003: Security Architecture

## Status

Accepted

## Context

ALPIP requires secure access control before handling legal data.

## Decision

The system will use:

- Token-based authentication
- Password hashing
- Permission-based authorization

## Principles

- Secure by design
- Least privilege
- Separation of authentication and authorization

## Consequences

All protected resources must pass security checks.
