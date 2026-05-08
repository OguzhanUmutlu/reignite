from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class ImplicitSpringDamper(Model):
    def __init__(self, implicit_spring_damper: bool = False):
        self.implicit_spring_damper = implicit_spring_damper

    def to_sdf(self) -> ET.Element:
        el = ET.Element("implicit_spring_damper")
        if self.implicit_spring_damper is not None:
            el.text = str(self.implicit_spring_damper).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ImplicitSpringDamper":
        _text = el.text or False
        _implicit_spring_damper = _text.strip().lower() == 'true'
        return cls(implicit_spring_damper=_implicit_spring_damper)
