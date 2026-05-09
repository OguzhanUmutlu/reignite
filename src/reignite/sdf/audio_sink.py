from __future__ import annotations

from xml.etree import ElementTree as ET

from ._base import Model


class AudioSink(Model):
    def __init__(self, sdf_version: str):
        self.__version__ = sdf_version

    def to_version(self, target_version: str) -> "AudioSink":
        kwargs = {"sdf_version": target_version}
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("audio_sink")
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "AudioSink":
        return cls(sdf_version=version)
