from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_0.models.topic import Topic as _PrevTopic


class Topic(_PrevTopic):
    def __init__(self, topic: str = "__default"):
        super().__init__(topic=topic)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Topic":
        _base = _PrevTopic.from_sdf(el)
        return cls(topic=_base.topic)
