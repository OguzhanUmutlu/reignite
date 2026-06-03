from .GzGui import GzGui
from ...plugin import Plugin


class TeleopPlugin(Plugin):
    def __init__(
            self,
            topic: str | None = None,
            name: str = "Teleop",
            **gui_kwargs
    ):
        super().__init__(
            filename="Teleop",
            name=name,
            elements=[
                GzGui(**gui_kwargs)
            ],
            topic=topic,
        )
