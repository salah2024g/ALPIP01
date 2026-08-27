from core.search.models.query import SearchResult


class SearchResultMerger:
    """Deterministically merge ranked search result streams."""

    def merge(
        self,
        result_groups: list[list[SearchResult]],
    ) -> list[SearchResult]:
        merged: dict[str, SearchResult] = {}

        for group in result_groups:
            for result in group:
                existing = merged.get(result.document_id)

                if existing is None:
                    merged[result.document_id] = result
                    continue

                merged[result.document_id] = SearchResult(
                    document_id=result.document_id,
                    score=max(existing.score, result.score),
                    snippet=(
                        result.snippet
                        if result.score > existing.score
                        else existing.snippet
                    ),
                    metadata=(
                        dict(result.metadata)
                        if result.score > existing.score
                        else dict(existing.metadata)
                    ),
                )

        return sorted(
            merged.values(),
            key=lambda result: (
                -result.score,
                result.document_id,
            ),
        )
