from dataclasses import dataclass


@dataclass(slots=True)
class DocumentMetadata:
    source: str = ""
    document_type: str = ""
    jurisdiction: str = ""
    language: str = "ar"
    effective_date: str = ""
