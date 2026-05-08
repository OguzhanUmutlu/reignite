from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .voltage import Voltage


class Battery(Model):
    def __init__(self, name: str = "__default__", voltage: "Voltage" = None):
        self.name = name
        self.voltage = voltage

    def to_sdf(self) -> ET.Element:
        el = ET.Element("battery")
        if self.name is not None:
            el.set("name", self.name)
        if self.voltage is not None:
            el.append(self.voltage.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Battery":
        _name = el.get("name", "__default__")
        _c_voltage = el.find("voltage")
        _voltage = Voltage.from_sdf(_c_voltage) if _c_voltage is not None else None
        return cls(name=_name, voltage=_voltage)
