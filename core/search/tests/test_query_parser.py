from core.search.query.parser import LegalQueryParser


def test_query_parser_strips_text() -> None:
    parser = LegalQueryParser()

    query = parser.parse(
        "  ضريبة الدخل  ",
        filters={"document_type": "law"},
        limit=20,
    )

    assert query.text == "ضريبة الدخل"
    assert query.filters == {"document_type": "law"}
    assert query.limit == 20


def test_query_parser_defaults() -> None:
    parser = LegalQueryParser()

    query = parser.parse("tax")

    assert query.text == "tax"
    assert query.filters == {}
    assert query.limit == 10


def test_query_parser_empty_text() -> None:
    parser = LegalQueryParser()

    query = parser.parse("   ")

    assert query.text == ""
