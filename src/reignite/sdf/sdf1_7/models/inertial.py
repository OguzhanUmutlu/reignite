from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_6.models.inertial import Inertial as _PrevInertial
from .pose import Pose
from .mass import Mass
from .inertia import Inertia


class Inertial(_PrevInertial):
    def __init__(self, pose: "Pose" = None, mass: "Mass" = None, inertia: "Inertia" = None):
        super().__init__(pose=pose, mass=mass, inertia=inertia)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Inertial":
        _base = _PrevInertial.from_sdf(el)
        return cls(pose=_base.pose, mass=_base.mass, inertia=_base.inertia)
