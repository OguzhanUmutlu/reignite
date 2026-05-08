from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .c1 import C1
from .c2 import C2
from .c3 import C3
from .f import F
from .fun import Fun


class CustomFunction(Model):
    def __init__(
        self,
        c1: "C1" = None,
        c2: "C2" = None,
        c3: "C3" = None,
        f: "F" = None,
        fun: "Fun" = None
    ):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.f = f
        self.fun = fun

    def to_sdf(self) -> ET.Element:
        el = ET.Element("custom_function")
        if self.c1 is not None:
            el.append(self.c1.to_sdf())
        if self.c2 is not None:
            el.append(self.c2.to_sdf())
        if self.c3 is not None:
            el.append(self.c3.to_sdf())
        if self.f is not None:
            el.append(self.f.to_sdf())
        if self.fun is not None:
            el.append(self.fun.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CustomFunction":
        _c_c1 = el.find("c1")
        _c1 = C1.from_sdf(_c_c1) if _c_c1 is not None else None
        _c_c2 = el.find("c2")
        _c2 = C2.from_sdf(_c_c2) if _c_c2 is not None else None
        _c_c3 = el.find("c3")
        _c3 = C3.from_sdf(_c_c3) if _c_c3 is not None else None
        _c_f = el.find("f")
        _f = F.from_sdf(_c_f) if _c_f is not None else None
        _c_fun = el.find("fun")
        _fun = Fun.from_sdf(_c_fun) if _c_fun is not None else None
        return cls(c1=_c1, c2=_c2, c3=_c3, f=_f, fun=_fun)
