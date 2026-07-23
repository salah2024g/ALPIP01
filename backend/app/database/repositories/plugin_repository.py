from .base import BaseRepository

from app.database.models.plugin import PluginModel


class PluginRepository(
    BaseRepository
):

    def __init__(self):
        super().__init__(
            PluginModel
        )
