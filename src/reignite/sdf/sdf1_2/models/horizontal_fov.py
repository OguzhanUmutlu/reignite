from __future__ import annotations

import math
from xml.etree import ElementTree as ET

from ...sdf1_0.models.horizontal_fov import HorizontalFov as _PrevHorizontalFov


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


class HorizontalFov(_PrevHorizontalFov):
    def __init__(self, horizontal_fov: float = 1.047):
        super().__init__()
        self.horizontal_fov = horizontal_fov

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.horizontal_fov is not None:
            el.text = str(self.horizontal_fov)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "HorizontalFov":
        _text = el.text or 1.047
        _horizontal_fov = _parse_double(_text)
        return cls(horizontal_fov=_horizontal_fov)
