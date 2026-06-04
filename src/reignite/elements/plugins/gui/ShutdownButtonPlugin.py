from .GzGui import GzGui
from ...plugin import Plugin


@Plugin.register("ShutdownButton", "ShutdownButton")
class ShutdownButtonPlugin(Plugin):
    def __init__(
            self,
            name: str = "ShutdownButton",
            **gui_kwargs
    ):
        super().__init__(
            filename="ShutdownButton",
            name=name,
            elements=[
                GzGui(**gui_kwargs)
            ],
        )
