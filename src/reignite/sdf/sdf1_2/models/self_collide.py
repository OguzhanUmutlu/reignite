from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class SelfCollide(Model):
    def __init__(self, self_collide: bool = False):
        self.self_collide = self_collide

    def to_sdf(self) -> ET.Element:
        el = ET.Element("self_collide")
        if self.self_collide is not None:
            el.text = str(self.self_collide).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SelfCollide":
        _text = el.text or False
        _self_collide = _text.strip().lower() == 'true'
        return cls(self_collide=_self_collide)
