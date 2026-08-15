from core.search.models.query import SearchQuery


class LegalQueryParser:
    """Parse structured legal search queries."""

    def parse(
        self,
        text: str,
        *,
        filters: dict[str, str] | None = None,
        limit: int = 10,
    ) -> SearchQuery:
        normalized = text.strip()

        return SearchQuery(
            text=normalized,
            filters=filters or {},
            limit=limit,
        )
