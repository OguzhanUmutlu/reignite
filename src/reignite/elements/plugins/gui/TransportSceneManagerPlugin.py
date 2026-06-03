from .GzGui import GzGui
from ...plugin import Plugin


class TransportSceneManagerPlugin(Plugin):
    def __init__(
            self,
            deletion_topic: str | None = None,
            pose_topic: str | None = None,
            scene_topic: str | None = None,
            service: str | None = None,
            name: str = "TransportSceneManager",
            **gui_kwargs
    ):
        super().__init__(
            filename="TransportSceneManager",
            name=name,
            elements=[
                GzGui(**gui_kwargs)
            ],
            deletion_topic=deletion_topic,
            pose_topic=pose_topic,
            scene_topic=scene_topic,
            service=service,
        )
