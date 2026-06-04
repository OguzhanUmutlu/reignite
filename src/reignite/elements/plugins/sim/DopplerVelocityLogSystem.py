from ...plugin import Plugin


@Plugin.register("gz-sim-doppler-velocity-log-system", "gz::sim::systems::DopplerVelocityLogSystem")
class DopplerVelocityLogSystemPlugin(Plugin):
    def __init__(self):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-doppler-velocity-log-system",
            name="gz::sim::systems::DopplerVelocityLogSystem"
        )
