from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .p_fx import PFx
from .p_fy import PFy
from .p_cx import PCx
from .p_cy import PCy
from .tx import Tx
from .ty import Ty


class Projection(Model):
    def __init__(
        self,
        p_fx: "PFx" = None,
        p_fy: "PFy" = None,
        p_cx: "PCx" = None,
        p_cy: "PCy" = None,
        tx: "Tx" = None,
        ty: "Ty" = None
    ):
        self.p_fx = p_fx
        self.p_fy = p_fy
        self.p_cx = p_cx
        self.p_cy = p_cy
        self.tx = tx
        self.ty = ty

    def to_sdf(self) -> ET.Element:
        el = ET.Element("projection")
        if self.p_fx is not None:
            el.append(self.p_fx.to_sdf())
        if self.p_fy is not None:
            el.append(self.p_fy.to_sdf())
        if self.p_cx is not None:
            el.append(self.p_cx.to_sdf())
        if self.p_cy is not None:
            el.append(self.p_cy.to_sdf())
        if self.tx is not None:
            el.append(self.tx.to_sdf())
        if self.ty is not None:
            el.append(self.ty.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Projection":
        _c_p_fx = el.find("p_fx")
        _p_fx = PFx.from_sdf(_c_p_fx) if _c_p_fx is not None else None
        _c_p_fy = el.find("p_fy")
        _p_fy = PFy.from_sdf(_c_p_fy) if _c_p_fy is not None else None
        _c_p_cx = el.find("p_cx")
        _p_cx = PCx.from_sdf(_c_p_cx) if _c_p_cx is not None else None
        _c_p_cy = el.find("p_cy")
        _p_cy = PCy.from_sdf(_c_p_cy) if _c_p_cy is not None else None
        _c_tx = el.find("tx")
        _tx = Tx.from_sdf(_c_tx) if _c_tx is not None else None
        _c_ty = el.find("ty")
        _ty = Ty.from_sdf(_c_ty) if _c_ty is not None else None
        return cls(p_fx=_p_fx, p_fy=_p_fy, p_cx=_p_cx, p_cy=_p_cy, tx=_tx, ty=_ty)
