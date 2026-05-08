from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_6.models.texture import Texture as _PrevTexture
from .size import Size
from .diffuse import Diffuse
from .normal import Normal


class Texture(_PrevTexture):
    def __init__(self, size: "Size" = None, diffuse: "Diffuse" = None, normal: "Normal" = None):
        super().__init__(size=size, diffuse=diffuse, normal=normal)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Texture":
        _base = _PrevTexture.from_sdf(el)
        return cls(size=_base.size, diffuse=_base.diffuse, normal=_base.normal)
