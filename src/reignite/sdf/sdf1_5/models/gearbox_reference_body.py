from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_4.models.gearbox_reference_body import GearboxReferenceBody as _PrevGearboxReferenceBody


class GearboxReferenceBody(_PrevGearboxReferenceBody):
    def __init__(self, gearbox_reference_body: str = "__default__"):
        super().__init__(gearbox_reference_body=gearbox_reference_body)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "GearboxReferenceBody":
        _base = _PrevGearboxReferenceBody.from_sdf(el)
        return cls(gearbox_reference_body=_base.gearbox_reference_body)
