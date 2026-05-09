from __future__ import annotations

import math
from typing import List
from xml.etree import ElementTree as ET

from .camera import Camera
from .contact import Contact
from .origin import Origin
from .plugin import Plugin
from .ray import Ray
from .rfid import Rfid
from .rfidtag import Rfidtag
from .topic import Topic
from ..model import Model


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


class Sensor(Model):
    def __init__(
            self,
            name: str = "__default__",
            type: str = "__default__",
            always_on: bool = False,
            update_rate: float = 0,
            visualize: bool = False,
            plugin: List["Plugin"] = None,
            camera: "Camera" = None,
            ray: "Ray" = None,
            contact: "Contact" = None,
            rfidtag: "Rfidtag" = None,
            rfid: "Rfid" = None,
            origin: "Origin" = None,
            topic: "Topic" = None
    ):
        self.name = name
        self.type = type
        self.always_on = always_on
        self.update_rate = update_rate
        self.visualize = visualize
        self.plugin = plugin or []
        self.camera = camera
        self.ray = ray
        self.contact = contact
        self.rfidtag = rfidtag
        self.rfid = rfid
        self.origin = origin
        self.topic = topic

    def to_sdf(self) -> ET.Element:
        el = ET.Element("sensor")
        if self.name is not None:
            el.set("name", self.name)
        if self.type is not None:
            el.set("type", self.type)
        if self.always_on is not None:
            el.set("always_on", str(self.always_on).lower())
        if self.update_rate is not None:
            el.set("update_rate", str(self.update_rate))
        if self.visualize is not None:
            el.set("visualize", str(self.visualize).lower())
        for item in (self.plugin or []):
            el.append(item.to_sdf())
        if self.camera is not None:
            el.append(self.camera.to_sdf())
        if self.ray is not None:
            el.append(self.ray.to_sdf())
        if self.contact is not None:
            el.append(self.contact.to_sdf())
        if self.rfidtag is not None:
            el.append(self.rfidtag.to_sdf())
        if self.rfid is not None:
            el.append(self.rfid.to_sdf())
        if self.origin is not None:
            el.append(self.origin.to_sdf())
        if self.topic is not None:
            el.append(self.topic.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Sensor":
        _name = el.get("name", "__default__")
        _type = el.get("type", "__default__")
        _always_on = el.get("always_on", False).strip().lower() == 'true'
        _update_rate = _parse_double(el.get("update_rate", 0))
        _visualize = el.get("visualize", False).strip().lower() == 'true'
        _plugin = [Plugin.from_sdf(c) for c in el.findall("plugin")]
        _c_camera = el.find("camera")
        _camera = Camera.from_sdf(_c_camera) if _c_camera is not None else None
        _c_ray = el.find("ray")
        _ray = Ray.from_sdf(_c_ray) if _c_ray is not None else None
        _c_contact = el.find("contact")
        _contact = Contact.from_sdf(_c_contact) if _c_contact is not None else None
        _c_rfidtag = el.find("rfidtag")
        _rfidtag = Rfidtag.from_sdf(_c_rfidtag) if _c_rfidtag is not None else None
        _c_rfid = el.find("rfid")
        _rfid = Rfid.from_sdf(_c_rfid) if _c_rfid is not None else None
        _c_origin = el.find("origin")
        _origin = Origin.from_sdf(_c_origin) if _c_origin is not None else None
        _c_topic = el.find("topic")
        _topic = Topic.from_sdf(_c_topic) if _c_topic is not None else None
        return cls(name=_name, type=_type, always_on=_always_on, update_rate=_update_rate, visualize=_visualize,
                   plugin=_plugin, camera=_camera, ray=_ray, contact=_contact, rfidtag=_rfidtag, rfid=_rfid,
                   origin=_origin, topic=_topic)
