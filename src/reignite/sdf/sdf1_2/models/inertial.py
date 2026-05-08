from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_0.models.inertial import Inertial as _PrevInertial
from .mass import Mass
from .pose import Pose
from .inertia import Inertia


class Inertial(_PrevInertial):
    def __init__(self, mass: "Mass" = None, pose: "Pose" = None, inertia: "Inertia" = None):
        super().__init__(mass=mass, inertia=inertia)
        self.pose = pose

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Inertial":
        _base = _PrevInertial.from_sdf(el)
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        return cls(mass=_base.mass, pose=_pose, inertia=_base.inertia)
