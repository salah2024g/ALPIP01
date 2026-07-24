from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class Document:

    id: str

    path: Path

    media_type: str

    metadata: dict[str, Any] = field(default_factory=dict)
