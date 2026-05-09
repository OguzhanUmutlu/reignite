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


class VisibilityMask(Model):
    def __init__(self, visibility_mask: int = 4294967295):
        self.visibility_mask = visibility_mask

    def to_sdf(self) -> ET.Element:
        el = ET.Element("visibility_mask")
        if self.visibility_mask is not None:
            el.text = str(self.visibility_mask)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "VisibilityMask":
        _text = el.text or 4294967295
        _visibility_mask = _parse_uint32(_text)
        return cls(visibility_mask=_visibility_mask)
