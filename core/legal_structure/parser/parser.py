from core.legal_structure.models.nodes import LegalNode
from core.legal_structure.parser.normalizer import normalize_number
from core.legal_structure.parser.patterns import (
    ARTICLE_PATTERN,
    BOOK_PATTERN,
    CHAPTER_PATTERN,
    SECTION_PATTERN,
)


class LegalStructureParser:
    def parse(self, text: str):

        root = LegalNode(node_type="document", title="document")

        current_book = root
        current_chapter = root
        current_section = root
        current_article = None

        for raw in text.splitlines():
            line = raw.strip()

            if not line:
                continue

            if BOOK_PATTERN.match(line):
                node = LegalNode("book", line)

                root.add_child(node)

                current_book = node
                current_chapter = node
                current_section = node
                current_article = None

                continue

            if CHAPTER_PATTERN.match(line):
                node = LegalNode("chapter", line)

                current_book.add_child(node)

                current_chapter = node
                current_section = node
                current_article = None

                continue

            if SECTION_PATTERN.match(line):
                node = LegalNode("section", line)

                current_chapter.add_child(node)

                current_section = node
                current_article = None

                continue

            match = ARTICLE_PATTERN.match(line)

            if match:
                number = normalize_number(match.group(1))

                node = LegalNode(node_type="article", title=line, number=number)

                current_section.add_child(node)

                current_article = node

                continue

            if current_article is not None:
                if current_article.text:
                    current_article.text += "\n"

                current_article.text += line

        return root
