from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class LightOn(Model):
    def __init__(self, light_on: bool = True):
        self.light_on = light_on

    def to_sdf(self) -> ET.Element:
        el = ET.Element("light_on")
        if self.light_on is not None:
            el.text = str(self.light_on).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "LightOn":
        _text = el.text or True
        _light_on = _text.strip().lower() == 'true'
        return cls(light_on=_light_on)
