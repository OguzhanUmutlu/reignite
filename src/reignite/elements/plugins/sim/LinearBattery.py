from ...plugin import Plugin


@Plugin.register("gz-sim-linearbatteryplugin-system", "gz::sim::systems::LinearBatteryPlugin")
class LinearBatteryPlugin(Plugin):
    def __init__(
            self,
            battery_name: str,
            voltage: float,
            capacity: float,
            power_load: float,
            open_circuit_voltage_constant_coef: float | None = None,
            open_circuit_voltage_linear_coef: float | None = None,
            initial_charge: float | None = None,
            resistance: float | None = None,
            smooth_current_tau: float | None = None,
            fix_issue_225: bool | None = None,
            invert_current_sign: bool | None = None,
            enable_recharge: bool = False,
            charging_time: float | None = None,
            recharge_by_topic: bool | None = None,
            start_draining: bool | None = None,
            power_draining_topic: str | list[str] | None = None,
            stop_power_draining_topic: str | list[str] | None = None
    ):
        if enable_recharge and charging_time is None:
            raise ValueError("charging_time must be specified if enable_recharge is True.")

        if capacity <= 0:
            raise ValueError("capacity must be greater than 0.")

        super().__init__(
            sdf_version=None,
            filename="gz-sim-linearbatteryplugin-system",
            name="gz::sim::systems::LinearBatteryPlugin",
            battery_name=battery_name,
            voltage=voltage,
            capacity=capacity,
            power_load=power_load,
            open_circuit_voltage_constant_coef=open_circuit_voltage_constant_coef,
            open_circuit_voltage_linear_coef=open_circuit_voltage_linear_coef,
            initial_charge=initial_charge,
            resistance=resistance,
            smooth_current_tau=smooth_current_tau,
            fix_issue_225=fix_issue_225,
            invert_current_sign=invert_current_sign,
            enable_recharge=enable_recharge,
            charging_time=charging_time,
            recharge_by_topic=recharge_by_topic,
            start_draining=start_draining,
            power_draining_topic=power_draining_topic,
            stop_power_draining_topic=stop_power_draining_topic
        )
