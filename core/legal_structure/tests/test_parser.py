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
