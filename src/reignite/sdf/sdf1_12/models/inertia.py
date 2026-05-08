from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_11.models.inertia import Inertia as _PrevInertia
from .ixx import Ixx
from .ixy import Ixy
from .ixz import Ixz
from .iyy import Iyy
from .iyz import Iyz
from .izz import Izz


class Inertia(_PrevInertia):
    def __init__(
        self,
        ixx: "Ixx" = None,
        ixy: "Ixy" = None,
        ixz: "Ixz" = None,
        iyy: "Iyy" = None,
        iyz: "Iyz" = None,
        izz: "Izz" = None
    ):
        super().__init__(ixx=ixx, ixy=ixy, ixz=ixz, iyy=iyy, iyz=iyz, izz=izz)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Inertia":
        _base = _PrevInertia.from_sdf(el)
        return cls(ixx=_base.ixx, ixy=_base.ixy, ixz=_base.ixz, iyy=_base.iyy, iyz=_base.iyz, izz=_base.izz)
