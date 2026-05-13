from reignite.elements import Plugin
from reignite.elements.plugins.gui.GzGui import GzGui


class CameraTrackingPlugin(Plugin):
    def __init__(self, name="Camera Tracking", **gui_kwargs):
        super().__init__(name=name, filename="CameraTracking", elements=[
            GzGui(**{"resizable": False, "width": 5.0, "height": 5.0, "state": "floating", "show_title_bar": False,
                     **gui_kwargs}),
        ])
