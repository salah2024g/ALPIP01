# ADR-009

## Title

Document Provider Architecture

## Status

Accepted

## Decision

The document engine uses provider-based extraction.

Providers can include:

- pypdf
- PyMuPDF
- OCR
- Future custom providers

The processing pipeline is independent of extraction libraries.
