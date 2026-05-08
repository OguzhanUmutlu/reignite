from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Loop(Model):
    def __init__(self, loop: bool = False):
        self.loop = loop

    def to_sdf(self) -> ET.Element:
        el = ET.Element("loop")
        if self.loop is not None:
            el.text = str(self.loop).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Loop":
        _text = el.text or False
        _loop = _text.strip().lower() == 'true'
        return cls(loop=_loop)
