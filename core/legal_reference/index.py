from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class CitationIndex:
    internal: list[Any] = field(default_factory=list)

    external: list[Any] = field(default_factory=list)

    def add_internal(self, reference):

        self.internal.append(reference)

    def add_external(self, reference):

        self.external.append(reference)
