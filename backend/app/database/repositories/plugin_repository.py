from app.database.models.plugin import PluginModel

from .base import BaseRepository


class PluginRepository(BaseRepository):
    def __init__(self):
        super().__init__(PluginModel)
