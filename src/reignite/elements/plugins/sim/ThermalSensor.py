from ...plugin import Plugin


class ThermalSensorPlugin(Plugin):
    def __init__(
            self,
            resolution: float | None = None,
            min_temp: float | None = None,
            max_temp: float | None = None,
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-thermal-sensor-system",
            name="gz::sim::systems::ThermalSensor",
            resolution=resolution,
            min_temp=min_temp,
            max_temp=max_temp,
        )
