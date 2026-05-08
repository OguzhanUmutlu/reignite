from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class CollisionDetector(Model):
    def __init__(self, collision_detector: str = "fcl"):
        self.collision_detector = collision_detector

    def to_sdf(self) -> ET.Element:
        el = ET.Element("collision_detector")
        if self.collision_detector is not None:
            el.text = self.collision_detector
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CollisionDetector":
        _text = el.text or "fcl"
        _collision_detector = _text
        return cls(collision_detector=_collision_detector)
