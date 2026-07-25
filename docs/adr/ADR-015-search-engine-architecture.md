# ADR-015: Search Engine Architecture

## Status

Accepted

## Context

ALPIP requires a scalable legal search capability that can support structured legal documents, ALDF documents, and future semantic search features.

The search layer must remain independent from document storage and extraction layers.

## Decision

A modular search architecture is adopted:
Legal Document
      |
      v
LegalDocumentIndexer
      |
      v
SearchPipeline
      |
      v
DocumentChunker
      |
      v
IndexRepository
      |
      v
SearchService

## Components

### Search Models

Defines searchable documents, chunks, queries, and results.

### Index Layer

Provides indexing abstraction and future replacement with persistent or vector databases.

### Repository Layer

Separates storage implementation from search logic.

### Query Layer

Handles user query parsing and normalization.

### Service Layer

Executes search operations.

## Future Extensions

The architecture supports:

- Full text search.
- Semantic embeddings.
- Vector databases.
- Ranking algorithms.
- Legal relationship-aware search.

## Consequences

Benefits:

- Modular architecture.
- Easy replacement of storage engines.
- Supports offline-first operation.
- Ready for AI search integration.

Trade-offs:

- Additional abstraction layers.
- More components to maintain.
