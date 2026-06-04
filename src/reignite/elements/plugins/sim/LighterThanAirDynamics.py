from ...plugin import Plugin


@Plugin.register("gz-sim-lighter-than-air-dynamics-system", "gz::sim::systems::LighterThanAirDynamics")
class LighterThanAirDynamicsPlugin(Plugin):
    def __init__(
            self,
            air_density: float | None = None,
            link_name: str | None = None,
            moment_inviscid_coeff: float | None = None,
            moment_viscous_coeff: float | None = None,
            force_inviscid_coeff: float | None = None,
            force_viscous_coeff: float | None = None,
            eps_v: float | None = None,
            axial_drag_coeff: float | None = None,
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-lighter-than-air-dynamics-system",
            name="gz::sim::systems::LighterThanAirDynamics",
            air_density=air_density,
            link_name=link_name,
            moment_inviscid_coeff=moment_inviscid_coeff,
            moment_viscous_coeff=moment_viscous_coeff,
            force_inviscid_coeff=force_inviscid_coeff,
            force_viscous_coeff=force_viscous_coeff,
            eps_v=eps_v,
            axial_drag_coeff=axial_drag_coeff,
        )
