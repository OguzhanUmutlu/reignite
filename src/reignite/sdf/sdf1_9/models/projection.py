from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_8.models.projection import Projection as _PrevProjection
from .p_fx import PFx
from .p_fy import PFy
from .p_cx import PCx
from .p_cy import PCy
from .tx import Tx
from .ty import Ty


class Projection(_PrevProjection):
    def __init__(
        self,
        p_fx: "PFx" = None,
        p_fy: "PFy" = None,
        p_cx: "PCx" = None,
        p_cy: "PCy" = None,
        tx: "Tx" = None,
        ty: "Ty" = None
    ):
        super().__init__(p_fx=p_fx, p_fy=p_fy, p_cx=p_cx, p_cy=p_cy, tx=tx, ty=ty)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Projection":
        _base = _PrevProjection.from_sdf(el)
        return cls(p_fx=_base.p_fx, p_fy=_base.p_fy, p_cx=_base.p_cx, p_cy=_base.p_cy, tx=_base.tx, ty=_base.ty)
