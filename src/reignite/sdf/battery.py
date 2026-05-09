from __future__ import annotations

from xml.etree import ElementTree as ET

from ._base import Model


import math

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
    if not math.isfinite(v) or abs(v) > math.inf:
        raise ValueError(f"double out of range: {raw}")
    return v



class Voltage(Model):
    def __init__(self, sdf_version: str, voltage: float = 0.0):
        self.__version__ = sdf_version
        self.voltage = voltage

    def to_version(self, target_version: str) -> "Voltage":
        kwargs = {"sdf_version": target_version}
        kwargs["voltage"] = self.voltage
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("voltage")
        if self.voltage is not None:
            el.text = str(self.voltage)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Voltage":
        _text = el.text or 0.0
        _voltage = _parse_double(_text)
        return cls(sdf_version=version, voltage=_voltage)


class Battery(Model):
    def __init__(self, sdf_version: str, name: str = "__default__", voltage: "Voltage" = None):
        self.__version__ = sdf_version
        self.name = name
        self.voltage = voltage

    def to_version(self, target_version: str) -> "Battery":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["voltage"] = self.voltage.to_version(target_version) if self.voltage is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("battery")
        if self.name is not None:
            el.set("name", self.name)
        if self.voltage is not None:
            el.append(self.voltage.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Battery":
        _name = el.get("name", "__default__")
        _c_voltage = el.find("voltage")
        _voltage = Voltage.from_sdf(_c_voltage, version) if _c_voltage is not None else None
        return cls(sdf_version=version, name=_name, voltage=_voltage)
