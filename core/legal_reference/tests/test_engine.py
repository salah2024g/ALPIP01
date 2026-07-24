from core.legal_reference.engine import (
    ReferenceEngine
)


def test_reference_engine():

    engine = ReferenceEngine()

    text = """

تطبق المادة (15)

وفقاً للقانون رقم 206 لسنة 2020.

"""

    index, graph = engine.analyze(text)

    assert len(index.internal) == 1

    assert len(index.external) == 1

    assert "article:15" in graph.neighbors("document")
