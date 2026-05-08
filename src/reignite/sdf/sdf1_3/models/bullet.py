from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_2.models.bullet import Bullet as _PrevBullet
from .dt import Dt


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
