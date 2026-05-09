from __future__ import annotations

from xml.etree import ElementTree as ET

from .dt import Dt
from ...sdf1_0.models.bullet import Bullet as _PrevBullet


class Bullet(_PrevBullet):
    def __init__(self, dt: "Dt" = None):
        super().__init__(dt=dt)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Bullet":
        _base = _PrevBullet.from_sdf(el)
        return cls(dt=_base.dt)
