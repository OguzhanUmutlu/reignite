from __future__ import annotations

from xml.etree import ElementTree as ET

from .voltage import Voltage
from ...sdf1_5.models.battery import Battery as _PrevBattery


class Battery(_PrevBattery):
    def __init__(self, name: str = "__default__", voltage: "Voltage" = None):
        super().__init__(name=name, voltage=voltage)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Battery":
        _base = _PrevBattery.from_sdf(el)
        return cls(name=_base.name, voltage=_base.voltage)
