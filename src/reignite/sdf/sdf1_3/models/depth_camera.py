from __future__ import annotations

from xml.etree import ElementTree as ET

from .output import Output
from ...sdf1_2.models.depth_camera import DepthCamera as _PrevDepthCamera


class DepthCamera(_PrevDepthCamera):
    def __init__(self, output: "Output" = None):
        super().__init__(output=output)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "DepthCamera":
        _base = _PrevDepthCamera.from_sdf(el)
        return cls(output=_base.output)
