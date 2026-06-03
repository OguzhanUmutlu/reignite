from .GzGui import GzGui
from ...plugin import Plugin


class ComponentInspectorPlugin(Plugin):
    def __init__(self, name="Component inspector", **gui_kwargs):
        super().__init__(name=name, filename="ComponentInspector", elements=[
            GzGui(**{"state": "docked", **gui_kwargs})
        ])
