from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class TriggerTopic(Model):
    def __init__(self, trigger_topic: str = ""):
        self.trigger_topic = trigger_topic

    def to_sdf(self) -> ET.Element:
        el = ET.Element("trigger_topic")
        if self.trigger_topic is not None:
            el.text = self.trigger_topic
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "TriggerTopic":
        _text = el.text or ""
        _trigger_topic = _text
        return cls(trigger_topic=_trigger_topic)
