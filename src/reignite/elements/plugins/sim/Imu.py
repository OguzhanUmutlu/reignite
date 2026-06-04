from ...plugin import Plugin


@Plugin.register("gz-sim-imu-system", "gz::sim::systems::Imu")
class ImuPlugin(Plugin):
    def __init__(self):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-imu-system",
            name="gz::sim::systems::Imu"
        )
