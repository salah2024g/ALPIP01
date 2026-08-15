from dataclasses import dataclass, field


@dataclass(slots=True)
class DocumentMetadata:
    source: str = ""
    document_type: str = ""
    jurisdiction: str = ""
    language: str = "ar"
    effective_date: str = ""
    version: str = ""
    publisher: str = ""
    tags: list[str] = field(default_factory=list)
    attributes: dict[str, str] = field(default_factory=dict)
