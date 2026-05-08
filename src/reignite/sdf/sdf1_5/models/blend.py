from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_4.models.blend import Blend as _PrevBlend
from .min_height import MinHeight
from .fade_dist import FadeDist


class Blend(_PrevBlend):
    def __init__(self, min_height: "MinHeight" = None, fade_dist: "FadeDist" = None):
        super().__init__(min_height=min_height, fade_dist=fade_dist)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Blend":
        _base = _PrevBlend.from_sdf(el)
        return cls(min_height=_base.min_height, fade_dist=_base.fade_dist)
