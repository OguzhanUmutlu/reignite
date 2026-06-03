from reignite.elements.plugin import Plugin, ParentElement


class WheelSlipPlugin(Plugin):
    class Wheel(ParentElement):
        def __init__(
                self,
                link_name: str,
                slip_compliance_lateral: float | None = None,
                slip_compliance_longitudinal: float | None = None,
                wheel_normal_force: float | None = None,
                wheel_radius: float | None = None
        ):
            super().__init__(
                "wheel",
                link_name=link_name,
                slip_compliance_lateral=slip_compliance_lateral,
                slip_compliance_longitudinal=slip_compliance_longitudinal,
                wheel_normal_force=wheel_normal_force,
                wheel_radius=wheel_radius
            )

    def __init__(
            self,
            wheel: list[Wheel] | Wheel | None = None,
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-wheel-slip-system",
            name="gz::sim::systems::WheelSlip",
            elements=[wheel] if isinstance(wheel, WheelSlipPlugin.Wheel) else wheel
        )
