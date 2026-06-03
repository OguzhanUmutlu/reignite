from .GzGui import GzGui
from ...plugin import Plugin


class TopicViewerPlugin(Plugin):
    def __init__(
            self,
            name: str = "TopicViewer",
            **gui_kwargs
    ):
        super().__init__(
            filename="TopicViewer",
            name=name,
            elements=[
                GzGui(**gui_kwargs)
            ],
        )
