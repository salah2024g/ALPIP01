from core.search.services.pipeline import SearchPipeline


class LegalDocumentIndexer:
    """
    Indexes ALDF legal documents into search engine.
    """

    def __init__(
        self,
        pipeline: SearchPipeline,
    ) -> None:
        self.pipeline = pipeline

    def index(
        self,
        document_id: str,
        title: str,
        content: str,
    ) -> int:
        searchable_content = (
            f"{title}\n{content}"
        )

        return self.pipeline.index_document(
            document_id,
            searchable_content,
        )
