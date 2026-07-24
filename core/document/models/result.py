from dataclasses import dataclass, field


@dataclass(slots=True)
class ProcessingResult:

    success: bool

    text: str = ""

    errors: list[str] = field(default_factory=list)
