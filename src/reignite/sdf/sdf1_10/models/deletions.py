from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .name import Name
from ...sdf1_9.models.deletions import Deletions as _PrevDeletions


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
