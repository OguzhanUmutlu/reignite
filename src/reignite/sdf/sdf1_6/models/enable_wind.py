from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class EnableWind(Model):
    def __init__(self, enable_wind: bool = False):
        self.enable_wind = enable_wind

    def to_sdf(self) -> ET.Element:
        el = ET.Element("enable_wind")
        if self.enable_wind is not None:
            el.text = str(self.enable_wind).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "EnableWind":
        _text = el.text or False
        _enable_wind = _text.strip().lower() == 'true'
        return cls(enable_wind=_enable_wind)
