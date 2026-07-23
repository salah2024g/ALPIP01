from dataclasses import dataclass


@dataclass
class DocumentChunk:

    document_id: int
    content: str
    position: int
