from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_6.models.self_collide import SelfCollide as _PrevSelfCollide


class SelfCollide(_PrevSelfCollide):
    def __init__(self, self_collide: bool = False):
        super().__init__(self_collide=self_collide)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SelfCollide":
        _base = _PrevSelfCollide.from_sdf(el)
        return cls(self_collide=_base.self_collide)
