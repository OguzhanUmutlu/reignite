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

        super().__init__(
            sdf_version=None,
            filename="gz-sim-diff-drive-system",
            name="gz::sim::systems::DiffDrive",
            left_joint=_get_names(left_joint),
            right_joint=_get_names(right_joint),
            wheel_separation=wheel_separation,
            wheel_radius=wheel_radius,
            min_velocity=min_velocity,
            min_linear_velocity=min_linear_velocity,
            min_angular_velocity=min_angular_velocity,
            max_velocity=max_velocity,
            max_linear_velocity=max_linear_velocity,
            max_angular_velocity=max_angular_velocity,
            min_acceleration=min_acceleration,
            min_linear_acceleration=min_linear_acceleration,
            min_angular_acceleration=min_angular_acceleration,
            max_acceleration=max_acceleration,
            max_linear_acceleration=max_linear_acceleration,
            max_angular_acceleration=max_angular_acceleration,
            min_jerk=min_jerk,
            min_linear_jerk=min_linear_jerk,
            min_angular_jerk=min_angular_jerk,
            max_jerk=max_jerk,
            max_linear_jerk=max_linear_jerk,
            max_angular_jerk=max_angular_jerk,
            odom_publish_frequency=odom_publish_frequency,
            topic=topic,
            odom_topic=odom_topic,
            tf_topic=tf_topic,
            frame_id=frame_id,
            child_frame_id=child_frame_id
        )
