from xml.etree import ElementTree as ET
from ...joint import Joint
from ...plugin import Plugin


@Plugin.register("gz-sim-joint-controller-system", "gz::sim::systems::JointController")
class JointControllerPlugin(Plugin):
    def __init__(
            self,
            joint_name: str | Joint | list[str | Joint],
            initial_velocity: float | None = None,
            use_force_commands: bool = False,
            p_gain: float = 1.0,
            i_gain: float = 0.0,
            d_gain: float = 0.0,
            i_max: float = 1.0,
            i_min: float = -1.0,
            cmd_max: float = 1000.0,
            cmd_min: float = -1000.0,
            cmd_offset: float = 0.0,
            disable_braking: bool = False,
            use_actuator_msg: bool = False,
            actuator_number: int | None = None,
            topic: str | None = None,
            sub_topic: str | None = None
    ):
        if not joint_name:
            raise ValueError("joint_name is required.")

        if use_actuator_msg and actuator_number is None:
            raise ValueError("actuator_number must be specified if use_actuator_msg is True.")

        def _get_names(joints):
            if joints is None:
                return None
            if isinstance(joints, list):
                return [j.name if isinstance(j, Joint) else j for j in joints]
            return joints.name if isinstance(joints, Joint) else joints

        self.joint_name = _get_names(joint_name)
        self.initial_velocity = initial_velocity
        self.use_force_commands = use_force_commands
        self.p_gain = p_gain
        self.i_gain = i_gain
        self.d_gain = d_gain
        self.i_max = i_max
        self.i_min = i_min
        self.cmd_max = cmd_max
        self.cmd_min = cmd_min
        self.cmd_offset = cmd_offset
        self.disable_braking = disable_braking
        self.use_actuator_msg = use_actuator_msg
        self.actuator_number = actuator_number
        self.topic = topic
        self.sub_topic = sub_topic
        super().__init__(sdf_version=None, filename="gz-sim-joint-controller-system", name="gz::sim::systems::JointController")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        joint_name_els = el.findall('joint_name')
        joint_name_vals = [e.text for e in joint_name_els if e.text is not None] if joint_name_els else None
        initial_velocity_el = el.find('initial_velocity')
        use_force_commands_el = el.find('use_force_commands')
        p_gain_el = el.find('p_gain')
        i_gain_el = el.find('i_gain')
        d_gain_el = el.find('d_gain')
        i_max_el = el.find('i_max')
        i_min_el = el.find('i_min')
        cmd_max_el = el.find('cmd_max')
        cmd_min_el = el.find('cmd_min')
        cmd_offset_el = el.find('cmd_offset')
        disable_braking_el = el.find('disable_braking')
        use_actuator_msg_el = el.find('use_actuator_msg')
        actuator_number_el = el.find('actuator_number')
        topic_el = el.find('topic')
        sub_topic_el = el.find('sub_topic')

        return cls(
            joint_name=joint_name_vals,
            initial_velocity=float(initial_velocity_el.text) if initial_velocity_el is not None and initial_velocity_el.text is not None else None,
            use_force_commands=use_force_commands_el.text.lower() == 'true' if use_force_commands_el is not None and use_force_commands_el.text is not None else None,
            p_gain=float(p_gain_el.text) if p_gain_el is not None and p_gain_el.text is not None else None,
            i_gain=float(i_gain_el.text) if i_gain_el is not None and i_gain_el.text is not None else None,
            d_gain=float(d_gain_el.text) if d_gain_el is not None and d_gain_el.text is not None else None,
            i_max=float(i_max_el.text) if i_max_el is not None and i_max_el.text is not None else None,
            i_min=float(i_min_el.text) if i_min_el is not None and i_min_el.text is not None else None,
            cmd_max=float(cmd_max_el.text) if cmd_max_el is not None and cmd_max_el.text is not None else None,
            cmd_min=float(cmd_min_el.text) if cmd_min_el is not None and cmd_min_el.text is not None else None,
            cmd_offset=float(cmd_offset_el.text) if cmd_offset_el is not None and cmd_offset_el.text is not None else None,
            disable_braking=disable_braking_el.text.lower() == 'true' if disable_braking_el is not None and disable_braking_el.text is not None else None,
            use_actuator_msg=use_actuator_msg_el.text.lower() == 'true' if use_actuator_msg_el is not None and use_actuator_msg_el.text is not None else None,
            actuator_number=int(actuator_number_el.text) if actuator_number_el is not None and actuator_number_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            sub_topic=sub_topic_el.text if sub_topic_el is not None and sub_topic_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::JointController", filename="gz-sim-joint-controller-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        if self.joint_name is not None:
            for v in (self.joint_name if isinstance(self.joint_name, list) else [self.joint_name]):
                _add('joint_name', v)
        _add('initial_velocity', self.initial_velocity)
        _add('use_force_commands', self.use_force_commands)
        _add('p_gain', self.p_gain)
        _add('i_gain', self.i_gain)
        _add('d_gain', self.d_gain)
        _add('i_max', self.i_max)
        _add('i_min', self.i_min)
        _add('cmd_max', self.cmd_max)
        _add('cmd_min', self.cmd_min)
        _add('cmd_offset', self.cmd_offset)
        _add('disable_braking', self.disable_braking)
        _add('use_actuator_msg', self.use_actuator_msg)
        _add('actuator_number', self.actuator_number)
        _add('topic', self.topic)
        _add('sub_topic', self.sub_topic)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        joint_name_els = el.findall('joint_name')
        joint_name_vals = [e.text for e in joint_name_els if e.text is not None] if joint_name_els else None
        initial_velocity_el = el.find('initial_velocity')
        use_force_commands_el = el.find('use_force_commands')
        p_gain_el = el.find('p_gain')
        i_gain_el = el.find('i_gain')
        d_gain_el = el.find('d_gain')
        i_max_el = el.find('i_max')
        i_min_el = el.find('i_min')
        cmd_max_el = el.find('cmd_max')
        cmd_min_el = el.find('cmd_min')
        cmd_offset_el = el.find('cmd_offset')
        disable_braking_el = el.find('disable_braking')
        use_actuator_msg_el = el.find('use_actuator_msg')
        actuator_number_el = el.find('actuator_number')
        topic_el = el.find('topic')
        sub_topic_el = el.find('sub_topic')

        return cls(
            joint_name=joint_name_vals,
            initial_velocity=float(initial_velocity_el.text) if initial_velocity_el is not None and initial_velocity_el.text is not None else None,
            use_force_commands=use_force_commands_el.text.lower() == 'true' if use_force_commands_el is not None and use_force_commands_el.text is not None else None,
            p_gain=float(p_gain_el.text) if p_gain_el is not None and p_gain_el.text is not None else None,
            i_gain=float(i_gain_el.text) if i_gain_el is not None and i_gain_el.text is not None else None,
            d_gain=float(d_gain_el.text) if d_gain_el is not None and d_gain_el.text is not None else None,
            i_max=float(i_max_el.text) if i_max_el is not None and i_max_el.text is not None else None,
            i_min=float(i_min_el.text) if i_min_el is not None and i_min_el.text is not None else None,
            cmd_max=float(cmd_max_el.text) if cmd_max_el is not None and cmd_max_el.text is not None else None,
            cmd_min=float(cmd_min_el.text) if cmd_min_el is not None and cmd_min_el.text is not None else None,
            cmd_offset=float(cmd_offset_el.text) if cmd_offset_el is not None and cmd_offset_el.text is not None else None,
            disable_braking=disable_braking_el.text.lower() == 'true' if disable_braking_el is not None and disable_braking_el.text is not None else None,
            use_actuator_msg=use_actuator_msg_el.text.lower() == 'true' if use_actuator_msg_el is not None and use_actuator_msg_el.text is not None else None,
            actuator_number=int(actuator_number_el.text) if actuator_number_el is not None and actuator_number_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            sub_topic=sub_topic_el.text if sub_topic_el is not None and sub_topic_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::JointController", filename="gz-sim-joint-controller-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        if self.joint_name is not None:
            for v in (self.joint_name if isinstance(self.joint_name, list) else [self.joint_name]):
                _add('joint_name', v)
        _add('initial_velocity', self.initial_velocity)
        _add('use_force_commands', self.use_force_commands)
        _add('p_gain', self.p_gain)
        _add('i_gain', self.i_gain)
        _add('d_gain', self.d_gain)
        _add('i_max', self.i_max)
        _add('i_min', self.i_min)
        _add('cmd_max', self.cmd_max)
        _add('cmd_min', self.cmd_min)
        _add('cmd_offset', self.cmd_offset)
        _add('disable_braking', self.disable_braking)
        _add('use_actuator_msg', self.use_actuator_msg)
        _add('actuator_number', self.actuator_number)
        _add('topic', self.topic)
        _add('sub_topic', self.sub_topic)
            
        return el

    def to_version(self, target_version: str):
        return self
