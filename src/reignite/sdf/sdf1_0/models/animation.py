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


class Animation(Model):
    def __init__(
            self,
            name: str = "__default__",
            filename: str = "__default__",
            scale: float = 1.0,
            interpolate_x: bool = False
    ):
        self.name = name
        self.filename = filename
        self.scale = scale
        self.interpolate_x = interpolate_x

    def to_sdf(self) -> ET.Element:
        el = ET.Element("animation")
        if self.name is not None:
            el.set("name", self.name)
        if self.filename is not None:
            el.set("filename", self.filename)
        if self.scale is not None:
            el.set("scale", str(self.scale))
        if self.interpolate_x is not None:
            el.set("interpolate_x", str(self.interpolate_x).lower())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Animation":
        _name = el.get("name", "__default__")
        _filename = el.get("filename", "__default__")
        _scale = _parse_double(el.get("scale", 1.0))
        _interpolate_x = el.get("interpolate_x", False).strip().lower() == 'true'
        return cls(name=_name, filename=_filename, scale=_scale, interpolate_x=_interpolate_x)
