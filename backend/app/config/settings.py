from dataclasses import dataclass


@dataclass
class Settings:

    app_name: str = "ALPIP"
    version: str = "2.5"
    environment: str = "development"



settings = Settings()
