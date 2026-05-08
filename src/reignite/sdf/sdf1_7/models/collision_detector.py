from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_6.models.collision_detector import CollisionDetector as _PrevCollisionDetector


class CollisionDetector(_PrevCollisionDetector):
    def __init__(self, collision_detector: str = "fcl"):
        super().__init__(collision_detector=collision_detector)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CollisionDetector":
        _base = _PrevCollisionDetector.from_sdf(el)
        return cls(collision_detector=_base.collision_detector)
