from core.search.models.query import SearchQuery


class SearchHighlighter:
    """Generate a concise highlighted search snippet."""

    def highlight(
        self,
        query: SearchQuery,
        content: str,
        radius: int = 120,
    ) -> str:
        text = query.text.strip()

        if not text:
            return content[: radius * 2]

        position = content.lower().find(text.lower())

        if position == -1:
            return content[: radius * 2]

        start = max(0, position - radius)
        end = min(len(content), position + len(text) + radius)

        snippet = content[start:end]
        relative = position - start
        length = len(text)

        return (
            snippet[:relative]
            + "【"
            + snippet[relative : relative + length]
            + "】"
            + snippet[relative + length :]
        )
