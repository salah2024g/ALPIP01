from core.legal_reference.graph import ReferenceGraph
from core.legal_reference.index import CitationIndex
from core.legal_reference.parser.external_parser import ExternalReferenceParser
from core.legal_reference.parser.parser import LegalReferenceParser


class ReferenceEngine:
    def __init__(self):

        self.internal = LegalReferenceParser()

        self.external = ExternalReferenceParser()

    def analyze(self, text: str):

        index = CitationIndex()

        graph = ReferenceGraph()

        for ref in self.internal.parse(text):
            index.add_internal(ref)

            graph.add_edge("document", f"article:{ref.article_number}")

        for ref in self.external.parse(text):
            index.add_external(ref)

            graph.add_edge(
                "document", f"{ref.reference_type}:{ref.law_number or 'unknown'}"
            )

        return index, graph
