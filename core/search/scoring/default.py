from core.search.models.query import SearchQuery, SearchResult


class DefaultScoring:
    """Default deterministic scoring for legal search results."""

    def score(
        self,
        query: SearchQuery,
        document_id: str,
        content: str,
    ) -> SearchResult:
        text = query.text.strip().lower()
        body = content.lower()

        if not text:
            score = 0.0
        else:
            occurrences = body.count(text)
            score = float(occurrences)

        return SearchResult(
            document_id=document_id,
            score=score,
            snippet=content,
        )
