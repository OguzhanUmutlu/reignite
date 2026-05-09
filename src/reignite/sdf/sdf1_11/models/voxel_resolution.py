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


class VoxelResolution(Model):
    def __init__(self, voxel_resolution: int = 200000):
        self.voxel_resolution = voxel_resolution

    def to_sdf(self) -> ET.Element:
        el = ET.Element("voxel_resolution")
        if self.voxel_resolution is not None:
            el.text = str(self.voxel_resolution)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "VoxelResolution":
        _text = el.text or 200000
        _voxel_resolution = _parse_uint32(_text)
        return cls(voxel_resolution=_voxel_resolution)
