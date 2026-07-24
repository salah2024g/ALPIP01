from core.legal_reference.models.external_reference import (
    ExternalReference
)

from core.legal_reference.parser.external_patterns import (
    LAW_PATTERN,
    DECISION_PATTERN,
    REGULATION_PATTERN
)

from core.legal_structure.parser.normalizer import (
    normalize_number
)


class ExternalReferenceParser:


    def parse(
        self,
        text: str
    ):

        references = []


        for match in LAW_PATTERN.finditer(text):

            references.append(

                ExternalReference(

                    reference_type="law",

                    law_number=normalize_number(
                        match.group(1)
                    ),

                    year=normalize_number(
                        match.group(2)
                    ),

                    matched_text=match.group(0),

                    start=match.start(),

                    end=match.end()

                )

            )


        for match in DECISION_PATTERN.finditer(text):

            references.append(

                ExternalReference(

                    reference_type="decision",

                    law_number=normalize_number(
                        match.group(1)
                    ),

                    year=normalize_number(
                        match.group(2)
                    ),

                    matched_text=match.group(0),

                    start=match.start(),

                    end=match.end()

                )

            )


        for match in REGULATION_PATTERN.finditer(text):

            references.append(

                ExternalReference(

                    reference_type="regulation",

                    law_number=None,

                    year=None,

                    matched_text=match.group(0),

                    start=match.start(),

                    end=match.end()

                )

            )

        references.sort(
            key=lambda item: item.start
        )

        return references
