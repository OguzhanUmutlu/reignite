from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_7.models.enable_wind import EnableWind as _PrevEnableWind


class EnableWind(_PrevEnableWind):
    def __init__(self, enable_wind: bool = False):
        super().__init__(enable_wind=enable_wind)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "EnableWind":
        _base = _PrevEnableWind.from_sdf(el)
        return cls(enable_wind=_base.enable_wind)
