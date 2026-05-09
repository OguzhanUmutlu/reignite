from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .attenuation import Attenuation
from .cast_shadows import CastShadows
from .diffuse import Diffuse
from .direction import Direction
from .frame import Frame
from .pose import Pose
from .specular import Specular
from .spot import Spot
from ..model import Model


class Light(Model):
    def __init__(
            self,
            name: str = "__default__",
            type: str = "point",
            frame: List["Frame"] = None,
            pose: "Pose" = None,
            cast_shadows: "CastShadows" = None,
            diffuse: "Diffuse" = None,
            specular: "Specular" = None,
            attenuation: "Attenuation" = None,
            direction: "Direction" = None,
            spot: "Spot" = None
    ):
        self.name = name
        self.type = type
        self.frame = frame or []
        self.pose = pose
        self.cast_shadows = cast_shadows
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
        for item in (self.frame or []):
            el.append(item.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.cast_shadows is not None:
            el.append(self.cast_shadows.to_sdf())
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
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_cast_shadows = el.find("cast_shadows")
        _cast_shadows = CastShadows.from_sdf(_c_cast_shadows) if _c_cast_shadows is not None else None
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
        return cls(name=_name, type=_type, frame=_frame, pose=_pose, cast_shadows=_cast_shadows, diffuse=_diffuse,
                   specular=_specular, attenuation=_attenuation, direction=_direction, spot=_spot)
