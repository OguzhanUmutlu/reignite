from ...plugin import Plugin


class SceneBroadcasterPlugin(Plugin):
    def __init__(
            self,
            dynamic_pose_hertz: int | None = None,
            state_hertz: float | None = None,
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-scene-broadcaster-system",
            name="gz::sim::systems::SceneBroadcaster",
            dynamic_pose_hertz=dynamic_pose_hertz,
            state_hertz=state_hertz,
        )
