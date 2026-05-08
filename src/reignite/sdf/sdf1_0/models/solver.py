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



class Solver(Model):
    def __init__(
        self,
        type: str = "quick",
        dt: float = 0.001,
        iters: int = 50,
        precon_iters: int = 0,
        sor: float = 1.3
    ):
        self.type = type
        self.dt = dt
        self.iters = iters
        self.precon_iters = precon_iters
        self.sor = sor

    def to_sdf(self) -> ET.Element:
        el = ET.Element("solver")
        if self.type is not None:
            el.set("type", self.type)
        if self.dt is not None:
            el.set("dt", str(self.dt))
        if self.iters is not None:
            el.set("iters", str(self.iters))
        if self.precon_iters is not None:
            el.set("precon_iters", str(self.precon_iters))
        if self.sor is not None:
            el.set("sor", str(self.sor))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Solver":
        _type = el.get("type", "quick")
        _dt = _parse_double(el.get("dt", 0.001))
        _iters = _parse_int32(el.get("iters", 50))
        _precon_iters = _parse_int32(el.get("precon_iters", 0))
        _sor = _parse_double(el.get("sor", 1.3))
        return cls(type=_type, dt=_dt, iters=_iters, precon_iters=_precon_iters, sor=_sor)
