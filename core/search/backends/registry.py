from core.search.backends.base import SearchBackend


class SearchEngineRegistry:
    """
    Registry for available search backends.
    """

    def __init__(self) -> None:
        self._backends: dict[str, SearchBackend] = {}

    def register(
        self,
        name: str,
        backend: SearchBackend,
    ) -> None:
        self._backends[name] = backend

    def get(
        self,
        name: str,
    ) -> SearchBackend:
        try:
            return self._backends[name]
        except KeyError as exc:
            raise ValueError(f"Unknown search backend: {name}") from exc

    def available(self) -> list[str]:
        return sorted(self._backends.keys())
