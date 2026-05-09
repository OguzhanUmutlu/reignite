from __future__ import annotations

from xml.etree import ElementTree as ET

from .essid import Essid
from .frequency import Frequency
from .gain import Gain
from .max_frequency import MaxFrequency
from .min_frequency import MinFrequency
from .power import Power
from .sensitivity import Sensitivity
from ...sdf1_8.models.transceiver import Transceiver as _PrevTransceiver


class Transceiver(_PrevTransceiver):
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
        super().__init__(essid=essid, frequency=frequency, min_frequency=min_frequency, max_frequency=max_frequency,
                         gain=gain, power=power, sensitivity=sensitivity)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Transceiver":
        _base = _PrevTransceiver.from_sdf(el)
        return cls(essid=_base.essid, frequency=_base.frequency, min_frequency=_base.min_frequency,
                   max_frequency=_base.max_frequency, gain=_base.gain, power=_base.power, sensitivity=_base.sensitivity)
