from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_9.models.trigger_topic import TriggerTopic as _PrevTriggerTopic


class TriggerTopic(_PrevTriggerTopic):
    def __init__(self, trigger_topic: str = ""):
        super().__init__(trigger_topic=trigger_topic)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "TriggerTopic":
        _base = _PrevTriggerTopic.from_sdf(el)
        return cls(trigger_topic=_base.trigger_topic)
