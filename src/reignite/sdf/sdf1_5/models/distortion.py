from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .k1 import K1
from .k2 import K2
from .k3 import K3
from .p1 import P1
from .p2 import P2
from .center import Center


class Distortion(Model):
    def __init__(
        self,
        k1: "K1" = None,
        k2: "K2" = None,
        k3: "K3" = None,
        p1: "P1" = None,
        p2: "P2" = None,
        center: "Center" = None
    ):
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.p1 = p1
        self.p2 = p2
        self.center = center

    def to_sdf(self) -> ET.Element:
        el = ET.Element("distortion")
        if self.k1 is not None:
            el.append(self.k1.to_sdf())
        if self.k2 is not None:
            el.append(self.k2.to_sdf())
        if self.k3 is not None:
            el.append(self.k3.to_sdf())
        if self.p1 is not None:
            el.append(self.p1.to_sdf())
        if self.p2 is not None:
            el.append(self.p2.to_sdf())
        if self.center is not None:
            el.append(self.center.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Distortion":
        _c_k1 = el.find("k1")
        _k1 = K1.from_sdf(_c_k1) if _c_k1 is not None else None
        _c_k2 = el.find("k2")
        _k2 = K2.from_sdf(_c_k2) if _c_k2 is not None else None
        _c_k3 = el.find("k3")
        _k3 = K3.from_sdf(_c_k3) if _c_k3 is not None else None
        _c_p1 = el.find("p1")
        _p1 = P1.from_sdf(_c_p1) if _c_p1 is not None else None
        _c_p2 = el.find("p2")
        _p2 = P2.from_sdf(_c_p2) if _c_p2 is not None else None
        _c_center = el.find("center")
        _center = Center.from_sdf(_c_center) if _c_center is not None else None
        return cls(k1=_k1, k2=_k2, k3=_k3, p1=_p1, p2=_p2, center=_center)
