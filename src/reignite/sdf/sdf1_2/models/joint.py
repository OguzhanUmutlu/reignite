from __future__ import annotations

from xml.etree import ElementTree as ET

from .axis import Axis
from .axis2 import Axis2
from .child import Child
from .parent import Parent
from .physics import Physics
from .pose import Pose
from .thread_pitch import ThreadPitch
from ...sdf1_0.models.joint import Joint as _PrevJoint


class Joint(_PrevJoint):
    def __init__(
            self,
            name: str = "__default__",
            type: str = "__default__",
            parent: "Parent" = None,
            child: "Child" = None,
            pose: "Pose" = None,
            thread_pitch: "ThreadPitch" = None,
            axis: "Axis" = None,
            axis2: "Axis2" = None,
            physics: "Physics" = None
    ):
        super().__init__(name=name, type=type, parent=parent, child=child, thread_pitch=thread_pitch, axis=axis,
                         axis2=axis2, physics=physics)
        self.pose = pose

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Joint":
        _base = _PrevJoint.from_sdf(el)
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        return cls(name=_base.name, type=_base.type, parent=_base.parent, child=_base.child, pose=_pose,
                   thread_pitch=_base.thread_pitch, axis=_base.axis, axis2=_base.axis2, physics=_base.physics)
