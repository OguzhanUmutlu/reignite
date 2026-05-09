from __future__ import annotations

from xml.etree import ElementTree as ET

from .angular_velocity import AngularVelocity
from .enable_orientation import EnableOrientation
from .linear_acceleration import LinearAcceleration
from .orientation_reference_frame import OrientationReferenceFrame
from .topic import Topic
from ...sdf1_5.models.imu import Imu as _PrevImu


class Imu(_PrevImu):
    def __init__(
            self,
            orientation_reference_frame: "OrientationReferenceFrame" = None,
            topic: "Topic" = None,
            angular_velocity: "AngularVelocity" = None,
            linear_acceleration: "LinearAcceleration" = None,
            enable_orientation: "EnableOrientation" = None
    ):
        super().__init__(topic=topic, angular_velocity=angular_velocity, linear_acceleration=linear_acceleration)
        self.orientation_reference_frame = orientation_reference_frame
        self.enable_orientation = enable_orientation

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.orientation_reference_frame is not None:
            el.append(self.orientation_reference_frame.to_sdf())
        if self.enable_orientation is not None:
            el.append(self.enable_orientation.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Imu":
        _base = _PrevImu.from_sdf(el)
        _c_orientation_reference_frame = el.find("orientation_reference_frame")
        _orientation_reference_frame = OrientationReferenceFrame.from_sdf(
            _c_orientation_reference_frame) if _c_orientation_reference_frame is not None else None
        _c_enable_orientation = el.find("enable_orientation")
        _enable_orientation = EnableOrientation.from_sdf(
            _c_enable_orientation) if _c_enable_orientation is not None else None
        return cls(orientation_reference_frame=_orientation_reference_frame, topic=_base.topic,
                   angular_velocity=_base.angular_velocity, linear_acceleration=_base.linear_acceleration,
                   enable_orientation=_enable_orientation)
