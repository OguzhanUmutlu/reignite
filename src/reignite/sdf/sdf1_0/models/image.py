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


class Image(Model):
    def __init__(
            self,
            filename: str = "__default__",
            scale: float = 1,
            threshold: int = 200,
            height: float = 1,
            granularity: int = 1
    ):
        self.filename = filename
        self.scale = scale
        self.threshold = threshold
        self.height = height
        self.granularity = granularity

    def to_sdf(self) -> ET.Element:
        el = ET.Element("image")
        if self.filename is not None:
            el.set("filename", self.filename)
        if self.scale is not None:
            el.set("scale", str(self.scale))
        if self.threshold is not None:
            el.set("threshold", str(self.threshold))
        if self.height is not None:
            el.set("height", str(self.height))
        if self.granularity is not None:
            el.set("granularity", str(self.granularity))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Image":
        _filename = el.get("filename", "__default__")
        _scale = _parse_double(el.get("scale", 1))
        _threshold = _parse_int32(el.get("threshold", 200))
        _height = _parse_double(el.get("height", 1))
        _granularity = _parse_int32(el.get("granularity", 1))
        return cls(filename=_filename, scale=_scale, threshold=_threshold, height=_height, granularity=_granularity)
