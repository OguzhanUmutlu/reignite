from __future__ import annotations

from xml.etree import ElementTree as ET

from .cx import Cx
from .cy import Cy
from .fx import Fx
from .fy import Fy
from .s import S
from ...sdf1_11.models.intrinsics import Intrinsics as _PrevIntrinsics


class Intrinsics(_PrevIntrinsics):
    def __init__(
            self,
            fx: "Fx" = None,
            fy: "Fy" = None,
            cx: "Cx" = None,
            cy: "Cy" = None,
            s: "S" = None
    ):
        super().__init__(fx=fx, fy=fy, cx=cx, cy=cy, s=s)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Intrinsics":
        _base = _PrevIntrinsics.from_sdf(el)
        return cls(fx=_base.fx, fy=_base.fy, cx=_base.cx, cy=_base.cy, s=_base.s)
