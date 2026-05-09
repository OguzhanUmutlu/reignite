from __future__ import annotations

import math
from typing import List
from xml.etree import ElementTree as ET

from .always_on import AlwaysOn
from .camera import Camera
from .contact import Contact
from .imu import Imu
from .plugin import Plugin
from .pose import Pose
from .ray import Ray
from .rfid import Rfid
from .rfidtag import Rfidtag
from .topic import Topic
from .visualize import Visualize
from ...sdf1_2.models.sensor import Sensor as _PrevSensor
from ...sdf1_2.models.update_rate import UpdateRate as _PrevUpdateRate


def _parse_int32(raw: str) -> int:
    v = int(raw)
    if not (-2147483648 <= v <= 2147483647):
        raise ValueError(f"int32 out of range: {v}")
    return v


def _parse_uint32(raw: str) -> int:
    v = int(raw)
    if not (0 <= v <= 4294967295):
        raise ValueError(f"uint32 out of range: {v}")
    return v


def _parse_double(raw: str) -> float:
    v = float(raw)
    if not math.isfinite(v) or abs(v) > 1.7976931348623157e+308:
        raise ValueError(f"double out of range: {raw}")
    return v


class UpdateRate(_PrevUpdateRate):
    def __init__(self, update_rate: float = 0):
        super().__init__(update_rate=update_rate)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "UpdateRate":
        _base = _PrevUpdateRate.from_sdf(el)
        return cls(update_rate=_base.update_rate)


class Sensor(_PrevSensor):
    def __init__(
            self,
            name: str = "__default__",
            type: str = "__default__",
            plugin: List["Plugin"] = None,
            camera: "Camera" = None,
            ray: "Ray" = None,
            contact: "Contact" = None,
            rfidtag: "Rfidtag" = None,
            rfid: "Rfid" = None,
            imu: "Imu" = None,
            always_on: "AlwaysOn" = None,
            update_rate: "UpdateRate" = None,
            visualize: "Visualize" = None,
            pose: "Pose" = None,
            topic: "Topic" = None
    ):
        super().__init__(name=name, type=type, plugin=plugin, camera=camera, ray=ray, contact=contact, rfidtag=rfidtag,
                         rfid=rfid, always_on=always_on, update_rate=update_rate, visualize=visualize, pose=pose,
                         topic=topic)
        self.imu = imu

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.imu is not None:
            el.append(self.imu.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Sensor":
        _base = _PrevSensor.from_sdf(el)
        _c_imu = el.find("imu")
        _imu = Imu.from_sdf(_c_imu) if _c_imu is not None else None
        return cls(name=_base.name, type=_base.type, plugin=_base.plugin, camera=_base.camera, ray=_base.ray,
                   contact=_base.contact, rfidtag=_base.rfidtag, rfid=_base.rfid, imu=_imu, always_on=_base.always_on,
                   update_rate=_base.update_rate, visualize=_base.visualize, pose=_base.pose, topic=_base.topic)
