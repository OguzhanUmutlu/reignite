from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_3.models.cast_shadows import CastShadows as _PrevCastShadows
from ...sdf1_3.models.diffuse import Diffuse as _PrevDiffuse
from ...sdf1_3.models.specular import Specular as _PrevSpecular
from ...sdf1_3.models.light import Light as _PrevLight
from ....utils.color import Color
from .pose import Pose
from .attenuation import Attenuation
from .direction import Direction
from .spot import Spot


class CastShadows(_PrevCastShadows):
    def __init__(self, cast_shadows: bool = False):
        super().__init__(cast_shadows=cast_shadows)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CastShadows":
        _base = _PrevCastShadows.from_sdf(el)
        return cls(cast_shadows=_base.cast_shadows)


class Diffuse(_PrevDiffuse):
    def __init__(self, diffuse: Color = None):
        if diffuse is None:
            diffuse = Color.from_sdf("1 1 1 1")
        super().__init__(diffuse=diffuse)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Diffuse":
        _base = _PrevDiffuse.from_sdf(el)
        return cls(diffuse=_base.diffuse)


class Specular(_PrevSpecular):
    def __init__(self, specular: Color = None):
        if specular is None:
            specular = Color.from_sdf(".1 .1 .1 1")
        super().__init__(specular=specular)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Specular":
        _base = _PrevSpecular.from_sdf(el)
        return cls(specular=_base.specular)


class Light(_PrevLight):
    def __init__(
        self,
        name: str = "__default__",
        type: str = "point",
        cast_shadows: "CastShadows" = None,
        pose: "Pose" = None,
        diffuse: "Diffuse" = None,
        specular: "Specular" = None,
        attenuation: "Attenuation" = None,
        direction: "Direction" = None,
        spot: "Spot" = None
    ):
        super().__init__(name=name, type=type, cast_shadows=cast_shadows, pose=pose, diffuse=diffuse, specular=specular, attenuation=attenuation, direction=direction, spot=spot)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Light":
        _base = _PrevLight.from_sdf(el)
        return cls(name=_base.name, type=_base.type, cast_shadows=_base.cast_shadows, pose=_base.pose, diffuse=_base.diffuse, specular=_base.specular, attenuation=_base.attenuation, direction=_base.direction, spot=_base.spot)
