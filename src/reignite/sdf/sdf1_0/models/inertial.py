from __future__ import annotations

import math
from xml.etree import ElementTree as ET

from .inertia import Inertia
from .origin import Origin
from ..model import Model


def _parse_int32(raw: str) -> int:
    v = int(raw)
    if not (-2147483648 <= v <= 2147483647):
        raise ValueError(f"int32 out of range: {v}")
    return v


def _parse_uint32(raw: str) -> int:
    v = int(raw)
    if not (0 <= v <= 4294967295):
        raise ValueError(f"uint32 out of range: {v}")
    return v


def _parse_double(raw: str) -> float:
    v = float(raw)
    if not math.isfinite(v) or abs(v) > 1.7976931348623157e+308:
        raise ValueError(f"double out of range: {raw}")
    return v


class Inertial(Model):
    def __init__(
            self,
            mass: float = 1.0,
            density: float = 1.0,
            origin: "Origin" = None,
            inertia: "Inertia" = None
    ):
        self.mass = mass
        self.density = density
        self.origin = origin
        self.inertia = inertia

    def to_sdf(self) -> ET.Element:
        el = ET.Element("inertial")
        if self.mass is not None:
            el.set("mass", str(self.mass))
        if self.density is not None:
            el.set("density", str(self.density))
        if self.origin is not None:
            el.append(self.origin.to_sdf())
        if self.inertia is not None:
            el.append(self.inertia.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Inertial":
        _mass = _parse_double(el.get("mass", 1.0))
        _density = _parse_double(el.get("density", 1.0))
        _c_origin = el.find("origin")
        _origin = Origin.from_sdf(_c_origin) if _c_origin is not None else None
        _c_inertia = el.find("inertia")
        _inertia = Inertia.from_sdf(_c_inertia) if _c_inertia is not None else None
        return cls(mass=_mass, density=_density, origin=_origin, inertia=_inertia)
