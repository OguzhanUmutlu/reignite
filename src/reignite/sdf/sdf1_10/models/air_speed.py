from __future__ import annotations

from xml.etree import ElementTree as ET

from .pressure import Pressure
from ..model import Model


class AirSpeed(Model):
    def __init__(self, pressure: "Pressure" = None):
        self.pressure = pressure

    def to_sdf(self) -> ET.Element:
        el = ET.Element("air_speed")
        if self.pressure is not None:
            el.append(self.pressure.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AirSpeed":
        _c_pressure = el.find("pressure")
        _pressure = Pressure.from_sdf(_c_pressure) if _c_pressure is not None else None
        return cls(pressure=_pressure)
