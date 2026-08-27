from core.search.aggregation.default import SearchResultAggregator
from core.search.models.query import SearchResult


def test_aggregator_merges_result_groups() -> None:
    aggregator = SearchResultAggregator()

    results = aggregator.aggregate(
        [
            [
                SearchResult("law-1", 2.0, "tax law"),
                SearchResult("law-2", 1.0, "income tax"),
            ],
            [
                SearchResult("law-3", 3.0, "tax regulation"),
            ],
        ]
    )

    assert [result.document_id for result in results] == [
        "law-3",
        "law-1",
        "law-2",
    ]


def test_aggregator_keeps_highest_score_for_duplicate() -> None:
    aggregator = SearchResultAggregator()

    results = aggregator.aggregate(
        [
            [SearchResult("law-1", 1.0, "tax")],
            [SearchResult("law-1", 3.0, "tax law")],
        ]
    )

    assert len(results) == 1
    assert results[0].document_id == "law-1"
    assert results[0].score == 3.0
    assert results[0].snippet == "tax law"


def test_aggregator_uses_document_id_as_tiebreaker() -> None:
    aggregator = SearchResultAggregator()

    results = aggregator.aggregate(
        [
            [
                SearchResult("law-3", 2.0, "tax"),
                SearchResult("law-1", 2.0, "tax"),
            ],
            [SearchResult("law-2", 2.0, "tax")],
        ]
    )

    assert [result.document_id for result in results] == [
        "law-1",
        "law-2",
        "law-3",
    ]


def test_aggregator_handles_empty_groups() -> None:
    aggregator = SearchResultAggregator()

    assert aggregator.aggregate([[], []]) == []
