from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.color import Color
from ....utils.pose import Pose
from .attenuation import Attenuation
from .direction import Direction
from .spot import Spot


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


class Pose(Model):
    def __init__(self, pose: Pose = None):
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        self.pose = pose

    def to_sdf(self) -> ET.Element:
        el = ET.Element("pose")
        if self.pose is not None:
            el.text = self.pose.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pose":
        _text = el.text or "0 0 0 0 0 0"
        _pose = Pose.from_sdf(_text)
        return cls(pose=_pose)


class Diffuse(Model):
    def __init__(self, diffuse: Color = None):
        if diffuse is None:
            diffuse = Color.from_sdf("1 1 1 1")
        self.diffuse = diffuse

    def to_sdf(self) -> ET.Element:
        el = ET.Element("diffuse")
        if self.diffuse is not None:
            el.text = self.diffuse.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Diffuse":
        _text = el.text or "1 1 1 1"
        _diffuse = Color.from_sdf(_text)
        return cls(diffuse=_diffuse)


class Specular(Model):
    def __init__(self, specular: Color = None):
        if specular is None:
            specular = Color.from_sdf(".1 .1 .1 1")
        self.specular = specular

    def to_sdf(self) -> ET.Element:
        el = ET.Element("specular")
        if self.specular is not None:
            el.text = self.specular.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Specular":
        _text = el.text or ".1 .1 .1 1"
        _specular = Color.from_sdf(_text)
        return cls(specular=_specular)


class Light(Model):
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
        self.name = name
        self.type = type
        self.cast_shadows = cast_shadows
        self.pose = pose
        self.diffuse = diffuse
        self.specular = specular
        self.attenuation = attenuation
        self.direction = direction
        self.spot = spot

    def to_sdf(self) -> ET.Element:
        el = ET.Element("light")
        if self.name is not None:
            el.set("name", self.name)
        if self.type is not None:
            el.set("type", self.type)
        if self.cast_shadows is not None:
            el.append(self.cast_shadows.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.diffuse is not None:
            el.append(self.diffuse.to_sdf())
        if self.specular is not None:
            el.append(self.specular.to_sdf())
        if self.attenuation is not None:
            el.append(self.attenuation.to_sdf())
        if self.direction is not None:
            el.append(self.direction.to_sdf())
        if self.spot is not None:
            el.append(self.spot.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Light":
        _name = el.get("name", "__default__")
        _type = el.get("type", "point")
        _c_cast_shadows = el.find("cast_shadows")
        _cast_shadows = CastShadows.from_sdf(_c_cast_shadows) if _c_cast_shadows is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_diffuse = el.find("diffuse")
        _diffuse = Diffuse.from_sdf(_c_diffuse) if _c_diffuse is not None else None
        _c_specular = el.find("specular")
        _specular = Specular.from_sdf(_c_specular) if _c_specular is not None else None
        _c_attenuation = el.find("attenuation")
        _attenuation = Attenuation.from_sdf(_c_attenuation) if _c_attenuation is not None else None
        _c_direction = el.find("direction")
        _direction = Direction.from_sdf(_c_direction) if _c_direction is not None else None
        _c_spot = el.find("spot")
        _spot = Spot.from_sdf(_c_spot) if _c_spot is not None else None
        return cls(name=_name, type=_type, cast_shadows=_cast_shadows, pose=_pose, diffuse=_diffuse, specular=_specular, attenuation=_attenuation, direction=_direction, spot=_spot)
