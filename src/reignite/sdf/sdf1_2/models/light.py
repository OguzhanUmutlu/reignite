from __future__ import annotations

from xml.etree import ElementTree as ET

from .attenuation import Attenuation
from .direction import Direction
from .pose import Pose
from .spot import Spot
from ..model import Model
from ...sdf1_0.models.diffuse import Diffuse as _PrevDiffuse
from ...sdf1_0.models.light import Light as _PrevLight
from ...sdf1_0.models.specular import Specular as _PrevSpecular
from ....utils.color import Color


class CastShadows(Model):
    def __init__(self, cast_shadows: bool = False):
        self.cast_shadows = cast_shadows

    def to_sdf(self) -> ET.Element:
        el = ET.Element("cast_shadows")
        if self.cast_shadows is not None:
            el.text = str(self.cast_shadows).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CastShadows":
        _text = el.text or False
        _cast_shadows = _text.strip().lower() == 'true'
        return cls(cast_shadows=_cast_shadows)


class Diffuse(_PrevDiffuse):
    def __init__(self, diffuse: Color = None):
        if diffuse is None:
            diffuse = Color.from_sdf("1 1 1 1")
        super().__init__()
        self.diffuse = diffuse

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.diffuse is not None:
            el.text = self.diffuse.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Diffuse":
        _text = el.text or "1 1 1 1"
        _diffuse = Color.from_sdf(_text)
        return cls(diffuse=_diffuse)


class Specular(_PrevSpecular):
    def __init__(self, specular: Color = None):
        if specular is None:
            specular = Color.from_sdf(".1 .1 .1 1")
        super().__init__()
        self.specular = specular

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.specular is not None:
            el.text = self.specular.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Specular":
        _text = el.text or ".1 .1 .1 1"
        _specular = Color.from_sdf(_text)
        return cls(specular=_specular)


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
        super().__init__(name=name, type=type, cast_shadows=cast_shadows, diffuse=diffuse, specular=specular,
                         attenuation=attenuation, direction=direction, spot=spot)
        self.pose = pose

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Light":
        _base = _PrevLight.from_sdf(el)
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        return cls(name=_base.name, type=_base.type, cast_shadows=_base.cast_shadows, pose=_pose, diffuse=_base.diffuse,
                   specular=_base.specular, attenuation=_base.attenuation, direction=_base.direction, spot=_base.spot)
