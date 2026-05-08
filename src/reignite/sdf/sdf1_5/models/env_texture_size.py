from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


import math
import sys

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



class EnvTextureSize(Model):
    def __init__(self, env_texture_size: int = 256):
        self.env_texture_size = env_texture_size

    def to_sdf(self) -> ET.Element:
        el = ET.Element("env_texture_size")
        if self.env_texture_size is not None:
            el.text = str(self.env_texture_size)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "EnvTextureSize":
        _text = el.text or 256
        _env_texture_size = _parse_int32(_text)
        return cls(env_texture_size=_env_texture_size)
