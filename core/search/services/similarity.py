from abc import ABC, abstractmethod


class SimilarityEngine(ABC):


    @abstractmethod
    def calculate(
        self,
        first: str,
        second: str
    ) -> float:

        pass
