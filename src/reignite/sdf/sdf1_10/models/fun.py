from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_9.models.fun import Fun as _PrevFun


class Fun(_PrevFun):
    def __init__(self, fun: str = "tan"):
        super().__init__(fun=fun)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Fun":
        _base = _PrevFun.from_sdf(el)
        return cls(fun=_base.fun)
