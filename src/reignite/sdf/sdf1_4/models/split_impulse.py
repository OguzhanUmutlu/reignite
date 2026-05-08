from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class SplitImpulse(Model):
    def __init__(self, split_impulse: bool = True):
        self.split_impulse = split_impulse

    def to_sdf(self) -> ET.Element:
        el = ET.Element("split_impulse")
        if self.split_impulse is not None:
            el.text = str(self.split_impulse).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SplitImpulse":
        _text = el.text or True
        _split_impulse = _text.strip().lower() == 'true'
        return cls(split_impulse=_split_impulse)
