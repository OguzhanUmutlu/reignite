from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from .trajectory import Trajectory


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



class Script(Model):
    def __init__(
        self,
        loop: bool = True,
        delay_start: float = 0.0,
        auto_start: bool = True,
        trajectory: List["Trajectory"] = None
    ):
        self.loop = loop
        self.delay_start = delay_start
        self.auto_start = auto_start
        self.trajectory = trajectory or []

    def to_sdf(self) -> ET.Element:
        el = ET.Element("script")
        if self.loop is not None:
            el.set("loop", str(self.loop).lower())
        if self.delay_start is not None:
            el.set("delay_start", str(self.delay_start))
        if self.auto_start is not None:
            el.set("auto_start", str(self.auto_start).lower())
        for item in (self.trajectory or []):
            el.append(item.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Script":
        _loop = el.get("loop", True).strip().lower() == 'true'
        _delay_start = _parse_double(el.get("delay_start", 0.0))
        _auto_start = el.get("auto_start", True).strip().lower() == 'true'
        _trajectory = [Trajectory.from_sdf(c) for c in el.findall("trajectory")]
        return cls(loop=_loop, delay_start=_delay_start, auto_start=_auto_start, trajectory=_trajectory)
