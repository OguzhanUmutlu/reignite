from ...plugin import Plugin


class DopplerVelocityLogSystem(Plugin):
    def __init__(self):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-doppler-velocity-log-system",
            name="gz::sim::systems::DopplerVelocityLogSystem"
        )
