from dataclasses import dataclass


@dataclass(slots=True)
class SearchExplanation:
    document_id: str
    score: float
    matched_terms: list[str]


class SearchExplainer:
    """Explain deterministic search matches."""

    def explain(
        self,
        document_id: str,
        query_text: str,
        content: str,
        score: float,
    ) -> SearchExplanation:
        terms = [
            term
            for term in query_text.split()
            if term and term.lower() in content.lower()
        ]

        unique_terms = list(dict.fromkeys(terms))

        return SearchExplanation(
            document_id=document_id,
            score=score,
            matched_terms=unique_terms,
        )
