from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class AlwaysOn(Model):
    def __init__(self, always_on: bool = False):
        self.always_on = always_on

    def to_sdf(self) -> ET.Element:
        el = ET.Element("always_on")
        if self.always_on is not None:
            el.text = str(self.always_on).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AlwaysOn":
        _text = el.text or False
        _always_on = _text.strip().lower() == 'true'
        return cls(always_on=_always_on)
