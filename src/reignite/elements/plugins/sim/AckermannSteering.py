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

        super().__init__(
            sdf_version=None,
            filename="gz-sim-ackermann-steering-system",
            name="gz::sim::systems::AckermannSteering",
            left_steering_joint=_get_names(left_steering_joint),
            right_steering_joint=_get_names(right_steering_joint),
            left_joint=_get_names(left_joint),
            right_joint=_get_names(right_joint),
            steering_only=steering_only,
            use_actuator_msg=use_actuator_msg,
            actuator_number=actuator_number,
            wheel_radius=wheel_radius,
            kingpin_width=kingpin_width,
            wheel_separation=wheel_separation,
            wheel_base=wheel_base,
            steering_limit=steering_limit,
            steer_p_gain=steer_p_gain,
            min_velocity=min_velocity,
            max_velocity=max_velocity,
            min_acceleration=min_acceleration,
            max_acceleration=max_acceleration,
            min_jerk=min_jerk,
            max_jerk=max_jerk,
            odom_publish_frequency=odom_publish_frequency,
            topic=topic,
            sub_topic=sub_topic,
            odom_topic=odom_topic,
            tf_topic=tf_topic,
            frame_id=frame_id,
            child_frame_id=child_frame_id
        )
