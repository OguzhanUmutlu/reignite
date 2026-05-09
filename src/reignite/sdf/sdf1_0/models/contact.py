from __future__ import annotations

import math
from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.vector3 import Vector3


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


class Ode(Model):
    def __init__(
            self,
            mu: float = -1,
            mu2: float = -1,
            fdir1: Vector3 = None,
            slip1: float = 0.0,
            slip2: float = 0.0
    ):
        if fdir1 is None:
            fdir1 = Vector3.from_sdf("0 0 0")
        self.mu = mu
        self.mu2 = mu2
        self.fdir1 = fdir1
        self.slip1 = slip1
        self.slip2 = slip2

    def to_sdf(self) -> ET.Element:
        el = ET.Element("ode")
        if self.mu is not None:
            el.set("mu", str(self.mu))
        if self.mu2 is not None:
            el.set("mu2", str(self.mu2))
        if self.fdir1 is not None:
            el.set("fdir1", self.fdir1.to_sdf())
        if self.slip1 is not None:
            el.set("slip1", str(self.slip1))
        if self.slip2 is not None:
            el.set("slip2", str(self.slip2))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ode":
        _mu = _parse_double(el.get("mu", -1))
        _mu2 = _parse_double(el.get("mu2", -1))
        _fdir1 = Vector3.from_sdf(el.get("fdir1", "0 0 0"))
        _slip1 = _parse_double(el.get("slip1", 0.0))
        _slip2 = _parse_double(el.get("slip2", 0.0))
        return cls(mu=_mu, mu2=_mu2, fdir1=_fdir1, slip1=_slip1, slip2=_slip2)


class Contact(Model):
    def __init__(self, ode: "Ode" = None):
        self.ode = ode

    def to_sdf(self) -> ET.Element:
        el = ET.Element("contact")
        if self.ode is not None:
            el.append(self.ode.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Contact":
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode) if _c_ode is not None else None
        return cls(ode=_ode)
