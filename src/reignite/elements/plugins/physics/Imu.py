from ...plugin import Plugin


class ImuPlugin(Plugin):
    def __init__(self):
        super().__init__(name="gz::sim::systems::Imu", filename="gz-sim-imu-system")
