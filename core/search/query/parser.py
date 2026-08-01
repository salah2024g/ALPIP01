from core.search.models.query import SearchQuery


class QueryParser:
    """
    Converts raw user input into a SearchQuery object.
    """

    def parse(self, text: str) -> SearchQuery:
        return SearchQuery(text=text.strip())
