from dataclasses import dataclass, field


@dataclass
class SearchDocument:
    document_id: str
    title: str
    content: str
    metadata: dict = field(default_factory=dict)


@dataclass
class DocumentChunk:
    chunk_id: str
    document_id: str
    content: str
    position: int
    metadata: dict = field(default_factory=dict)
