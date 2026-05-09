from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_7.models.lighting import Lighting as _PrevLighting


class Lighting(_PrevLighting):
    def __init__(self, lighting: bool = True):
        super().__init__(lighting=lighting)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Lighting":
        _base = _PrevLighting.from_sdf(el)
        return cls(lighting=_base.lighting)
