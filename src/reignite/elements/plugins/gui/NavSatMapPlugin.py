from .GzGui import GzGui
from ...plugin import Plugin


@Plugin.register("NavSatMap", "NavSatMap")
class NavSatMapPlugin(Plugin):
    def __init__(
            self,
            topic: str | None = None,
            topic_picker: bool | None = None,
            name: str = "NavSatMap",
            **gui_kwargs
    ):
        super().__init__(
            filename="NavSatMap",
            name=name,
            elements=[
                GzGui(**gui_kwargs)
            ],
            topic=topic,
            topic_picker=topic_picker,
        )
