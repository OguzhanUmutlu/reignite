from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_10.models.imu import Imu as _PrevImu
from .orientation_reference_frame import OrientationReferenceFrame
from .angular_velocity import AngularVelocity
from .linear_acceleration import LinearAcceleration
from .enable_orientation import EnableOrientation


class Imu(_PrevImu):
    def __init__(
        self,
        orientation_reference_frame: "OrientationReferenceFrame" = None,
        angular_velocity: "AngularVelocity" = None,
        linear_acceleration: "LinearAcceleration" = None,
        enable_orientation: "EnableOrientation" = None
    ):
        super().__init__(orientation_reference_frame=orientation_reference_frame, angular_velocity=angular_velocity, linear_acceleration=linear_acceleration, enable_orientation=enable_orientation)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Imu":
        _base = _PrevImu.from_sdf(el)
        return cls(orientation_reference_frame=_base.orientation_reference_frame, angular_velocity=_base.angular_velocity, linear_acceleration=_base.linear_acceleration, enable_orientation=_base.enable_orientation)
