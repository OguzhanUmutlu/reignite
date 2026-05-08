from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_10.models.gravity import Gravity as _PrevGravity


class Gravity(_PrevGravity):
    def __init__(self, gravity: bool = True):
        super().__init__(gravity=gravity)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Gravity":
        _base = _PrevGravity.from_sdf(el)
        return cls(gravity=_base.gravity)
