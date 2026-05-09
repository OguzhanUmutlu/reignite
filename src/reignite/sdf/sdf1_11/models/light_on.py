from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_10.models.light_on import LightOn as _PrevLightOn


class LightOn(_PrevLightOn):
    def __init__(self, light_on: bool = True):
        super().__init__(light_on=light_on)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "LightOn":
        _base = _PrevLightOn.from_sdf(el)
        return cls(light_on=_base.light_on)
