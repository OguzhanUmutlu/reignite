from .GzGui import GzGui
from ...plugin import Plugin


@Plugin.register("Publisher", "Publisher")
class PublisherPlugin(Plugin):
    def __init__(
            self,
            frequency: float | None = None,
            message: str | None = None,
            message_type: str | None = None,
            topic: str | None = None,
            name: str = "Publisher",
            **gui_kwargs
    ):
        super().__init__(
            filename="Publisher",
            name=name,
            elements=[
                GzGui(**gui_kwargs)
            ],
            frequency=frequency,
            message=message,
            message_type=message_type,
            topic=topic,
        )
