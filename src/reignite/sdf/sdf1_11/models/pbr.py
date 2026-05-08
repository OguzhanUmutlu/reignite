from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_10.models.pbr import Pbr as _PrevPbr
from .metal import Metal
from .specular import Specular


class Pbr(_PrevPbr):
    def __init__(self, metal: "Metal" = None, specular: "Specular" = None):
        super().__init__(metal=metal, specular=specular)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pbr":
        _base = _PrevPbr.from_sdf(el)
        return cls(metal=_base.metal, specular=_base.specular)
