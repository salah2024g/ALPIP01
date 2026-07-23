from dataclasses import dataclass


@dataclass
class Settings:
    app_name: str = "ALPIP"
    environment: str = "development"


settings = Settings()
