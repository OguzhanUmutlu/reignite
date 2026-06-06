from xml.etree import ElementTree as ET

from reignite.elements.plugin import Plugin


@Plugin.register("gz-sim-thruster-system", "gz::sim::systems::Thruster")
class ThrusterPlugin(Plugin):
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
        self.joint_name = joint_name
        self.namespace = namespace
        self.thrust_coefficient = thrust_coefficient
        self.propeller_diameter = propeller_diameter
        self.fluid_density = fluid_density
        self.use_angvel_cmd = use_angvel_cmd
        self.wake_fraction = wake_fraction
        self.alpha_1 = alpha_1
        self.alpha_2 = alpha_2
        self.deadband = deadband
        self.topic = topic
        self.max_thrust_cmd = max_thrust_cmd
        self.min_thrust_cmd = min_thrust_cmd
        self.velocity_control = velocity_control
        self.p_gain = p_gain
        self.i_gain = i_gain
        self.d_gain = d_gain
        self.power_load = power_load
        self.battery_name = battery_name
        super().__init__(sdf_version=None, filename="gz-sim-thruster-system", name="gz::sim::systems::Thruster")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        joint_name_el = el.find('joint_name')
        namespace_el = el.find('namespace')
        thrust_coefficient_el = el.find('thrust_coefficient')
        propeller_diameter_el = el.find('propeller_diameter')
        fluid_density_el = el.find('fluid_density')
        use_angvel_cmd_el = el.find('use_angvel_cmd')
        wake_fraction_el = el.find('wake_fraction')
        alpha_1_el = el.find('alpha_1')
        alpha_2_el = el.find('alpha_2')
        deadband_el = el.find('deadband')
        topic_el = el.find('topic')
        max_thrust_cmd_el = el.find('max_thrust_cmd')
        min_thrust_cmd_el = el.find('min_thrust_cmd')
        velocity_control_el = el.find('velocity_control')
        p_gain_el = el.find('p_gain')
        i_gain_el = el.find('i_gain')
        d_gain_el = el.find('d_gain')
        power_load_el = el.find('power_load')
        battery_name_el = el.find('battery_name')

        return cls(
            joint_name=joint_name_el.text if joint_name_el is not None and joint_name_el.text is not None else None,
            namespace=namespace_el.text if namespace_el is not None and namespace_el.text is not None else None,
            thrust_coefficient=float(
                thrust_coefficient_el.text) if thrust_coefficient_el is not None and thrust_coefficient_el.text is not None else None,
            propeller_diameter=float(
                propeller_diameter_el.text) if propeller_diameter_el is not None and propeller_diameter_el.text is not None else None,
            fluid_density=float(
                fluid_density_el.text) if fluid_density_el is not None and fluid_density_el.text is not None else None,
            use_angvel_cmd=use_angvel_cmd_el.text.lower() == 'true' if use_angvel_cmd_el is not None and use_angvel_cmd_el.text is not None else None,
            wake_fraction=float(
                wake_fraction_el.text) if wake_fraction_el is not None and wake_fraction_el.text is not None else None,
            alpha_1=float(alpha_1_el.text) if alpha_1_el is not None and alpha_1_el.text is not None else None,
            alpha_2=float(alpha_2_el.text) if alpha_2_el is not None and alpha_2_el.text is not None else None,
            deadband=float(deadband_el.text) if deadband_el is not None and deadband_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            max_thrust_cmd=float(
                max_thrust_cmd_el.text) if max_thrust_cmd_el is not None and max_thrust_cmd_el.text is not None else None,
            min_thrust_cmd=float(
                min_thrust_cmd_el.text) if min_thrust_cmd_el is not None and min_thrust_cmd_el.text is not None else None,
            velocity_control=velocity_control_el.text.lower() == 'true' if velocity_control_el is not None and velocity_control_el.text is not None else None,
            p_gain=float(p_gain_el.text) if p_gain_el is not None and p_gain_el.text is not None else None,
            i_gain=float(i_gain_el.text) if i_gain_el is not None and i_gain_el.text is not None else None,
            d_gain=float(d_gain_el.text) if d_gain_el is not None and d_gain_el.text is not None else None,
            power_load=float(
                power_load_el.text) if power_load_el is not None and power_load_el.text is not None else None,
            battery_name=battery_name_el.text if battery_name_el is not None and battery_name_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::Thruster",
                        filename="gz-sim-thruster-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('joint_name', self.joint_name)
        _add('namespace', self.namespace)
        _add('thrust_coefficient', self.thrust_coefficient)
        _add('propeller_diameter', self.propeller_diameter)
        _add('fluid_density', self.fluid_density)
        _add('use_angvel_cmd', self.use_angvel_cmd)
        _add('wake_fraction', self.wake_fraction)
        _add('alpha_1', self.alpha_1)
        _add('alpha_2', self.alpha_2)
        _add('deadband', self.deadband)
        _add('topic', self.topic)
        _add('max_thrust_cmd', self.max_thrust_cmd)
        _add('min_thrust_cmd', self.min_thrust_cmd)
        _add('velocity_control', self.velocity_control)
        _add('p_gain', self.p_gain)
        _add('i_gain', self.i_gain)
        _add('d_gain', self.d_gain)
        _add('power_load', self.power_load)
        _add('battery_name', self.battery_name)

        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        joint_name_el = el.find('joint_name')
        namespace_el = el.find('namespace')
        thrust_coefficient_el = el.find('thrust_coefficient')
        propeller_diameter_el = el.find('propeller_diameter')
        fluid_density_el = el.find('fluid_density')
        use_angvel_cmd_el = el.find('use_angvel_cmd')
        wake_fraction_el = el.find('wake_fraction')
        alpha_1_el = el.find('alpha_1')
        alpha_2_el = el.find('alpha_2')
        deadband_el = el.find('deadband')
        topic_el = el.find('topic')
        max_thrust_cmd_el = el.find('max_thrust_cmd')
        min_thrust_cmd_el = el.find('min_thrust_cmd')
        velocity_control_el = el.find('velocity_control')
        p_gain_el = el.find('p_gain')
        i_gain_el = el.find('i_gain')
        d_gain_el = el.find('d_gain')
        power_load_el = el.find('power_load')
        battery_name_el = el.find('battery_name')

        return cls(
            joint_name=joint_name_el.text if joint_name_el is not None and joint_name_el.text is not None else None,
            namespace=namespace_el.text if namespace_el is not None and namespace_el.text is not None else None,
            thrust_coefficient=float(
                thrust_coefficient_el.text) if thrust_coefficient_el is not None and thrust_coefficient_el.text is not None else None,
            propeller_diameter=float(
                propeller_diameter_el.text) if propeller_diameter_el is not None and propeller_diameter_el.text is not None else None,
            fluid_density=float(
                fluid_density_el.text) if fluid_density_el is not None and fluid_density_el.text is not None else None,
            use_angvel_cmd=use_angvel_cmd_el.text.lower() == 'true' if use_angvel_cmd_el is not None and use_angvel_cmd_el.text is not None else None,
            wake_fraction=float(
                wake_fraction_el.text) if wake_fraction_el is not None and wake_fraction_el.text is not None else None,
            alpha_1=float(alpha_1_el.text) if alpha_1_el is not None and alpha_1_el.text is not None else None,
            alpha_2=float(alpha_2_el.text) if alpha_2_el is not None and alpha_2_el.text is not None else None,
            deadband=float(deadband_el.text) if deadband_el is not None and deadband_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            max_thrust_cmd=float(
                max_thrust_cmd_el.text) if max_thrust_cmd_el is not None and max_thrust_cmd_el.text is not None else None,
            min_thrust_cmd=float(
                min_thrust_cmd_el.text) if min_thrust_cmd_el is not None and min_thrust_cmd_el.text is not None else None,
            velocity_control=velocity_control_el.text.lower() == 'true' if velocity_control_el is not None and velocity_control_el.text is not None else None,
            p_gain=float(p_gain_el.text) if p_gain_el is not None and p_gain_el.text is not None else None,
            i_gain=float(i_gain_el.text) if i_gain_el is not None and i_gain_el.text is not None else None,
            d_gain=float(d_gain_el.text) if d_gain_el is not None and d_gain_el.text is not None else None,
            power_load=float(
                power_load_el.text) if power_load_el is not None and power_load_el.text is not None else None,
            battery_name=battery_name_el.text if battery_name_el is not None and battery_name_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::Thruster",
                        filename="gz-sim-thruster-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('joint_name', self.joint_name)
        _add('namespace', self.namespace)
        _add('thrust_coefficient', self.thrust_coefficient)
        _add('propeller_diameter', self.propeller_diameter)
        _add('fluid_density', self.fluid_density)
        _add('use_angvel_cmd', self.use_angvel_cmd)
        _add('wake_fraction', self.wake_fraction)
        _add('alpha_1', self.alpha_1)
        _add('alpha_2', self.alpha_2)
        _add('deadband', self.deadband)
        _add('topic', self.topic)
        _add('max_thrust_cmd', self.max_thrust_cmd)
        _add('min_thrust_cmd', self.min_thrust_cmd)
        _add('velocity_control', self.velocity_control)
        _add('p_gain', self.p_gain)
        _add('i_gain', self.i_gain)
        _add('d_gain', self.d_gain)
        _add('power_load', self.power_load)
        _add('battery_name', self.battery_name)

        return el

    def to_version(self, target_version: str):
        return self
