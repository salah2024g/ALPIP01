from abc import ABC, abstractmethod


class PluginContract(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def initialize(self) -> None:
        pass

    @abstractmethod
    def execute(self, payload: dict) -> dict:
        pass
