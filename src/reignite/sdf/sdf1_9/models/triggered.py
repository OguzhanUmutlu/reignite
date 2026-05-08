from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Triggered(Model):
    def __init__(self, triggered: bool = False):
        self.triggered = triggered

    def to_sdf(self) -> ET.Element:
        el = ET.Element("triggered")
        if self.triggered is not None:
            el.text = str(self.triggered).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Triggered":
        _text = el.text or False
        _triggered = _text.strip().lower() == 'true'
        return cls(triggered=_triggered)
