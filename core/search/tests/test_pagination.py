import pytest

from core.search.pagination.default import SearchPage, SearchPaginator


def test_paginator_creates_first_page() -> None:
    paginator = SearchPaginator()

    result = paginator.create(
        page=1,
        page_size=10,
        total=25,
    )

    assert result == SearchPage(
        page=1,
        page_size=10,
        total=25,
        offset=0,
        has_next=True,
    )


def test_paginator_creates_middle_page() -> None:
    paginator = SearchPaginator()

    result = paginator.create(
        page=2,
        page_size=10,
        total=25,
    )

    assert result.offset == 10
    assert result.has_next is True


def test_paginator_creates_last_page() -> None:
    paginator = SearchPaginator()

    result = paginator.create(
        page=3,
        page_size=10,
        total=25,
    )

    assert result.offset == 20
    assert result.has_next is False


def test_paginator_exact_boundary() -> None:
    paginator = SearchPaginator()

    result = paginator.create(
        page=2,
        page_size=10,
        total=20,
    )

    assert result.offset == 10
    assert result.has_next is False


@pytest.mark.parametrize(
    ("page", "page_size", "total", "message"),
    [
        (0, 10, 20, "page must be greater than zero"),
        (1, 0, 20, "page_size must be greater than zero"),
        (1, 10, -1, "total must not be negative"),
    ],
)
def test_paginator_rejects_invalid_values(
    page: int,
    page_size: int,
    total: int,
    message: str,
) -> None:
    paginator = SearchPaginator()

    with pytest.raises(ValueError, match=message):
        paginator.create(page, page_size, total)
