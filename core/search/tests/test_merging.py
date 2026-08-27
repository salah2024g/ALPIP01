from core.search.merging.default import SearchResultMerger
from core.search.models.query import SearchResult


def test_merger_combines_result_groups() -> None:
    merger = SearchResultMerger()

    results = merger.merge(
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


def test_merger_keeps_highest_duplicate_score() -> None:
    merger = SearchResultMerger()

    results = merger.merge(
        [
            [SearchResult("law-1", 1.0, "tax")],
            [
                SearchResult(
                    "law-1",
                    4.0,
                    "tax law",
                    {"jurisdiction": "EG"},
                )
            ],
        ]
    )

    assert len(results) == 1
    assert results[0].score == 4.0
    assert results[0].snippet == "tax law"
    assert results[0].metadata == {"jurisdiction": "EG"}


def test_merger_preserves_existing_result_on_lower_score() -> None:
    merger = SearchResultMerger()

    results = merger.merge(
        [
            [
                SearchResult(
                    "law-1",
                    4.0,
                    "original",
                    {"source": "primary"},
                )
            ],
            [
                SearchResult(
                    "law-1",
                    2.0,
                    "lower",
                    {"source": "secondary"},
                )
            ],
        ]
    )

    assert results[0].score == 4.0
    assert results[0].snippet == "original"
    assert results[0].metadata == {"source": "primary"}


def test_merger_is_deterministic_for_equal_scores() -> None:
    merger = SearchResultMerger()

    results = merger.merge(
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


def test_merger_handles_empty_groups() -> None:
    merger = SearchResultMerger()

    assert merger.merge([[], []]) == []
