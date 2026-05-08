from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_5.models.custom_function import CustomFunction as _PrevCustomFunction
from .c1 import C1
from .c2 import C2
from .c3 import C3
from .f import F
from .fun import Fun


class CustomFunction(_PrevCustomFunction):
    def __init__(
        self,
        c1: "C1" = None,
        c2: "C2" = None,
        c3: "C3" = None,
        f: "F" = None,
        fun: "Fun" = None
    ):
        super().__init__(c1=c1, c2=c2, c3=c3, f=f, fun=fun)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CustomFunction":
        _base = _PrevCustomFunction.from_sdf(el)
        return cls(c1=_base.c1, c2=_base.c2, c3=_base.c3, f=_base.f, fun=_base.fun)
