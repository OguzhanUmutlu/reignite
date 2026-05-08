from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_7.models.depth_camera import DepthCamera as _PrevDepthCamera
from .output import Output
from .clip import Clip


class DepthCamera(_PrevDepthCamera):
    def __init__(self, output: "Output" = None, clip: "Clip" = None):
        super().__init__(output=output, clip=clip)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "DepthCamera":
        _base = _PrevDepthCamera.from_sdf(el)
        return cls(output=_base.output, clip=_base.clip)
