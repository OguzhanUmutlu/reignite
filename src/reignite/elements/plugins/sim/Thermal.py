from ...plugin import Plugin


@Plugin.register("gz-sim-thermal-system", "gz::sim::systems::Thermal")
class ThermalPlugin(Plugin):
    def __init__(
            self,
            temperature: float | None = None,
            heat_signature: str | None = None,
            min_temp: float | None = None,
            max_temp: float | None = None,
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-thermal-system",
            name="gz::sim::systems::Thermal",
            temperature=temperature,
            heat_signature=heat_signature,
            min_temp=min_temp,
            max_temp=max_temp,
        )
