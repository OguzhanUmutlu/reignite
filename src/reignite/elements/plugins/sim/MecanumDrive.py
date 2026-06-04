from xml.etree import ElementTree as ET
from ...plugin import Plugin


@Plugin.register("gz-sim-mecanum-drive-system", "gz::sim::systems::MecanumDrive")
class MecanumDrivePlugin(Plugin):
    def __init__(
            self,
            front_left_joint: list[str] | str | None = None,
            front_right_joint: list[str] | str | None = None,
            back_left_joint: list[str] | str | None = None,
            back_right_joint: list[str] | str | None = None,
            wheel_separation: float | None = None,
            wheelbase: float | None = None,
            wheel_radius: float | None = None,
            min_velocity: float | None = None,
            max_velocity: float | None = None,
            min_acceleration: float | None = None,
            max_acceleration: float | None = None,
            min_jerk: float | None = None,
            max_jerk: float | None = None,
            odom_publish_frequency: float | None = None,
            topic: str | None = None,
            odom_topic: str | None = None,
            tf_topic: str | None = None,
            frame_id: str | None = None,
            child_frame_id: str | None = None,
    ):
        self.front_left_joint = front_left_joint
        self.front_right_joint = front_right_joint
        self.back_left_joint = back_left_joint
        self.back_right_joint = back_right_joint
        self.wheel_separation = wheel_separation
        self.wheelbase = wheelbase
        self.wheel_radius = wheel_radius
        self.min_velocity = min_velocity
        self.max_velocity = max_velocity
        self.min_acceleration = min_acceleration
        self.max_acceleration = max_acceleration
        self.min_jerk = min_jerk
        self.max_jerk = max_jerk
        self.odom_publish_frequency = odom_publish_frequency
        self.topic = topic
        self.odom_topic = odom_topic
        self.tf_topic = tf_topic
        self.frame_id = frame_id
        self.child_frame_id = child_frame_id
        super().__init__(sdf_version=None, filename="gz-sim-mecanum-drive-system", name="gz::sim::systems::MecanumDrive")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        front_left_joint_els = el.findall('front_left_joint')
        front_left_joint_vals = [e.text for e in front_left_joint_els if e.text is not None] if front_left_joint_els else None
        front_right_joint_els = el.findall('front_right_joint')
        front_right_joint_vals = [e.text for e in front_right_joint_els if e.text is not None] if front_right_joint_els else None
        back_left_joint_els = el.findall('back_left_joint')
        back_left_joint_vals = [e.text for e in back_left_joint_els if e.text is not None] if back_left_joint_els else None
        back_right_joint_els = el.findall('back_right_joint')
        back_right_joint_vals = [e.text for e in back_right_joint_els if e.text is not None] if back_right_joint_els else None
        wheel_separation_el = el.find('wheel_separation')
        wheelbase_el = el.find('wheelbase')
        wheel_radius_el = el.find('wheel_radius')
        min_velocity_el = el.find('min_velocity')
        max_velocity_el = el.find('max_velocity')
        min_acceleration_el = el.find('min_acceleration')
        max_acceleration_el = el.find('max_acceleration')
        min_jerk_el = el.find('min_jerk')
        max_jerk_el = el.find('max_jerk')
        odom_publish_frequency_el = el.find('odom_publish_frequency')
        topic_el = el.find('topic')
        odom_topic_el = el.find('odom_topic')
        tf_topic_el = el.find('tf_topic')
        frame_id_el = el.find('frame_id')
        child_frame_id_el = el.find('child_frame_id')

        return cls(
            front_left_joint=front_left_joint_vals,
            front_right_joint=front_right_joint_vals,
            back_left_joint=back_left_joint_vals,
            back_right_joint=back_right_joint_vals,
            wheel_separation=float(wheel_separation_el.text) if wheel_separation_el is not None and wheel_separation_el.text is not None else None,
            wheelbase=float(wheelbase_el.text) if wheelbase_el is not None and wheelbase_el.text is not None else None,
            wheel_radius=float(wheel_radius_el.text) if wheel_radius_el is not None and wheel_radius_el.text is not None else None,
            min_velocity=float(min_velocity_el.text) if min_velocity_el is not None and min_velocity_el.text is not None else None,
            max_velocity=float(max_velocity_el.text) if max_velocity_el is not None and max_velocity_el.text is not None else None,
            min_acceleration=float(min_acceleration_el.text) if min_acceleration_el is not None and min_acceleration_el.text is not None else None,
            max_acceleration=float(max_acceleration_el.text) if max_acceleration_el is not None and max_acceleration_el.text is not None else None,
            min_jerk=float(min_jerk_el.text) if min_jerk_el is not None and min_jerk_el.text is not None else None,
            max_jerk=float(max_jerk_el.text) if max_jerk_el is not None and max_jerk_el.text is not None else None,
            odom_publish_frequency=float(odom_publish_frequency_el.text) if odom_publish_frequency_el is not None and odom_publish_frequency_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            odom_topic=odom_topic_el.text if odom_topic_el is not None and odom_topic_el.text is not None else None,
            tf_topic=tf_topic_el.text if tf_topic_el is not None and tf_topic_el.text is not None else None,
            frame_id=frame_id_el.text if frame_id_el is not None and frame_id_el.text is not None else None,
            child_frame_id=child_frame_id_el.text if child_frame_id_el is not None and child_frame_id_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::MecanumDrive", filename="gz-sim-mecanum-drive-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        if self.front_left_joint is not None:
            for v in (self.front_left_joint if isinstance(self.front_left_joint, list) else [self.front_left_joint]):
                _add('front_left_joint', v)
        if self.front_right_joint is not None:
            for v in (self.front_right_joint if isinstance(self.front_right_joint, list) else [self.front_right_joint]):
                _add('front_right_joint', v)
        if self.back_left_joint is not None:
            for v in (self.back_left_joint if isinstance(self.back_left_joint, list) else [self.back_left_joint]):
                _add('back_left_joint', v)
        if self.back_right_joint is not None:
            for v in (self.back_right_joint if isinstance(self.back_right_joint, list) else [self.back_right_joint]):
                _add('back_right_joint', v)
        _add('wheel_separation', self.wheel_separation)
        _add('wheelbase', self.wheelbase)
        _add('wheel_radius', self.wheel_radius)
        _add('min_velocity', self.min_velocity)
        _add('max_velocity', self.max_velocity)
        _add('min_acceleration', self.min_acceleration)
        _add('max_acceleration', self.max_acceleration)
        _add('min_jerk', self.min_jerk)
        _add('max_jerk', self.max_jerk)
        _add('odom_publish_frequency', self.odom_publish_frequency)
        _add('topic', self.topic)
        _add('odom_topic', self.odom_topic)
        _add('tf_topic', self.tf_topic)
        _add('frame_id', self.frame_id)
        _add('child_frame_id', self.child_frame_id)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        front_left_joint_els = el.findall('front_left_joint')
        front_left_joint_vals = [e.text for e in front_left_joint_els if e.text is not None] if front_left_joint_els else None
        front_right_joint_els = el.findall('front_right_joint')
        front_right_joint_vals = [e.text for e in front_right_joint_els if e.text is not None] if front_right_joint_els else None
        back_left_joint_els = el.findall('back_left_joint')
        back_left_joint_vals = [e.text for e in back_left_joint_els if e.text is not None] if back_left_joint_els else None
        back_right_joint_els = el.findall('back_right_joint')
        back_right_joint_vals = [e.text for e in back_right_joint_els if e.text is not None] if back_right_joint_els else None
        wheel_separation_el = el.find('wheel_separation')
        wheelbase_el = el.find('wheelbase')
        wheel_radius_el = el.find('wheel_radius')
        min_velocity_el = el.find('min_velocity')
        max_velocity_el = el.find('max_velocity')
        min_acceleration_el = el.find('min_acceleration')
        max_acceleration_el = el.find('max_acceleration')
        min_jerk_el = el.find('min_jerk')
        max_jerk_el = el.find('max_jerk')
        odom_publish_frequency_el = el.find('odom_publish_frequency')
        topic_el = el.find('topic')
        odom_topic_el = el.find('odom_topic')
        tf_topic_el = el.find('tf_topic')
        frame_id_el = el.find('frame_id')
        child_frame_id_el = el.find('child_frame_id')

        return cls(
            front_left_joint=front_left_joint_vals,
            front_right_joint=front_right_joint_vals,
            back_left_joint=back_left_joint_vals,
            back_right_joint=back_right_joint_vals,
            wheel_separation=float(wheel_separation_el.text) if wheel_separation_el is not None and wheel_separation_el.text is not None else None,
            wheelbase=float(wheelbase_el.text) if wheelbase_el is not None and wheelbase_el.text is not None else None,
            wheel_radius=float(wheel_radius_el.text) if wheel_radius_el is not None and wheel_radius_el.text is not None else None,
            min_velocity=float(min_velocity_el.text) if min_velocity_el is not None and min_velocity_el.text is not None else None,
            max_velocity=float(max_velocity_el.text) if max_velocity_el is not None and max_velocity_el.text is not None else None,
            min_acceleration=float(min_acceleration_el.text) if min_acceleration_el is not None and min_acceleration_el.text is not None else None,
            max_acceleration=float(max_acceleration_el.text) if max_acceleration_el is not None and max_acceleration_el.text is not None else None,
            min_jerk=float(min_jerk_el.text) if min_jerk_el is not None and min_jerk_el.text is not None else None,
            max_jerk=float(max_jerk_el.text) if max_jerk_el is not None and max_jerk_el.text is not None else None,
            odom_publish_frequency=float(odom_publish_frequency_el.text) if odom_publish_frequency_el is not None and odom_publish_frequency_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            odom_topic=odom_topic_el.text if odom_topic_el is not None and odom_topic_el.text is not None else None,
            tf_topic=tf_topic_el.text if tf_topic_el is not None and tf_topic_el.text is not None else None,
            frame_id=frame_id_el.text if frame_id_el is not None and frame_id_el.text is not None else None,
            child_frame_id=child_frame_id_el.text if child_frame_id_el is not None and child_frame_id_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::MecanumDrive", filename="gz-sim-mecanum-drive-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        if self.front_left_joint is not None:
            for v in (self.front_left_joint if isinstance(self.front_left_joint, list) else [self.front_left_joint]):
                _add('front_left_joint', v)
        if self.front_right_joint is not None:
            for v in (self.front_right_joint if isinstance(self.front_right_joint, list) else [self.front_right_joint]):
                _add('front_right_joint', v)
        if self.back_left_joint is not None:
            for v in (self.back_left_joint if isinstance(self.back_left_joint, list) else [self.back_left_joint]):
                _add('back_left_joint', v)
        if self.back_right_joint is not None:
            for v in (self.back_right_joint if isinstance(self.back_right_joint, list) else [self.back_right_joint]):
                _add('back_right_joint', v)
        _add('wheel_separation', self.wheel_separation)
        _add('wheelbase', self.wheelbase)
        _add('wheel_radius', self.wheel_radius)
        _add('min_velocity', self.min_velocity)
        _add('max_velocity', self.max_velocity)
        _add('min_acceleration', self.min_acceleration)
        _add('max_acceleration', self.max_acceleration)
        _add('min_jerk', self.min_jerk)
        _add('max_jerk', self.max_jerk)
        _add('odom_publish_frequency', self.odom_publish_frequency)
        _add('topic', self.topic)
        _add('odom_topic', self.odom_topic)
        _add('tf_topic', self.tf_topic)
        _add('frame_id', self.frame_id)
        _add('child_frame_id', self.child_frame_id)
            
        return el

    def to_version(self, target_version: str):
        return self
