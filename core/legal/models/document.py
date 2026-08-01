from dataclasses import dataclass


@dataclass
class LegalDocument:
    filename: str
    file_type: str
    source: str
    language: str = "ar"
