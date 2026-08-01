from core.search.backends.memory import MemorySearchBackend
from core.search.backends.registry import SearchEngineRegistry
from core.search.repository.index_repository import IndexRepository


def test_search_engine_registry() -> None:
    repository = IndexRepository()
    backend = MemorySearchBackend(repository)

    registry = SearchEngineRegistry()

    registry.register("exact", backend)

    assert registry.get("exact") is backend
    assert registry.available() == ["exact"]
