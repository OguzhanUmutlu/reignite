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



class Essid(Model):
    def __init__(self, sdf_version: str, essid: str = "wireless"):
        self.__version__ = sdf_version
        self.essid = essid

    def to_version(self, target_version: str) -> "Essid":
        kwargs = {"sdf_version": target_version}
        kwargs["essid"] = self.essid
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("essid")
        if self.essid is not None:
            el.text = self.essid
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Essid":
        _text = el.text or "wireless"
        _essid = _text
        return cls(sdf_version=version, essid=_essid)


class Frequency(Model):
    def __init__(self, sdf_version: str, frequency: float = 2442):
        self.__version__ = sdf_version
        self.frequency = frequency

    def to_version(self, target_version: str) -> "Frequency":
        kwargs = {"sdf_version": target_version}
        kwargs["frequency"] = self.frequency
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("frequency")
        if self.frequency is not None:
            el.text = str(self.frequency)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Frequency":
        _text = el.text or 2442
        _frequency = _parse_double(_text)
        return cls(sdf_version=version, frequency=_frequency)


class MinFrequency(Model):
    def __init__(self, sdf_version: str, min_frequency: float = 2412):
        self.__version__ = sdf_version
        self.min_frequency = min_frequency

    def to_version(self, target_version: str) -> "MinFrequency":
        kwargs = {"sdf_version": target_version}
        kwargs["min_frequency"] = self.min_frequency
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("min_frequency")
        if self.min_frequency is not None:
            el.text = str(self.min_frequency)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MinFrequency":
        _text = el.text or 2412
        _min_frequency = _parse_double(_text)
        return cls(sdf_version=version, min_frequency=_min_frequency)


class MaxFrequency(Model):
    def __init__(self, sdf_version: str, max_frequency: float = 2484):
        self.__version__ = sdf_version
        self.max_frequency = max_frequency

    def to_version(self, target_version: str) -> "MaxFrequency":
        kwargs = {"sdf_version": target_version}
        kwargs["max_frequency"] = self.max_frequency
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max_frequency")
        if self.max_frequency is not None:
            el.text = str(self.max_frequency)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MaxFrequency":
        _text = el.text or 2484
        _max_frequency = _parse_double(_text)
        return cls(sdf_version=version, max_frequency=_max_frequency)


class Gain(Model):
    def __init__(self, sdf_version: str, gain: float = 2.5):
        self.__version__ = sdf_version
        self.gain = gain

    def to_version(self, target_version: str) -> "Gain":
        kwargs = {"sdf_version": target_version}
        kwargs["gain"] = self.gain
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("gain")
        if self.gain is not None:
            el.text = str(self.gain)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Gain":
        _text = el.text or 2.5
        _gain = _parse_double(_text)
        return cls(sdf_version=version, gain=_gain)


class Power(Model):
    def __init__(self, sdf_version: str, power: float = 14.50):
        self.__version__ = sdf_version
        self.power = power

    def to_version(self, target_version: str) -> "Power":
        kwargs = {"sdf_version": target_version}
        kwargs["power"] = self.power
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("power")
        if self.power is not None:
            el.text = str(self.power)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Power":
        _text = el.text or 14.50
        _power = _parse_double(_text)
        return cls(sdf_version=version, power=_power)


class Sensitivity(Model):
    def __init__(self, sdf_version: str, sensitivity: float = -90):
        self.__version__ = sdf_version
        self.sensitivity = sensitivity

    def to_version(self, target_version: str) -> "Sensitivity":
        kwargs = {"sdf_version": target_version}
        kwargs["sensitivity"] = self.sensitivity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sensitivity")
        if self.sensitivity is not None:
            el.text = str(self.sensitivity)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Sensitivity":
        _text = el.text or -90
        _sensitivity = _parse_double(_text)
        return cls(sdf_version=version, sensitivity=_sensitivity)


class Transceiver(Model):
    def __init__(
        self,
        sdf_version: str,
        essid: "Essid" = None,
        frequency: "Frequency" = None,
        min_frequency: "MinFrequency" = None,
        max_frequency: "MaxFrequency" = None,
        gain: "Gain" = None,
        power: "Power" = None,
        sensitivity: "Sensitivity" = None
    ):
        self.__version__ = sdf_version
        self.essid = essid
        self.frequency = frequency
        self.min_frequency = min_frequency
        self.max_frequency = max_frequency
        self.gain = gain
        self.power = power
        self.sensitivity = sensitivity

    def to_version(self, target_version: str) -> "Transceiver":
        kwargs = {"sdf_version": target_version}
        kwargs["essid"] = self.essid.to_version(target_version) if self.essid is not None else None
        kwargs["frequency"] = self.frequency.to_version(target_version) if self.frequency is not None else None
        kwargs["min_frequency"] = self.min_frequency.to_version(target_version) if self.min_frequency is not None else None
        kwargs["max_frequency"] = self.max_frequency.to_version(target_version) if self.max_frequency is not None else None
        kwargs["gain"] = self.gain.to_version(target_version) if self.gain is not None else None
        kwargs["power"] = self.power.to_version(target_version) if self.power is not None else None
        kwargs["sensitivity"] = self.sensitivity.to_version(target_version) if self.sensitivity is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("transceiver")
        if self.essid is not None:
            el.append(self.essid.to_sdf(version))
        if self.frequency is not None:
            el.append(self.frequency.to_sdf(version))
        if self.min_frequency is not None:
            el.append(self.min_frequency.to_sdf(version))
        if self.max_frequency is not None:
            el.append(self.max_frequency.to_sdf(version))
        if self.gain is not None:
            el.append(self.gain.to_sdf(version))
        if self.power is not None:
            el.append(self.power.to_sdf(version))
        if self.sensitivity is not None:
            el.append(self.sensitivity.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Transceiver":
        _c_essid = el.find("essid")
        _essid = Essid.from_sdf(_c_essid, version) if _c_essid is not None else None
        _c_frequency = el.find("frequency")
        _frequency = Frequency.from_sdf(_c_frequency, version) if _c_frequency is not None else None
        _c_min_frequency = el.find("min_frequency")
        _min_frequency = MinFrequency.from_sdf(_c_min_frequency, version) if _c_min_frequency is not None else None
        _c_max_frequency = el.find("max_frequency")
        _max_frequency = MaxFrequency.from_sdf(_c_max_frequency, version) if _c_max_frequency is not None else None
        _c_gain = el.find("gain")
        _gain = Gain.from_sdf(_c_gain, version) if _c_gain is not None else None
        _c_power = el.find("power")
        _power = Power.from_sdf(_c_power, version) if _c_power is not None else None
        _c_sensitivity = el.find("sensitivity")
        _sensitivity = Sensitivity.from_sdf(_c_sensitivity, version) if _c_sensitivity is not None else None
        return cls(sdf_version=version, essid=_essid, frequency=_frequency, min_frequency=_min_frequency, max_frequency=_max_frequency, gain=_gain, power=_power, sensitivity=_sensitivity)
