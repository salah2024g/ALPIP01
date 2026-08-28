from core.search.candidates.default import CandidateGenerator
from core.search.models.query import SearchQuery
from core.search.repository.index_repository import IndexRepository


def test_candidate_generator_supports_phrase_queries() -> None:
    repository = IndexRepository()

    repository.save(
        "law-1",
        "The income tax law applies.",
    )
    repository.save(
        "law-2",
        "The income and tax law applies.",
    )

    generator = CandidateGenerator(repository)

    results = generator.generate(
        SearchQuery(text='"income tax"'),
    )

    assert [result.document_id for result in results] == ["law-1"]
    assert results[0].score == 3.0


def test_candidate_generator_supports_mixed_term_and_phrase_queries() -> None:
    repository = IndexRepository()

    repository.save(
        "law-1",
        "income tax law and tax returns",
    )
    repository.save(
        "law-2",
        "income tax regulation",
    )

    generator = CandidateGenerator(repository)

    results = generator.generate(
        SearchQuery(text='tax "income tax"'),
    )

    assert [result.document_id for result in results] == ["law-1", "law-2"]
    assert results[0].score == 4.0
    assert results[1].score == 3.0


def test_candidate_generator_phrase_results_are_deterministic() -> None:
    repository = IndexRepository()

    repository.save(
        "law-b",
        "income tax law",
    )
    repository.save(
        "law-a",
        "income tax regulation",
    )

    generator = CandidateGenerator(repository)

    first = generator.generate(
        SearchQuery(text='"income tax"'),
    )
    second = generator.generate(
        SearchQuery(text='"income tax"'),
    )

    assert first == second
    assert [result.document_id for result in first] == [
        "law-a",
        "law-b",
    ]


def test_candidate_generator_keeps_empty_query_empty() -> None:
    repository = IndexRepository()
    repository.save("law-1", "income tax law")

    generator = CandidateGenerator(repository)

    assert generator.generate(SearchQuery(text="")) == []
