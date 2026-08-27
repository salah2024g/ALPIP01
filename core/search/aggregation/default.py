from core.search.models.query import SearchResult


class SearchResultAggregator:
    """Deterministic aggregation of legal search results."""

    def aggregate(
        self,
        result_groups: list[list[SearchResult]],
    ) -> list[SearchResult]:
        merged: dict[str, SearchResult] = {}

        for group in result_groups:
            for result in group:
                existing = merged.get(result.document_id)

                if existing is None or result.score > existing.score:
                    merged[result.document_id] = result

        return sorted(
            merged.values(),
            key=lambda result: (
                -result.score,
                result.document_id,
            ),
        )
