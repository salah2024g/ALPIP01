# ADR-005: Arabic NLP and Search Architecture

## Status

Accepted


## Context

ALPIP requires Arabic legal text understanding and retrieval.


## Decision

The platform will separate:

- Text normalization
- Tokenization
- Document chunking
- Search indexing
- Similarity engines


## Benefits

- Better legal document retrieval
- Future AI integration
- Independent NLP modules


## Consequences

All search operations must use the search layer.
