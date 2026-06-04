from .GzGui import GzGui
from ...plugin import Plugin


@Plugin.register("CameraTracking", "CameraTrackingConfig")
class CameraTrackingConfigPlugin(Plugin):
    def __init__(
            self,
            name: str = "CameraTrackingConfig",
            **gui_kwargs
    ):
        super().__init__(
            filename="CameraTracking",
            name=name,
            elements=[
                GzGui(**gui_kwargs)
            ],
        )
