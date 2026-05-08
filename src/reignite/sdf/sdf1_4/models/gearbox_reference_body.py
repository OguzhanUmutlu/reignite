from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class GearboxReferenceBody(Model):
    def __init__(self, gearbox_reference_body: str = "__default__"):
        self.gearbox_reference_body = gearbox_reference_body

    def to_sdf(self) -> ET.Element:
        el = ET.Element("gearbox_reference_body")
        if self.gearbox_reference_body is not None:
            el.text = self.gearbox_reference_body
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "GearboxReferenceBody":
        _text = el.text or "__default__"
        _gearbox_reference_body = _text
        return cls(gearbox_reference_body=_gearbox_reference_body)
