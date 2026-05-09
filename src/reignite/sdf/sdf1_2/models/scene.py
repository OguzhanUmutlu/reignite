from __future__ import annotations

from xml.etree import ElementTree as ET

from .background import Background
from .fog import Fog
from .grid import Grid
from .shadows import Shadows
from .sky import Sky
from ...sdf1_0.models.ambient import Ambient as _PrevAmbient
from ...sdf1_0.models.scene import Scene as _PrevScene
from ....utils.color import Color


class Ambient(_PrevAmbient):
    def __init__(self, ambient: Color = None):
        if ambient is None:
            ambient = Color.from_sdf("0.0 0.0 0.0 1.0")
        super().__init__()
        self.ambient = ambient

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.ambient is not None:
            el.text = self.ambient.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ambient":
        _text = el.text or "0.0 0.0 0.0 1.0"
        _ambient = Color.from_sdf(_text)
        return cls(ambient=_ambient)


class Scene(_PrevScene):
    def __init__(
            self,
            ambient: "Ambient" = None,
            background: "Background" = None,
            sky: "Sky" = None,
            shadows: "Shadows" = None,
            fog: "Fog" = None,
            grid: "Grid" = None
    ):
        super().__init__(ambient=ambient, background=background, shadows=shadows, fog=fog, grid=grid)
        self.sky = sky

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.sky is not None:
            el.append(self.sky.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Scene":
        _base = _PrevScene.from_sdf(el)
        _c_sky = el.find("sky")
        _sky = Sky.from_sdf(_c_sky) if _c_sky is not None else None
        return cls(ambient=_base.ambient, background=_base.background, sky=_sky, shadows=_base.shadows, fog=_base.fog,
                   grid=_base.grid)
