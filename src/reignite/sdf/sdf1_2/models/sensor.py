from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_0.models.sensor import Sensor as _PrevSensor
from .plugin import Plugin
from .camera import Camera
from .ray import Ray
from .contact import Contact
from .rfidtag import Rfidtag
from .rfid import Rfid
from .always_on import AlwaysOn
from .visualize import Visualize
from .pose import Pose
from .topic import Topic


import math
import sys

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



class UpdateRate(Model):
    def __init__(self, update_rate: float = 0):
        self.update_rate = update_rate

    def to_sdf(self) -> ET.Element:
        el = ET.Element("update_rate")
        if self.update_rate is not None:
            el.text = str(self.update_rate)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "UpdateRate":
        _text = el.text or 0
        _update_rate = _parse_double(_text)
        return cls(update_rate=_update_rate)


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
        always_on: "AlwaysOn" = None,
        update_rate: "UpdateRate" = None,
        visualize: "Visualize" = None,
        pose: "Pose" = None,
        topic: "Topic" = None
    ):
        super().__init__(name=name, type=type, plugin=plugin, camera=camera, ray=ray, contact=contact, rfidtag=rfidtag, rfid=rfid, always_on=always_on, update_rate=update_rate, visualize=visualize, topic=topic)
        self.pose = pose

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Sensor":
        _base = _PrevSensor.from_sdf(el)
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        return cls(name=_base.name, type=_base.type, plugin=_base.plugin, camera=_base.camera, ray=_base.ray, contact=_base.contact, rfidtag=_base.rfidtag, rfid=_base.rfid, always_on=_base.always_on, update_rate=_base.update_rate, visualize=_base.visualize, pose=_pose, topic=_base.topic)
