from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


import math
import sys

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
    if not math.isfinite(v) or abs(v) > 1.7976931348623157e+308:
        raise ValueError(f"double out of range: {raw}")
    return v



class SimTime(Model):
    def __init__(self, sim_time: float = "0 0"):
        self.sim_time = sim_time

    def to_sdf(self) -> ET.Element:
        el = ET.Element("sim_time")
        if self.sim_time is not None:
            el.text = str(self.sim_time)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SimTime":
        _text = el.text or "0 0"
        _sim_time = _parse_double(_text)
        return cls(sim_time=_sim_time)
