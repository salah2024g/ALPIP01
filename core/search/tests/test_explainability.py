from core.search.explainability.default import SearchExplainer


def test_search_explainer_returns_matched_terms() -> None:
    explainer = SearchExplainer()

    result = explainer.explain(
        "law-1",
        "tax income",
        "Income tax law",
        2.0,
    )

    assert result.document_id == "law-1"
    assert result.score == 2.0
    assert result.matched_terms == ["tax", "income"]


def test_search_explainer_is_case_insensitive() -> None:
    explainer = SearchExplainer()

    result = explainer.explain(
        "law-1",
        "Tax",
        "TAX law",
        1.0,
    )

    assert result.matched_terms == ["Tax"]


def test_search_explainer_ignores_unmatched_terms() -> None:
    explainer = SearchExplainer()

    result = explainer.explain(
        "law-1",
        "tax regulation",
        "tax law",
        1.0,
    )

    assert result.matched_terms == ["tax"]
