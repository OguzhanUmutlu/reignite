from __future__ import annotations

from xml.etree import ElementTree as ET

from .essid import Essid
from .frequency import Frequency
from .gain import Gain
from .max_frequency import MaxFrequency
from .min_frequency import MinFrequency
from .power import Power
from .sensitivity import Sensitivity
from ..model import Model


class Transceiver(Model):
    def __init__(
            self,
            essid: "Essid" = None,
            frequency: "Frequency" = None,
            min_frequency: "MinFrequency" = None,
            max_frequency: "MaxFrequency" = None,
            gain: "Gain" = None,
            power: "Power" = None,
            sensitivity: "Sensitivity" = None
    ):
        self.essid = essid
        self.frequency = frequency
        self.min_frequency = min_frequency
        self.max_frequency = max_frequency
        self.gain = gain
        self.power = power
        self.sensitivity = sensitivity

    def to_sdf(self) -> ET.Element:
        el = ET.Element("transceiver")
        if self.essid is not None:
            el.append(self.essid.to_sdf())
        if self.frequency is not None:
            el.append(self.frequency.to_sdf())
        if self.min_frequency is not None:
            el.append(self.min_frequency.to_sdf())
        if self.max_frequency is not None:
            el.append(self.max_frequency.to_sdf())
        if self.gain is not None:
            el.append(self.gain.to_sdf())
        if self.power is not None:
            el.append(self.power.to_sdf())
        if self.sensitivity is not None:
            el.append(self.sensitivity.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Transceiver":
        _c_essid = el.find("essid")
        _essid = Essid.from_sdf(_c_essid) if _c_essid is not None else None
        _c_frequency = el.find("frequency")
        _frequency = Frequency.from_sdf(_c_frequency) if _c_frequency is not None else None
        _c_min_frequency = el.find("min_frequency")
        _min_frequency = MinFrequency.from_sdf(_c_min_frequency) if _c_min_frequency is not None else None
        _c_max_frequency = el.find("max_frequency")
        _max_frequency = MaxFrequency.from_sdf(_c_max_frequency) if _c_max_frequency is not None else None
        _c_gain = el.find("gain")
        _gain = Gain.from_sdf(_c_gain) if _c_gain is not None else None
        _c_power = el.find("power")
        _power = Power.from_sdf(_c_power) if _c_power is not None else None
        _c_sensitivity = el.find("sensitivity")
        _sensitivity = Sensitivity.from_sdf(_c_sensitivity) if _c_sensitivity is not None else None
        return cls(essid=_essid, frequency=_frequency, min_frequency=_min_frequency, max_frequency=_max_frequency,
                   gain=_gain, power=_power, sensitivity=_sensitivity)
