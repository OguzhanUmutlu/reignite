from reignite.elements import Plugin
from reignite.elements.plugins.gui.GzGui import GzGui


class ComponentInspectorPlugin(Plugin):
    def __init__(self, name="Component inspector", **gui_kwargs):
        super().__init__(name=name, filename="ComponentInspector", elements=[
            GzGui(**{"state": "docked", **gui_kwargs})
        ])
