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



class GraspCheck(Model):
    def __init__(self, detach_steps: int = 40, attach_steps: int = 20, min_contact_count: int = 2):
        self.detach_steps = detach_steps
        self.attach_steps = attach_steps
        self.min_contact_count = min_contact_count

    def to_sdf(self) -> ET.Element:
        el = ET.Element("grasp_check")
        if self.detach_steps is not None:
            el.set("detach_steps", str(self.detach_steps))
        if self.attach_steps is not None:
            el.set("attach_steps", str(self.attach_steps))
        if self.min_contact_count is not None:
            el.set("min_contact_count", str(self.min_contact_count))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "GraspCheck":
        _detach_steps = _parse_int32(el.get("detach_steps", 40))
        _attach_steps = _parse_int32(el.get("attach_steps", 20))
        _min_contact_count = _parse_uint32(el.get("min_contact_count", 2))
        return cls(detach_steps=_detach_steps, attach_steps=_attach_steps, min_contact_count=_min_contact_count)
