from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.vector3 import Vector3


class GravDirX(Model):
    def __init__(self, grav_dir_x: Vector3 = None, parent_frame: str = ""):
        if grav_dir_x is None:
            grav_dir_x = Vector3.from_sdf("1 0 0")
        self.grav_dir_x = grav_dir_x
        self.parent_frame = parent_frame

    def to_sdf(self) -> ET.Element:
        el = ET.Element("grav_dir_x")
        if self.grav_dir_x is not None:
            el.text = self.grav_dir_x.to_sdf()
        if self.parent_frame is not None:
            el.set("parent_frame", self.parent_frame)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "GravDirX":
        _text = el.text or "1 0 0"
        _grav_dir_x = Vector3.from_sdf(_text)
        _parent_frame = el.get("parent_frame", "")
        return cls(grav_dir_x=_grav_dir_x, parent_frame=_parent_frame)
