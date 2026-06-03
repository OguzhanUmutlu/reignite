from .GzGui import GzGui
from ...plugin import Plugin


class EntityContextMenuPlugin(Plugin):
    def __init__(self, name="Entity context menu", **gui_kwargs):
        super().__init__(name=name, filename="EntityContextMenuPlugin", elements=[
            GzGui(**{"state": "floating", "width": 5.0, "height": 5.0, "show_title_bar": False, **gui_kwargs})
        ])
