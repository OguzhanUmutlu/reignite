from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_2.models.joint import Joint as _PrevJoint
from .parent import Parent
from .child import Child
from .pose import Pose
from .thread_pitch import ThreadPitch
from .axis import Axis
from .axis2 import Axis2
from .physics import Physics


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
        super().__init__(name=name, type=type, parent=parent, child=child, pose=pose, thread_pitch=thread_pitch, axis=axis, axis2=axis2, physics=physics)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Joint":
        _base = _PrevJoint.from_sdf(el)
        return cls(name=_base.name, type=_base.type, parent=_base.parent, child=_base.child, pose=_base.pose, thread_pitch=_base.thread_pitch, axis=_base.axis, axis2=_base.axis2, physics=_base.physics)
