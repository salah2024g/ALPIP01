from enum import Enum


class DocumentType(str, Enum):

    LAW = "law"
    REGULATION = "regulation"
    DECISION = "decision"
    INSTRUCTION = "instruction"
