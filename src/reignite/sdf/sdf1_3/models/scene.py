from __future__ import annotations

from xml.etree import ElementTree as ET

from .background import Background
from .fog import Fog
from .grid import Grid
from .shadows import Shadows
from .sky import Sky
from ..model import Model
from ....utils.color import Color


class Ambient(Model):
    def __init__(self, ambient: Color = None):
        if ambient is None:
            ambient = Color.from_sdf("0.2 0.2 0.2 1.0")
        self.ambient = ambient

    def to_sdf(self) -> ET.Element:
        el = ET.Element("ambient")
        if self.ambient is not None:
            el.text = self.ambient.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ambient":
        _text = el.text or "0.2 0.2 0.2 1.0"
        _ambient = Color.from_sdf(_text)
        return cls(ambient=_ambient)


class Scene(Model):
    def __init__(
            self,
            ambient: "Ambient" = None,
            background: "Background" = None,
            sky: "Sky" = None,
            shadows: "Shadows" = None,
            fog: "Fog" = None,
            grid: "Grid" = None
    ):
        self.ambient = ambient
        self.background = background
        self.sky = sky
        self.shadows = shadows
        self.fog = fog
        self.grid = grid

    def to_sdf(self) -> ET.Element:
        el = ET.Element("scene")
        if self.ambient is not None:
            el.append(self.ambient.to_sdf())
        if self.background is not None:
            el.append(self.background.to_sdf())
        if self.sky is not None:
            el.append(self.sky.to_sdf())
        if self.shadows is not None:
            el.append(self.shadows.to_sdf())
        if self.fog is not None:
            el.append(self.fog.to_sdf())
        if self.grid is not None:
            el.append(self.grid.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Scene":
        _c_ambient = el.find("ambient")
        _ambient = Ambient.from_sdf(_c_ambient) if _c_ambient is not None else None
        _c_background = el.find("background")
        _background = Background.from_sdf(_c_background) if _c_background is not None else None
        _c_sky = el.find("sky")
        _sky = Sky.from_sdf(_c_sky) if _c_sky is not None else None
        _c_shadows = el.find("shadows")
        _shadows = Shadows.from_sdf(_c_shadows) if _c_shadows is not None else None
        _c_fog = el.find("fog")
        _fog = Fog.from_sdf(_c_fog) if _c_fog is not None else None
        _c_grid = el.find("grid")
        _grid = Grid.from_sdf(_c_grid) if _c_grid is not None else None
        return cls(ambient=_ambient, background=_background, sky=_sky, shadows=_shadows, fog=_fog, grid=_grid)
