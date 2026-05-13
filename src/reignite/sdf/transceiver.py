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
    class Essid(BaseModel):
        def __init__(self, sdf_version: str | None = None, essid: str = "wireless"):
            super().__init__(sdf_version)
            self.essid = essid

        def to_version(self, target_version: str) -> "Transceiver.Essid":
            kwargs = {"sdf_version": target_version}
            kwargs["essid"] = self.essid
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("essid")
            if self.essid is not None:
                el.text = self.essid
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Transceiver.Essid | SDFError":
            _text = el.text or "wireless"
            _essid = _text
            if isinstance(_essid, SDFError):
                return _essid
            return cls(sdf_version=version, essid=_essid)

    class Frequency(BaseModel):
        def __init__(self, sdf_version: str | None = None, frequency: float = 2442):
            super().__init__(sdf_version)
            self.frequency = frequency

        def to_version(self, target_version: str) -> "Transceiver.Frequency":
            kwargs = {"sdf_version": target_version}
            kwargs["frequency"] = self.frequency
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("frequency")
            if self.frequency is not None:
                el.text = str(self.frequency)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Transceiver.Frequency | SDFError":
            _text = el.text or 2442
            _frequency = _parse_double(_text)
            if isinstance(_frequency, SDFError):
                return _frequency
            return cls(sdf_version=version, frequency=_frequency)

    class Gain(BaseModel):
        def __init__(self, sdf_version: str | None = None, gain: float = 2.5):
            super().__init__(sdf_version)
            self.gain = gain

        def to_version(self, target_version: str) -> "Transceiver.Gain":
            kwargs = {"sdf_version": target_version}
            kwargs["gain"] = self.gain
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("gain")
            if self.gain is not None:
                el.text = str(self.gain)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Transceiver.Gain | SDFError":
            _text = el.text or 2.5
            _gain = _parse_double(_text)
            if isinstance(_gain, SDFError):
                return _gain
            return cls(sdf_version=version, gain=_gain)

    class MaxFrequency(BaseModel):
        def __init__(self, sdf_version: str | None = None, max_frequency: float = 2484):
            super().__init__(sdf_version)
            self.max_frequency = max_frequency

        def to_version(self, target_version: str) -> "Transceiver.MaxFrequency":
            kwargs = {"sdf_version": target_version}
            kwargs["max_frequency"] = self.max_frequency
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("max_frequency")
            if self.max_frequency is not None:
                el.text = str(self.max_frequency)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Transceiver.MaxFrequency | SDFError":
            _text = el.text or 2484
            _max_frequency = _parse_double(_text)
            if isinstance(_max_frequency, SDFError):
                return _max_frequency
            return cls(sdf_version=version, max_frequency=_max_frequency)

    class MinFrequency(BaseModel):
        def __init__(self, sdf_version: str | None = None, min_frequency: float = 2412):
            super().__init__(sdf_version)
            self.min_frequency = min_frequency

        def to_version(self, target_version: str) -> "Transceiver.MinFrequency":
            kwargs = {"sdf_version": target_version}
            kwargs["min_frequency"] = self.min_frequency
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("min_frequency")
            if self.min_frequency is not None:
                el.text = str(self.min_frequency)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Transceiver.MinFrequency | SDFError":
            _text = el.text or 2412
            _min_frequency = _parse_double(_text)
            if isinstance(_min_frequency, SDFError):
                return _min_frequency
            return cls(sdf_version=version, min_frequency=_min_frequency)

    class Power(BaseModel):
        def __init__(self, sdf_version: str | None = None, power: float = 14.50):
            super().__init__(sdf_version)
            self.power = power

        def to_version(self, target_version: str) -> "Transceiver.Power":
            kwargs = {"sdf_version": target_version}
            kwargs["power"] = self.power
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("power")
            if self.power is not None:
                el.text = str(self.power)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Transceiver.Power | SDFError":
            _text = el.text or 14.50
            _power = _parse_double(_text)
            if isinstance(_power, SDFError):
                return _power
            return cls(sdf_version=version, power=_power)

    class Sensitivity(BaseModel):
        def __init__(self, sdf_version: str | None = None, sensitivity: float = -90):
            super().__init__(sdf_version)
            self.sensitivity = sensitivity

        def to_version(self, target_version: str) -> "Transceiver.Sensitivity":
            kwargs = {"sdf_version": target_version}
            kwargs["sensitivity"] = self.sensitivity
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("sensitivity")
            if self.sensitivity is not None:
                el.text = str(self.sensitivity)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Transceiver.Sensitivity | SDFError":
            _text = el.text or -90
            _sensitivity = _parse_double(_text)
            if isinstance(_sensitivity, SDFError):
                return _sensitivity
            return cls(sdf_version=version, sensitivity=_sensitivity)

    def __init__(
        self,
        sdf_version: str | None = None,
        essid: "Transceiver.Essid" = None,
        frequency: "Transceiver.Frequency" = None,
        gain: "Transceiver.Gain" = None,
        max_frequency: "Transceiver.MaxFrequency" = None,
        min_frequency: "Transceiver.MinFrequency" = None,
        power: "Transceiver.Power" = None,
        sensitivity: "Transceiver.Sensitivity" = None
    ):
        super().__init__(sdf_version)
        self.essid = essid
        self.frequency = frequency
        self.gain = gain
        self.max_frequency = max_frequency
        self.min_frequency = min_frequency
        self.power = power
        self.sensitivity = sensitivity
        if self.essid is not None:
            if getattr(self.essid, '__version__', None) is None:
                self.essid.__version__ = self.__version__
            elif getattr(self.essid, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.essid = self.essid.to_version(self.__version__)
        if self.frequency is not None:
            if getattr(self.frequency, '__version__', None) is None:
                self.frequency.__version__ = self.__version__
            elif getattr(self.frequency, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.frequency = self.frequency.to_version(self.__version__)
        if self.gain is not None:
            if getattr(self.gain, '__version__', None) is None:
                self.gain.__version__ = self.__version__
            elif getattr(self.gain, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.gain = self.gain.to_version(self.__version__)
        if self.max_frequency is not None:
            if getattr(self.max_frequency, '__version__', None) is None:
                self.max_frequency.__version__ = self.__version__
            elif getattr(self.max_frequency, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.max_frequency = self.max_frequency.to_version(self.__version__)
        if self.min_frequency is not None:
            if getattr(self.min_frequency, '__version__', None) is None:
                self.min_frequency.__version__ = self.__version__
            elif getattr(self.min_frequency, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.min_frequency = self.min_frequency.to_version(self.__version__)
        if self.power is not None:
            if getattr(self.power, '__version__', None) is None:
                self.power.__version__ = self.__version__
            elif getattr(self.power, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.power = self.power.to_version(self.__version__)
        if self.sensitivity is not None:
            if getattr(self.sensitivity, '__version__', None) is None:
                self.sensitivity.__version__ = self.__version__
            elif getattr(self.sensitivity, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.sensitivity = self.sensitivity.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Transceiver":
        kwargs = {"sdf_version": target_version}
        kwargs["essid"] = self.essid.to_version(target_version) if self.essid is not None else None
        kwargs["frequency"] = self.frequency.to_version(target_version) if self.frequency is not None else None
        kwargs["gain"] = self.gain.to_version(target_version) if self.gain is not None else None
        kwargs["max_frequency"] = self.max_frequency.to_version(target_version) if self.max_frequency is not None else None
        kwargs["min_frequency"] = self.min_frequency.to_version(target_version) if self.min_frequency is not None else None
        kwargs["power"] = self.power.to_version(target_version) if self.power is not None else None
        kwargs["sensitivity"] = self.sensitivity.to_version(target_version) if self.sensitivity is not None else None
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
            el.append(self.essid.to_sdf(version))
        if self.frequency is not None:
            el.append(self.frequency.to_sdf(version))
        if self.gain is not None:
            el.append(self.gain.to_sdf(version))
        if self.max_frequency is not None:
            el.append(self.max_frequency.to_sdf(version))
        if self.min_frequency is not None:
            el.append(self.min_frequency.to_sdf(version))
        if self.power is not None:
            el.append(self.power.to_sdf(version))
        if self.sensitivity is not None:
            el.append(self.sensitivity.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Transceiver | SDFError":
        _c_essid = el.find("essid")
        if _c_essid is not None:
            _res = cls.Essid._from_sdf(_c_essid, version)
            if isinstance(_res, SDFError):
                return _res.extend("essid")
            _essid = _res
        else:
            _essid = None
        _c_frequency = el.find("frequency")
        if _c_frequency is not None:
            _res = cls.Frequency._from_sdf(_c_frequency, version)
            if isinstance(_res, SDFError):
                return _res.extend("frequency")
            _frequency = _res
        else:
            _frequency = None
        _c_gain = el.find("gain")
        if _c_gain is not None:
            _res = cls.Gain._from_sdf(_c_gain, version)
            if isinstance(_res, SDFError):
                return _res.extend("gain")
            _gain = _res
        else:
            _gain = None
        _c_max_frequency = el.find("max_frequency")
        if _c_max_frequency is not None:
            _res = cls.MaxFrequency._from_sdf(_c_max_frequency, version)
            if isinstance(_res, SDFError):
                return _res.extend("max_frequency")
            _max_frequency = _res
        else:
            _max_frequency = None
        _c_min_frequency = el.find("min_frequency")
        if _c_min_frequency is not None:
            _res = cls.MinFrequency._from_sdf(_c_min_frequency, version)
            if isinstance(_res, SDFError):
                return _res.extend("min_frequency")
            _min_frequency = _res
        else:
            _min_frequency = None
        _c_power = el.find("power")
        if _c_power is not None:
            _res = cls.Power._from_sdf(_c_power, version)
            if isinstance(_res, SDFError):
                return _res.extend("power")
            _power = _res
        else:
            _power = None
        _c_sensitivity = el.find("sensitivity")
        if _c_sensitivity is not None:
            _res = cls.Sensitivity._from_sdf(_c_sensitivity, version)
            if isinstance(_res, SDFError):
                return _res.extend("sensitivity")
            _sensitivity = _res
        else:
            _sensitivity = None
        return cls(sdf_version=version, essid=_essid, frequency=_frequency, gain=_gain, max_frequency=_max_frequency, min_frequency=_min_frequency, power=_power, sensitivity=_sensitivity)
