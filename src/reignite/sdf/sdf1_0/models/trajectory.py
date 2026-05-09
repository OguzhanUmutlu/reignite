from __future__ import annotations

import math
from typing import List
from xml.etree import ElementTree as ET

from .waypoint import Waypoint
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


class Trajectory(Model):
    def __init__(self, id: int = 0, type: str = "__default__", waypoint: List["Waypoint"] = None):
        self.id = id
        self.type = type
        self.waypoint = waypoint or []

    def to_sdf(self) -> ET.Element:
        el = ET.Element("trajectory")
        if self.id is not None:
            el.set("id", str(self.id))
        if self.type is not None:
            el.set("type", self.type)
        for item in (self.waypoint or []):
            el.append(item.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Trajectory":
        _id = _parse_int32(el.get("id", 0))
        _type = el.get("type", "__default__")
        _waypoint = [Waypoint.from_sdf(c) for c in el.findall("waypoint")]
        return cls(id=_id, type=_type, waypoint=_waypoint)
