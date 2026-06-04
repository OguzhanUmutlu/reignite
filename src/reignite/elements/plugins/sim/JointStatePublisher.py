from ...joint import Joint
from ...plugin import Plugin


@Plugin.register("gz-sim-joint-state-publisher-system", "gz::sim::systems::JointStatePublisher")
class JointStatePublisherPlugin(Plugin):
    def __init__(
            self,
            joint_name: str | Joint | list[str | Joint] | None = None,
            topic: str | None = None,
            update_rate: float | None = None
    ):
        def _get_names(joints):
            if joints is None:
                return None
            if isinstance(joints, list):
                return [j.name if isinstance(j, Joint) else j for j in joints]
            return joints.name if isinstance(joints, Joint) else joints

        super().__init__(
            sdf_version=None,
            filename="gz-sim-joint-state-publisher-system",
            name="gz::sim::systems::JointStatePublisher",
            joint_name=_get_names(joint_name),
            topic=topic,
            update_rate=update_rate
        )
