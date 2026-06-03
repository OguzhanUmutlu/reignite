from ...plugin import Plugin


class LogicalCameraPlugin(Plugin):
    def __init__(
            self,
            topic: str | None = None,
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-logical-camera-system",
            name="gz::sim::systems::LogicalCamera",
            topic=topic,
        )
