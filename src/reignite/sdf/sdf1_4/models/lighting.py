from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Lighting(Model):
    def __init__(self, lighting: bool = True):
        self.lighting = lighting

    def to_sdf(self) -> ET.Element:
        el = ET.Element("lighting")
        if self.lighting is not None:
            el.text = str(self.lighting).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Lighting":
        _text = el.text or True
        _lighting = _text.strip().lower() == 'true'
        return cls(lighting=_lighting)
