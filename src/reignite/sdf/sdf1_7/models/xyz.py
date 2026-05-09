from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_6.models.xyz import Xyz as _PrevXyz
from ....utils.vector3 import Vector3


class Xyz(_PrevXyz):
    def __init__(self, xyz: Vector3 = None, expressed_in: str = ""):
        if xyz is None:
            xyz = Vector3.from_sdf("0 0 1")
        super().__init__(xyz=xyz)
        self.expressed_in = expressed_in

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.expressed_in is not None:
            el.set("expressed_in", self.expressed_in)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Xyz":
        _base = _PrevXyz.from_sdf(el)
        _expressed_in = el.get("expressed_in", "")
        return cls(xyz=_base.xyz, expressed_in=_expressed_in)
