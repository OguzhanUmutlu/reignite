from typing import Optional

from .GzGui import GzGui
from ...plugin import Plugin


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
            GzGui(**{"show_title_bar": False, "resizable": False, "height": 72.0, "z": 1.0, "state": "floating",
                     "anchor": "3D View", "anchors": [
                    GzGui.Anchor("left", "left"),
                    GzGui.Anchor("bottom", "bottom")
                ], **gui_kwargs})
        ], play_pause=play_pause, step=step, start_paused=start_paused, use_event=use_event, stats_topic=stats_topic)
