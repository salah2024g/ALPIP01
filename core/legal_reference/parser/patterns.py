import re

ARTICLE_REFERENCE_PATTERN = re.compile(
    r"(?:المادة|مادة)\s*\(?([0-9٠-٩]+)\)?"
)
