from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .fx import Fx
from .fy import Fy
from .cx import Cx
from .cy import Cy
from .s import S


class Intrinsics(Model):
    def __init__(
        self,
        fx: "Fx" = None,
        fy: "Fy" = None,
        cx: "Cx" = None,
        cy: "Cy" = None,
        s: "S" = None
    ):
        self.fx = fx
        self.fy = fy
        self.cx = cx
        self.cy = cy
        self.s = s

    def to_sdf(self) -> ET.Element:
        el = ET.Element("intrinsics")
        if self.fx is not None:
            el.append(self.fx.to_sdf())
        if self.fy is not None:
            el.append(self.fy.to_sdf())
        if self.cx is not None:
            el.append(self.cx.to_sdf())
        if self.cy is not None:
            el.append(self.cy.to_sdf())
        if self.s is not None:
            el.append(self.s.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Intrinsics":
        _c_fx = el.find("fx")
        _fx = Fx.from_sdf(_c_fx) if _c_fx is not None else None
        _c_fy = el.find("fy")
        _fy = Fy.from_sdf(_c_fy) if _c_fy is not None else None
        _c_cx = el.find("cx")
        _cx = Cx.from_sdf(_c_cx) if _c_cx is not None else None
        _c_cy = el.find("cy")
        _cy = Cy.from_sdf(_c_cy) if _c_cy is not None else None
        _c_s = el.find("s")
        _s = S.from_sdf(_c_s) if _c_s is not None else None
        return cls(fx=_fx, fy=_fy, cx=_cx, cy=_cy, s=_s)
