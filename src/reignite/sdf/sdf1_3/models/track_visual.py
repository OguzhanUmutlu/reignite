from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .min_dist import MinDist
from .max_dist import MaxDist


class Name(Model):
    def __init__(self, name: str = "__default__"):
        self.name = name

    def to_sdf(self) -> ET.Element:
        el = ET.Element("name")
        if self.name is not None:
            el.text = self.name
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Name":
        _text = el.text or "__default__"
        _name = _text
        return cls(name=_name)


class TrackVisual(Model):
    def __init__(self, name: "Name" = None, min_dist: "MinDist" = None, max_dist: "MaxDist" = None):
        self.name = name
        self.min_dist = min_dist
        self.max_dist = max_dist

    def to_sdf(self) -> ET.Element:
        el = ET.Element("track_visual")
        if self.name is not None:
            el.append(self.name.to_sdf())
        if self.min_dist is not None:
            el.append(self.min_dist.to_sdf())
        if self.max_dist is not None:
            el.append(self.max_dist.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "TrackVisual":
        _c_name = el.find("name")
        _name = Name.from_sdf(_c_name) if _c_name is not None else None
        _c_min_dist = el.find("min_dist")
        _min_dist = MinDist.from_sdf(_c_min_dist) if _c_min_dist is not None else None
        _c_max_dist = el.find("max_dist")
        _max_dist = MaxDist.from_sdf(_c_max_dist) if _c_max_dist is not None else None
        return cls(name=_name, min_dist=_min_dist, max_dist=_max_dist)
