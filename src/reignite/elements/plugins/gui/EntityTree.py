from .GzGui import GzGui
from ...plugin import Plugin


class EntityTreePlugin(Plugin):
    def __init__(self, name="Entity tree", **gui_kwargs):
        super().__init__(name=name, filename="EntityTree", elements=[
            GzGui(**{"state": "docked", **gui_kwargs})
        ])
