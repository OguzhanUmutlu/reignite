from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class OriginVisual(Model):
    def __init__(self, origin_visual: bool = True):
        self.origin_visual = origin_visual

    def to_sdf(self) -> ET.Element:
        el = ET.Element("origin_visual")
        if self.origin_visual is not None:
            el.text = str(self.origin_visual).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "OriginVisual":
        _text = el.text or True
        _origin_visual = _text.strip().lower() == 'true'
        return cls(origin_visual=_origin_visual)
