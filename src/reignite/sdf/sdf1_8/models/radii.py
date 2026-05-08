from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.vector3 import Vector3


class Radii(Model):
    def __init__(self, radii: Vector3 = None):
        if radii is None:
            radii = Vector3.from_sdf("1 1 1")
        self.radii = radii

    def to_sdf(self) -> ET.Element:
        el = ET.Element("radii")
        if self.radii is not None:
            el.text = self.radii.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Radii":
        _text = el.text or "1 1 1"
        _radii = Vector3.from_sdf(_text)
        return cls(radii=_radii)
