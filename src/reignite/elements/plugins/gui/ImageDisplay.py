from reignite.elements import Plugin
from reignite.elements.plugins.gui.GzGui import GzGui


class ImageDisplayPlugin(Plugin):
    def __init__(self, topic: str, topic_picker: bool = True, show_depth_flip: bool = True, name="Camera",
                 **gui_kwargs):
        super().__init__(name=name, filename="WorldControl", elements=[GzGui(**{"state": "docked", **gui_kwargs})],
                         topic=topic, topic_picker=str(topic_picker).lower(),
                         show_depth_flip=str(show_depth_flip).lower())
