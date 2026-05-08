from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class InterpolateX(Model):
    def __init__(self, interpolate_x: bool = False):
        self.interpolate_x = interpolate_x

    def to_sdf(self) -> ET.Element:
        el = ET.Element("interpolate_x")
        if self.interpolate_x is not None:
            el.text = str(self.interpolate_x).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "InterpolateX":
        _text = el.text or False
        _interpolate_x = _text.strip().lower() == 'true'
        return cls(interpolate_x=_interpolate_x)
