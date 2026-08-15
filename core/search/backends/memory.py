from core.search.backends.base import SearchBackend
from core.search.models.query import SearchQuery, SearchResult
from core.search.repository.index_repository import IndexRepository


class MemorySearchBackend(SearchBackend):
    """In-memory search backend using repository abstraction."""

    def __init__(
        self,
        repository: IndexRepository,
    ) -> None:
        self._repository = repository

    def _matches_filters(
        self,
        document,
        filters: dict[str, str],
    ) -> bool:
        if not filters:
            return True

        metadata = getattr(document, "metadata", None)

        if metadata is None:
            return False

        for key, expected in filters.items():
            if getattr(metadata, key, None) != expected:
                return False

        return True

    def _calculate_score(
        self,
        content: str,
        query_text: str,
    ) -> float:
        normalized_content = content.lower()
        normalized_query = query_text.lower().strip()

        if not normalized_query:
            return 0.0

        occurrences = normalized_content.count(normalized_query)

        if occurrences == 0:
            return 0.0

        return float(occurrences)

    def search(
        self,
        query: SearchQuery,
    ) -> list[SearchResult]:
        results: list[SearchResult] = []

        for document_id in self._repository.all_documents():
            document = self._repository.get_document(document_id)

            if document is None:
                continue

            if not self._matches_filters(
                document,
                query.filters,
            ):
                continue

            score = self._calculate_score(
                document.content,
                query.text,
            )

            if score <= 0:
                continue

            results.append(
                SearchResult(
                    document_id=document_id,
                    score=score,
                    snippet=document.content,
                )
            )

        return results[: query.limit]
