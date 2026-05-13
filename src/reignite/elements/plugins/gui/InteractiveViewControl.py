from reignite.elements import Plugin
from reignite.elements.plugins.gui.GzGui import GzGui


class InteractiveViewControlPlugin(Plugin):
    def __init__(self, name="Interactive view control", **gui_kwargs):
        super().__init__(name=name, filename="InteractiveViewControl", elements=[
            GzGui(**{"resizable": False, "width": 5.0, "height": 5.0, "state": "floating", "show_title_bar": False,
                     **gui_kwargs}),
        ])
