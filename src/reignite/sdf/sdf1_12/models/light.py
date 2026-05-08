from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_11.models.light import Light as _PrevLight
from .pose import Pose
from .cast_shadows import CastShadows
from .light_on import LightOn
from .visualize import Visualize
from .intensity import Intensity
from .diffuse import Diffuse
from .specular import Specular
from .attenuation import Attenuation
from .direction import Direction
from .spot import Spot


class Light(_PrevLight):
    def __init__(
        self,
        name: str = "__default__",
        type: str = "point",
        pose: "Pose" = None,
        cast_shadows: "CastShadows" = None,
        light_on: "LightOn" = None,
        visualize: "Visualize" = None,
        intensity: "Intensity" = None,
        diffuse: "Diffuse" = None,
        specular: "Specular" = None,
        attenuation: "Attenuation" = None,
        direction: "Direction" = None,
        spot: "Spot" = None
    ):
        super().__init__(name=name, type=type, pose=pose, cast_shadows=cast_shadows, light_on=light_on, visualize=visualize, intensity=intensity, diffuse=diffuse, specular=specular, attenuation=attenuation, direction=direction, spot=spot)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Light":
        _base = _PrevLight.from_sdf(el)
        return cls(name=_base.name, type=_base.type, pose=_base.pose, cast_shadows=_base.cast_shadows, light_on=_base.light_on, visualize=_base.visualize, intensity=_base.intensity, diffuse=_base.diffuse, specular=_base.specular, attenuation=_base.attenuation, direction=_base.direction, spot=_base.spot)
