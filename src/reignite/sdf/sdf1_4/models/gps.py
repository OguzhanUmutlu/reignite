from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .position_sensing import PositionSensing
from .velocity_sensing import VelocitySensing


class Gps(Model):
    def __init__(
        self,
        position_sensing: "PositionSensing" = None,
        velocity_sensing: "VelocitySensing" = None
    ):
        self.position_sensing = position_sensing
        self.velocity_sensing = velocity_sensing

    def to_sdf(self) -> ET.Element:
        el = ET.Element("gps")
        if self.position_sensing is not None:
            el.append(self.position_sensing.to_sdf())
        if self.velocity_sensing is not None:
            el.append(self.velocity_sensing.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Gps":
        _c_position_sensing = el.find("position_sensing")
        _position_sensing = PositionSensing.from_sdf(_c_position_sensing) if _c_position_sensing is not None else None
        _c_velocity_sensing = el.find("velocity_sensing")
        _velocity_sensing = VelocitySensing.from_sdf(_c_velocity_sensing) if _c_velocity_sensing is not None else None
        return cls(position_sensing=_position_sensing, velocity_sensing=_velocity_sensing)
