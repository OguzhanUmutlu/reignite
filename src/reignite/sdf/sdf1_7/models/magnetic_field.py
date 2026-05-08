from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_6.models.magnetic_field import MagneticField as _PrevMagneticField
from ....utils.vector3 import Vector3


class MagneticField(_PrevMagneticField):
    def __init__(self, magnetic_field: Vector3 = None):
        if magnetic_field is None:
            magnetic_field = Vector3.from_sdf("5.5645e-6 22.8758e-6 -42.3884e-6")
        super().__init__(magnetic_field=magnetic_field)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MagneticField":
        _base = _PrevMagneticField.from_sdf(el)
        return cls(magnetic_field=_base.magnetic_field)
