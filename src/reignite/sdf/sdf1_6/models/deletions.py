from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_5.models.deletions import Deletions as _PrevDeletions
from .name import Name


class Deletions(_PrevDeletions):
    def __init__(self, name: List["Name"] = None):
        super().__init__(name=name)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Deletions":
        _base = _PrevDeletions.from_sdf(el)
        return cls(name=_base.name)
