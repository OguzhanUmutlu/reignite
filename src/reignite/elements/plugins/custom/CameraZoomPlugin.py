from typing import Optional
from ...plugin import Plugin

@Plugin.register("CameraZoomPlugin", "CameraZoomPlugin")
class CameraZoomPlugin(Plugin):
    def __init__(
            self,
            max_zoom: float | None = None,
            slew_rate: float | None = None,
            topic: str | list[str] | None = None,
            **kwargs
    ):
        super().__init__(
            filename="CameraZoomPlugin",
            name="CameraZoomPlugin",
            max_zoom=max_zoom,
            slew_rate=slew_rate,
            topic=topic,
            **kwargs
        )
