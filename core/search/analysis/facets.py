from collections import Counter
from dataclasses import dataclass, field

from core.search.models.document import SearchDocument
from core.search.models.metadata import DocumentMetadata


@dataclass(slots=True)
class SearchFacets:
    """Aggregate legal-document metadata for search result facets."""

    counts: dict[str, dict[str, int]] = field(default_factory=dict)

    @classmethod
    def from_documents(
        cls,
        documents: list[SearchDocument],
    ) -> "SearchFacets":
        fields = (
            "document_type",
            "jurisdiction",
            "language",
            "source",
            "effective_date",
        )

        counts: dict[str, dict[str, int]] = {}

        for field_name in fields:
            values: list[str] = []

            for document in documents:
                metadata = document.metadata

                if isinstance(metadata, DocumentMetadata):
                    value = getattr(metadata, field_name, "")
                elif isinstance(metadata, dict):
                    value = str(metadata.get(field_name, ""))
                else:
                    value = ""

                if value:
                    values.append(value)

            counts[field_name] = dict(Counter(values))

        return cls(counts=counts)

    def get(self, field_name: str) -> dict[str, int]:
        return dict(self.counts.get(field_name, {}))
