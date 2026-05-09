from __future__ import annotations

import math
from xml.etree import ElementTree as ET

from .acceleration import Acceleration
from .position import Position
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


class Velocity(Model):
    def __init__(self, velocity: float = 0, degrees: bool = False):
        self.velocity = velocity
        self.degrees = degrees

    def to_sdf(self) -> ET.Element:
        el = ET.Element("velocity")
        if self.velocity is not None:
            el.text = str(self.velocity)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Velocity":
        _text = el.text or 0
        _velocity = _parse_double(_text)
        _degrees = el.get("degrees", False).strip().lower() == 'true'
        return cls(velocity=_velocity, degrees=_degrees)


class Effort(Model):
    def __init__(self, effort: float = 0):
        self.effort = effort

    def to_sdf(self) -> ET.Element:
        el = ET.Element("effort")
        if self.effort is not None:
            el.text = str(self.effort)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Effort":
        _text = el.text or 0
        _effort = _parse_double(_text)
        return cls(effort=_effort)


class AxisState(Model):
    def __init__(
            self,
            position: "Position" = None,
            velocity: "Velocity" = None,
            acceleration: "Acceleration" = None,
            effort: "Effort" = None
    ):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.effort = effort

    def to_sdf(self) -> ET.Element:
        el = ET.Element("axis_state")
        if self.position is not None:
            el.append(self.position.to_sdf())
        if self.velocity is not None:
            el.append(self.velocity.to_sdf())
        if self.acceleration is not None:
            el.append(self.acceleration.to_sdf())
        if self.effort is not None:
            el.append(self.effort.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AxisState":
        _c_position = el.find("position")
        _position = Position.from_sdf(_c_position) if _c_position is not None else None
        _c_velocity = el.find("velocity")
        _velocity = Velocity.from_sdf(_c_velocity) if _c_velocity is not None else None
        _c_acceleration = el.find("acceleration")
        _acceleration = Acceleration.from_sdf(_c_acceleration) if _c_acceleration is not None else None
        _c_effort = el.find("effort")
        _effort = Effort.from_sdf(_c_effort) if _c_effort is not None else None
        return cls(position=_position, velocity=_velocity, acceleration=_acceleration, effort=_effort)
