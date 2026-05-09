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


class LightMap(Model):
    def __init__(self, light_map: str = "", uv_set: int = 0):
        self.light_map = light_map
        self.uv_set = uv_set

    def to_sdf(self) -> ET.Element:
        el = ET.Element("light_map")
        if self.light_map is not None:
            el.text = self.light_map
        if self.uv_set is not None:
            el.set("uv_set", str(self.uv_set))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "LightMap":
        _text = el.text or ""
        _light_map = _text
        _uv_set = _parse_uint32(el.get("uv_set", 0))
        return cls(light_map=_light_map, uv_set=_uv_set)
