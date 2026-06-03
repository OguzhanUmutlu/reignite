from ...plugin import Plugin
from .GzGui import GzGui


class ImageDisplayPlugin(Plugin):
    def __init__(self, topic: str, topic_picker: bool = True, show_depth_flip: bool = True, name="Camera",
                 **gui_kwargs):
        super().__init__(name=name, filename="WorldControl", elements=[GzGui(**{"state": "docked", **gui_kwargs})],
                         topic=topic, topic_picker=topic_picker,
                         show_depth_flip=show_depth_flip)
