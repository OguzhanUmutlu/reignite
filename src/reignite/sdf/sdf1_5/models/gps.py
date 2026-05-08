from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_4.models.gps import Gps as _PrevGps
from .position_sensing import PositionSensing
from .velocity_sensing import VelocitySensing


class Gps(_PrevGps):
    def __init__(
        self,
        position_sensing: "PositionSensing" = None,
        velocity_sensing: "VelocitySensing" = None
    ):
        super().__init__(position_sensing=position_sensing, velocity_sensing=velocity_sensing)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Gps":
        _base = _PrevGps.from_sdf(el)
        return cls(position_sensing=_base.position_sensing, velocity_sensing=_base.velocity_sensing)
