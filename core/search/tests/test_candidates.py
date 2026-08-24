from core.search.candidates.default import CandidateGenerator
from core.search.models.metadata import DocumentMetadata
from core.search.models.query import SearchQuery
from core.search.repository.index_repository import IndexRepository


def test_candidate_generator_uses_and_semantics() -> None:
    repository = IndexRepository()

    repository.save("law-1", "tax income law")
    repository.save("law-2", "tax law")
    repository.save("law-3", "income law")

    generator = CandidateGenerator(repository)

    results = generator.generate(
        SearchQuery(text="tax income"),
    )

    assert [result.document_id for result in results] == ["law-1"]


def test_candidate_generator_ranks_by_deterministic_score() -> None:
    repository = IndexRepository()

    repository.save("law-1", "tax tax income")
    repository.save("law-2", "tax income")
    repository.save("law-3", "tax tax tax income")

    generator = CandidateGenerator(repository)

    results = generator.generate(
        SearchQuery(text="tax income"),
    )

    assert [result.document_id for result in results] == [
        "law-3",
        "law-1",
        "law-2",
    ]

    assert [result.score for result in results] == [
        4.0,
        3.0,
        2.0,
    ]


def test_candidate_generator_has_stable_tie_breaking() -> None:
    repository = IndexRepository()

    repository.save("law-b", "tax income")
    repository.save("law-a", "tax income")

    generator = CandidateGenerator(repository)

    results = generator.generate(
        SearchQuery(text="tax income"),
    )

    assert [result.document_id for result in results] == [
        "law-a",
        "law-b",
    ]


def test_candidate_generator_is_bounded_by_query_limit() -> None:
    repository = IndexRepository()

    repository.save("law-1", "tax income")
    repository.save("law-2", "tax income")
    repository.save("law-3", "tax income")

    generator = CandidateGenerator(repository)

    results = generator.generate(
        SearchQuery(
            text="tax income",
            limit=2,
        ),
    )

    assert len(results) == 2


def test_candidate_generator_empty_query_returns_no_candidates() -> None:
    repository = IndexRepository()
    repository.save("law-1", "tax income")

    generator = CandidateGenerator(repository)

    results = generator.generate(SearchQuery(text=""))

    assert results == []


def test_candidate_generator_applies_metadata_filters() -> None:
    repository = IndexRepository()

    repository.save(
        "law-1",
        "tax income law",
        metadata=DocumentMetadata(
            document_type="law",
            jurisdiction="EG",
        ),
    )
    repository.save(
        "reg-1",
        "tax income regulation",
        metadata=DocumentMetadata(
            document_type="regulation",
            jurisdiction="EG",
        ),
    )

    generator = CandidateGenerator(repository)

    results = generator.generate(
        SearchQuery(
            text="tax income",
            filters={"document_type": "law"},
        ),
    )

    assert [result.document_id for result in results] == ["law-1"]


def test_candidate_generator_applies_multiple_metadata_filters() -> None:
    repository = IndexRepository()

    repository.save(
        "law-eg",
        "tax income law",
        metadata=DocumentMetadata(
            document_type="law",
            jurisdiction="EG",
        ),
    )
    repository.save(
        "law-uk",
        "tax income law",
        metadata=DocumentMetadata(
            document_type="law",
            jurisdiction="UK",
        ),
    )

    generator = CandidateGenerator(repository)

    results = generator.generate(
        SearchQuery(
            text="tax income",
            filters={
                "document_type": "law",
                "jurisdiction": "EG",
            },
        ),
    )

    assert [result.document_id for result in results] == ["law-eg"]
