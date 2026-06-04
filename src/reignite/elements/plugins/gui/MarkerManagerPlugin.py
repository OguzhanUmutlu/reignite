from .GzGui import GzGui
from ...plugin import Plugin


@Plugin.register("MarkerManager", "MarkerManager")
class MarkerManagerPlugin(Plugin):
    def __init__(
            self,
            stats_topic: str | None = None,
            topic_name: str | None = None,
            warn_on_action_failure: bool | None = None,
            name: str = "MarkerManager",
            **gui_kwargs
    ):
        super().__init__(
            filename="MarkerManager",
            name=name,
            elements=[
                GzGui(**gui_kwargs)
            ],
            stats_topic=stats_topic,
            topic_name=topic_name,
            warn_on_action_failure=warn_on_action_failure,
        )
