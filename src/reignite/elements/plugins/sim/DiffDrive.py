from xml.etree import ElementTree as ET

from ...joint import Joint
from ...plugin import Plugin


@Plugin.register("gz-sim-diff-drive-system", "gz::sim::systems::DiffDrive")
class DiffDrivePlugin(Plugin):
    def __init__(
            self,
            left_joint: str | Joint | list[str | Joint],
            right_joint: str | Joint | list[str | Joint],
            wheel_separation: float = 1.0,
            wheel_radius: float = 0.2,
            min_velocity: float | None = None,
            min_linear_velocity: float | None = None,
            min_angular_velocity: float | None = None,
            max_velocity: float | None = None,
            max_linear_velocity: float | None = None,
            max_angular_velocity: float | None = None,
            min_acceleration: float | None = None,
            min_linear_acceleration: float | None = None,
            min_angular_acceleration: float | None = None,
            max_acceleration: float | None = None,
            max_linear_acceleration: float | None = None,
            max_angular_acceleration: float | None = None,
            min_jerk: float | None = None,
            min_linear_jerk: float | None = None,
            min_angular_jerk: float | None = None,
            max_jerk: float | None = None,
            max_linear_jerk: float | None = None,
            max_angular_jerk: float | None = None,
            odom_publish_frequency: float = 50.0,
            topic: str | None = None,
            odom_topic: str | None = None,
            tf_topic: str | None = None,
            frame_id: str | None = None,
            child_frame_id: str | None = None
    ):
        if not left_joint or not right_joint:
            raise ValueError("left_joint and right_joint are required.")

        def _get_names(joints):
            if joints is None:
                return None
            if isinstance(joints, list):
                return [j.name if isinstance(j, Joint) else j for j in joints]
            return joints.name if isinstance(joints, Joint) else joints

        self.left_joint = _get_names(left_joint)
        self.right_joint = _get_names(right_joint)
        self.wheel_separation = wheel_separation
        self.wheel_radius = wheel_radius
        self.min_velocity = min_velocity
        self.min_linear_velocity = min_linear_velocity
        self.min_angular_velocity = min_angular_velocity
        self.max_velocity = max_velocity
        self.max_linear_velocity = max_linear_velocity
        self.max_angular_velocity = max_angular_velocity
        self.min_acceleration = min_acceleration
        self.min_linear_acceleration = min_linear_acceleration
        self.min_angular_acceleration = min_angular_acceleration
        self.max_acceleration = max_acceleration
        self.max_linear_acceleration = max_linear_acceleration
        self.max_angular_acceleration = max_angular_acceleration
        self.min_jerk = min_jerk
        self.min_linear_jerk = min_linear_jerk
        self.min_angular_jerk = min_angular_jerk
        self.max_jerk = max_jerk
        self.max_linear_jerk = max_linear_jerk
        self.max_angular_jerk = max_angular_jerk
        self.odom_publish_frequency = odom_publish_frequency
        self.topic = topic
        self.odom_topic = odom_topic
        self.tf_topic = tf_topic
        self.frame_id = frame_id
        self.child_frame_id = child_frame_id
        super().__init__(sdf_version=None, filename="gz-sim-diff-drive-system", name="gz::sim::systems::DiffDrive")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        left_joint_els = el.findall('left_joint')
        left_joint_vals = [e.text for e in left_joint_els if e.text is not None] if left_joint_els else None
        right_joint_els = el.findall('right_joint')
        right_joint_vals = [e.text for e in right_joint_els if e.text is not None] if right_joint_els else None
        wheel_separation_el = el.find('wheel_separation')
        wheel_radius_el = el.find('wheel_radius')
        min_velocity_el = el.find('min_velocity')
        min_linear_velocity_el = el.find('min_linear_velocity')
        min_angular_velocity_el = el.find('min_angular_velocity')
        max_velocity_el = el.find('max_velocity')
        max_linear_velocity_el = el.find('max_linear_velocity')
        max_angular_velocity_el = el.find('max_angular_velocity')
        min_acceleration_el = el.find('min_acceleration')
        min_linear_acceleration_el = el.find('min_linear_acceleration')
        min_angular_acceleration_el = el.find('min_angular_acceleration')
        max_acceleration_el = el.find('max_acceleration')
        max_linear_acceleration_el = el.find('max_linear_acceleration')
        max_angular_acceleration_el = el.find('max_angular_acceleration')
        min_jerk_el = el.find('min_jerk')
        min_linear_jerk_el = el.find('min_linear_jerk')
        min_angular_jerk_el = el.find('min_angular_jerk')
        max_jerk_el = el.find('max_jerk')
        max_linear_jerk_el = el.find('max_linear_jerk')
        max_angular_jerk_el = el.find('max_angular_jerk')
        odom_publish_frequency_el = el.find('odom_publish_frequency')
        topic_el = el.find('topic')
        odom_topic_el = el.find('odom_topic')
        tf_topic_el = el.find('tf_topic')
        frame_id_el = el.find('frame_id')
        child_frame_id_el = el.find('child_frame_id')

        return cls(
            left_joint=left_joint_vals,
            right_joint=right_joint_vals,
            wheel_separation=float(
                wheel_separation_el.text) if wheel_separation_el is not None and wheel_separation_el.text is not None else None,
            wheel_radius=float(
                wheel_radius_el.text) if wheel_radius_el is not None and wheel_radius_el.text is not None else None,
            min_velocity=float(
                min_velocity_el.text) if min_velocity_el is not None and min_velocity_el.text is not None else None,
            min_linear_velocity=float(
                min_linear_velocity_el.text) if min_linear_velocity_el is not None and min_linear_velocity_el.text is not None else None,
            min_angular_velocity=float(
                min_angular_velocity_el.text) if min_angular_velocity_el is not None and min_angular_velocity_el.text is not None else None,
            max_velocity=float(
                max_velocity_el.text) if max_velocity_el is not None and max_velocity_el.text is not None else None,
            max_linear_velocity=float(
                max_linear_velocity_el.text) if max_linear_velocity_el is not None and max_linear_velocity_el.text is not None else None,
            max_angular_velocity=float(
                max_angular_velocity_el.text) if max_angular_velocity_el is not None and max_angular_velocity_el.text is not None else None,
            min_acceleration=float(
                min_acceleration_el.text) if min_acceleration_el is not None and min_acceleration_el.text is not None else None,
            min_linear_acceleration=float(
                min_linear_acceleration_el.text) if min_linear_acceleration_el is not None and min_linear_acceleration_el.text is not None else None,
            min_angular_acceleration=float(
                min_angular_acceleration_el.text) if min_angular_acceleration_el is not None and min_angular_acceleration_el.text is not None else None,
            max_acceleration=float(
                max_acceleration_el.text) if max_acceleration_el is not None and max_acceleration_el.text is not None else None,
            max_linear_acceleration=float(
                max_linear_acceleration_el.text) if max_linear_acceleration_el is not None and max_linear_acceleration_el.text is not None else None,
            max_angular_acceleration=float(
                max_angular_acceleration_el.text) if max_angular_acceleration_el is not None and max_angular_acceleration_el.text is not None else None,
            min_jerk=float(min_jerk_el.text) if min_jerk_el is not None and min_jerk_el.text is not None else None,
            min_linear_jerk=float(
                min_linear_jerk_el.text) if min_linear_jerk_el is not None and min_linear_jerk_el.text is not None else None,
            min_angular_jerk=float(
                min_angular_jerk_el.text) if min_angular_jerk_el is not None and min_angular_jerk_el.text is not None else None,
            max_jerk=float(max_jerk_el.text) if max_jerk_el is not None and max_jerk_el.text is not None else None,
            max_linear_jerk=float(
                max_linear_jerk_el.text) if max_linear_jerk_el is not None and max_linear_jerk_el.text is not None else None,
            max_angular_jerk=float(
                max_angular_jerk_el.text) if max_angular_jerk_el is not None and max_angular_jerk_el.text is not None else None,
            odom_publish_frequency=float(
                odom_publish_frequency_el.text) if odom_publish_frequency_el is not None and odom_publish_frequency_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            odom_topic=odom_topic_el.text if odom_topic_el is not None and odom_topic_el.text is not None else None,
            tf_topic=tf_topic_el.text if tf_topic_el is not None and tf_topic_el.text is not None else None,
            frame_id=frame_id_el.text if frame_id_el is not None and frame_id_el.text is not None else None,
            child_frame_id=child_frame_id_el.text if child_frame_id_el is not None and child_frame_id_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::DiffDrive",
                        filename="gz-sim-diff-drive-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        if self.left_joint is not None:
            for v in (self.left_joint if isinstance(self.left_joint, list) else [self.left_joint]):
                _add('left_joint', v)
        if self.right_joint is not None:
            for v in (self.right_joint if isinstance(self.right_joint, list) else [self.right_joint]):
                _add('right_joint', v)
        _add('wheel_separation', self.wheel_separation)
        _add('wheel_radius', self.wheel_radius)
        _add('min_velocity', self.min_velocity)
        _add('min_linear_velocity', self.min_linear_velocity)
        _add('min_angular_velocity', self.min_angular_velocity)
        _add('max_velocity', self.max_velocity)
        _add('max_linear_velocity', self.max_linear_velocity)
        _add('max_angular_velocity', self.max_angular_velocity)
        _add('min_acceleration', self.min_acceleration)
        _add('min_linear_acceleration', self.min_linear_acceleration)
        _add('min_angular_acceleration', self.min_angular_acceleration)
        _add('max_acceleration', self.max_acceleration)
        _add('max_linear_acceleration', self.max_linear_acceleration)
        _add('max_angular_acceleration', self.max_angular_acceleration)
        _add('min_jerk', self.min_jerk)
        _add('min_linear_jerk', self.min_linear_jerk)
        _add('min_angular_jerk', self.min_angular_jerk)
        _add('max_jerk', self.max_jerk)
        _add('max_linear_jerk', self.max_linear_jerk)
        _add('max_angular_jerk', self.max_angular_jerk)
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
        left_joint_els = el.findall('left_joint')
        left_joint_vals = [e.text for e in left_joint_els if e.text is not None] if left_joint_els else None
        right_joint_els = el.findall('right_joint')
        right_joint_vals = [e.text for e in right_joint_els if e.text is not None] if right_joint_els else None
        wheel_separation_el = el.find('wheel_separation')
        wheel_radius_el = el.find('wheel_radius')
        min_velocity_el = el.find('min_velocity')
        min_linear_velocity_el = el.find('min_linear_velocity')
        min_angular_velocity_el = el.find('min_angular_velocity')
        max_velocity_el = el.find('max_velocity')
        max_linear_velocity_el = el.find('max_linear_velocity')
        max_angular_velocity_el = el.find('max_angular_velocity')
        min_acceleration_el = el.find('min_acceleration')
        min_linear_acceleration_el = el.find('min_linear_acceleration')
        min_angular_acceleration_el = el.find('min_angular_acceleration')
        max_acceleration_el = el.find('max_acceleration')
        max_linear_acceleration_el = el.find('max_linear_acceleration')
        max_angular_acceleration_el = el.find('max_angular_acceleration')
        min_jerk_el = el.find('min_jerk')
        min_linear_jerk_el = el.find('min_linear_jerk')
        min_angular_jerk_el = el.find('min_angular_jerk')
        max_jerk_el = el.find('max_jerk')
        max_linear_jerk_el = el.find('max_linear_jerk')
        max_angular_jerk_el = el.find('max_angular_jerk')
        odom_publish_frequency_el = el.find('odom_publish_frequency')
        topic_el = el.find('topic')
        odom_topic_el = el.find('odom_topic')
        tf_topic_el = el.find('tf_topic')
        frame_id_el = el.find('frame_id')
        child_frame_id_el = el.find('child_frame_id')

        return cls(
            left_joint=left_joint_vals,
            right_joint=right_joint_vals,
            wheel_separation=float(
                wheel_separation_el.text) if wheel_separation_el is not None and wheel_separation_el.text is not None else None,
            wheel_radius=float(
                wheel_radius_el.text) if wheel_radius_el is not None and wheel_radius_el.text is not None else None,
            min_velocity=float(
                min_velocity_el.text) if min_velocity_el is not None and min_velocity_el.text is not None else None,
            min_linear_velocity=float(
                min_linear_velocity_el.text) if min_linear_velocity_el is not None and min_linear_velocity_el.text is not None else None,
            min_angular_velocity=float(
                min_angular_velocity_el.text) if min_angular_velocity_el is not None and min_angular_velocity_el.text is not None else None,
            max_velocity=float(
                max_velocity_el.text) if max_velocity_el is not None and max_velocity_el.text is not None else None,
            max_linear_velocity=float(
                max_linear_velocity_el.text) if max_linear_velocity_el is not None and max_linear_velocity_el.text is not None else None,
            max_angular_velocity=float(
                max_angular_velocity_el.text) if max_angular_velocity_el is not None and max_angular_velocity_el.text is not None else None,
            min_acceleration=float(
                min_acceleration_el.text) if min_acceleration_el is not None and min_acceleration_el.text is not None else None,
            min_linear_acceleration=float(
                min_linear_acceleration_el.text) if min_linear_acceleration_el is not None and min_linear_acceleration_el.text is not None else None,
            min_angular_acceleration=float(
                min_angular_acceleration_el.text) if min_angular_acceleration_el is not None and min_angular_acceleration_el.text is not None else None,
            max_acceleration=float(
                max_acceleration_el.text) if max_acceleration_el is not None and max_acceleration_el.text is not None else None,
            max_linear_acceleration=float(
                max_linear_acceleration_el.text) if max_linear_acceleration_el is not None and max_linear_acceleration_el.text is not None else None,
            max_angular_acceleration=float(
                max_angular_acceleration_el.text) if max_angular_acceleration_el is not None and max_angular_acceleration_el.text is not None else None,
            min_jerk=float(min_jerk_el.text) if min_jerk_el is not None and min_jerk_el.text is not None else None,
            min_linear_jerk=float(
                min_linear_jerk_el.text) if min_linear_jerk_el is not None and min_linear_jerk_el.text is not None else None,
            min_angular_jerk=float(
                min_angular_jerk_el.text) if min_angular_jerk_el is not None and min_angular_jerk_el.text is not None else None,
            max_jerk=float(max_jerk_el.text) if max_jerk_el is not None and max_jerk_el.text is not None else None,
            max_linear_jerk=float(
                max_linear_jerk_el.text) if max_linear_jerk_el is not None and max_linear_jerk_el.text is not None else None,
            max_angular_jerk=float(
                max_angular_jerk_el.text) if max_angular_jerk_el is not None and max_angular_jerk_el.text is not None else None,
            odom_publish_frequency=float(
                odom_publish_frequency_el.text) if odom_publish_frequency_el is not None and odom_publish_frequency_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            odom_topic=odom_topic_el.text if odom_topic_el is not None and odom_topic_el.text is not None else None,
            tf_topic=tf_topic_el.text if tf_topic_el is not None and tf_topic_el.text is not None else None,
            frame_id=frame_id_el.text if frame_id_el is not None and frame_id_el.text is not None else None,
            child_frame_id=child_frame_id_el.text if child_frame_id_el is not None and child_frame_id_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::DiffDrive",
                        filename="gz-sim-diff-drive-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        if self.left_joint is not None:
            for v in (self.left_joint if isinstance(self.left_joint, list) else [self.left_joint]):
                _add('left_joint', v)
        if self.right_joint is not None:
            for v in (self.right_joint if isinstance(self.right_joint, list) else [self.right_joint]):
                _add('right_joint', v)
        _add('wheel_separation', self.wheel_separation)
        _add('wheel_radius', self.wheel_radius)
        _add('min_velocity', self.min_velocity)
        _add('min_linear_velocity', self.min_linear_velocity)
        _add('min_angular_velocity', self.min_angular_velocity)
        _add('max_velocity', self.max_velocity)
        _add('max_linear_velocity', self.max_linear_velocity)
        _add('max_angular_velocity', self.max_angular_velocity)
        _add('min_acceleration', self.min_acceleration)
        _add('min_linear_acceleration', self.min_linear_acceleration)
        _add('min_angular_acceleration', self.min_angular_acceleration)
        _add('max_acceleration', self.max_acceleration)
        _add('max_linear_acceleration', self.max_linear_acceleration)
        _add('max_angular_acceleration', self.max_angular_acceleration)
        _add('min_jerk', self.min_jerk)
        _add('min_linear_jerk', self.min_linear_jerk)
        _add('min_angular_jerk', self.min_angular_jerk)
        _add('max_jerk', self.max_jerk)
        _add('max_linear_jerk', self.max_linear_jerk)
        _add('max_angular_jerk', self.max_angular_jerk)
        _add('odom_publish_frequency', self.odom_publish_frequency)
        _add('topic', self.topic)
        _add('odom_topic', self.odom_topic)
        _add('tf_topic', self.tf_topic)
        _add('frame_id', self.frame_id)
        _add('child_frame_id', self.child_frame_id)

        return el

    def to_version(self, target_version: str):
        return self
