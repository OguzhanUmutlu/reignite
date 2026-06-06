from xml.etree import ElementTree as ET

from ...joint import Joint
from ...plugin import Plugin


@Plugin.register("gz-sim-joint-trajectory-controller-system", "gz::sim::systems::JointTrajectoryController")
class JointTrajectoryControllerPlugin(Plugin):
    def __init__(
            self,
            joint_name: str | Joint | list[str | Joint] | None = None,
            use_header_start_time: bool = False,
            topic: str | None = None,
            initial_position: float | list[float] | None = None,
            position_p_gain: float | list[float] | None = None,
            position_i_gain: float | list[float] | None = None,
            position_d_gain: float | list[float] | None = None,
            position_i_min: float | list[float] | None = None,
            position_i_max: float | list[float] | None = None,
            position_cmd_min: float | list[float] | None = None,
            position_cmd_max: float | list[float] | None = None,
            position_cmd_offset: float | list[float] | None = None,
            velocity_p_gain: float | list[float] | None = None,
            velocity_i_gain: float | list[float] | None = None,
            velocity_d_gain: float | list[float] | None = None,
            velocity_i_min: float | list[float] | None = None,
            velocity_i_max: float | list[float] | None = None,
            velocity_cmd_min: float | list[float] | None = None,
            velocity_cmd_max: float | list[float] | None = None,
            velocity_cmd_offset: float | list[float] | None = None
    ):
        def _get_names(joints):
            if joints is None:
                return None
            if isinstance(joints, list):
                return [j.name if isinstance(j, Joint) else j for j in joints]
            return joints.name if isinstance(joints, Joint) else joints

        self.joint_name = _get_names(joint_name)
        self.use_header_start_time = use_header_start_time
        self.topic = topic
        self.initial_position = initial_position
        self.position_p_gain = position_p_gain
        self.position_i_gain = position_i_gain
        self.position_d_gain = position_d_gain
        self.position_i_min = position_i_min
        self.position_i_max = position_i_max
        self.position_cmd_min = position_cmd_min
        self.position_cmd_max = position_cmd_max
        self.position_cmd_offset = position_cmd_offset
        self.velocity_p_gain = velocity_p_gain
        self.velocity_i_gain = velocity_i_gain
        self.velocity_d_gain = velocity_d_gain
        self.velocity_i_min = velocity_i_min
        self.velocity_i_max = velocity_i_max
        self.velocity_cmd_min = velocity_cmd_min
        self.velocity_cmd_max = velocity_cmd_max
        self.velocity_cmd_offset = velocity_cmd_offset
        super().__init__(sdf_version=None, filename="gz-sim-joint-trajectory-controller-system",
                         name="gz::sim::systems::JointTrajectoryController")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        joint_name_els = el.findall('joint_name')
        joint_name_vals = [e.text for e in joint_name_els if e.text is not None] if joint_name_els else None
        use_header_start_time_el = el.find('use_header_start_time')
        topic_el = el.find('topic')
        initial_position_els = el.findall('initial_position')
        initial_position_vals = [e.text for e in initial_position_els if
                                 e.text is not None] if initial_position_els else None
        position_p_gain_els = el.findall('position_p_gain')
        position_p_gain_vals = [e.text for e in position_p_gain_els if
                                e.text is not None] if position_p_gain_els else None
        position_i_gain_els = el.findall('position_i_gain')
        position_i_gain_vals = [e.text for e in position_i_gain_els if
                                e.text is not None] if position_i_gain_els else None
        position_d_gain_els = el.findall('position_d_gain')
        position_d_gain_vals = [e.text for e in position_d_gain_els if
                                e.text is not None] if position_d_gain_els else None
        position_i_min_els = el.findall('position_i_min')
        position_i_min_vals = [e.text for e in position_i_min_els if e.text is not None] if position_i_min_els else None
        position_i_max_els = el.findall('position_i_max')
        position_i_max_vals = [e.text for e in position_i_max_els if e.text is not None] if position_i_max_els else None
        position_cmd_min_els = el.findall('position_cmd_min')
        position_cmd_min_vals = [e.text for e in position_cmd_min_els if
                                 e.text is not None] if position_cmd_min_els else None
        position_cmd_max_els = el.findall('position_cmd_max')
        position_cmd_max_vals = [e.text for e in position_cmd_max_els if
                                 e.text is not None] if position_cmd_max_els else None
        position_cmd_offset_els = el.findall('position_cmd_offset')
        position_cmd_offset_vals = [e.text for e in position_cmd_offset_els if
                                    e.text is not None] if position_cmd_offset_els else None
        velocity_p_gain_els = el.findall('velocity_p_gain')
        velocity_p_gain_vals = [e.text for e in velocity_p_gain_els if
                                e.text is not None] if velocity_p_gain_els else None
        velocity_i_gain_els = el.findall('velocity_i_gain')
        velocity_i_gain_vals = [e.text for e in velocity_i_gain_els if
                                e.text is not None] if velocity_i_gain_els else None
        velocity_d_gain_els = el.findall('velocity_d_gain')
        velocity_d_gain_vals = [e.text for e in velocity_d_gain_els if
                                e.text is not None] if velocity_d_gain_els else None
        velocity_i_min_els = el.findall('velocity_i_min')
        velocity_i_min_vals = [e.text for e in velocity_i_min_els if e.text is not None] if velocity_i_min_els else None
        velocity_i_max_els = el.findall('velocity_i_max')
        velocity_i_max_vals = [e.text for e in velocity_i_max_els if e.text is not None] if velocity_i_max_els else None
        velocity_cmd_min_els = el.findall('velocity_cmd_min')
        velocity_cmd_min_vals = [e.text for e in velocity_cmd_min_els if
                                 e.text is not None] if velocity_cmd_min_els else None
        velocity_cmd_max_els = el.findall('velocity_cmd_max')
        velocity_cmd_max_vals = [e.text for e in velocity_cmd_max_els if
                                 e.text is not None] if velocity_cmd_max_els else None
        velocity_cmd_offset_els = el.findall('velocity_cmd_offset')
        velocity_cmd_offset_vals = [e.text for e in velocity_cmd_offset_els if
                                    e.text is not None] if velocity_cmd_offset_els else None

        return cls(
            joint_name=joint_name_vals,
            use_header_start_time=use_header_start_time_el.text.lower() == 'true' if use_header_start_time_el is not None and use_header_start_time_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            initial_position=initial_position_vals,
            position_p_gain=position_p_gain_vals,
            position_i_gain=position_i_gain_vals,
            position_d_gain=position_d_gain_vals,
            position_i_min=position_i_min_vals,
            position_i_max=position_i_max_vals,
            position_cmd_min=position_cmd_min_vals,
            position_cmd_max=position_cmd_max_vals,
            position_cmd_offset=position_cmd_offset_vals,
            velocity_p_gain=velocity_p_gain_vals,
            velocity_i_gain=velocity_i_gain_vals,
            velocity_d_gain=velocity_d_gain_vals,
            velocity_i_min=velocity_i_min_vals,
            velocity_i_max=velocity_i_max_vals,
            velocity_cmd_min=velocity_cmd_min_vals,
            velocity_cmd_max=velocity_cmd_max_vals,
            velocity_cmd_offset=velocity_cmd_offset_vals,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin",
                        name=self.name if hasattr(self, 'name') else "gz::sim::systems::JointTrajectoryController",
                        filename="gz-sim-joint-trajectory-controller-system")

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
        _add('use_header_start_time', self.use_header_start_time)
        _add('topic', self.topic)
        if self.initial_position is not None:
            for v in (self.initial_position if isinstance(self.initial_position, list) else [self.initial_position]):
                _add('initial_position', v)
        if self.position_p_gain is not None:
            for v in (self.position_p_gain if isinstance(self.position_p_gain, list) else [self.position_p_gain]):
                _add('position_p_gain', v)
        if self.position_i_gain is not None:
            for v in (self.position_i_gain if isinstance(self.position_i_gain, list) else [self.position_i_gain]):
                _add('position_i_gain', v)
        if self.position_d_gain is not None:
            for v in (self.position_d_gain if isinstance(self.position_d_gain, list) else [self.position_d_gain]):
                _add('position_d_gain', v)
        if self.position_i_min is not None:
            for v in (self.position_i_min if isinstance(self.position_i_min, list) else [self.position_i_min]):
                _add('position_i_min', v)
        if self.position_i_max is not None:
            for v in (self.position_i_max if isinstance(self.position_i_max, list) else [self.position_i_max]):
                _add('position_i_max', v)
        if self.position_cmd_min is not None:
            for v in (self.position_cmd_min if isinstance(self.position_cmd_min, list) else [self.position_cmd_min]):
                _add('position_cmd_min', v)
        if self.position_cmd_max is not None:
            for v in (self.position_cmd_max if isinstance(self.position_cmd_max, list) else [self.position_cmd_max]):
                _add('position_cmd_max', v)
        if self.position_cmd_offset is not None:
            for v in (
            self.position_cmd_offset if isinstance(self.position_cmd_offset, list) else [self.position_cmd_offset]):
                _add('position_cmd_offset', v)
        if self.velocity_p_gain is not None:
            for v in (self.velocity_p_gain if isinstance(self.velocity_p_gain, list) else [self.velocity_p_gain]):
                _add('velocity_p_gain', v)
        if self.velocity_i_gain is not None:
            for v in (self.velocity_i_gain if isinstance(self.velocity_i_gain, list) else [self.velocity_i_gain]):
                _add('velocity_i_gain', v)
        if self.velocity_d_gain is not None:
            for v in (self.velocity_d_gain if isinstance(self.velocity_d_gain, list) else [self.velocity_d_gain]):
                _add('velocity_d_gain', v)
        if self.velocity_i_min is not None:
            for v in (self.velocity_i_min if isinstance(self.velocity_i_min, list) else [self.velocity_i_min]):
                _add('velocity_i_min', v)
        if self.velocity_i_max is not None:
            for v in (self.velocity_i_max if isinstance(self.velocity_i_max, list) else [self.velocity_i_max]):
                _add('velocity_i_max', v)
        if self.velocity_cmd_min is not None:
            for v in (self.velocity_cmd_min if isinstance(self.velocity_cmd_min, list) else [self.velocity_cmd_min]):
                _add('velocity_cmd_min', v)
        if self.velocity_cmd_max is not None:
            for v in (self.velocity_cmd_max if isinstance(self.velocity_cmd_max, list) else [self.velocity_cmd_max]):
                _add('velocity_cmd_max', v)
        if self.velocity_cmd_offset is not None:
            for v in (
            self.velocity_cmd_offset if isinstance(self.velocity_cmd_offset, list) else [self.velocity_cmd_offset]):
                _add('velocity_cmd_offset', v)

        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        joint_name_els = el.findall('joint_name')
        joint_name_vals = [e.text for e in joint_name_els if e.text is not None] if joint_name_els else None
        use_header_start_time_el = el.find('use_header_start_time')
        topic_el = el.find('topic')
        initial_position_els = el.findall('initial_position')
        initial_position_vals = [e.text for e in initial_position_els if
                                 e.text is not None] if initial_position_els else None
        position_p_gain_els = el.findall('position_p_gain')
        position_p_gain_vals = [e.text for e in position_p_gain_els if
                                e.text is not None] if position_p_gain_els else None
        position_i_gain_els = el.findall('position_i_gain')
        position_i_gain_vals = [e.text for e in position_i_gain_els if
                                e.text is not None] if position_i_gain_els else None
        position_d_gain_els = el.findall('position_d_gain')
        position_d_gain_vals = [e.text for e in position_d_gain_els if
                                e.text is not None] if position_d_gain_els else None
        position_i_min_els = el.findall('position_i_min')
        position_i_min_vals = [e.text for e in position_i_min_els if e.text is not None] if position_i_min_els else None
        position_i_max_els = el.findall('position_i_max')
        position_i_max_vals = [e.text for e in position_i_max_els if e.text is not None] if position_i_max_els else None
        position_cmd_min_els = el.findall('position_cmd_min')
        position_cmd_min_vals = [e.text for e in position_cmd_min_els if
                                 e.text is not None] if position_cmd_min_els else None
        position_cmd_max_els = el.findall('position_cmd_max')
        position_cmd_max_vals = [e.text for e in position_cmd_max_els if
                                 e.text is not None] if position_cmd_max_els else None
        position_cmd_offset_els = el.findall('position_cmd_offset')
        position_cmd_offset_vals = [e.text for e in position_cmd_offset_els if
                                    e.text is not None] if position_cmd_offset_els else None
        velocity_p_gain_els = el.findall('velocity_p_gain')
        velocity_p_gain_vals = [e.text for e in velocity_p_gain_els if
                                e.text is not None] if velocity_p_gain_els else None
        velocity_i_gain_els = el.findall('velocity_i_gain')
        velocity_i_gain_vals = [e.text for e in velocity_i_gain_els if
                                e.text is not None] if velocity_i_gain_els else None
        velocity_d_gain_els = el.findall('velocity_d_gain')
        velocity_d_gain_vals = [e.text for e in velocity_d_gain_els if
                                e.text is not None] if velocity_d_gain_els else None
        velocity_i_min_els = el.findall('velocity_i_min')
        velocity_i_min_vals = [e.text for e in velocity_i_min_els if e.text is not None] if velocity_i_min_els else None
        velocity_i_max_els = el.findall('velocity_i_max')
        velocity_i_max_vals = [e.text for e in velocity_i_max_els if e.text is not None] if velocity_i_max_els else None
        velocity_cmd_min_els = el.findall('velocity_cmd_min')
        velocity_cmd_min_vals = [e.text for e in velocity_cmd_min_els if
                                 e.text is not None] if velocity_cmd_min_els else None
        velocity_cmd_max_els = el.findall('velocity_cmd_max')
        velocity_cmd_max_vals = [e.text for e in velocity_cmd_max_els if
                                 e.text is not None] if velocity_cmd_max_els else None
        velocity_cmd_offset_els = el.findall('velocity_cmd_offset')
        velocity_cmd_offset_vals = [e.text for e in velocity_cmd_offset_els if
                                    e.text is not None] if velocity_cmd_offset_els else None

        return cls(
            joint_name=joint_name_vals,
            use_header_start_time=use_header_start_time_el.text.lower() == 'true' if use_header_start_time_el is not None and use_header_start_time_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            initial_position=initial_position_vals,
            position_p_gain=position_p_gain_vals,
            position_i_gain=position_i_gain_vals,
            position_d_gain=position_d_gain_vals,
            position_i_min=position_i_min_vals,
            position_i_max=position_i_max_vals,
            position_cmd_min=position_cmd_min_vals,
            position_cmd_max=position_cmd_max_vals,
            position_cmd_offset=position_cmd_offset_vals,
            velocity_p_gain=velocity_p_gain_vals,
            velocity_i_gain=velocity_i_gain_vals,
            velocity_d_gain=velocity_d_gain_vals,
            velocity_i_min=velocity_i_min_vals,
            velocity_i_max=velocity_i_max_vals,
            velocity_cmd_min=velocity_cmd_min_vals,
            velocity_cmd_max=velocity_cmd_max_vals,
            velocity_cmd_offset=velocity_cmd_offset_vals,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin",
                        name=self.name if hasattr(self, 'name') else "gz::sim::systems::JointTrajectoryController",
                        filename="gz-sim-joint-trajectory-controller-system")

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
        _add('use_header_start_time', self.use_header_start_time)
        _add('topic', self.topic)
        if self.initial_position is not None:
            for v in (self.initial_position if isinstance(self.initial_position, list) else [self.initial_position]):
                _add('initial_position', v)
        if self.position_p_gain is not None:
            for v in (self.position_p_gain if isinstance(self.position_p_gain, list) else [self.position_p_gain]):
                _add('position_p_gain', v)
        if self.position_i_gain is not None:
            for v in (self.position_i_gain if isinstance(self.position_i_gain, list) else [self.position_i_gain]):
                _add('position_i_gain', v)
        if self.position_d_gain is not None:
            for v in (self.position_d_gain if isinstance(self.position_d_gain, list) else [self.position_d_gain]):
                _add('position_d_gain', v)
        if self.position_i_min is not None:
            for v in (self.position_i_min if isinstance(self.position_i_min, list) else [self.position_i_min]):
                _add('position_i_min', v)
        if self.position_i_max is not None:
            for v in (self.position_i_max if isinstance(self.position_i_max, list) else [self.position_i_max]):
                _add('position_i_max', v)
        if self.position_cmd_min is not None:
            for v in (self.position_cmd_min if isinstance(self.position_cmd_min, list) else [self.position_cmd_min]):
                _add('position_cmd_min', v)
        if self.position_cmd_max is not None:
            for v in (self.position_cmd_max if isinstance(self.position_cmd_max, list) else [self.position_cmd_max]):
                _add('position_cmd_max', v)
        if self.position_cmd_offset is not None:
            for v in (
            self.position_cmd_offset if isinstance(self.position_cmd_offset, list) else [self.position_cmd_offset]):
                _add('position_cmd_offset', v)
        if self.velocity_p_gain is not None:
            for v in (self.velocity_p_gain if isinstance(self.velocity_p_gain, list) else [self.velocity_p_gain]):
                _add('velocity_p_gain', v)
        if self.velocity_i_gain is not None:
            for v in (self.velocity_i_gain if isinstance(self.velocity_i_gain, list) else [self.velocity_i_gain]):
                _add('velocity_i_gain', v)
        if self.velocity_d_gain is not None:
            for v in (self.velocity_d_gain if isinstance(self.velocity_d_gain, list) else [self.velocity_d_gain]):
                _add('velocity_d_gain', v)
        if self.velocity_i_min is not None:
            for v in (self.velocity_i_min if isinstance(self.velocity_i_min, list) else [self.velocity_i_min]):
                _add('velocity_i_min', v)
        if self.velocity_i_max is not None:
            for v in (self.velocity_i_max if isinstance(self.velocity_i_max, list) else [self.velocity_i_max]):
                _add('velocity_i_max', v)
        if self.velocity_cmd_min is not None:
            for v in (self.velocity_cmd_min if isinstance(self.velocity_cmd_min, list) else [self.velocity_cmd_min]):
                _add('velocity_cmd_min', v)
        if self.velocity_cmd_max is not None:
            for v in (self.velocity_cmd_max if isinstance(self.velocity_cmd_max, list) else [self.velocity_cmd_max]):
                _add('velocity_cmd_max', v)
        if self.velocity_cmd_offset is not None:
            for v in (
            self.velocity_cmd_offset if isinstance(self.velocity_cmd_offset, list) else [self.velocity_cmd_offset]):
                _add('velocity_cmd_offset', v)

        return el

    def to_version(self, target_version: str):
        return self
