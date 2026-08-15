from core.search.models.query import SearchQuery
from core.search.scoring.default import DefaultScoring


def test_default_scoring_counts_occurrences() -> None:
    scorer = DefaultScoring()

    result = scorer.score(
        SearchQuery(text="tax"),
        "doc-1",
        "tax law and tax regulation",
    )

    assert result.document_id == "doc-1"
    assert result.score == 2.0


def test_default_scoring_is_case_insensitive() -> None:
    scorer = DefaultScoring()

    result = scorer.score(
        SearchQuery(text="Tax"),
        "doc-1",
        "TAX law",
    )

    assert result.score == 1.0


def test_default_scoring_empty_query() -> None:
    scorer = DefaultScoring()

    result = scorer.score(
        SearchQuery(text=""),
        "doc-1",
        "tax law",
    )

    assert result.score == 0.0
