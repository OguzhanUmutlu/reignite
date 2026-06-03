from ...plugin import Plugin
from .GzGui import GzGui


class GzSceneManagerPlugin(Plugin):
    def __init__(self, name="Scene Manager", **gui_kwargs):
        super().__init__(name=name, filename="GzSceneManager", elements=[
            GzGui(**{"resizable": False, "width": 5.0, "height": 5.0, "state": "floating", "show_title_bar": False,
                     **gui_kwargs}),
        ])
