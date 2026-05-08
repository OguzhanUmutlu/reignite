from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class CollisionState(Model):
    def __init__(self, name: str = "__default__"):
        self.name = name

    def to_sdf(self) -> ET.Element:
        el = ET.Element("collision_state")
        if self.name is not None:
            el.set("name", self.name)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CollisionState":
        _name = el.get("name", "__default__")
        return cls(name=_name)
