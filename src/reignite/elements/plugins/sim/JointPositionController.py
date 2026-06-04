from xml.etree import ElementTree as ET
from ...joint import Joint
from ...plugin import Plugin


@Plugin.register("gz-sim-joint-position-controller-system", "gz::sim::systems::JointPositionController")
class JointPositionControllerPlugin(Plugin):
    def __init__(
            self,
            joint_name: str | Joint | list[str | Joint],
            joint_index: int = 0,
            p_gain: float = 1.0,
            i_gain: float = 0.1,
            d_gain: float = 0.01,
            i_max: float = 1.0,
            i_min: float = -1.0,
            cmd_max: float = 1000.0,
            cmd_min: float = -1000.0,
            cmd_offset: float = 0.0,
            use_velocity_commands: bool = False,
            initial_position: float | None = None,
            use_actuator_msg: bool = False,
            actuator_number: int | None = None,
            sub_topic: str | None = None,
            topic: str | None = None
    ):
        if use_actuator_msg and actuator_number is None:
            raise ValueError("actuator_number must be specified if use_actuator_msg is True.")

        if not joint_name:
            raise ValueError("joint_name is required.")

        def _get_names(joints):
            if joints is None:
                return None
            if isinstance(joints, list):
                return [j.name if isinstance(j, Joint) else j for j in joints]
            return joints.name if isinstance(joints, Joint) else joints

        self.joint_name = _get_names(joint_name)
        self.joint_index = joint_index
        self.p_gain = p_gain
        self.i_gain = i_gain
        self.d_gain = d_gain
        self.i_max = i_max
        self.i_min = i_min
        self.cmd_max = cmd_max
        self.cmd_min = cmd_min
        self.cmd_offset = cmd_offset
        self.use_velocity_commands = use_velocity_commands
        self.initial_position = initial_position
        self.use_actuator_msg = use_actuator_msg
        self.actuator_number = actuator_number
        self.sub_topic = sub_topic
        self.topic = topic
        super().__init__(sdf_version=None, filename="gz-sim-joint-position-controller-system", name="gz::sim::systems::JointPositionController")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        joint_name_els = el.findall('joint_name')
        joint_name_vals = [e.text for e in joint_name_els if e.text is not None] if joint_name_els else None
        joint_index_el = el.find('joint_index')
        p_gain_el = el.find('p_gain')
        i_gain_el = el.find('i_gain')
        d_gain_el = el.find('d_gain')
        i_max_el = el.find('i_max')
        i_min_el = el.find('i_min')
        cmd_max_el = el.find('cmd_max')
        cmd_min_el = el.find('cmd_min')
        cmd_offset_el = el.find('cmd_offset')
        use_velocity_commands_el = el.find('use_velocity_commands')
        initial_position_el = el.find('initial_position')
        use_actuator_msg_el = el.find('use_actuator_msg')
        actuator_number_el = el.find('actuator_number')
        sub_topic_el = el.find('sub_topic')
        topic_el = el.find('topic')

        return cls(
            joint_name=joint_name_vals,
            joint_index=int(joint_index_el.text) if joint_index_el is not None and joint_index_el.text is not None else None,
            p_gain=float(p_gain_el.text) if p_gain_el is not None and p_gain_el.text is not None else None,
            i_gain=float(i_gain_el.text) if i_gain_el is not None and i_gain_el.text is not None else None,
            d_gain=float(d_gain_el.text) if d_gain_el is not None and d_gain_el.text is not None else None,
            i_max=float(i_max_el.text) if i_max_el is not None and i_max_el.text is not None else None,
            i_min=float(i_min_el.text) if i_min_el is not None and i_min_el.text is not None else None,
            cmd_max=float(cmd_max_el.text) if cmd_max_el is not None and cmd_max_el.text is not None else None,
            cmd_min=float(cmd_min_el.text) if cmd_min_el is not None and cmd_min_el.text is not None else None,
            cmd_offset=float(cmd_offset_el.text) if cmd_offset_el is not None and cmd_offset_el.text is not None else None,
            use_velocity_commands=use_velocity_commands_el.text.lower() == 'true' if use_velocity_commands_el is not None and use_velocity_commands_el.text is not None else None,
            initial_position=float(initial_position_el.text) if initial_position_el is not None and initial_position_el.text is not None else None,
            use_actuator_msg=use_actuator_msg_el.text.lower() == 'true' if use_actuator_msg_el is not None and use_actuator_msg_el.text is not None else None,
            actuator_number=int(actuator_number_el.text) if actuator_number_el is not None and actuator_number_el.text is not None else None,
            sub_topic=sub_topic_el.text if sub_topic_el is not None and sub_topic_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::JointPositionController", filename="gz-sim-joint-position-controller-system")
        
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
        _add('joint_index', self.joint_index)
        _add('p_gain', self.p_gain)
        _add('i_gain', self.i_gain)
        _add('d_gain', self.d_gain)
        _add('i_max', self.i_max)
        _add('i_min', self.i_min)
        _add('cmd_max', self.cmd_max)
        _add('cmd_min', self.cmd_min)
        _add('cmd_offset', self.cmd_offset)
        _add('use_velocity_commands', self.use_velocity_commands)
        _add('initial_position', self.initial_position)
        _add('use_actuator_msg', self.use_actuator_msg)
        _add('actuator_number', self.actuator_number)
        _add('sub_topic', self.sub_topic)
        _add('topic', self.topic)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        joint_name_els = el.findall('joint_name')
        joint_name_vals = [e.text for e in joint_name_els if e.text is not None] if joint_name_els else None
        joint_index_el = el.find('joint_index')
        p_gain_el = el.find('p_gain')
        i_gain_el = el.find('i_gain')
        d_gain_el = el.find('d_gain')
        i_max_el = el.find('i_max')
        i_min_el = el.find('i_min')
        cmd_max_el = el.find('cmd_max')
        cmd_min_el = el.find('cmd_min')
        cmd_offset_el = el.find('cmd_offset')
        use_velocity_commands_el = el.find('use_velocity_commands')
        initial_position_el = el.find('initial_position')
        use_actuator_msg_el = el.find('use_actuator_msg')
        actuator_number_el = el.find('actuator_number')
        sub_topic_el = el.find('sub_topic')
        topic_el = el.find('topic')

        return cls(
            joint_name=joint_name_vals,
            joint_index=int(joint_index_el.text) if joint_index_el is not None and joint_index_el.text is not None else None,
            p_gain=float(p_gain_el.text) if p_gain_el is not None and p_gain_el.text is not None else None,
            i_gain=float(i_gain_el.text) if i_gain_el is not None and i_gain_el.text is not None else None,
            d_gain=float(d_gain_el.text) if d_gain_el is not None and d_gain_el.text is not None else None,
            i_max=float(i_max_el.text) if i_max_el is not None and i_max_el.text is not None else None,
            i_min=float(i_min_el.text) if i_min_el is not None and i_min_el.text is not None else None,
            cmd_max=float(cmd_max_el.text) if cmd_max_el is not None and cmd_max_el.text is not None else None,
            cmd_min=float(cmd_min_el.text) if cmd_min_el is not None and cmd_min_el.text is not None else None,
            cmd_offset=float(cmd_offset_el.text) if cmd_offset_el is not None and cmd_offset_el.text is not None else None,
            use_velocity_commands=use_velocity_commands_el.text.lower() == 'true' if use_velocity_commands_el is not None and use_velocity_commands_el.text is not None else None,
            initial_position=float(initial_position_el.text) if initial_position_el is not None and initial_position_el.text is not None else None,
            use_actuator_msg=use_actuator_msg_el.text.lower() == 'true' if use_actuator_msg_el is not None and use_actuator_msg_el.text is not None else None,
            actuator_number=int(actuator_number_el.text) if actuator_number_el is not None and actuator_number_el.text is not None else None,
            sub_topic=sub_topic_el.text if sub_topic_el is not None and sub_topic_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::JointPositionController", filename="gz-sim-joint-position-controller-system")
        
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
        _add('joint_index', self.joint_index)
        _add('p_gain', self.p_gain)
        _add('i_gain', self.i_gain)
        _add('d_gain', self.d_gain)
        _add('i_max', self.i_max)
        _add('i_min', self.i_min)
        _add('cmd_max', self.cmd_max)
        _add('cmd_min', self.cmd_min)
        _add('cmd_offset', self.cmd_offset)
        _add('use_velocity_commands', self.use_velocity_commands)
        _add('initial_position', self.initial_position)
        _add('use_actuator_msg', self.use_actuator_msg)
        _add('actuator_number', self.actuator_number)
        _add('sub_topic', self.sub_topic)
        _add('topic', self.topic)
            
        return el

    def to_version(self, target_version: str):
        return self
