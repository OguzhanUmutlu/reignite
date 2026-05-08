from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_11.models.collide_without_contact import CollideWithoutContact as _PrevCollideWithoutContact


class CollideWithoutContact(_PrevCollideWithoutContact):
    def __init__(self, collide_without_contact: bool = False):
        super().__init__(collide_without_contact=collide_without_contact)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CollideWithoutContact":
        _base = _PrevCollideWithoutContact.from_sdf(el)
        return cls(collide_without_contact=_base.collide_without_contact)
