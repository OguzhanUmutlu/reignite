from __future__ import annotations

from xml.etree import ElementTree as ET

from .sky import Sky
from ..model import Model
from ....utils.color import Color


class Background(Model):
    def __init__(self, rgba: Color = None, sky: "Sky" = None):
        if rgba is None:
            rgba = Color.from_sdf(".7 .7 .7 1")
        self.rgba = rgba
        self.sky = sky

    def to_sdf(self) -> ET.Element:
        el = ET.Element("background")
        if self.rgba is not None:
            el.set("rgba", self.rgba.to_sdf())
        if self.sky is not None:
            el.append(self.sky.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Background":
        _rgba = Color.from_sdf(el.get("rgba", ".7 .7 .7 1"))
        _c_sky = el.find("sky")
        _sky = Sky.from_sdf(_c_sky) if _c_sky is not None else None
        return cls(rgba=_rgba, sky=_sky)
