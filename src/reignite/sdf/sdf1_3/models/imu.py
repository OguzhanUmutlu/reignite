from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .topic import Topic


class Imu(Model):
    def __init__(self, topic: "Topic" = None):
        self.topic = topic

    def to_sdf(self) -> ET.Element:
        el = ET.Element("imu")
        if self.topic is not None:
            el.append(self.topic.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Imu":
        _c_topic = el.find("topic")
        _topic = Topic.from_sdf(_c_topic) if _c_topic is not None else None
        return cls(topic=_topic)
