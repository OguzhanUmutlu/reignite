from ...link import Link
from ...model import Model
from ...plugin import Plugin


class DetachableJointPlugin(Plugin):
    def __init__(
            self,
            parent_link: Link | str,
            child_model: Model | str,
            child_link: Link | str,
            detach_topic: str | None = None,
            topic: str | None = None,
            attach_topic: str | None = None,
            output_topic: str | None = None,
            suppress_child_warning: bool = True
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-detachable-joint-system",
            name="gz::sim:systems::DetachableJoint",
            parent_link=parent_link if isinstance(parent_link, str) else parent_link.name,
            child_model=child_model if isinstance(child_model, str) else child_model.name,
            child_link=child_link if isinstance(child_link, str) else child_link.name,
            detach_topic=detach_topic,
            topic=topic,
            attach_topic=attach_topic,
            output_topic=output_topic,
            suppress_child_warning=suppress_child_warning
        )
