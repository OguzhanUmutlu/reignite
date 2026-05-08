from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_11.models.custom_rpy import CustomRpy as _PrevCustomRpy
from ....utils.vector3 import Vector3


class CustomRpy(_PrevCustomRpy):
    def __init__(self, custom_rpy: Vector3 = None, parent_frame: str = ""):
        if custom_rpy is None:
            custom_rpy = Vector3.from_sdf("0 0 0")
        super().__init__(custom_rpy=custom_rpy, parent_frame=parent_frame)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CustomRpy":
        _base = _PrevCustomRpy.from_sdf(el)
        return cls(custom_rpy=_base.custom_rpy, parent_frame=_base.parent_frame)
