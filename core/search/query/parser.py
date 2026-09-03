from core.search.models.query import SearchQuery
from core.search.query.normalizer import ArabicQueryNormalizer
from core.search.validation.default import SearchQueryValidator


class LegalQueryParser:
    """Parse and normalize structured legal search queries."""

    def __init__(self) -> None:
        self._normalizer = ArabicQueryNormalizer()
        self._validator = SearchQueryValidator()

    def parse(
        self,
        text: str,
        *,
        filters: dict[str, str] | None = None,
        limit: int = 10,
    ) -> SearchQuery:
        normalized = self._normalizer.normalize(text)

        query = SearchQuery(
            text=normalized,
            filters=dict(filters or {}),
            limit=limit,
        )

        self._validator.validate(query)

        return query
