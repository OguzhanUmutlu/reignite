from __future__ import annotations

import math
from xml.etree import ElementTree as ET

from ..model import Model


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


class Inertia(Model):
    def __init__(
            self,
            ixx: float = 0.0,
            ixy: float = 0.0,
            ixz: float = 0.0,
            iyy: float = 0.0,
            iyz: float = 0.0,
            izz: float = 0.0
    ):
        self.ixx = ixx
        self.ixy = ixy
        self.ixz = ixz
        self.iyy = iyy
        self.iyz = iyz
        self.izz = izz

    def to_sdf(self) -> ET.Element:
        el = ET.Element("inertia")
        if self.ixx is not None:
            el.set("ixx", str(self.ixx))
        if self.ixy is not None:
            el.set("ixy", str(self.ixy))
        if self.ixz is not None:
            el.set("ixz", str(self.ixz))
        if self.iyy is not None:
            el.set("iyy", str(self.iyy))
        if self.iyz is not None:
            el.set("iyz", str(self.iyz))
        if self.izz is not None:
            el.set("izz", str(self.izz))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Inertia":
        _ixx = _parse_double(el.get("ixx", 0.0))
        _ixy = _parse_double(el.get("ixy", 0.0))
        _ixz = _parse_double(el.get("ixz", 0.0))
        _iyy = _parse_double(el.get("iyy", 0.0))
        _iyz = _parse_double(el.get("iyz", 0.0))
        _izz = _parse_double(el.get("izz", 0.0))
        return cls(ixx=_ixx, ixy=_ixy, ixz=_ixz, iyy=_iyy, iyz=_iyz, izz=_izz)
