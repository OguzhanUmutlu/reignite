from ...plugin import Plugin


class SpacecraftThrusterModelPlugin(Plugin):
    def __init__(
            self,
            topic: str | None = None,
            link_name: str | None = None,
            actuator_number: int | None = None,
            max_thrust: float | None = None,
            duty_cycle_frequency: float | None = None,
            sub_topic: str | None = None,
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-spacecraft-thruster-model-system",
            name="gz::sim::systems::SpacecraftThrusterModel",
            topic=topic,
            link_name=link_name,
            actuator_number=actuator_number,
            max_thrust=max_thrust,
            duty_cycle_frequency=duty_cycle_frequency,
            sub_topic=sub_topic,
        )
