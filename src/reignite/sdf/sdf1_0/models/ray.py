from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .scan import Scan
from .range import Range


class Ray(Model):
    def __init__(self, scan: "Scan" = None, range: "Range" = None):
        self.scan = scan
        self.range = range

    def to_sdf(self) -> ET.Element:
        el = ET.Element("ray")
        if self.scan is not None:
            el.append(self.scan.to_sdf())
        if self.range is not None:
            el.append(self.range.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ray":
        _c_scan = el.find("scan")
        _scan = Scan.from_sdf(_c_scan) if _c_scan is not None else None
        _c_range = el.find("range")
        _range = Range.from_sdf(_c_range) if _c_range is not None else None
        return cls(scan=_scan, range=_range)
