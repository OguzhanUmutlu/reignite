from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .vertical_position import VerticalPosition
from .vertical_velocity import VerticalVelocity


class Altimeter(Model):
    def __init__(
        self,
        vertical_position: "VerticalPosition" = None,
        vertical_velocity: "VerticalVelocity" = None
    ):
        self.vertical_position = vertical_position
        self.vertical_velocity = vertical_velocity

    def to_sdf(self) -> ET.Element:
        el = ET.Element("altimeter")
        if self.vertical_position is not None:
            el.append(self.vertical_position.to_sdf())
        if self.vertical_velocity is not None:
            el.append(self.vertical_velocity.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Altimeter":
        _c_vertical_position = el.find("vertical_position")
        _vertical_position = VerticalPosition.from_sdf(_c_vertical_position) if _c_vertical_position is not None else None
        _c_vertical_velocity = el.find("vertical_velocity")
        _vertical_velocity = VerticalVelocity.from_sdf(_c_vertical_velocity) if _c_vertical_velocity is not None else None
        return cls(vertical_position=_vertical_position, vertical_velocity=_vertical_velocity)
