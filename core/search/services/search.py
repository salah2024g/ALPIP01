from core.search.models.query import SearchQuery, SearchResult
from core.search.repository.index_repository import IndexRepository


class SearchService:
    """
    Search service using repository abstraction.
    """

    def __init__(
        self,
        repository: IndexRepository,
    ) -> None:
        self.repository = repository

    def search(
        self,
        query: SearchQuery,
    ) -> list[SearchResult]:

        results = []

        for document_id in self.repository.all_documents():
            content = self.repository.find(document_id)

            if content and query.text.lower() in content.lower():
                results.append(
                    SearchResult(
                        document_id=document_id,
                        score=1.0,
                        snippet=content,
                    )
                )

        return results[: query.limit]
