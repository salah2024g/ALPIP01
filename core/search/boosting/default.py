from core.search.models.query import SearchQuery, SearchResult


class SearchResultBooster:
    """Apply deterministic metadata-aware boosting to legal search results."""

    def boost(
        self,
        query: SearchQuery,
        results: list[SearchResult],
    ) -> list[SearchResult]:
        boosted: list[SearchResult] = []

        for result in results:
            score = result.score

            for key, expected in query.filters.items():
                if result.metadata.get(key) == expected:
                    score += 1.0

            boosted.append(
                SearchResult(
                    document_id=result.document_id,
                    score=score,
                    snippet=result.snippet,
                    metadata=dict(result.metadata),
                )
            )

        return sorted(
            boosted,
            key=lambda result: (
                -result.score,
                result.document_id,
            ),
        )
