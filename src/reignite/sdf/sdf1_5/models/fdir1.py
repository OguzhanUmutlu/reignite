from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_4.models.fdir1 import Fdir1 as _PrevFdir1
from ....utils.vector3 import Vector3


class Fdir1(_PrevFdir1):
    def __init__(self, fdir1: Vector3 = None):
        if fdir1 is None:
            fdir1 = Vector3.from_sdf("0 0 0")
        super().__init__(fdir1=fdir1)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Fdir1":
        _base = _PrevFdir1.from_sdf(el)
        return cls(fdir1=_base.fdir1)
