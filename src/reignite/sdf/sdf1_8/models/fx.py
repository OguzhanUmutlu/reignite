from __future__ import annotations

import math
from xml.etree import ElementTree as ET

from ...sdf1_7.models.fx import Fx as _PrevFx


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


class Fx(_PrevFx):
    def __init__(self, fx: float = 277):
        super().__init__(fx=fx)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Fx":
        _base = _PrevFx.from_sdf(el)
        return cls(fx=_base.fx)
