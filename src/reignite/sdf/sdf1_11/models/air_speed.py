from __future__ import annotations

from xml.etree import ElementTree as ET

from .pressure import Pressure
from ...sdf1_10.models.air_speed import AirSpeed as _PrevAirSpeed


class AirSpeed(_PrevAirSpeed):
    def __init__(self, pressure: "Pressure" = None):
        super().__init__(pressure=pressure)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AirSpeed":
        _base = _PrevAirSpeed.from_sdf(el)
        return cls(pressure=_base.pressure)
