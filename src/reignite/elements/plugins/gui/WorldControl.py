from typing import Optional

from reignite.elements import Plugin
from reignite.elements.plugin import TextElement
from reignite.elements.plugins.gui.GzGui import GzGui


class WorldControlPlugin(Plugin):
    def __init__(self,
                 play_pause: bool = True,
                 step: bool = True,
                 start_paused: bool = False,
                 use_event: bool = True,
                 stats_topic: Optional[str] = None,

                 name="World control", **gui_kwargs
                 ):
        super().__init__(name=name, filename="WorldControl", elements=[
            GzGui(**{"showTitleBar": False, "resizable": False, "height": 72.0, "z": 1.0, "state": "floating",
                     "anchor": "3D View", "anchors": [
                    GzGui.Anchor("left", "left"),
                    GzGui.Anchor("bottom", "bottom")
                ], **gui_kwargs}),
            TextElement("play_pause", str(play_pause).lower()),
            TextElement("step", str(step).lower()),
            TextElement("start_paused", str(start_paused).lower()),
            TextElement("use_event", str(use_event).lower())
        ])
        if stats_topic is not None:
            self.elements.append(TextElement("stats_topic", stats_topic))
