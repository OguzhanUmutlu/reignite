from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.pose import Pose


class Origin(Model):
    def __init__(self, pose: Pose = None):
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        self.pose = pose

    def to_sdf(self) -> ET.Element:
        el = ET.Element("origin")
        if self.pose is not None:
            el.set("pose", self.pose.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Origin":
        _pose = Pose.from_sdf(el.get("pose", "0 0 0 0 0 0"))
        return cls(pose=_pose)
