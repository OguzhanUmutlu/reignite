from ...link import Link
from ...plugin import Plugin


class BuoyancyEnginePlugin(Plugin):
    def __init__(
            self,
            link_name: str | Link,
            min_volume: float | None = None,
            max_volume: float | None = None,
            fluid_density: float | None = None,
            default_volume: float | None = None,
            neutral_volume: float | None = None,
            max_inflation_rate: float | None = None,
            surface: float | None = None,
            namespace: str | None = None
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-buoyancy-engine-system",
            name="gz::sim::systems::BuoyancyEngine",
            link_name=link_name.name if isinstance(link_name, Link) else link_name,
            min_volume=min_volume,
            max_volume=max_volume,
            fluid_density=fluid_density,
            default_volume=default_volume,
            neutral_volume=neutral_volume,
            max_inflation_rate=max_inflation_rate,
            surface=surface,
            namespace=namespace
        )
