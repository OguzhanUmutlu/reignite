from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class PalmLink(Model):
    def __init__(self, palm_link: str = "__default__"):
        self.palm_link = palm_link

    def to_sdf(self) -> ET.Element:
        el = ET.Element("palm_link")
        if self.palm_link is not None:
            el.text = self.palm_link
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "PalmLink":
        _text = el.text or "__default__"
        _palm_link = _text
        return cls(palm_link=_palm_link)
