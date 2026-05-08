from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.pose import Pose


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



class Waypoint(Model):
    def __init__(self, time: float = 0.0, pose: Pose = None):
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        self.time = time
        self.pose = pose

    def to_sdf(self) -> ET.Element:
        el = ET.Element("waypoint")
        if self.time is not None:
            el.set("time", str(self.time))
        if self.pose is not None:
            el.set("pose", self.pose.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Waypoint":
        _time = _parse_double(el.get("time", 0.0))
        _pose = Pose.from_sdf(el.get("pose", "0 0 0 0 0 0"))
        return cls(time=_time, pose=_pose)
