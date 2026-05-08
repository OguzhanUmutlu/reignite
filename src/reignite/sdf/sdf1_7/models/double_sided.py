from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class DoubleSided(Model):
    def __init__(self, double_sided: bool = False):
        self.double_sided = double_sided

    def to_sdf(self) -> ET.Element:
        el = ET.Element("double_sided")
        if self.double_sided is not None:
            el.text = str(self.double_sided).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "DoubleSided":
        _text = el.text or False
        _double_sided = _text.strip().lower() == 'true'
        return cls(double_sided=_double_sided)
