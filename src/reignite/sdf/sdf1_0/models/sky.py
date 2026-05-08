from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Sky(Model):
    def __init__(self, material: str = "Gazebo/CloudySky"):
        self.material = material

    def to_sdf(self) -> ET.Element:
        el = ET.Element("sky")
        if self.material is not None:
            el.set("material", self.material)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Sky":
        _material = el.get("material", "Gazebo/CloudySky")
        return cls(material=_material)
