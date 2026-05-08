from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_10.models.box_type import BoxType as _PrevBoxType


class BoxType(_PrevBoxType):
    def __init__(self, box_type: str = "2d"):
        super().__init__(box_type=box_type)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "BoxType":
        _base = _PrevBoxType.from_sdf(el)
        return cls(box_type=_base.box_type)
