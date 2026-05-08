from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_11.models.altimeter import Altimeter as _PrevAltimeter
from .vertical_position import VerticalPosition
from .vertical_velocity import VerticalVelocity


class Altimeter(_PrevAltimeter):
    def __init__(
        self,
        vertical_position: "VerticalPosition" = None,
        vertical_velocity: "VerticalVelocity" = None
    ):
        super().__init__(vertical_position=vertical_position, vertical_velocity=vertical_velocity)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Altimeter":
        _base = _PrevAltimeter.from_sdf(el)
        return cls(vertical_position=_base.vertical_position, vertical_velocity=_base.vertical_velocity)
