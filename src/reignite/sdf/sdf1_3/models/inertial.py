from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_2.models.inertial import Inertial as _PrevInertial
from .mass import Mass
from .pose import Pose
from .inertia import Inertia


class Inertial(_PrevInertial):
    def __init__(self, mass: "Mass" = None, pose: "Pose" = None, inertia: "Inertia" = None):
        super().__init__(mass=mass, pose=pose, inertia=inertia)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Inertial":
        _base = _PrevInertial.from_sdf(el)
        return cls(mass=_base.mass, pose=_base.pose, inertia=_base.inertia)
