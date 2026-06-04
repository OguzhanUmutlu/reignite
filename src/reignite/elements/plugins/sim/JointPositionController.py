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

        super().__init__(
            sdf_version=None,
            filename="gz-sim-joint-position-controller-system",
            name="gz::sim::systems::JointPositionController",
            joint_name=_get_names(joint_name),
            joint_index=joint_index,
            p_gain=p_gain,
            i_gain=i_gain,
            d_gain=d_gain,
            i_max=i_max,
            i_min=i_min,
            cmd_max=cmd_max,
            cmd_min=cmd_min,
            cmd_offset=cmd_offset,
            use_velocity_commands=use_velocity_commands,
            initial_position=initial_position,
            use_actuator_msg=use_actuator_msg,
            actuator_number=actuator_number,
            sub_topic=sub_topic,
            topic=topic
        )
