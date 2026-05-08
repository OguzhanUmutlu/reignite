from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Shadows(Model):
    def __init__(self, shadows: bool = True):
        self.shadows = shadows

    def to_sdf(self) -> ET.Element:
        el = ET.Element("shadows")
        if self.shadows is not None:
            el.text = str(self.shadows).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Shadows":
        _text = el.text or True
        _shadows = _text.strip().lower() == 'true'
        return cls(shadows=_shadows)
