from dataclasses import dataclass


@dataclass
class LegalArticle:

    id: int
    article_number: str
    text: str
    legislation_id: int
