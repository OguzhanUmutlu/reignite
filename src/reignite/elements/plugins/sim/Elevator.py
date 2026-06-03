from ...joint import Joint
from ...plugin import Plugin


class ElevatorPlugin(Plugin):
    def __init__(
            self,
            cabin_joint: str | Joint = "lift",
            update_rate: float = 10.0,
            floor_link_prefix: str = "floor_",
            door_joint_prefix: str = "door_",
            open_door_wait_duration: float = 5.0,
            state_topic: str | None = None,
            state_publish_rate: float = 5.0,
            cmd_topic: str | None = None
    ):
        def _get_name(joint):
            if joint is None:
                return None
            return joint.name if isinstance(joint, Joint) else joint

        super().__init__(
            sdf_version=None,
            filename="gz-sim-elevator-system",
            name="gz::sim::systems::Elevator",
            cabin_joint=_get_name(cabin_joint),
            update_rate=update_rate,
            floor_link_prefix=floor_link_prefix,
            door_joint_prefix=door_joint_prefix,
            open_door_wait_duration=open_door_wait_duration,
            state_topic=state_topic,
            state_publish_rate=state_publish_rate,
            cmd_topic=cmd_topic
        )
