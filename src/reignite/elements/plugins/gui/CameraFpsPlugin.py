from .GzGui import GzGui
from ...plugin import Plugin


@Plugin.register("CameraFps", "CameraFps")
class CameraFpsPlugin(Plugin):
    def __init__(
            self,
            name: str = "CameraFps",
            **gui_kwargs
    ):
        super().__init__(
            filename="CameraFps",
            name=name,
            elements=[
                GzGui(**gui_kwargs)
            ],
        )
