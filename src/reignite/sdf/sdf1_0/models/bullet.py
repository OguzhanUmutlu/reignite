from __future__ import annotations

from xml.etree import ElementTree as ET

from .dt import Dt
from ..model import Model


class Bullet(Model):
    def __init__(self, dt: "Dt" = None):
        self.dt = dt

    def to_sdf(self) -> ET.Element:
        el = ET.Element("bullet")
        if self.dt is not None:
            el.append(self.dt.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Bullet":
        _c_dt = el.find("dt")
        _dt = Dt.from_sdf(_c_dt) if _c_dt is not None else None
        return cls(dt=_dt)
