from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .min_height import MinHeight
from .fade_dist import FadeDist


class Blend(Model):
    def __init__(self, min_height: "MinHeight" = None, fade_dist: "FadeDist" = None):
        self.min_height = min_height
        self.fade_dist = fade_dist

    def to_sdf(self) -> ET.Element:
        el = ET.Element("blend")
        if self.min_height is not None:
            el.append(self.min_height.to_sdf())
        if self.fade_dist is not None:
            el.append(self.fade_dist.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Blend":
        _c_min_height = el.find("min_height")
        _min_height = MinHeight.from_sdf(_c_min_height) if _c_min_height is not None else None
        _c_fade_dist = el.find("fade_dist")
        _fade_dist = FadeDist.from_sdf(_c_fade_dist) if _c_fade_dist is not None else None
        return cls(min_height=_min_height, fade_dist=_fade_dist)
