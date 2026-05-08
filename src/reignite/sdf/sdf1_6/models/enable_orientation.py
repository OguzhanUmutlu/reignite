from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class EnableOrientation(Model):
    def __init__(self, enable_orientation: bool = True):
        self.enable_orientation = enable_orientation

    def to_sdf(self) -> ET.Element:
        el = ET.Element("enable_orientation")
        if self.enable_orientation is not None:
            el.text = str(self.enable_orientation).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "EnableOrientation":
        _text = el.text or True
        _enable_orientation = _text.strip().lower() == 'true'
        return cls(enable_orientation=_enable_orientation)
