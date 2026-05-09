from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .frame import Frame
from .inertia import Inertia
from .mass import Mass
from .pose import Pose
from ...sdf1_5.models.inertial import Inertial as _PrevInertial


class Inertial(_PrevInertial):
    def __init__(
            self,
            frame: List["Frame"] = None,
            pose: "Pose" = None,
            mass: "Mass" = None,
            inertia: "Inertia" = None
    ):
        super().__init__(frame=frame, pose=pose, mass=mass, inertia=inertia)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Inertial":
        _base = _PrevInertial.from_sdf(el)
        return cls(frame=_base.frame, pose=_base.pose, mass=_base.mass, inertia=_base.inertia)
