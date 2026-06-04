from .GzGui import GzGui
from ...plugin import Plugin


@Plugin.register("KeyPublisher", "KeyPublisher")
class KeyPublisherPlugin(Plugin):
    def __init__(
            self,
            name: str = "KeyPublisher",
            **gui_kwargs
    ):
        super().__init__(
            filename="KeyPublisher",
            name=name,
            elements=[
                GzGui(**gui_kwargs)
            ],
        )
