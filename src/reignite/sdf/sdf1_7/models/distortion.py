from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_6.models.distortion import Distortion as _PrevDistortion
from .k1 import K1
from .k2 import K2
from .k3 import K3
from .p1 import P1
from .p2 import P2
from .center import Center


class Distortion(_PrevDistortion):
    def __init__(
        self,
        k1: "K1" = None,
        k2: "K2" = None,
        k3: "K3" = None,
        p1: "P1" = None,
        p2: "P2" = None,
        center: "Center" = None
    ):
        super().__init__(k1=k1, k2=k2, k3=k3, p1=p1, p2=p2, center=center)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Distortion":
        _base = _PrevDistortion.from_sdf(el)
        return cls(k1=_base.k1, k2=_base.k2, k3=_base.k3, p1=_base.p1, p2=_base.p2, center=_base.center)
