from typing import Optional

from ...plugin import Plugin
from .GzGui import GzGui


class WorldStatsPlugin(Plugin):
    def __init__(self,
                 sim_time: bool = True,
                 real_time: bool = True,
                 real_time_factor: bool = True,
                 iterations: bool = True,
                 topic: Optional[str] = None,

                 name="World stats", **gui_kwargs
                 ):
        super().__init__(name=name, filename="WorldControl", elements=[
            GzGui(
                **{"title": "World stats", "show_title_bar": True, "resizable": False, "height": 110.0, "width": 290.0,
                   "z": 1.0, "state": "floating", "anchor": "3D View", "anchors": [
                        GzGui.Anchor("right", "right"),
                        GzGui.Anchor("bottom", "bottom")
                    ], **gui_kwargs})
        ], sim_time=sim_time, real_time=real_time, real_time_factor=real_time_factor, iterations=iterations,
                         topic=topic)
