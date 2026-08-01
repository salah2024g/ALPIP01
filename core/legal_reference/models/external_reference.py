from dataclasses import dataclass


@dataclass(slots=True)
class ExternalReference:
    reference_type: str

    law_number: str | None

    year: str | None

    matched_text: str

    start: int

    end: int
