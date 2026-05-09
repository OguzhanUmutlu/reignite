from __future__ import annotations

from xml.etree import ElementTree as ET

from .background import Background
from .fog import Fog
from .grid import Grid
from .origin_visual import OriginVisual
from .shadows import Shadows
from .sky import Sky
from ...sdf1_4.models.ambient import Ambient as _PrevAmbient
from ...sdf1_4.models.scene import Scene as _PrevScene
from ....utils.color import Color


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
        super().__init__(ambient=ambient, background=background, sky=sky, shadows=shadows, fog=fog, grid=grid)
        self.origin_visual = origin_visual

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.origin_visual is not None:
            el.append(self.origin_visual.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Scene":
        _base = _PrevScene.from_sdf(el)
        _c_origin_visual = el.find("origin_visual")
        _origin_visual = OriginVisual.from_sdf(_c_origin_visual) if _c_origin_visual is not None else None
        return cls(ambient=_base.ambient, background=_base.background, sky=_base.sky, shadows=_base.shadows,
                   fog=_base.fog, grid=_base.grid, origin_visual=_origin_visual)
