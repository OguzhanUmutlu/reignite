from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Kinematic(Model):
    def __init__(self, kinematic: bool = False):
        self.kinematic = kinematic

    def to_sdf(self) -> ET.Element:
        el = ET.Element("kinematic")
        if self.kinematic is not None:
            el.text = str(self.kinematic).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Kinematic":
        _text = el.text or False
        _kinematic = _text.strip().lower() == 'true'
        return cls(kinematic=_kinematic)
