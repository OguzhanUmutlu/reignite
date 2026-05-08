from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .reference_altitude import ReferenceAltitude
from .pressure import Pressure


class AirPressure(Model):
    def __init__(self, reference_altitude: "ReferenceAltitude" = None, pressure: "Pressure" = None):
        self.reference_altitude = reference_altitude
        self.pressure = pressure

    def to_sdf(self) -> ET.Element:
        el = ET.Element("air_pressure")
        if self.reference_altitude is not None:
            el.append(self.reference_altitude.to_sdf())
        if self.pressure is not None:
            el.append(self.pressure.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AirPressure":
        _c_reference_altitude = el.find("reference_altitude")
        _reference_altitude = ReferenceAltitude.from_sdf(_c_reference_altitude) if _c_reference_altitude is not None else None
        _c_pressure = el.find("pressure")
        _pressure = Pressure.from_sdf(_c_pressure) if _c_pressure is not None else None
        return cls(reference_altitude=_reference_altitude, pressure=_pressure)
