from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Static(Model):
    def __init__(self, static: bool = True):
        self.static = static

    def to_sdf(self) -> ET.Element:
        el = ET.Element("static")
        if self.static is not None:
            el.text = str(self.static).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Static":
        _text = el.text or True
        _static = _text.strip().lower() == 'true'
        return cls(static=_static)
