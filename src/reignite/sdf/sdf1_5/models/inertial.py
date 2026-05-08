from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_4.models.inertial import Inertial as _PrevInertial
from .frame import Frame
from .pose import Pose
from .mass import Mass
from .inertia import Inertia


class Inertial(_PrevInertial):
    def __init__(
        self,
        frame: List["Frame"] = None,
        pose: "Pose" = None,
        mass: "Mass" = None,
        inertia: "Inertia" = None
    ):
        super().__init__(pose=pose, mass=mass, inertia=inertia)
        self.frame = frame or []

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        for item in (self.frame or []):
            el.append(item.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Inertial":
        _base = _PrevInertial.from_sdf(el)
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        return cls(frame=_frame, pose=_base.pose, mass=_base.mass, inertia=_base.inertia)
