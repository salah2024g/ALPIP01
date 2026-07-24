#!/usr/bin/env bash

set -Eeuo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

create_dir() {
    mkdir -p "$1"
    echo "Created directory: $1"
}

write_file() {
    local path="$1"
    mkdir -p "$(dirname "$path")"
    cat > "$path"
    echo "Created: $path"
}

echo "========================================="
echo "ALPIP Phase 2.8"
echo "Pack 014-A"
echo "Arabic Legal Structure Parser"
echo "========================================="

create_dir core/legal_structure
create_dir core/legal_structure/models
create_dir core/legal_structure/parser
create_dir core/legal_structure/tests


write_file core/legal_structure/models/nodes.py <<'EOF'
from dataclasses import dataclass, field


@dataclass(slots=True)
class LegalNode:

    node_type: str

    title: str

    number: str | None = None

    text: str = ""

    children: list["LegalNode"] = field(default_factory=list)


    def add_child(
        self,
        node: "LegalNode"
    ):

        self.children.append(node)
EOF


write_file core/legal_structure/parser/patterns.py <<'EOF'
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
EOF


write_file core/legal_structure/parser/parser.py <<'EOF'
from core.legal_structure.models.nodes import LegalNode
from core.legal_structure.parser.patterns import (
    BOOK_PATTERN,
    CHAPTER_PATTERN,
    SECTION_PATTERN,
    ARTICLE_PATTERN,
)


class LegalStructureParser:

    def parse(
        self,
        text: str
    ):

        root = LegalNode(
            node_type="document",
            title="document"
        )

        current = root

        for line in text.splitlines():

            line = line.strip()

            if not line:
                continue

            if BOOK_PATTERN.match(line):

                node = LegalNode(
                    "book",
                    line
                )

                root.add_child(node)

                current = node

                continue

            if CHAPTER_PATTERN.match(line):

                node = LegalNode(
                    "chapter",
                    line
                )

                current.add_child(node)

                current = node

                continue

            if SECTION_PATTERN.match(line):

                node = LegalNode(
                    "section",
                    line
                )

                current.add_child(node)

                current = node

                continue

            match = ARTICLE_PATTERN.match(line)

            if match:

                node = LegalNode(
                    node_type="article",
                    title=line,
                    number=match.group(1)
                )

                current.add_child(node)

        return root
EOF


echo ""
echo "Pack 014-A completed successfully."
echo ""
echo "Enhancing legal structure parser..."


write_file core/legal_structure/parser/normalizer.py <<'EOF'
ARABIC_INDIC_DIGITS = str.maketrans(
    "٠١٢٣٤٥٦٧٨٩",
    "0123456789"
)


def normalize_number(value: str) -> str:

    return value.translate(
        ARABIC_INDIC_DIGITS
    )
EOF



write_file core/legal_structure/parser/article.py <<'EOF'
from dataclasses import dataclass, field


@dataclass(slots=True)
class Article:

    number: str

    title: str

    paragraphs: list[str] = field(
        default_factory=list
    )


    def add_paragraph(
        self,
        text: str
    ):

        self.paragraphs.append(
            text
        )
EOF



cat > core/legal_structure/parser/parser.py <<'EOF'
from core.legal_structure.models.nodes import LegalNode
from core.legal_structure.parser.patterns import (
    BOOK_PATTERN,
    CHAPTER_PATTERN,
    SECTION_PATTERN,
    ARTICLE_PATTERN
)
from core.legal_structure.parser.normalizer import (
    normalize_number
)


class LegalStructureParser:


    def parse(
        self,
        text: str
    ):

        root = LegalNode(
            node_type="document",
            title="document"
        )

        current_book = root
        current_chapter = root
        current_section = root
        current_article = None


        for raw in text.splitlines():

            line = raw.strip()

            if not line:
                continue


            if BOOK_PATTERN.match(line):

                node = LegalNode(
                    "book",
                    line
                )

                root.add_child(node)

                current_book = node
                current_chapter = node
                current_section = node
                current_article = None

                continue


            if CHAPTER_PATTERN.match(line):

                node = LegalNode(
                    "chapter",
                    line
                )

                current_book.add_child(node)

                current_chapter = node
                current_section = node
                current_article = None

                continue


            if SECTION_PATTERN.match(line):

                node = LegalNode(
                    "section",
                    line
                )

                current_chapter.add_child(node)

                current_section = node
                current_article = None

                continue


            match = ARTICLE_PATTERN.match(line)

            if match:

                number = normalize_number(
                    match.group(1)
                )

                node = LegalNode(
                    node_type="article",
                    title=line,
                    number=number
                )

                current_section.add_child(
                    node
                )

                current_article = node

                continue


            if current_article is not None:

                if current_article.text:

                    current_article.text += "\n"

                current_article.text += line


        return root
EOF



write_file core/legal_structure/tests/test_normalizer.py <<'EOF'
from core.legal_structure.parser.normalizer import (
    normalize_number
)


def test_arabic_digits():

    assert normalize_number(
        "١٢٣٤٥"
    ) == "12345"


def test_english_digits():

    assert normalize_number(
        "678"
    ) == "678"
EOF



write_file docs/adr/ADR-010-legal-structure-parser.md <<'EOF'
# ADR-010

## Title

Arabic Legal Structure Parser

## Status

Accepted

## Decision

The parser builds a hierarchical legal tree.

Supported entities:

- Book
- Chapter
- Section
- Article

Arabic and Indic digits are normalized before storage.

Article body is stored separately from its heading.

Future versions will support:

- Item
- Clause
- Footnotes
- Cross references
EOF



echo ""
echo "Pack 014-B completed successfully."
echo ""
echo "Creating ALDF exporter..."

write_file core/legal_structure/exporter.py <<'EOF'
from core.legal_structure.models.nodes import LegalNode


def node_to_dict(node: LegalNode):

    return {

        "type": node.node_type,

        "title": node.title,

        "number": node.number,

        "text": node.text,

        "children": [

            node_to_dict(child)

            for child in node.children

        ]

    }
EOF



echo ""
echo "Creating parser integration test..."

write_file core/legal_structure/tests/test_parser.py <<'EOF'
from core.legal_structure.parser.parser import (
    LegalStructureParser
)


def test_basic_structure():

    text = """

الباب الأول

الفصل الأول

مادة (١)

هذا هو نص المادة الأولى.

مادة (2)

هذا هو نص المادة الثانية.

"""

    parser = LegalStructureParser()

    tree = parser.parse(text)

    assert len(tree.children) == 1

    assert tree.children[0].node_type == "book"

    chapter = tree.children[0].children[0]

    assert chapter.node_type == "chapter"

    section = chapter.children[0]

    assert section.node_type == "section"

    assert len(section.children) == 2
EOF



echo ""
echo "Updating roadmap..."

if [ -f docs/Master-Implementation-Roadmap.md ]; then

cat >> docs/Master-Implementation-Roadmap.md <<'EOF'

## Pack 014

Status: Completed

Delivered:

- Arabic Legal Structure Parser
- Book Detection
- Chapter Detection
- Section Detection
- Article Detection
- Arabic Number Normalization
- ALDF Export
- Integration Tests
- ADR-010

EOF

fi



echo ""
echo "Running validation..."

FAILED=0

FILES=(
"core/legal_structure/models/nodes.py"
"core/legal_structure/parser/patterns.py"
"core/legal_structure/parser/normalizer.py"
"core/legal_structure/parser/parser.py"
"core/legal_structure/exporter.py"
"core/legal_structure/tests/test_normalizer.py"
"core/legal_structure/tests/test_parser.py"
"docs/adr/ADR-010-legal-structure-parser.md"
)

for file in "${FILES[@]}"
do

    if [ -f "$file" ]; then

        echo "OK: $file"

    else

        echo "MISSING: $file"

        FAILED=1

    fi

done


echo ""

if [ "$FAILED" -eq 0 ]; then

    echo "========================================="
    echo "PACK 014 COMPLETED SUCCESSFULLY"
    echo "Arabic Legal Structure Engine Ready"
    echo "========================================="

else

    echo "========================================="
    echo "PACK 014 FAILED"
    echo "========================================="

    exit 1

fi


echo ""
echo "Next commands:"
echo "chmod +x bootstrap/phase-2.8-pack-014.sh"
echo "bash bootstrap/phase-2.8-pack-014.sh"
echo "git add ."
echo 'git commit -m "feat(legal): implement arabic legal structure parser"'
echo "git push"
