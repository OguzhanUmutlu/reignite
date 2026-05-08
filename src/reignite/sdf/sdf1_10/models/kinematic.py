from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_9.models.kinematic import Kinematic as _PrevKinematic


class Kinematic(_PrevKinematic):
    def __init__(self, kinematic: bool = False):
        super().__init__(kinematic=kinematic)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Kinematic":
        _base = _PrevKinematic.from_sdf(el)
        return cls(kinematic=_base.kinematic)
