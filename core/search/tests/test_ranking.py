from core.search.models.query import SearchResult
from core.search.ranking.default import DefaultRankingStrategy


def test_default_ranking_orders_by_score_descending() -> None:
    ranking = DefaultRankingStrategy()

    results = [
        SearchResult(
            document_id="low",
            score=1.0,
            snippet="low",
        ),
        SearchResult(
            document_id="high",
            score=3.0,
            snippet="high",
        ),
        SearchResult(
            document_id="medium",
            score=2.0,
            snippet="medium",
        ),
    ]

    ranked = ranking.rank(results)

    assert [item.document_id for item in ranked] == [
        "high",
        "medium",
        "low",
    ]
