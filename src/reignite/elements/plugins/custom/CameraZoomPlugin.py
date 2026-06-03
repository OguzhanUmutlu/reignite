from typing import Optional
from ...plugin import Plugin

class CameraZoomPlugin(Plugin):
    def __init__(
            self,
            max_zoom: Optional[float] = None,
            slew_rate: Optional[float] = None,
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
