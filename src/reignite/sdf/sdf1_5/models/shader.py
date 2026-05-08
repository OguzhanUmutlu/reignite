from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_4.models.shader import Shader as _PrevShader
from .normal_map import NormalMap


class Shader(_PrevShader):
    def __init__(self, type: str = "pixel", normal_map: "NormalMap" = None):
        super().__init__(type=type, normal_map=normal_map)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Shader":
        _base = _PrevShader.from_sdf(el)
        return cls(type=_base.type, normal_map=_base.normal_map)
