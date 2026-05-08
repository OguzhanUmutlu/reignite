from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.vector3 import Vector3


class Fdir1(Model):
    def __init__(self, fdir1: Vector3 = None):
        if fdir1 is None:
            fdir1 = Vector3.from_sdf("0 0 0")
        self.fdir1 = fdir1

    def to_sdf(self) -> ET.Element:
        el = ET.Element("fdir1")
        if self.fdir1 is not None:
            el.text = self.fdir1.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Fdir1":
        _text = el.text or "0 0 0"
        _fdir1 = Vector3.from_sdf(_text)
        return cls(fdir1=_fdir1)
