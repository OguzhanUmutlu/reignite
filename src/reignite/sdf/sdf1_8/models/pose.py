from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_7.models.pose import Pose as _PrevPose
from ....utils.pose import Pose


class Pose(_PrevPose):
    def __init__(self, pose: Pose = None, relative_to: str = ""):
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        super().__init__(pose=pose)
        self.relative_to = relative_to

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pose":
        _base = _PrevPose.from_sdf(el)
        _relative_to = el.get("relative_to", "")
        return cls(pose=_base.pose, relative_to=_relative_to)
