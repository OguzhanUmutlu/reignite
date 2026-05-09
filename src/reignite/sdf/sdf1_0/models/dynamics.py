from __future__ import annotations

import math
from xml.etree import ElementTree as ET

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


class Dynamics(Model):
    def __init__(self, damping: float = 0, friction: float = 0):
        self.damping = damping
        self.friction = friction

    def to_sdf(self) -> ET.Element:
        el = ET.Element("dynamics")
        if self.damping is not None:
            el.set("damping", str(self.damping))
        if self.friction is not None:
            el.set("friction", str(self.friction))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Dynamics":
        _damping = _parse_double(el.get("damping", 0))
        _friction = _parse_double(el.get("friction", 0))
        return cls(damping=_damping, friction=_friction)
