import re


BOOK_PATTERN = re.compile(
    r"^\s*الكتاب\s+(.+)$"
)

CHAPTER_PATTERN = re.compile(
    r"^\s*الباب\s+(.+)$"
)

SECTION_PATTERN = re.compile(
    r"^\s*الفصل\s+(.+)$"
)

ARTICLE_PATTERN = re.compile(
    r"^\s*مادة\s*\(?([0-9٠-٩]+)\)?"
)
