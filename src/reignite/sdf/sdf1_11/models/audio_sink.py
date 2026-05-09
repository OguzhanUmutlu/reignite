from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_10.models.audio_sink import AudioSink as _PrevAudioSink


class AudioSink(_PrevAudioSink):
    def __init__(self):
        super().__init__()

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AudioSink":
        return cls()
