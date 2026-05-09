from __future__ import annotations

from xml.etree import ElementTree as ET

from .background import Background
from .fog import Fog
from .grid import Grid
from .shadows import Shadows
from ..model import Model
from ....utils.color import Color


class Ambient(Model):
    def __init__(self, rgba: Color = None):
        if rgba is None:
            rgba = Color.from_sdf("0.0 0.0 0.0 1.0")
        self.rgba = rgba

    def to_sdf(self) -> ET.Element:
        el = ET.Element("ambient")
        if self.rgba is not None:
            el.set("rgba", self.rgba.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ambient":
        _rgba = Color.from_sdf(el.get("rgba", "0.0 0.0 0.0 1.0"))
        return cls(rgba=_rgba)


class Scene(Model):
    def __init__(
            self,
            ambient: "Ambient" = None,
            background: "Background" = None,
            shadows: "Shadows" = None,
            fog: "Fog" = None,
            grid: "Grid" = None
    ):
        self.ambient = ambient
        self.background = background
        self.shadows = shadows
        self.fog = fog
        self.grid = grid

    def to_sdf(self) -> ET.Element:
        el = ET.Element("scene")
        if self.ambient is not None:
            el.append(self.ambient.to_sdf())
        if self.background is not None:
            el.append(self.background.to_sdf())
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
        _c_shadows = el.find("shadows")
        _shadows = Shadows.from_sdf(_c_shadows) if _c_shadows is not None else None
        _c_fog = el.find("fog")
        _fog = Fog.from_sdf(_c_fog) if _c_fog is not None else None
        _c_grid = el.find("grid")
        _grid = Grid.from_sdf(_c_grid) if _c_grid is not None else None
        return cls(ambient=_ambient, background=_background, shadows=_shadows, fog=_fog, grid=_grid)
