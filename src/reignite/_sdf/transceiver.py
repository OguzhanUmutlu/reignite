### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double
from ..utils.model import BaseModel
from ..utils.errors import SDFError


# noinspection PyUnusedImports
class Transceiver(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        essid: str | None = "wireless",
        frequency: float | None = 2442,
        gain: float | None = 2.5,
        max_frequency: float | None = 2484,
        min_frequency: float | None = 2412,
        power: float | None = 14.50,
        sensitivity: float | None = -90
    ):
        super().__init__(sdf_version)
        self.essid = essid if essid is not None else "wireless"
        self.frequency = frequency if frequency is not None else 2442
        self.gain = gain if gain is not None else 2.5
        self.max_frequency = max_frequency if max_frequency is not None else 2484
        self.min_frequency = min_frequency if min_frequency is not None else 2412
        self.power = power if power is not None else 14.50
        self.sensitivity = sensitivity if sensitivity is not None else -90

    def to_version(self, target_version: str) -> "Transceiver":
        kwargs: dict = {"sdf_version": target_version, "essid": self.essid, "frequency": self.frequency, "gain": self.gain, "max_frequency": self.max_frequency, "min_frequency": self.min_frequency, "power": self.power, "sensitivity": self.sensitivity}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
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
