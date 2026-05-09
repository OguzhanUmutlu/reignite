from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_11.models.double_sided import DoubleSided as _PrevDoubleSided


class DoubleSided(_PrevDoubleSided):
    def __init__(self, double_sided: bool = False):
        super().__init__(double_sided=double_sided)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "DoubleSided":
        _base = _PrevDoubleSided.from_sdf(el)
        return cls(double_sided=_base.double_sided)
