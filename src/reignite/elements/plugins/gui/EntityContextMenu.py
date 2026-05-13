from reignite.elements import Plugin
from reignite.elements.plugins.gui.GzGui import GzGui


class EntityContextMenuPlugin(Plugin):
    def __init__(self, name="Entity context menu", **gui_kwargs):
        super().__init__(name=name, filename="MinimalScene", elements=[
            GzGui(**{"state": "floating", "width": 5.0, "height": 5.0, "showTitleBar": False, **gui_kwargs})
        ])
