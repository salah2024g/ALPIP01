from dataclasses import dataclass


@dataclass
class PromptTemplate:

    name: str
    content: str


    def render(
        self,
        variables: dict
    ) -> str:

        return self.content.format(
            **variables
        )
