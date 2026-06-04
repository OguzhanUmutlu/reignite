from .GzGui import GzGui
from ...plugin import Plugin


@Plugin.register("TopicEcho", "TopicEcho")
class TopicEchoPlugin(Plugin):
    def __init__(
            self,
            name: str = "TopicEcho",
            **gui_kwargs
    ):
        super().__init__(
            filename="TopicEcho",
            name=name,
            elements=[
                GzGui(**gui_kwargs)
            ],
        )
