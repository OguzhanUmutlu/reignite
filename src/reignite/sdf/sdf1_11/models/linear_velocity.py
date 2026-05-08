from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_10.models.linear_velocity import LinearVelocity as _PrevLinearVelocity
from ....utils.vector3 import Vector3


class LinearVelocity(_PrevLinearVelocity):
    def __init__(self, linear_velocity: Vector3 = None):
        if linear_velocity is None:
            linear_velocity = Vector3.from_sdf("0 0 0")
        super().__init__(linear_velocity=linear_velocity)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "LinearVelocity":
        _base = _PrevLinearVelocity.from_sdf(el)
        return cls(linear_velocity=_base.linear_velocity)
