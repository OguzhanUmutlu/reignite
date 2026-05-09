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


class PreconIters(Model):
    def __init__(self, precon_iters: int = 0):
        self.precon_iters = precon_iters

    def to_sdf(self) -> ET.Element:
        el = ET.Element("precon_iters")
        if self.precon_iters is not None:
            el.text = str(self.precon_iters)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "PreconIters":
        _text = el.text or 0
        _precon_iters = _parse_int32(_text)
        return cls(precon_iters=_precon_iters)
