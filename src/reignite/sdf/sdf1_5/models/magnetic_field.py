from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.vector3 import Vector3


class MagneticField(Model):
    def __init__(self, magnetic_field: Vector3 = None):
        if magnetic_field is None:
            magnetic_field = Vector3.from_sdf("5.5645e-6 22.8758e-6 -42.3884e-6")
        self.magnetic_field = magnetic_field

    def to_sdf(self) -> ET.Element:
        el = ET.Element("magnetic_field")
        if self.magnetic_field is not None:
            el.text = self.magnetic_field.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MagneticField":
        _text = el.text or "5.5645e-6 22.8758e-6 -42.3884e-6"
        _magnetic_field = Vector3.from_sdf(_text)
        return cls(magnetic_field=_magnetic_field)
