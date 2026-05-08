from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.vector3 import Vector3


class CustomRpy(Model):
    def __init__(self, custom_rpy: Vector3 = None, parent_frame: str = ""):
        if custom_rpy is None:
            custom_rpy = Vector3.from_sdf("0 0 0")
        self.custom_rpy = custom_rpy
        self.parent_frame = parent_frame

    def to_sdf(self) -> ET.Element:
        el = ET.Element("custom_rpy")
        if self.custom_rpy is not None:
            el.text = self.custom_rpy.to_sdf()
        if self.parent_frame is not None:
            el.set("parent_frame", self.parent_frame)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CustomRpy":
        _text = el.text or "0 0 0"
        _custom_rpy = Vector3.from_sdf(_text)
        _parent_frame = el.get("parent_frame", "")
        return cls(custom_rpy=_custom_rpy, parent_frame=_parent_frame)
