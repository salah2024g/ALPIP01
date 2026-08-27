from core.search.models.query import SearchResult


class SearchResultOrdering:
    """Deterministic ordering for legal search results."""

    def order(
        self,
        results: list[SearchResult],
    ) -> list[SearchResult]:
        return sorted(
            results,
            key=lambda result: (
                -result.score,
                result.document_id,
            ),
        )
