from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_11.models.mimic import Mimic as _PrevMimic
from .multiplier import Multiplier
from .offset import Offset
from .reference import Reference


class Mimic(_PrevMimic):
    def __init__(
        self,
        joint: str = "",
        axis: str = "axis",
        multiplier: "Multiplier" = None,
        offset: "Offset" = None,
        reference: "Reference" = None
    ):
        super().__init__(joint=joint, axis=axis, multiplier=multiplier, offset=offset, reference=reference)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Mimic":
        _base = _PrevMimic.from_sdf(el)
        return cls(joint=_base.joint, axis=_base.axis, multiplier=_base.multiplier, offset=_base.offset, reference=_base.reference)
