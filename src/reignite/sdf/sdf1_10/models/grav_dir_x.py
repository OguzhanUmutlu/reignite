from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_9.models.grav_dir_x import GravDirX as _PrevGravDirX
from ....utils.vector3 import Vector3


class GravDirX(_PrevGravDirX):
    def __init__(self, grav_dir_x: Vector3 = None, parent_frame: str = ""):
        if grav_dir_x is None:
            grav_dir_x = Vector3.from_sdf("1 0 0")
        super().__init__(grav_dir_x=grav_dir_x, parent_frame=parent_frame)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "GravDirX":
        _base = _PrevGravDirX.from_sdf(el)
        return cls(grav_dir_x=_base.grav_dir_x, parent_frame=_base.parent_frame)
