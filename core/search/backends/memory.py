from core.search.backends.base import SearchBackend
from core.search.models.query import SearchQuery, SearchResult
from core.search.repository.index_repository import IndexRepository


class MemorySearchBackend(SearchBackend):
    """
    In-memory search backend using repository abstraction.
    """

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

    def search(
        self,
        query: SearchQuery,
    ) -> list[SearchResult]:
        results: list[SearchResult] = []

        for document_id in self._repository.all_documents():
            content = self._repository.find(document_id)

            if content is None:
                continue

            if query.text.lower() in content.lower():
                results.append(
                    SearchResult(
                        document_id=document_id,
                        score=1.0,
                        snippet=content,
                    )
                )

        return results


from core.search.backends.base import SearchBackend
from core.search.models.query import SearchQuery, SearchResult
from core.search.repository.index_repository import IndexRepository


class MemorySearchBackend(SearchBackend):
    """
    In-memory search backend using repository abstraction.
    """

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

    def search(
        self,
        query: SearchQuery,
    ) -> list[SearchResult]:
        results: list[SearchResult] = []

        for document_id in self._repository.all_documents():
            content = self._repository.find(document_id)

            if content is None:
                continue

            if query.text.lower() in content.lower():
                results.append(
                    SearchResult(
                        document_id=document_id,
                        score=1.0,
                        snippet=content,
                    )
                )

        return results
