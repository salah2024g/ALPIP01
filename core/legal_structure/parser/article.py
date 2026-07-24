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
