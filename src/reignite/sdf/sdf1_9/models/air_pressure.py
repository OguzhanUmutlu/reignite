from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_8.models.air_pressure import AirPressure as _PrevAirPressure
from .reference_altitude import ReferenceAltitude
from .pressure import Pressure


class AirPressure(_PrevAirPressure):
    def __init__(self, reference_altitude: "ReferenceAltitude" = None, pressure: "Pressure" = None):
        super().__init__(reference_altitude=reference_altitude, pressure=pressure)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AirPressure":
        _base = _PrevAirPressure.from_sdf(el)
        return cls(reference_altitude=_base.reference_altitude, pressure=_base.pressure)
