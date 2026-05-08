from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Center(Model):
    def __init__(self, center: bool = False):
        self.center = center

    def to_sdf(self) -> ET.Element:
        el = ET.Element("center")
        if self.center is not None:
            el.text = str(self.center).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Center":
        _text = el.text or False
        _center = _text.strip().lower() == 'true'
        return cls(center=_center)
