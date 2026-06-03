from ...plugin import Plugin


class LookupWheelSlipPlugin(Plugin):
    def __init__(
            self,
            slip_map: str | None = None,
            size_x: float | None = None,
            size_y: float | None = None,
            wheel_link_name: list[str] | str | None = None,
            slip_compliance_lateral_delta: float | None = None,
            slip_compliance_longitudinal_delta: float | None = None,
            friction_delta: float | None = None,
            **kwargs,
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-lookup-wheel-slip-system",
            name="gz::sim::systems::LookupWheelSlip",
            slip_map=slip_map,
            size_x=size_x,
            size_y=size_y,
            wheel_link_name=wheel_link_name,
            slip_compliance_lateral_delta=slip_compliance_lateral_delta,
            slip_compliance_longitudinal_delta=slip_compliance_longitudinal_delta,
            friction_delta=friction_delta,
            **kwargs,
        )
