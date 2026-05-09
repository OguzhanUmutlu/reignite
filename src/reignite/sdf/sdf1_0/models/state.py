from __future__ import annotations

import math
from typing import List
from xml.etree import ElementTree as ET

from .model import Model


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


class State(Model):
    def __init__(
            self,
            world_name: str = "__default__",
            time: float = "0 0",
            model: List["Model"] = None
    ):
        self.world_name = world_name
        self.time = time
        self.model = model or []

    def to_sdf(self) -> ET.Element:
        el = ET.Element("state")
        if self.world_name is not None:
            el.set("world_name", self.world_name)
        if self.time is not None:
            el.set("time", str(self.time))
        for item in (self.model or []):
            el.append(item.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "State":
        _world_name = el.get("world_name", "__default__")
        _time = _parse_double(el.get("time", "0 0"))
        _model = [Model.from_sdf(c) for c in el.findall("model")]
        return cls(world_name=_world_name, time=_time, model=_model)
