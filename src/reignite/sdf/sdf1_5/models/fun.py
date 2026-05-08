from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Fun(Model):
    def __init__(self, fun: str = "tan"):
        self.fun = fun

    def to_sdf(self) -> ET.Element:
        el = ET.Element("fun")
        if self.fun is not None:
            el.text = self.fun
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Fun":
        _text = el.text or "tan"
        _fun = _text
        return cls(fun=_fun)
