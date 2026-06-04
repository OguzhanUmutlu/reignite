from xml.etree import ElementTree as ET
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

        self.battery_name = battery_name
        self.voltage = voltage
        self.capacity = capacity
        self.power_load = power_load
        self.open_circuit_voltage_constant_coef = open_circuit_voltage_constant_coef
        self.open_circuit_voltage_linear_coef = open_circuit_voltage_linear_coef
        self.initial_charge = initial_charge
        self.resistance = resistance
        self.smooth_current_tau = smooth_current_tau
        self.fix_issue_225 = fix_issue_225
        self.invert_current_sign = invert_current_sign
        self.enable_recharge = enable_recharge
        self.charging_time = charging_time
        self.recharge_by_topic = recharge_by_topic
        self.start_draining = start_draining
        self.power_draining_topic = power_draining_topic
        self.stop_power_draining_topic = stop_power_draining_topic
        super().__init__(sdf_version=None, filename="gz-sim-linearbatteryplugin-system", name="gz::sim::systems::LinearBatteryPlugin")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        battery_name_el = el.find('battery_name')
        voltage_el = el.find('voltage')
        capacity_el = el.find('capacity')
        power_load_el = el.find('power_load')
        open_circuit_voltage_constant_coef_el = el.find('open_circuit_voltage_constant_coef')
        open_circuit_voltage_linear_coef_el = el.find('open_circuit_voltage_linear_coef')
        initial_charge_el = el.find('initial_charge')
        resistance_el = el.find('resistance')
        smooth_current_tau_el = el.find('smooth_current_tau')
        fix_issue_225_el = el.find('fix_issue_225')
        invert_current_sign_el = el.find('invert_current_sign')
        enable_recharge_el = el.find('enable_recharge')
        charging_time_el = el.find('charging_time')
        recharge_by_topic_el = el.find('recharge_by_topic')
        start_draining_el = el.find('start_draining')
        power_draining_topic_els = el.findall('power_draining_topic')
        power_draining_topic_vals = [e.text for e in power_draining_topic_els if e.text is not None] if power_draining_topic_els else None
        stop_power_draining_topic_els = el.findall('stop_power_draining_topic')
        stop_power_draining_topic_vals = [e.text for e in stop_power_draining_topic_els if e.text is not None] if stop_power_draining_topic_els else None

        return cls(
            battery_name=battery_name_el.text if battery_name_el is not None and battery_name_el.text is not None else None,
            voltage=float(voltage_el.text) if voltage_el is not None and voltage_el.text is not None else None,
            capacity=float(capacity_el.text) if capacity_el is not None and capacity_el.text is not None else None,
            power_load=float(power_load_el.text) if power_load_el is not None and power_load_el.text is not None else None,
            open_circuit_voltage_constant_coef=float(open_circuit_voltage_constant_coef_el.text) if open_circuit_voltage_constant_coef_el is not None and open_circuit_voltage_constant_coef_el.text is not None else None,
            open_circuit_voltage_linear_coef=float(open_circuit_voltage_linear_coef_el.text) if open_circuit_voltage_linear_coef_el is not None and open_circuit_voltage_linear_coef_el.text is not None else None,
            initial_charge=float(initial_charge_el.text) if initial_charge_el is not None and initial_charge_el.text is not None else None,
            resistance=float(resistance_el.text) if resistance_el is not None and resistance_el.text is not None else None,
            smooth_current_tau=float(smooth_current_tau_el.text) if smooth_current_tau_el is not None and smooth_current_tau_el.text is not None else None,
            fix_issue_225=fix_issue_225_el.text.lower() == 'true' if fix_issue_225_el is not None and fix_issue_225_el.text is not None else None,
            invert_current_sign=invert_current_sign_el.text.lower() == 'true' if invert_current_sign_el is not None and invert_current_sign_el.text is not None else None,
            enable_recharge=enable_recharge_el.text.lower() == 'true' if enable_recharge_el is not None and enable_recharge_el.text is not None else None,
            charging_time=float(charging_time_el.text) if charging_time_el is not None and charging_time_el.text is not None else None,
            recharge_by_topic=recharge_by_topic_el.text.lower() == 'true' if recharge_by_topic_el is not None and recharge_by_topic_el.text is not None else None,
            start_draining=start_draining_el.text.lower() == 'true' if start_draining_el is not None and start_draining_el.text is not None else None,
            power_draining_topic=power_draining_topic_vals,
            stop_power_draining_topic=stop_power_draining_topic_vals,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::LinearBatteryPlugin", filename="gz-sim-linearbatteryplugin-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('battery_name', self.battery_name)
        _add('voltage', self.voltage)
        _add('capacity', self.capacity)
        _add('power_load', self.power_load)
        _add('open_circuit_voltage_constant_coef', self.open_circuit_voltage_constant_coef)
        _add('open_circuit_voltage_linear_coef', self.open_circuit_voltage_linear_coef)
        _add('initial_charge', self.initial_charge)
        _add('resistance', self.resistance)
        _add('smooth_current_tau', self.smooth_current_tau)
        _add('fix_issue_225', self.fix_issue_225)
        _add('invert_current_sign', self.invert_current_sign)
        _add('enable_recharge', self.enable_recharge)
        _add('charging_time', self.charging_time)
        _add('recharge_by_topic', self.recharge_by_topic)
        _add('start_draining', self.start_draining)
        if self.power_draining_topic is not None:
            for v in (self.power_draining_topic if isinstance(self.power_draining_topic, list) else [self.power_draining_topic]):
                _add('power_draining_topic', v)
        if self.stop_power_draining_topic is not None:
            for v in (self.stop_power_draining_topic if isinstance(self.stop_power_draining_topic, list) else [self.stop_power_draining_topic]):
                _add('stop_power_draining_topic', v)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        battery_name_el = el.find('battery_name')
        voltage_el = el.find('voltage')
        capacity_el = el.find('capacity')
        power_load_el = el.find('power_load')
        open_circuit_voltage_constant_coef_el = el.find('open_circuit_voltage_constant_coef')
        open_circuit_voltage_linear_coef_el = el.find('open_circuit_voltage_linear_coef')
        initial_charge_el = el.find('initial_charge')
        resistance_el = el.find('resistance')
        smooth_current_tau_el = el.find('smooth_current_tau')
        fix_issue_225_el = el.find('fix_issue_225')
        invert_current_sign_el = el.find('invert_current_sign')
        enable_recharge_el = el.find('enable_recharge')
        charging_time_el = el.find('charging_time')
        recharge_by_topic_el = el.find('recharge_by_topic')
        start_draining_el = el.find('start_draining')
        power_draining_topic_els = el.findall('power_draining_topic')
        power_draining_topic_vals = [e.text for e in power_draining_topic_els if e.text is not None] if power_draining_topic_els else None
        stop_power_draining_topic_els = el.findall('stop_power_draining_topic')
        stop_power_draining_topic_vals = [e.text for e in stop_power_draining_topic_els if e.text is not None] if stop_power_draining_topic_els else None

        return cls(
            battery_name=battery_name_el.text if battery_name_el is not None and battery_name_el.text is not None else None,
            voltage=float(voltage_el.text) if voltage_el is not None and voltage_el.text is not None else None,
            capacity=float(capacity_el.text) if capacity_el is not None and capacity_el.text is not None else None,
            power_load=float(power_load_el.text) if power_load_el is not None and power_load_el.text is not None else None,
            open_circuit_voltage_constant_coef=float(open_circuit_voltage_constant_coef_el.text) if open_circuit_voltage_constant_coef_el is not None and open_circuit_voltage_constant_coef_el.text is not None else None,
            open_circuit_voltage_linear_coef=float(open_circuit_voltage_linear_coef_el.text) if open_circuit_voltage_linear_coef_el is not None and open_circuit_voltage_linear_coef_el.text is not None else None,
            initial_charge=float(initial_charge_el.text) if initial_charge_el is not None and initial_charge_el.text is not None else None,
            resistance=float(resistance_el.text) if resistance_el is not None and resistance_el.text is not None else None,
            smooth_current_tau=float(smooth_current_tau_el.text) if smooth_current_tau_el is not None and smooth_current_tau_el.text is not None else None,
            fix_issue_225=fix_issue_225_el.text.lower() == 'true' if fix_issue_225_el is not None and fix_issue_225_el.text is not None else None,
            invert_current_sign=invert_current_sign_el.text.lower() == 'true' if invert_current_sign_el is not None and invert_current_sign_el.text is not None else None,
            enable_recharge=enable_recharge_el.text.lower() == 'true' if enable_recharge_el is not None and enable_recharge_el.text is not None else None,
            charging_time=float(charging_time_el.text) if charging_time_el is not None and charging_time_el.text is not None else None,
            recharge_by_topic=recharge_by_topic_el.text.lower() == 'true' if recharge_by_topic_el is not None and recharge_by_topic_el.text is not None else None,
            start_draining=start_draining_el.text.lower() == 'true' if start_draining_el is not None and start_draining_el.text is not None else None,
            power_draining_topic=power_draining_topic_vals,
            stop_power_draining_topic=stop_power_draining_topic_vals,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::LinearBatteryPlugin", filename="gz-sim-linearbatteryplugin-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('battery_name', self.battery_name)
        _add('voltage', self.voltage)
        _add('capacity', self.capacity)
        _add('power_load', self.power_load)
        _add('open_circuit_voltage_constant_coef', self.open_circuit_voltage_constant_coef)
        _add('open_circuit_voltage_linear_coef', self.open_circuit_voltage_linear_coef)
        _add('initial_charge', self.initial_charge)
        _add('resistance', self.resistance)
        _add('smooth_current_tau', self.smooth_current_tau)
        _add('fix_issue_225', self.fix_issue_225)
        _add('invert_current_sign', self.invert_current_sign)
        _add('enable_recharge', self.enable_recharge)
        _add('charging_time', self.charging_time)
        _add('recharge_by_topic', self.recharge_by_topic)
        _add('start_draining', self.start_draining)
        if self.power_draining_topic is not None:
            for v in (self.power_draining_topic if isinstance(self.power_draining_topic, list) else [self.power_draining_topic]):
                _add('power_draining_topic', v)
        if self.stop_power_draining_topic is not None:
            for v in (self.stop_power_draining_topic if isinstance(self.stop_power_draining_topic, list) else [self.stop_power_draining_topic]):
                _add('stop_power_draining_topic', v)
            
        return el

    def to_version(self, target_version: str):
        return self
