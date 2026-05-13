### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError


import math

def _parse_int32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (-2147483648 <= v <= 2147483647):
            return SDFError(f"int32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid int32: {raw}")


def _parse_uint32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (0 <= v <= 4294967295):
            return SDFError(f"uint32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid uint32: {raw}")


def _parse_double(raw: str) -> float | SDFError:
    try:
        v = float(raw)
        if not math.isfinite(v) or abs(v) > math.inf:
            return SDFError(f"double out of range: {raw}")
        return v
    except ValueError:
        return SDFError(f"Invalid double: {raw}")



class Transceiver(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        essid: str = "wireless",
        frequency: float = 2442,
        gain: float = 2.5,
        max_frequency: float = 2484,
        min_frequency: float = 2412,
        power: float = 14.50,
        sensitivity: float = -90
    ):
        super().__init__(sdf_version)
        self.essid = essid
        self.frequency = frequency
        self.gain = gain
        self.max_frequency = max_frequency
        self.min_frequency = min_frequency
        self.power = power
        self.sensitivity = sensitivity

    def to_version(self, target_version: str) -> "Transceiver":
        kwargs = {"sdf_version": target_version}
        kwargs["essid"] = self.essid
        kwargs["frequency"] = self.frequency
        kwargs["gain"] = self.gain
        kwargs["max_frequency"] = self.max_frequency
        kwargs["min_frequency"] = self.min_frequency
        kwargs["power"] = self.power
        kwargs["sensitivity"] = self.sensitivity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("transceiver")
        if self.essid is not None:
            _c_tmp = ET.Element("essid")
            _c_tmp.text = self.essid
            el.append(_c_tmp)
        if self.frequency is not None:
            _c_tmp = ET.Element("frequency")
            _c_tmp.text = str(self.frequency)
            el.append(_c_tmp)
        if self.gain is not None:
            _c_tmp = ET.Element("gain")
            _c_tmp.text = str(self.gain)
            el.append(_c_tmp)
        if self.max_frequency is not None:
            _c_tmp = ET.Element("max_frequency")
            _c_tmp.text = str(self.max_frequency)
            el.append(_c_tmp)
        if self.min_frequency is not None:
            _c_tmp = ET.Element("min_frequency")
            _c_tmp.text = str(self.min_frequency)
            el.append(_c_tmp)
        if self.power is not None:
            _c_tmp = ET.Element("power")
            _c_tmp.text = str(self.power)
            el.append(_c_tmp)
        if self.sensitivity is not None:
            _c_tmp = ET.Element("sensitivity")
            _c_tmp.text = str(self.sensitivity)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Transceiver | SDFError":
        _c_tmp = el.find("essid")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "wireless"
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("essid")
            _essid = _val
        else:
            _essid = None
        _c_tmp = el.find("frequency")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 2442
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("frequency")
            _frequency = _val
        else:
            _frequency = None
        _c_tmp = el.find("gain")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 2.5
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("gain")
            _gain = _val
        else:
            _gain = None
        _c_tmp = el.find("max_frequency")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 2484
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("max_frequency")
            _max_frequency = _val
        else:
            _max_frequency = None
        _c_tmp = el.find("min_frequency")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 2412
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("min_frequency")
            _min_frequency = _val
        else:
            _min_frequency = None
        _c_tmp = el.find("power")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 14.50
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("power")
            _power = _val
        else:
            _power = None
        _c_tmp = el.find("sensitivity")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else -90
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("sensitivity")
            _sensitivity = _val
        else:
            _sensitivity = None
        return cls(sdf_version=version, essid=_essid, frequency=_frequency, gain=_gain, max_frequency=_max_frequency, min_frequency=_min_frequency, power=_power, sensitivity=_sensitivity)
