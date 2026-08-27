from core.search.models.query import SearchQuery


class SearchQueryValidator:
    """Validate legal search queries deterministically."""

    def validate(self, query: SearchQuery) -> None:
        if not isinstance(query.text, str):
            raise TypeError("query.text must be a string")

        if query.limit <= 0:
            raise ValueError("query.limit must be greater than zero")

        for key, value in query.filters.items():
            if not isinstance(key, str):
                raise TypeError("filter keys must be strings")

            if not isinstance(value, str):
                raise TypeError("filter values must be strings")
