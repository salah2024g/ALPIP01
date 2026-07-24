from core.legal_reference.models.reference import LegalReference
from core.legal_reference.parser.patterns import (
    ARTICLE_REFERENCE_PATTERN,
)
from core.legal_structure.parser.normalizer import normalize_number


class LegalReferenceParser:

    def parse(self, text: str):

        references = []

        for match in ARTICLE_REFERENCE_PATTERN.finditer(text):

            references.append(
                LegalReference(
                    article_number=normalize_number(match.group(1)),
                    matched_text=match.group(0),
                    start=match.start(),
                    end=match.end(),
                )
            )

        return references
