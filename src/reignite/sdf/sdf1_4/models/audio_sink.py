from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class AudioSink(Model):
    def __init__(self):
        pass

    def to_sdf(self) -> ET.Element:
        el = ET.Element("audio_sink")
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AudioSink":
        return cls()
