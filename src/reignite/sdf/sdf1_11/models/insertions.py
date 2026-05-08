from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_10.models.insertions import Insertions as _PrevInsertions
from .model import Model
from .light import Light


class Insertions(_PrevInsertions):
    def __init__(self, model: List["Model"] = None, light: List["Light"] = None):
        super().__init__(model=model, light=light)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Insertions":
        _base = _PrevInsertions.from_sdf(el)
        return cls(model=_base.model, light=_base.light)
