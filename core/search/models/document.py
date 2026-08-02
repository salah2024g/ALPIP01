from dataclasses import dataclass, field

from core.search.models.metadata import DocumentMetadata


@dataclass
class SearchDocument:
    document_id: str
    title: str
    content: str
    metadata: DocumentMetadata = field(
        default_factory=DocumentMetadata,
    )


@dataclass
class DocumentChunk:
    chunk_id: str
    document_id: str
    content: str
    position: int
    metadata: DocumentMetadata = field(
        default_factory=DocumentMetadata,
    )
