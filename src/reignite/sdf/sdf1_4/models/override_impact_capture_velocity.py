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



class OverrideImpactCaptureVelocity(Model):
    def __init__(self, override_impact_capture_velocity: float = 0.001):
        self.override_impact_capture_velocity = override_impact_capture_velocity

    def to_sdf(self) -> ET.Element:
        el = ET.Element("override_impact_capture_velocity")
        if self.override_impact_capture_velocity is not None:
            el.text = str(self.override_impact_capture_velocity)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "OverrideImpactCaptureVelocity":
        _text = el.text or 0.001
        _override_impact_capture_velocity = _parse_double(_text)
        return cls(override_impact_capture_velocity=_override_impact_capture_velocity)
