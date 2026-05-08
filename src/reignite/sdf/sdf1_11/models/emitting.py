from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_10.models.emitting import Emitting as _PrevEmitting


class Emitting(_PrevEmitting):
    def __init__(self, emitting: bool = True):
        super().__init__(emitting=emitting)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Emitting":
        _base = _PrevEmitting.from_sdf(el)
        return cls(emitting=_base.emitting)
