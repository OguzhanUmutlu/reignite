from ...joint import Joint
from ...plugin import Plugin


class ApplyJointForcePlugin(Plugin):
    def __init__(
            self,
            joint_name: str | Joint
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-apply-joint-force-system",
            name="gz::sim::systems::ApplyJointForce",
            joint_name=joint_name.name if isinstance(joint_name, Joint) else joint_name
        )
