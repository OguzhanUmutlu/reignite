from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_3.models.joint import Joint as _PrevJoint
from .sensor import Sensor
from .parent import Parent
from .child import Child
from .pose import Pose
from .gearbox_ratio import GearboxRatio
from .gearbox_reference_body import GearboxReferenceBody
from .thread_pitch import ThreadPitch
from .axis import Axis
from .axis2 import Axis2
from .physics import Physics


class Joint(_PrevJoint):
    def __init__(
        self,
        name: str = "__default__",
        type: str = "__default__",
        sensor: List["Sensor"] = None,
        parent: "Parent" = None,
        child: "Child" = None,
        pose: "Pose" = None,
        gearbox_ratio: "GearboxRatio" = None,
        gearbox_reference_body: "GearboxReferenceBody" = None,
        thread_pitch: "ThreadPitch" = None,
        axis: "Axis" = None,
        axis2: "Axis2" = None,
        physics: "Physics" = None
    ):
        super().__init__(name=name, type=type, parent=parent, child=child, pose=pose, thread_pitch=thread_pitch, axis=axis, axis2=axis2, physics=physics)
        self.sensor = sensor or []
        self.gearbox_ratio = gearbox_ratio
        self.gearbox_reference_body = gearbox_reference_body

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        for item in (self.sensor or []):
            el.append(item.to_sdf())
        if self.gearbox_ratio is not None:
            el.append(self.gearbox_ratio.to_sdf())
        if self.gearbox_reference_body is not None:
            el.append(self.gearbox_reference_body.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Joint":
        _base = _PrevJoint.from_sdf(el)
        _sensor = [Sensor.from_sdf(c) for c in el.findall("sensor")]
        _c_gearbox_ratio = el.find("gearbox_ratio")
        _gearbox_ratio = GearboxRatio.from_sdf(_c_gearbox_ratio) if _c_gearbox_ratio is not None else None
        _c_gearbox_reference_body = el.find("gearbox_reference_body")
        _gearbox_reference_body = GearboxReferenceBody.from_sdf(_c_gearbox_reference_body) if _c_gearbox_reference_body is not None else None
        return cls(name=_base.name, type=_base.type, sensor=_sensor, parent=_base.parent, child=_base.child, pose=_base.pose, gearbox_ratio=_gearbox_ratio, gearbox_reference_body=_gearbox_reference_body, thread_pitch=_base.thread_pitch, axis=_base.axis, axis2=_base.axis2, physics=_base.physics)
