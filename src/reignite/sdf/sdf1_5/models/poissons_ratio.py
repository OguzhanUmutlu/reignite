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


class PoissonsRatio(Model):
    def __init__(self, poissons_ratio: float = 0.3):
        self.poissons_ratio = poissons_ratio

    def to_sdf(self) -> ET.Element:
        el = ET.Element("poissons_ratio")
        if self.poissons_ratio is not None:
            el.text = str(self.poissons_ratio)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "PoissonsRatio":
        _text = el.text or 0.3
        _poissons_ratio = _parse_double(_text)
        return cls(poissons_ratio=_poissons_ratio)
