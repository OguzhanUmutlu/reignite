from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Topic(Model):
    def __init__(self, topic: str = "__default"):
        self.topic = topic

    def to_sdf(self) -> ET.Element:
        el = ET.Element("topic")
        if self.topic is not None:
            el.text = self.topic
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Topic":
        _text = el.text or "__default"
        _topic = _text
        return cls(topic=_topic)
