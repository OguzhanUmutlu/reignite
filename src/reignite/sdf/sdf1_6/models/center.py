from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_5.models.center import Center as _PrevCenter


class Center(_PrevCenter):
    def __init__(self, center: bool = False):
        super().__init__(center=center)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Center":
        _base = _PrevCenter.from_sdf(el)
        return cls(center=_base.center)
