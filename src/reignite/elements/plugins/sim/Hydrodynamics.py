from ...plugin import Plugin


@Plugin.register("gz-sim-hydrodynamics-system", "gz::sim::systems::Hydrodynamics")
class HydrodynamicsPlugin(Plugin):
    def __init__(
            self,
            link_name: str,
            namespace: str | None = None,
            disable_coriolis: bool = False,
            disable_added_mass: bool = False,
            default_current: list[float] | tuple[float, float, float] | None = None,
            lookup_current_x: str | None = None,
            lookup_current_y: str | None = None,
            lookup_current_z: str | None = None,
            **stability_derivatives: float
    ):
        if not link_name:
            raise ValueError("link_name is strictly required for the Hydrodynamics plugin to act upon.")

        if default_current is not None and len(default_current) != 3:
            raise ValueError("default_current must be a 3-dimensional vector (x, y, z) if specified.")

        # The C++ plugin expects stability derivatives in SNAME 1950 convention.
        # e.g., xU, yV, xUU, xUabsU, xDotU. We pass any additional kwargs directly.
        super().__init__(
            sdf_version=None,
            filename="gz-sim-hydrodynamics-system",
            name="gz::sim::systems::Hydrodynamics",
            link_name=link_name,
            namespace=namespace,
            disable_coriolis=disable_coriolis,
            disable_added_mass=disable_added_mass,
            default_current=default_current,
            lookup_current_x=lookup_current_x,
            lookup_current_y=lookup_current_y,
            lookup_current_z=lookup_current_z,
            **stability_derivatives
        )
