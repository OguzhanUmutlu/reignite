from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_5.models.xyz import Xyz as _PrevXyz
from ....utils.vector3 import Vector3


class Xyz(_PrevXyz):
    def __init__(self, xyz: Vector3 = None):
        if xyz is None:
            xyz = Vector3.from_sdf("0 0 1")
        super().__init__(xyz=xyz)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Xyz":
        _base = _PrevXyz.from_sdf(el)
        return cls(xyz=_base.xyz)
