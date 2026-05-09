from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_11.models.pose import Pose as _PrevPose
from ....utils.pose import Pose


class Pose(_PrevPose):
    def __init__(
            self,
            pose: Pose = None,
            relative_to: str = "",
            rotation_format: str = "euler_rpy",
            degrees: bool = False
    ):
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        super().__init__(pose=pose, relative_to=relative_to, rotation_format=rotation_format, degrees=degrees)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pose":
        _base = _PrevPose.from_sdf(el)
        return cls(pose=_base.pose, relative_to=_base.relative_to, rotation_format=_base.rotation_format,
                   degrees=_base.degrees)


class LightState(Model):
    def __init__(self, name: str = "__default__", pose: "Pose" = None):
        self.name = name
        self.pose = pose

    def to_sdf(self) -> ET.Element:
        el = ET.Element("light_state")
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "LightState":
        _name = el.get("name", "__default__")
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        return cls(name=_name, pose=_pose)
