from ...plugin import Plugin
from .GzGui import GzGui


class EntityTreePlugin(Plugin):
    def __init__(self, name="Entity tree", **gui_kwargs):
        super().__init__(name=name, filename="EntityTree", elements=[
            GzGui(**{"state": "docked", **gui_kwargs})
        ])
