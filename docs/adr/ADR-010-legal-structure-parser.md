# ADR-010

## Title

Arabic Legal Structure Parser

## Status

Accepted

## Decision

The parser builds a hierarchical legal tree.

Supported entities:

- Book
- Chapter
- Section
- Article

Arabic and Indic digits are normalized before storage.

Article body is stored separately from its heading.

Future versions will support:

- Item
- Clause
- Footnotes
- Cross references
