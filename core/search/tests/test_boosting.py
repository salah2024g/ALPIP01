from core.search.boosting.default import SearchResultBooster
from core.search.models.query import SearchQuery, SearchResult


def test_booster_increases_score_for_matching_filter() -> None:
    booster = SearchResultBooster()

    results = booster.boost(
        SearchQuery(
            text="tax",
            filters={"jurisdiction": "EG"},
        ),
        [
            SearchResult(
                "law-1",
                2.0,
                "tax law",
                {"jurisdiction": "EG"},
            ),
            SearchResult(
                "law-2",
                3.0,
                "tax law",
                {"jurisdiction": "OTHER"},
            ),
        ],
    )

    assert results[0].document_id == "law-1"
    assert results[0].score == 3.0
    assert results[1].score == 3.0


def test_booster_supports_multiple_matching_filters() -> None:
    booster = SearchResultBooster()

    results = booster.boost(
        SearchQuery(
            text="tax",
            filters={
                "jurisdiction": "EG",
                "language": "ar",
            },
        ),
        [
            SearchResult(
                "law-1",
                1.0,
                "tax law",
                {
                    "jurisdiction": "EG",
                    "language": "ar",
                },
            ),
        ],
    )

    assert results[0].score == 3.0


def test_booster_preserves_metadata_and_does_not_mutate_input() -> None:
    booster = SearchResultBooster()

    original = SearchResult(
        "law-1",
        2.0,
        "tax law",
        {"jurisdiction": "EG"},
    )

    results = booster.boost(
        SearchQuery(
            text="tax",
            filters={"jurisdiction": "EG"},
        ),
        [original],
    )

    assert original.score == 2.0
    assert original.metadata == {"jurisdiction": "EG"}
    assert results[0].metadata == {"jurisdiction": "EG"}


def test_booster_without_filters_preserves_scores() -> None:
    booster = SearchResultBooster()

    results = booster.boost(
        SearchQuery(text="tax"),
        [
            SearchResult("law-2", 1.0, "tax"),
            SearchResult("law-1", 2.0, "tax"),
        ],
    )

    assert [(result.document_id, result.score) for result in results] == [
        ("law-1", 2.0),
        ("law-2", 1.0),
    ]
