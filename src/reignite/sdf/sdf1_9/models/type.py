from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_8.models.type import Type as _PrevType


class Type(_PrevType):
    def __init__(self, type: str = "stereographic"):
        super().__init__(type=type)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Type":
        _base = _PrevType.from_sdf(el)
        return cls(type=_base.type)
