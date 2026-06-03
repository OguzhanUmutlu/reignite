from ...plugin import Plugin


class MagnetometerPlugin(Plugin):
    def __init__(
            self,
            use_units_gauss: bool | None = None,
            use_earth_frame_ned: bool | None = None,
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-magnetometer-system",
            name="gz::sim::systems::Magnetometer",
            use_units_gauss=use_units_gauss,
            use_earth_frame_ned=use_earth_frame_ned,
        )
