from typing import Generic, TypeVar


T = TypeVar("T")


class BaseRepository(Generic[T]):

    def __init__(self, model):
        self.model = model


    def get_model(self):
        return self.model
