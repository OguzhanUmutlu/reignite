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

        super().__init__(
            sdf_version=None,
            filename="gz-sim-joint-controller-system",
            name="gz::sim::systems::JointController",
            joint_name=_get_names(joint_name),
            initial_velocity=initial_velocity,
            use_force_commands=use_force_commands,
            p_gain=p_gain,
            i_gain=i_gain,
            d_gain=d_gain,
            i_max=i_max,
            i_min=i_min,
            cmd_max=cmd_max,
            cmd_min=cmd_min,
            cmd_offset=cmd_offset,
            disable_braking=disable_braking,
            use_actuator_msg=use_actuator_msg,
            actuator_number=actuator_number,
            topic=topic,
            sub_topic=sub_topic
        )
