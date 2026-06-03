from reignite.elements.plugin import Plugin


class Thruster(Plugin):
    def __init__(
            self,
            joint_name: str,
            namespace: str | None = None,
            thrust_coefficient: float | None = None,
            propeller_diameter: float | None = None,
            fluid_density: float | None = None,
            use_angvel_cmd: bool | None = None,
            wake_fraction: float | None = None,
            alpha_1: float | None = None,
            alpha_2: float | None = None,
            deadband: float | None = None,
            topic: str | None = None,
            max_thrust_cmd: float | None = None,
            min_thrust_cmd: float | None = None,
            velocity_control: bool | None = None,
            p_gain: float | None = None,
            i_gain: float | None = None,
            d_gain: float | None = None,
            power_load: float | None = None,
            battery_name: str | None = None,
            **kwargs
    ):
        super().__init__(
            filename="gz-sim-thruster-system",
            name="gz::sim::systems::Thruster",
            joint_name=joint_name,
            namespace=namespace,
            thrust_coefficient=thrust_coefficient,
            propeller_diameter=propeller_diameter,
            fluid_density=fluid_density,
            use_angvel_cmd=use_angvel_cmd,
            wake_fraction=wake_fraction,
            alpha_1=alpha_1,
            alpha_2=alpha_2,
            deadband=deadband,
            topic=topic,
            max_thrust_cmd=max_thrust_cmd,
            min_thrust_cmd=min_thrust_cmd,
            velocity_control=velocity_control,
            p_gain=p_gain,
            i_gain=i_gain,
            d_gain=d_gain,
            power_load=power_load,
            battery_name=battery_name,
            **kwargs
        )
