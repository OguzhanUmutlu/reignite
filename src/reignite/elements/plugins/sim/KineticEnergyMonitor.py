from ...plugin import Plugin


class KineticEnergyMonitorPlugin(Plugin):
    def __init__(
            self,
            link_name: str,
            kinetic_energy_threshold: float = 7.0,
            topic: str | None = None
    ):
        if not link_name:
            raise ValueError("link_name is required.")

        super().__init__(
            sdf_version=None,
            filename="gz-sim-kinetic-energy-monitor-system",
            name="gz::sim::systems::KineticEnergyMonitor",
            link_name=link_name,
            kinetic_energy_threshold=kinetic_energy_threshold,
            topic=topic
        )
