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

    def search(
        self,
        query: SearchQuery,
    ) -> list[SearchResult]:

        results: list[SearchResult] = []

        for document_id in self._repository.all_documents():
            content = self._repository.find(document_id)

            if content and query.text.lower() in content.lower():
                results.append(
                    SearchResult(
                        document_id=document_id,
                        score=1.0,
                        snippet=content,
                    )
                )

        return results
