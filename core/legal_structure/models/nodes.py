from dataclasses import dataclass, field


@dataclass(slots=True)
class LegalNode:
    node_type: str

    title: str

    number: str | None = None

    text: str = ""

    children: list["LegalNode"] = field(default_factory=list)

    def add_child(self, node: "LegalNode"):

        self.children.append(node)
