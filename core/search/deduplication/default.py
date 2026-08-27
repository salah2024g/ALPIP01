from core.search.models.query import SearchResult


class SearchResultDeduplicator:
    """Deterministic deduplication of legal search results."""

    def deduplicate(
        self,
        results: list[SearchResult],
    ) -> list[SearchResult]:
        unique: dict[str, SearchResult] = {}

        for result in results:
            existing = unique.get(result.document_id)

            if existing is None or result.score > existing.score:
                unique[result.document_id] = result

        return sorted(
            unique.values(),
            key=lambda result: (
                -result.score,
                result.document_id,
            ),
        )
