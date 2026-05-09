from __future__ import annotations

from xml.etree import ElementTree as ET

from .pose import Pose
from ...sdf1_5.models.frame import Frame as _PrevFrame


class Frame(_PrevFrame):
    def __init__(self, name: str = "", pose: "Pose" = None):
        super().__init__()
        self.name = name
        self.pose = pose

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Frame":
        _name = el.get("name", "")
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        return cls(name=_name, pose=_pose)
