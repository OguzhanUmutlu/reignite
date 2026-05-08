from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_8.models.suspension import Suspension as _PrevSuspension
from .cfm import Cfm
from .erp import Erp


class Suspension(_PrevSuspension):
    def __init__(self, cfm: "Cfm" = None, erp: "Erp" = None):
        super().__init__(cfm=cfm, erp=erp)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Suspension":
        _base = _PrevSuspension.from_sdf(el)
        return cls(cfm=_base.cfm, erp=_base.erp)
