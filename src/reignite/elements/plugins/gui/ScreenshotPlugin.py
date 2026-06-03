from .GzGui import GzGui
from ...plugin import Plugin


class ScreenshotPlugin(Plugin):
    def __init__(
            self,
            name: str = "Screenshot",
            **gui_kwargs
    ):
        super().__init__(
            filename="Screenshot",
            name=name,
            elements=[
                GzGui(**gui_kwargs)
            ],
        )
