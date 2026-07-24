from dataclasses import dataclass


@dataclass(slots=True)
class LegalReference:

    article_number: str

    matched_text: str

    start: int

    end: int
