from reignite.elements.plugin import Plugin


@Plugin.register("gz-sim-optical-tactile-plugin-system", "gz::sim::systems::OpticalTactilePlugin")
class OpticalTactilePlugin(Plugin):
    def __init__(
            self,
            enabled: bool | None = None,
            visualization_resolution: int | None = None,
            visualize_forces: bool | None = None,
            visualize_contacts: bool | None = None,
            extended_sensing: float | None = None,
            visualize_sensor: bool | None = None,
            force_length: float | None = None,
            namespace: str | None = None,
            size: list[float] | str | None = None,
            **kwargs
    ):
        if isinstance(size, list):
            size = " ".join(map(str, size))

        super().__init__(
            filename="gz-sim-optical-tactile-plugin-system",
            name="gz::sim::systems::OpticalTactilePlugin",
            enabled=enabled,
            visualization_resolution=visualization_resolution,
            visualize_forces=visualize_forces,
            visualize_contacts=visualize_contacts,
            extended_sensing=extended_sensing,
            visualize_sensor=visualize_sensor,
            force_length=force_length,
            namespace=namespace,
            size=size,
            **kwargs
        )
