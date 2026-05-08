from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Essid(Model):
    def __init__(self, essid: str = "wireless"):
        self.essid = essid

    def to_sdf(self) -> ET.Element:
        el = ET.Element("essid")
        if self.essid is not None:
            el.text = self.essid
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Essid":
        _text = el.text or "wireless"
        _essid = _text
        return cls(essid=_essid)
