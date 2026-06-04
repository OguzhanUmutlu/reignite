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

        super().__init__(
            sdf_version=None,
            filename="gz-sim-joint-trajectory-controller-system",
            name="gz::sim::systems::JointTrajectoryController",
            joint_name=_get_names(joint_name),
            use_header_start_time=use_header_start_time,
            topic=topic,
            initial_position=initial_position,
            position_p_gain=position_p_gain,
            position_i_gain=position_i_gain,
            position_d_gain=position_d_gain,
            position_i_min=position_i_min,
            position_i_max=position_i_max,
            position_cmd_min=position_cmd_min,
            position_cmd_max=position_cmd_max,
            position_cmd_offset=position_cmd_offset,
            velocity_p_gain=velocity_p_gain,
            velocity_i_gain=velocity_i_gain,
            velocity_d_gain=velocity_d_gain,
            velocity_i_min=velocity_i_min,
            velocity_i_max=velocity_i_max,
            velocity_cmd_min=velocity_cmd_min,
            velocity_cmd_max=velocity_cmd_max,
            velocity_cmd_offset=velocity_cmd_offset
        )
