from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_9.models.ambient import Ambient as _PrevAmbient
from ...sdf1_9.models.scene import Scene as _PrevScene
from ....utils.color import Color
from .background import Background
from .sky import Sky
from .shadows import Shadows
from .fog import Fog
from .grid import Grid
from .origin_visual import OriginVisual


class Ambient(_PrevAmbient):
    def __init__(self, ambient: Color = None):
        if ambient is None:
            ambient = Color.from_sdf("0.4 0.4 0.4 1.0")
        super().__init__(ambient=ambient)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ambient":
        _base = _PrevAmbient.from_sdf(el)
        return cls(ambient=_base.ambient)


class Scene(_PrevScene):
    def __init__(
        self,
        ambient: "Ambient" = None,
        background: "Background" = None,
        sky: "Sky" = None,
        shadows: "Shadows" = None,
        fog: "Fog" = None,
        grid: "Grid" = None,
        origin_visual: "OriginVisual" = None
    ):
        super().__init__(ambient=ambient, background=background, sky=sky, shadows=shadows, fog=fog, grid=grid, origin_visual=origin_visual)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Scene":
        _base = _PrevScene.from_sdf(el)
        return cls(ambient=_base.ambient, background=_base.background, sky=_base.sky, shadows=_base.shadows, fog=_base.fog, grid=_base.grid, origin_visual=_base.origin_visual)
