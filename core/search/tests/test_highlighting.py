from core.search.highlighting.default import SearchHighlighter
from core.search.models.query import SearchQuery


def test_highlighter_marks_matching_text() -> None:
    highlighter = SearchHighlighter()

    result = highlighter.highlight(
        SearchQuery(text="tax"),
        "Income tax law",
    )

    assert result == "Income 【tax】 law"


def test_highlighter_is_case_insensitive() -> None:
    highlighter = SearchHighlighter()

    result = highlighter.highlight(
        SearchQuery(text="tax"),
        "Income TAX law",
    )

    assert result == "Income 【TAX】 law"


def test_highlighter_returns_content_when_no_match() -> None:
    highlighter = SearchHighlighter()

    result = highlighter.highlight(
        SearchQuery(text="income"),
        "Tax law",
    )

    assert result == "Tax law"


def test_highlighter_handles_empty_query() -> None:
    highlighter = SearchHighlighter()

    result = highlighter.highlight(
        SearchQuery(text=""),
        "Tax law",
    )

    assert result == "Tax law"
