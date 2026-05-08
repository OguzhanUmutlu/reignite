from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.vector3 import Vector3


class Scale(Model):
    def __init__(self, scale: Vector3 = None):
        if scale is None:
            scale = Vector3.from_sdf("1 1 1")
        self.scale = scale

    def to_sdf(self) -> ET.Element:
        el = ET.Element("scale")
        if self.scale is not None:
            el.text = self.scale.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Scale":
        _text = el.text or "1 1 1"
        _scale = Vector3.from_sdf(_text)
        return cls(scale=_scale)
