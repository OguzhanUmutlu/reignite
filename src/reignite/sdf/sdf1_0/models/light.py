from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.color import Color
from .origin import Origin
from .attenuation import Attenuation
from .direction import Direction
from .spot import Spot


class Diffuse(Model):
    def __init__(self, rgba: Color = None):
        if rgba is None:
            rgba = Color.from_sdf("1 1 1 1")
        self.rgba = rgba

    def to_sdf(self) -> ET.Element:
        el = ET.Element("diffuse")
        if self.rgba is not None:
            el.set("rgba", self.rgba.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Diffuse":
        _rgba = Color.from_sdf(el.get("rgba", "1 1 1 1"))
        return cls(rgba=_rgba)


class Specular(Model):
    def __init__(self, rgba: Color = None):
        if rgba is None:
            rgba = Color.from_sdf(".1 .1 .1 1")
        self.rgba = rgba

    def to_sdf(self) -> ET.Element:
        el = ET.Element("specular")
        if self.rgba is not None:
            el.set("rgba", self.rgba.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Specular":
        _rgba = Color.from_sdf(el.get("rgba", ".1 .1 .1 1"))
        return cls(rgba=_rgba)


class Light(Model):
    def __init__(
        self,
        name: str = "__default__",
        type: str = "point",
        cast_shadows: bool = False,
        origin: "Origin" = None,
        diffuse: "Diffuse" = None,
        specular: "Specular" = None,
        attenuation: "Attenuation" = None,
        direction: "Direction" = None,
        spot: "Spot" = None
    ):
        self.name = name
        self.type = type
        self.cast_shadows = cast_shadows
        self.origin = origin
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
            el.set("cast_shadows", str(self.cast_shadows).lower())
        if self.origin is not None:
            el.append(self.origin.to_sdf())
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
        _cast_shadows = el.get("cast_shadows", False).strip().lower() == 'true'
        _c_origin = el.find("origin")
        _origin = Origin.from_sdf(_c_origin) if _c_origin is not None else None
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
        return cls(name=_name, type=_type, cast_shadows=_cast_shadows, origin=_origin, diffuse=_diffuse, specular=_specular, attenuation=_attenuation, direction=_direction, spot=_spot)
