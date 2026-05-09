from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_2.models.scale import Scale as _PrevScale
from ....utils.vector3 import Vector3


class Scale(_PrevScale):
    def __init__(self, scale: Vector3 = None):
        if scale is None:
            scale = Vector3.from_sdf("1 1 1")
        super().__init__(scale=scale)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Scale":
        _base = _PrevScale.from_sdf(el)
        return cls(scale=_base.scale)
