from xml.etree import ElementTree as ET
from ...joint import Joint
from ...plugin import Plugin


@Plugin.register("gz-sim-ackermann-steering-system", "gz::sim::systems::AckermannSteering")
class AckermannSteeringPlugin(Plugin):
    def __init__(
            self,
            left_steering_joint: str | Joint | list[str | Joint],
            right_steering_joint: str | Joint | list[str | Joint],
            left_joint: str | Joint | list[str | Joint] | None = None,
            right_joint: str | Joint | list[str | Joint] | None = None,
            steering_only: bool = False,
            use_actuator_msg: bool = False,
            actuator_number: int | None = None,
            wheel_radius: float = 0.2,
            kingpin_width: float = 0.8,
            wheel_separation: float = 1.0,
            wheel_base: float = 1.0,
            steering_limit: float = 0.5,
            steer_p_gain: float = 1.0,
            min_velocity: float | None = None,
            max_velocity: float | None = None,
            min_acceleration: float | None = None,
            max_acceleration: float | None = None,
            min_jerk: float | None = None,
            max_jerk: float | None = None,
            odom_publish_frequency: float = 50.0,
            topic: str | None = None,
            sub_topic: str | None = None,
            odom_topic: str | None = None,
            tf_topic: str | None = None,
            frame_id: str | None = None,
            child_frame_id: str | None = None
    ):
        if use_actuator_msg and actuator_number is None:
            raise ValueError("actuator_number must be specified if use_actuator_msg is True.")

        if not steering_only and (not left_joint or not right_joint):
            raise ValueError("left_joint and right_joint are required unless steering_only is True.")

        def _get_names(joints):
            if joints is None:
                return None
            if isinstance(joints, list):
                return [j.name if isinstance(j, Joint) else j for j in joints]
            return joints.name if isinstance(joints, Joint) else joints

        self.left_steering_joint = _get_names(left_steering_joint)
        self.right_steering_joint = _get_names(right_steering_joint)
        self.left_joint = _get_names(left_joint)
        self.right_joint = _get_names(right_joint)
        self.steering_only = steering_only
        self.use_actuator_msg = use_actuator_msg
        self.actuator_number = actuator_number
        self.wheel_radius = wheel_radius
        self.kingpin_width = kingpin_width
        self.wheel_separation = wheel_separation
        self.wheel_base = wheel_base
        self.steering_limit = steering_limit
        self.steer_p_gain = steer_p_gain
        self.min_velocity = min_velocity
        self.max_velocity = max_velocity
        self.min_acceleration = min_acceleration
        self.max_acceleration = max_acceleration
        self.min_jerk = min_jerk
        self.max_jerk = max_jerk
        self.odom_publish_frequency = odom_publish_frequency
        self.topic = topic
        self.sub_topic = sub_topic
        self.odom_topic = odom_topic
        self.tf_topic = tf_topic
        self.frame_id = frame_id
        self.child_frame_id = child_frame_id
        super().__init__(sdf_version=None, filename="gz-sim-ackermann-steering-system", name="gz::sim::systems::AckermannSteering")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        left_steering_joint_els = el.findall('left_steering_joint')
        left_steering_joint_vals = [e.text for e in left_steering_joint_els if e.text is not None] if left_steering_joint_els else None
        right_steering_joint_els = el.findall('right_steering_joint')
        right_steering_joint_vals = [e.text for e in right_steering_joint_els if e.text is not None] if right_steering_joint_els else None
        left_joint_els = el.findall('left_joint')
        left_joint_vals = [e.text for e in left_joint_els if e.text is not None] if left_joint_els else None
        right_joint_els = el.findall('right_joint')
        right_joint_vals = [e.text for e in right_joint_els if e.text is not None] if right_joint_els else None
        steering_only_el = el.find('steering_only')
        use_actuator_msg_el = el.find('use_actuator_msg')
        actuator_number_el = el.find('actuator_number')
        wheel_radius_el = el.find('wheel_radius')
        kingpin_width_el = el.find('kingpin_width')
        wheel_separation_el = el.find('wheel_separation')
        wheel_base_el = el.find('wheel_base')
        steering_limit_el = el.find('steering_limit')
        steer_p_gain_el = el.find('steer_p_gain')
        min_velocity_el = el.find('min_velocity')
        max_velocity_el = el.find('max_velocity')
        min_acceleration_el = el.find('min_acceleration')
        max_acceleration_el = el.find('max_acceleration')
        min_jerk_el = el.find('min_jerk')
        max_jerk_el = el.find('max_jerk')
        odom_publish_frequency_el = el.find('odom_publish_frequency')
        topic_el = el.find('topic')
        sub_topic_el = el.find('sub_topic')
        odom_topic_el = el.find('odom_topic')
        tf_topic_el = el.find('tf_topic')
        frame_id_el = el.find('frame_id')
        child_frame_id_el = el.find('child_frame_id')

        return cls(
            left_steering_joint=left_steering_joint_vals,
            right_steering_joint=right_steering_joint_vals,
            left_joint=left_joint_vals,
            right_joint=right_joint_vals,
            steering_only=steering_only_el.text.lower() == 'true' if steering_only_el is not None and steering_only_el.text is not None else None,
            use_actuator_msg=use_actuator_msg_el.text.lower() == 'true' if use_actuator_msg_el is not None and use_actuator_msg_el.text is not None else None,
            actuator_number=int(actuator_number_el.text) if actuator_number_el is not None and actuator_number_el.text is not None else None,
            wheel_radius=float(wheel_radius_el.text) if wheel_radius_el is not None and wheel_radius_el.text is not None else None,
            kingpin_width=float(kingpin_width_el.text) if kingpin_width_el is not None and kingpin_width_el.text is not None else None,
            wheel_separation=float(wheel_separation_el.text) if wheel_separation_el is not None and wheel_separation_el.text is not None else None,
            wheel_base=float(wheel_base_el.text) if wheel_base_el is not None and wheel_base_el.text is not None else None,
            steering_limit=float(steering_limit_el.text) if steering_limit_el is not None and steering_limit_el.text is not None else None,
            steer_p_gain=float(steer_p_gain_el.text) if steer_p_gain_el is not None and steer_p_gain_el.text is not None else None,
            min_velocity=float(min_velocity_el.text) if min_velocity_el is not None and min_velocity_el.text is not None else None,
            max_velocity=float(max_velocity_el.text) if max_velocity_el is not None and max_velocity_el.text is not None else None,
            min_acceleration=float(min_acceleration_el.text) if min_acceleration_el is not None and min_acceleration_el.text is not None else None,
            max_acceleration=float(max_acceleration_el.text) if max_acceleration_el is not None and max_acceleration_el.text is not None else None,
            min_jerk=float(min_jerk_el.text) if min_jerk_el is not None and min_jerk_el.text is not None else None,
            max_jerk=float(max_jerk_el.text) if max_jerk_el is not None and max_jerk_el.text is not None else None,
            odom_publish_frequency=float(odom_publish_frequency_el.text) if odom_publish_frequency_el is not None and odom_publish_frequency_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            sub_topic=sub_topic_el.text if sub_topic_el is not None and sub_topic_el.text is not None else None,
            odom_topic=odom_topic_el.text if odom_topic_el is not None and odom_topic_el.text is not None else None,
            tf_topic=tf_topic_el.text if tf_topic_el is not None and tf_topic_el.text is not None else None,
            frame_id=frame_id_el.text if frame_id_el is not None and frame_id_el.text is not None else None,
            child_frame_id=child_frame_id_el.text if child_frame_id_el is not None and child_frame_id_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::AckermannSteering", filename="gz-sim-ackermann-steering-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        if self.left_steering_joint is not None:
            for v in (self.left_steering_joint if isinstance(self.left_steering_joint, list) else [self.left_steering_joint]):
                _add('left_steering_joint', v)
        if self.right_steering_joint is not None:
            for v in (self.right_steering_joint if isinstance(self.right_steering_joint, list) else [self.right_steering_joint]):
                _add('right_steering_joint', v)
        if self.left_joint is not None:
            for v in (self.left_joint if isinstance(self.left_joint, list) else [self.left_joint]):
                _add('left_joint', v)
        if self.right_joint is not None:
            for v in (self.right_joint if isinstance(self.right_joint, list) else [self.right_joint]):
                _add('right_joint', v)
        _add('steering_only', self.steering_only)
        _add('use_actuator_msg', self.use_actuator_msg)
        _add('actuator_number', self.actuator_number)
        _add('wheel_radius', self.wheel_radius)
        _add('kingpin_width', self.kingpin_width)
        _add('wheel_separation', self.wheel_separation)
        _add('wheel_base', self.wheel_base)
        _add('steering_limit', self.steering_limit)
        _add('steer_p_gain', self.steer_p_gain)
        _add('min_velocity', self.min_velocity)
        _add('max_velocity', self.max_velocity)
        _add('min_acceleration', self.min_acceleration)
        _add('max_acceleration', self.max_acceleration)
        _add('min_jerk', self.min_jerk)
        _add('max_jerk', self.max_jerk)
        _add('odom_publish_frequency', self.odom_publish_frequency)
        _add('topic', self.topic)
        _add('sub_topic', self.sub_topic)
        _add('odom_topic', self.odom_topic)
        _add('tf_topic', self.tf_topic)
        _add('frame_id', self.frame_id)
        _add('child_frame_id', self.child_frame_id)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        left_steering_joint_els = el.findall('left_steering_joint')
        left_steering_joint_vals = [e.text for e in left_steering_joint_els if e.text is not None] if left_steering_joint_els else None
        right_steering_joint_els = el.findall('right_steering_joint')
        right_steering_joint_vals = [e.text for e in right_steering_joint_els if e.text is not None] if right_steering_joint_els else None
        left_joint_els = el.findall('left_joint')
        left_joint_vals = [e.text for e in left_joint_els if e.text is not None] if left_joint_els else None
        right_joint_els = el.findall('right_joint')
        right_joint_vals = [e.text for e in right_joint_els if e.text is not None] if right_joint_els else None
        steering_only_el = el.find('steering_only')
        use_actuator_msg_el = el.find('use_actuator_msg')
        actuator_number_el = el.find('actuator_number')
        wheel_radius_el = el.find('wheel_radius')
        kingpin_width_el = el.find('kingpin_width')
        wheel_separation_el = el.find('wheel_separation')
        wheel_base_el = el.find('wheel_base')
        steering_limit_el = el.find('steering_limit')
        steer_p_gain_el = el.find('steer_p_gain')
        min_velocity_el = el.find('min_velocity')
        max_velocity_el = el.find('max_velocity')
        min_acceleration_el = el.find('min_acceleration')
        max_acceleration_el = el.find('max_acceleration')
        min_jerk_el = el.find('min_jerk')
        max_jerk_el = el.find('max_jerk')
        odom_publish_frequency_el = el.find('odom_publish_frequency')
        topic_el = el.find('topic')
        sub_topic_el = el.find('sub_topic')
        odom_topic_el = el.find('odom_topic')
        tf_topic_el = el.find('tf_topic')
        frame_id_el = el.find('frame_id')
        child_frame_id_el = el.find('child_frame_id')

        return cls(
            left_steering_joint=left_steering_joint_vals,
            right_steering_joint=right_steering_joint_vals,
            left_joint=left_joint_vals,
            right_joint=right_joint_vals,
            steering_only=steering_only_el.text.lower() == 'true' if steering_only_el is not None and steering_only_el.text is not None else None,
            use_actuator_msg=use_actuator_msg_el.text.lower() == 'true' if use_actuator_msg_el is not None and use_actuator_msg_el.text is not None else None,
            actuator_number=int(actuator_number_el.text) if actuator_number_el is not None and actuator_number_el.text is not None else None,
            wheel_radius=float(wheel_radius_el.text) if wheel_radius_el is not None and wheel_radius_el.text is not None else None,
            kingpin_width=float(kingpin_width_el.text) if kingpin_width_el is not None and kingpin_width_el.text is not None else None,
            wheel_separation=float(wheel_separation_el.text) if wheel_separation_el is not None and wheel_separation_el.text is not None else None,
            wheel_base=float(wheel_base_el.text) if wheel_base_el is not None and wheel_base_el.text is not None else None,
            steering_limit=float(steering_limit_el.text) if steering_limit_el is not None and steering_limit_el.text is not None else None,
            steer_p_gain=float(steer_p_gain_el.text) if steer_p_gain_el is not None and steer_p_gain_el.text is not None else None,
            min_velocity=float(min_velocity_el.text) if min_velocity_el is not None and min_velocity_el.text is not None else None,
            max_velocity=float(max_velocity_el.text) if max_velocity_el is not None and max_velocity_el.text is not None else None,
            min_acceleration=float(min_acceleration_el.text) if min_acceleration_el is not None and min_acceleration_el.text is not None else None,
            max_acceleration=float(max_acceleration_el.text) if max_acceleration_el is not None and max_acceleration_el.text is not None else None,
            min_jerk=float(min_jerk_el.text) if min_jerk_el is not None and min_jerk_el.text is not None else None,
            max_jerk=float(max_jerk_el.text) if max_jerk_el is not None and max_jerk_el.text is not None else None,
            odom_publish_frequency=float(odom_publish_frequency_el.text) if odom_publish_frequency_el is not None and odom_publish_frequency_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            sub_topic=sub_topic_el.text if sub_topic_el is not None and sub_topic_el.text is not None else None,
            odom_topic=odom_topic_el.text if odom_topic_el is not None and odom_topic_el.text is not None else None,
            tf_topic=tf_topic_el.text if tf_topic_el is not None and tf_topic_el.text is not None else None,
            frame_id=frame_id_el.text if frame_id_el is not None and frame_id_el.text is not None else None,
            child_frame_id=child_frame_id_el.text if child_frame_id_el is not None and child_frame_id_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::AckermannSteering", filename="gz-sim-ackermann-steering-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        if self.left_steering_joint is not None:
            for v in (self.left_steering_joint if isinstance(self.left_steering_joint, list) else [self.left_steering_joint]):
                _add('left_steering_joint', v)
        if self.right_steering_joint is not None:
            for v in (self.right_steering_joint if isinstance(self.right_steering_joint, list) else [self.right_steering_joint]):
                _add('right_steering_joint', v)
        if self.left_joint is not None:
            for v in (self.left_joint if isinstance(self.left_joint, list) else [self.left_joint]):
                _add('left_joint', v)
        if self.right_joint is not None:
            for v in (self.right_joint if isinstance(self.right_joint, list) else [self.right_joint]):
                _add('right_joint', v)
        _add('steering_only', self.steering_only)
        _add('use_actuator_msg', self.use_actuator_msg)
        _add('actuator_number', self.actuator_number)
        _add('wheel_radius', self.wheel_radius)
        _add('kingpin_width', self.kingpin_width)
        _add('wheel_separation', self.wheel_separation)
        _add('wheel_base', self.wheel_base)
        _add('steering_limit', self.steering_limit)
        _add('steer_p_gain', self.steer_p_gain)
        _add('min_velocity', self.min_velocity)
        _add('max_velocity', self.max_velocity)
        _add('min_acceleration', self.min_acceleration)
        _add('max_acceleration', self.max_acceleration)
        _add('min_jerk', self.min_jerk)
        _add('max_jerk', self.max_jerk)
        _add('odom_publish_frequency', self.odom_publish_frequency)
        _add('topic', self.topic)
        _add('sub_topic', self.sub_topic)
        _add('odom_topic', self.odom_topic)
        _add('tf_topic', self.tf_topic)
        _add('frame_id', self.frame_id)
        _add('child_frame_id', self.child_frame_id)
            
        return el

    def to_version(self, target_version: str):
        return self
