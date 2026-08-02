from dataclasses import dataclass, field


@dataclass
class SearchQuery:
    text: str
    filters: dict[str, str] = field(default_factory=dict)
    limit: int = 10


@dataclass
class SearchResult:
    document_id: str
    score: float
    snippet: str
    metadata: dict = field(default_factory=dict)
