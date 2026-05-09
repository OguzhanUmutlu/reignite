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


class Suspension(Model):
    def __init__(self, cfm: float = 0.0, erp: float = 0.2):
        self.cfm = cfm
        self.erp = erp

    def to_sdf(self) -> ET.Element:
        el = ET.Element("suspension")
        if self.cfm is not None:
            el.set("cfm", str(self.cfm))
        if self.erp is not None:
            el.set("erp", str(self.erp))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Suspension":
        _cfm = _parse_double(el.get("cfm", 0.0))
        _erp = _parse_double(el.get("erp", 0.2))
        return cls(cfm=_cfm, erp=_erp)
