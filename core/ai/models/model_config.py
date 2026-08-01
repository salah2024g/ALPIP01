from dataclasses import dataclass


@dataclass
class ModelConfig:
    provider: str
    model_name: str
    temperature: float = 0.2
    max_tokens: int = 2000
