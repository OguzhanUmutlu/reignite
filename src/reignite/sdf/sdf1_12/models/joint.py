from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_11.models.joint import Joint as _PrevJoint
from .pose import Pose
from .sensor import Sensor
from .parent import Parent
from .child import Child
from .gearbox_ratio import GearboxRatio
from .gearbox_reference_body import GearboxReferenceBody
from .thread_pitch import ThreadPitch
from .screw_thread_pitch import ScrewThreadPitch
from .axis import Axis
from .axis2 import Axis2
from .physics import Physics


class Joint(_PrevJoint):
    def __init__(
        self,
        name: str = "__default__",
        type: str = "__default__",
        pose: "Pose" = None,
        sensor: List["Sensor"] = None,
        parent: "Parent" = None,
        child: "Child" = None,
        gearbox_ratio: "GearboxRatio" = None,
        gearbox_reference_body: "GearboxReferenceBody" = None,
        thread_pitch: "ThreadPitch" = None,
        screw_thread_pitch: "ScrewThreadPitch" = None,
        axis: "Axis" = None,
        axis2: "Axis2" = None,
        physics: "Physics" = None
    ):
        super().__init__(name=name, type=type, pose=pose, sensor=sensor, parent=parent, child=child, gearbox_ratio=gearbox_ratio, gearbox_reference_body=gearbox_reference_body, thread_pitch=thread_pitch, screw_thread_pitch=screw_thread_pitch, axis=axis, axis2=axis2, physics=physics)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Joint":
        _base = _PrevJoint.from_sdf(el)
        return cls(name=_base.name, type=_base.type, pose=_base.pose, sensor=_base.sensor, parent=_base.parent, child=_base.child, gearbox_ratio=_base.gearbox_ratio, gearbox_reference_body=_base.gearbox_reference_body, thread_pitch=_base.thread_pitch, screw_thread_pitch=_base.screw_thread_pitch, axis=_base.axis, axis2=_base.axis2, physics=_base.physics)
