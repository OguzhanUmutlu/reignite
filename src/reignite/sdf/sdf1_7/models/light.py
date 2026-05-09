from __future__ import annotations

from xml.etree import ElementTree as ET

from .attenuation import Attenuation
from .cast_shadows import CastShadows
from .diffuse import Diffuse
from .direction import Direction
from .pose import Pose
from .specular import Specular
from .spot import Spot
from ...sdf1_6.models.light import Light as _PrevLight


class Light(_PrevLight):
    def __init__(
            self,
            name: str = "__default__",
            type: str = "point",
            pose: "Pose" = None,
            cast_shadows: "CastShadows" = None,
            diffuse: "Diffuse" = None,
            specular: "Specular" = None,
            attenuation: "Attenuation" = None,
            direction: "Direction" = None,
            spot: "Spot" = None
    ):
        super().__init__(name=name, type=type, pose=pose, cast_shadows=cast_shadows, diffuse=diffuse, specular=specular,
                         attenuation=attenuation, direction=direction, spot=spot)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Light":
        _base = _PrevLight.from_sdf(el)
        return cls(name=_base.name, type=_base.type, pose=_base.pose, cast_shadows=_base.cast_shadows,
                   diffuse=_base.diffuse, specular=_base.specular, attenuation=_base.attenuation,
                   direction=_base.direction, spot=_base.spot)
