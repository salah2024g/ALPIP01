from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SearchPage:
    page: int
    page_size: int
    total: int
    offset: int
    has_next: bool


class SearchPaginator:
    """Deterministic pagination metadata for legal search results."""

    def create(
        self,
        page: int,
        page_size: int,
        total: int,
    ) -> SearchPage:
        if page <= 0:
            raise ValueError("page must be greater than zero")

        if page_size <= 0:
            raise ValueError("page_size must be greater than zero")

        if total < 0:
            raise ValueError("total must not be negative")

        offset = (page - 1) * page_size
        has_next = offset + page_size < total

        return SearchPage(
            page=page,
            page_size=page_size,
            total=total,
            offset=offset,
            has_next=has_next,
        )
