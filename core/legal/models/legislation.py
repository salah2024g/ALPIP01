from dataclasses import dataclass


@dataclass
class Legislation:

    id: int
    title: str
    number: str
    year: int
    document_type: str
