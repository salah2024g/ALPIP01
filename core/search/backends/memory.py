from core.search.backends.base import SearchBackend
from core.search.candidates.default import CandidateGenerator
from core.search.models.query import SearchQuery, SearchResult
from core.search.repository.index_repository import IndexRepository


class MemorySearchBackend(SearchBackend):
    """In-memory search backend using repository and candidate generation."""

    def __init__(
        self,
        repository: IndexRepository,
    ) -> None:
        self._repository = repository
        self._candidate_generator = CandidateGenerator(repository)

    def search(
        self,
        query: SearchQuery,
    ) -> list[SearchResult]:
        results: list[SearchResult] = []

        candidates = self._candidate_generator.generate(query)

        for candidate in candidates:
            document = self._repository.get_document(
                candidate.document_id,
            )

            if document is None:
                continue

            results.append(
                SearchResult(
                    document_id=document.document_id,
                    score=candidate.score,
                    snippet=document.content,
                    metadata={
                        "title": document.title,
                        "source": document.metadata.source,
                        "document_type": document.metadata.document_type,
                        "jurisdiction": document.metadata.jurisdiction,
                        "language": document.metadata.language,
                        "effective_date": document.metadata.effective_date,
                    },
                )
            )

        return results
