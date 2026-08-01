from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ALDFDocument:
    id: str

    text: str

    metadata: dict[str, Any] = field(default_factory=dict)
